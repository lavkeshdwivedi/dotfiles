#!/usr/bin/env python3
"""Inbox monitor. Plain rules, no model calls, no tokens.

Checks Gmail over IMAP (read-only), classifies new mail with fixed rules taken from the
inbox-replies skill, writes a small local log, and raises one Windows toast when something
needs a human. App passwords live in Windows Credential Manager, never in a file.

  python inbox_monitor.py --set-password you@gmail.com   store an app password (prompted)
  python inbox_monitor.py --selftest                      check the rules offline
  python inbox_monitor.py                                 one check (what the scheduler runs)
"""
import argparse
import ctypes
import ctypes.wintypes as wt
import datetime as dt
import email
import getpass
import html
import imaplib
import json
import os
import re
import subprocess
import sys
from email.header import decode_header, make_header

APP = os.path.join(os.environ.get("LOCALAPPDATA", os.path.expanduser("~")), "inbox-monitor")
STATE = os.path.join(APP, "state.json")
CONFIG = os.path.join(APP, "config.json")
LOGDIR = os.path.join(APP, "log")

DEFAULTS = {
    "accounts": ["d.lavkesh@gmail.com", "iamlavkesh@gmail.com"],
    "known_senders": ["vamsi.pathakoti@cloudtern.com", "ramu@cloudtern.com", "kanandcorp.com"],
    "dart_markers": [],  # DART was a one-off he did not join, so no special handling
    "ignore_domains": ["amazon.", "amazonpay.", "robinhood.", "paypal.", "netflix.", "carmax.", "fedex.",
                       "southwest", "labcorp", "bankofamerica.", "hsbc.", "experian.", "groww.", "walmart.",
                       "babbel.", "insurify.", "samsung", "ntta.org", "xe.com", "fetchpackage.",
                       "topresume.", "greatlearning."],
    "min_rate_per_hour": 70,
}

INTERVIEW = re.compile(r"interview|invitation|invite|teams meeting|zoom|calendar|scheduled|reschedul|accepted:", re.I)
RECRUITER = re.compile(r"\b(c2c|w2|corp[- ]to[- ]corp|contract|requirement|job description|opening|hiring|position|"
                       r"role|rate|recruiter|staffing|client|direct hire|permanent|perm|full[- ]?time|salary|"
                       r"technical recruiter|talent acquisition)\b", re.I)
SKIP = re.compile(r"\bw[- ]?2\b|\bfull[- ]?time\b|\bpermanent\b|\bperm\b|direct hire|\bfte\b|citizens? only|"
                  r"\busc\b|gc only|green card|\bno h1b\b|\bh4\b|\bopt\b|\bead\b|only on w2", re.I)
C2C = re.compile(r"\bc2c\b|corp[- ]to[- ]corp", re.I)
NO_C2C = re.compile(r"no c2c|c2c not|not open to c2c", re.I)
FIT = re.compile(r"\b(ai|agent|agentic|llm|genai|gen ai|forward deploy\w*|architect|\.net|python|azure|gcp|rag)\b", re.I)
JUNIOR = re.compile(r"\b(junior|entry[- ]level|intern|trainee)\b", re.I)
RATE = re.compile(r"\$\s?(\d{2,3})(?:\.\d+)?\s*(?:/|per)\s*(?:hr|hour)", re.I)


# ---------- credentials: Windows Credential Manager via ctypes, no files ----------
class CRED(ctypes.Structure):
    _fields_ = [("Flags", wt.DWORD), ("Type", wt.DWORD), ("TargetName", wt.LPWSTR), ("Comment", wt.LPWSTR),
                ("LastWritten", wt.FILETIME), ("CredentialBlobSize", wt.DWORD),
                ("CredentialBlob", ctypes.POINTER(ctypes.c_ubyte)), ("Persist", wt.DWORD),
                ("AttributeCount", wt.DWORD), ("Attributes", ctypes.c_void_p),
                ("TargetAlias", wt.LPWSTR), ("UserName", wt.LPWSTR)]


def cred_set(account, secret):
    blob = secret.encode("utf-16-le")
    buf = (ctypes.c_ubyte * len(blob)).from_buffer_copy(blob)
    c = CRED(0, 1, "inbox-monitor:" + account, None, wt.FILETIME(), len(blob), buf, 2, 0, None, None, account)
    if not ctypes.windll.advapi32.CredWriteW(ctypes.byref(c), 0):
        raise OSError("CredWrite failed")


def cred_get(account):
    p = ctypes.POINTER(CRED)()
    if not ctypes.windll.advapi32.CredReadW("inbox-monitor:" + account, 1, 0, ctypes.byref(p)):
        return None
    try:
        size = p.contents.CredentialBlobSize
        raw = bytes(ctypes.cast(p.contents.CredentialBlob, ctypes.POINTER(ctypes.c_ubyte * size)).contents)
        return raw.decode("utf-16-le")
    finally:
        ctypes.windll.advapi32.CredFree(p)


# ---------- classification: pure rules, no model ----------
def classify(sender, subject, body, headers=None, cfg=DEFAULTS):
    """Return (category, reason). Categories: dart, attention, fit, skip, ignore."""
    headers = headers or {}
    text = subject + "\n" + body
    s = sender.lower()
    if any(re.search(m, text, re.I) or re.search(m, s) for m in cfg["dart_markers"]):
        return "dart", "DART thread, handle it yourself"
    if any(k in s for k in cfg["known_senders"]):
        return "attention", "known contact"
    if "linkedin.com" in s:
        if re.search(r"jobalerts|invitation|news", s):
            return "ignore", "LinkedIn notification"
        if re.search(r"messaging|inmail|message", s + subject, re.I):
            if SKIP.search(text) and not C2C.search(text):
                return "skip", "LinkedIn message, W2 or perm"
            return "attention", "new LinkedIn message"
        return "ignore", "LinkedIn notification"
    if any(d in s for d in cfg["ignore_domains"]):
        return "ignore", "known non-recruiter sender"
    if re.match(r"\s*(re|fw|fwd):", subject, re.I) and not re.search(r"no-?reply|noreply|donotreply", s):
        if re.search(r"\bw[- ]?2\b", text, re.I) and not C2C.search(text):
            return "attention", "asks about W2, answer upfront that it is C2C only"
        return "attention", "reply or forward in a thread"
    if INTERVIEW.search(subject):
        return "attention", "interview or invite"
    if RECRUITER.search(text):
        c2c_ok = bool(C2C.search(text)) and not NO_C2C.search(text)
        if not c2c_ok and SKIP.search(text):
            return "skip", "W2, perm or citizen only"
        if JUNIOR.search(subject):
            return "skip", "junior role"
        rates = [int(r) for r in RATE.findall(text)]
        if rates and max(rates) < cfg["min_rate_per_hour"]:
            return "skip", "rate $%d/hr is below $%d" % (max(rates), cfg["min_rate_per_hour"])
        if FIT.search(text):
            return "fit", "contract or C2C-compatible role in your area"
        return "skip", "role outside your area"
    if "list-unsubscribe" in {k.lower() for k in headers} or headers.get("Precedence", "").lower() == "bulk":
        return "ignore", "bulk mail"
    return "attention", "personal mail, unclassified"


def selftest():
    cases = [
        ("recruiter@kpg99.in", "Contract W2: .NET AI Engineer Remote", "This role is only on w2", "skip"),
        ("a@x.com", "Urgent .NET Architect contract", "Contract role, W2/C2C ok, $95/hr, Azure and AI", "fit"),
        ("a@x.com", "Perm AI Engineer", "Direct hire, $150k, Plano, Python agentic AI", "skip"),
        ("a@x.com", "Data Center Technician", "Contract role, hiring a technician", "skip"),
        ("v@cloudtern.com", "RTR", "hello", "attention"),
        ("a@kanandcorp.com", "Lavkesh Dwivedi Interview", "Teams meeting", "attention"),
        ("x@22ndcentury.com", "DART update", "swati", "attention"),
        ("shipment-tracking@amazon.in", "Shipped", "your order", "ignore"),
        ("messaging-digest-noreply@linkedin.com", "New message from Kavita", "Platform engineer contract, C2C ok", "attention"),
        ("jobalerts-noreply@linkedin.com", "Principal Engineer AI at BMO", "jobs", "ignore"),
        ("p@y.com", "Re: AI Engineer role", "thanks", "attention"),
        ("p@y.com", "RE: .NET AI Engineer", "This role is only on w2", "attention"),
        ("a@x.com", "Backend developer", "Contract, $40 per hour, python", "skip"),
        ("a@x.com", "Hiring Forward Deployed Engineer", "client wants agentic AI, contract, C2C", "fit"),
    ]
    bad = 0
    for snd, sub, body, want in cases:
        got, why = classify(snd, sub, body)
        ok = got == want
        bad += not ok
        print("ok  " if ok else "FAIL", "%-9s got %-9s %-44s (%s)" % (want, got, sub[:44], why))
    own = [("Lavkesh <d.lavkesh@gmail.com>", "d.lavkesh@gmail.com", True),
           ("Kavita <kavita@recruiter.com>", "d.lavkesh@gmail.com", False),
           ("D.Lavkesh@Gmail.com", "d.lavkesh@gmail.com", True)]
    for snd, acct, want in own:
        ok = is_own(snd, acct) == want
        bad += not ok
        print("ok  " if ok else "FAIL", "own-mail check %-34s expected %s" % (snd, want))
    print("selftest:", "all passed" if not bad else "%d failed" % bad)
    return bad


# ---------- mail ----------
def dec(v):
    try:
        return str(make_header(decode_header(v or "")))
    except Exception:
        return v or ""


def body_text(msg):
    parts = msg.walk() if msg.is_multipart() else [msg]
    plain, htmls = "", ""
    for p in parts:
        ct = p.get_content_type()
        if ct not in ("text/plain", "text/html"):
            continue
        try:
            t = (p.get_payload(decode=True) or b"").decode(p.get_content_charset() or "utf-8", "replace")
        except Exception:
            continue
        if ct == "text/plain":
            plain += t
        else:
            t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
            htmls += re.sub(r"<[^>]+>", " ", html.unescape(t))
    return re.sub(r"\s+", " ", plain or htmls)[:6000]


def is_own(sender, account):
    """True for mail from the account itself (sent items, drafts, self-notes)."""
    return account.lower() in sender.lower()


def check_account(account, cfg, state, notes):
    pw = cred_get(account)
    if not pw:
        notes.append("%s: no app password stored, run --set-password" % account)
        return []
    found = []
    M = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    try:
        M.login(account, pw)
        # All Mail also holds mail that a Gmail filter keeps out of the Inbox (labelled and archived).
        # Trash and Spam are not in All Mail. The UID numbering differs per folder, so state is per folder.
        typ, _ = M.select('"[Gmail]/All Mail"', readonly=True)
        key = account + "|all"
        if typ != "OK":
            M.select("INBOX", readonly=True)
            key = account + "|inbox"
        _typ, data = M.uid("search", None, "ALL")
        uids = [int(x) for x in (data[0] or b"").split()]
        last = state.get(key)
        if last is None and any(k.startswith(account + "|") for k in state):
            # Switching folders must not drop mail that arrived since the last scan, so look back one day.
            since = (dt.date.today() - dt.timedelta(days=1)).strftime("%d-%b-%Y")
            _typ, d2 = M.uid("search", None, "SINCE", since)
            recent = [int(x) for x in (d2[0] or b"").split()]
            last = (min(recent) - 1) if recent else (max(uids) if uids else 0)
        if last is None:  # first run on this folder: remember where it is, alert on nothing old
            state[key] = max(uids) if uids else 0
            notes.append("%s: baselined %s at UID %d" % (account, key.split("|")[1], state[key]))
            return []
        for uid in [u for u in uids if u > last][-60:]:
            _t, d = M.uid("fetch", str(uid), "(BODY.PEEK[]<0.24000>)")
            raw = next((x[1] for x in d if isinstance(x, tuple)), b"")
            msg = email.message_from_bytes(raw)
            sender, subject = dec(msg.get("From")), dec(msg.get("Subject"))
            if is_own(sender, account):  # sent mail and drafts also live in All Mail
                continue
            cat, why = classify(sender, subject, body_text(msg), dict(msg.items()), cfg)
            found.append({"account": account, "uid": uid, "cat": cat, "why": why,
                          "from": re.sub(r"\s*<.*?>", "", sender)[:40], "subject": subject[:70]})
        if uids:
            state[key] = max(uids + [last])
    finally:
        try:
            M.logout()
        except Exception:
            pass
    return found


def toast(title, text):
    def esc(s):
        return html.escape(s, quote=True).replace("'", "''")
    ps = ("[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType=WindowsRuntime] | Out-Null;"
          "$x=[Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent('ToastText02');"
          "$t=$x.GetElementsByTagName('text');"
          "$t.Item(0).AppendChild($x.CreateTextNode('%s'))|Out-Null;"
          "$t.Item(1).AppendChild($x.CreateTextNode('%s'))|Out-Null;"
          "$n=[Windows.UI.Notifications.ToastNotification]::new($x);"
          "[Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier("
          "'{1AC14E77-02E7-4E5D-B744-2EB1AE5198B7}\\WindowsPowerShell\\v1.0\\powershell.exe').Show($n)") % (esc(title), esc(text))
    subprocess.run(["powershell", "-NoProfile", "-Command", ps], capture_output=True, timeout=30)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--set-password", metavar="ACCOUNT")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.set_password:
        pw = getpass.getpass("Gmail app password for %s (hidden): " % a.set_password).replace(" ", "")
        cred_set(a.set_password, pw)
        print("stored in Windows Credential Manager as inbox-monitor:" + a.set_password)
        return 0
    if a.selftest:
        return 1 if selftest() else 0
    os.makedirs(LOGDIR, exist_ok=True)
    cfg = dict(DEFAULTS)
    if os.path.exists(CONFIG):
        with open(CONFIG, encoding="utf-8") as f:
            cfg.update(json.load(f))
    state = {}
    if os.path.exists(STATE):
        with open(STATE, encoding="utf-8") as f:
            state = json.load(f)
    notes, hits = [], []
    for acct in cfg["accounts"]:
        try:
            hits += check_account(acct, cfg, state, notes)
        except Exception as e:
            notes.append("%s: %s %s" % (acct, type(e).__name__, str(e)[:80]))
    with open(STATE, "w", encoding="utf-8") as f:
        json.dump(state, f)
    now = dt.datetime.now().isoformat(timespec="seconds")
    with open(os.path.join(LOGDIR, dt.date.today().isoformat() + ".jsonl"), "a", encoding="utf-8") as f:
        for h in hits:
            f.write(json.dumps(dict(t=now, **h)) + "\n")
        for n in notes:
            f.write(json.dumps({"t": now, "note": n}) + "\n")
    alert = [h for h in hits if h["cat"] in ("attention", "fit", "dart")]
    if alert:
        lines = ["%s %s: %s" % ("DART" if h["cat"] == "dart" else h["cat"].upper(), h["from"], h["subject"]) for h in alert[:3]]
        toast("%d inbox item(s) need you" % len(alert), " | ".join(lines)[:230])
    return 0


if __name__ == "__main__":
    sys.exit(main())
