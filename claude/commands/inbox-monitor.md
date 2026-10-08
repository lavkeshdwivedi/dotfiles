Set up, run and tune the token-free inbox monitor that watches both Gmail inboxes and only uses a model when a reply needs judgment. Use when asked to monitor his inboxes, to check why a toast did or did not fire, or to change what counts as worth his attention.

## What it is

A plain Python script, `windows/inbox_monitor.py` in the dotfiles repo, run by Windows Task Scheduler every 15 minutes. It never calls a model. Monitoring costs no tokens.

- It reads Gmail over IMAP, read-only, for `d.lavkesh@gmail.com` and `iamlavkesh@gmail.com`, and only looks at mail newer than the last one it saw. The first run records where each inbox is and alerts on nothing old.
- It sorts each new message with fixed rules copied from the `/inbox-replies` skill. The rules live in `classify()` in the script, and `--selftest` checks them offline.
- It raises one Windows toast when something needs a person, and writes a small log line per message (sender, subject, category, reason, no body) to `%LOCALAPPDATA%\inbox-monitor\log\YYYY-MM-DD.jsonl`.
- LinkedIn is covered through LinkedIn's own notification emails in Gmail. Never script LinkedIn itself, because that risks the account.

## Categories

- `attention`: a known contact (Vamsi, Ramu, Kanand), a reply or forward in a thread, an interview or calendar invite, a new LinkedIn message, or personal mail the rules could not place.
- `fit`: a contract or C2C-compatible role in his area (AI, agents, Forward Deployed, architect, .NET, Python, Azure, GCP). This is the only case that may need a smart reply.
- `skip`: W2 only, permanent or direct hire, citizen only, junior, rate under $70 an hour, or a role outside his area.
- `ignore`: shipping, banks, shopping, newsletters, LinkedIn job alerts.

Only `attention` and `fit` raise a toast. Everything else is logged and stays quiet. A thread reply that mentions W2 without C2C is tagged "asks about W2", because the answer is always the same and should come upfront: C2C only through his employer, no W2 or transfer (see `/inbox-replies`).

## What happens when a toast fires

The model is used only here, and only when he opens a session and asks. Use `/inbox-replies` for the reply, not a background call. The monitor does not draft, send or reply to anything.

## Setup (he runs these, because they involve his passwords)

1. For each Gmail account, create an app password at myaccount.google.com/apppasswords (2-step verification must be on).
2. Store each one in Windows Credential Manager, never in a file or in chat. In the Claude Code prompt, type the command with a `!` prefix so the password prompt is his:
   `! python C:\Claude\Projects\dotfiles\windows\inbox_monitor.py --set-password d.lavkesh@gmail.com`
   `! python C:\Claude\Projects\dotfiles\windows\inbox_monitor.py --set-password iamlavkesh@gmail.com`
3. Check the rules: `python windows\inbox_monitor.py --selftest`.
4. Register the timer: `powershell -File C:\Claude\Projects\dotfiles\windows\install-inbox-monitor.ps1` (use `-Minutes 10` to change the interval, `-Remove` to delete it).
5. Run `python windows\inbox_monitor.py` once. It baselines each inbox. Alerts start with the next new mail.

## Tuning

Create `%LOCALAPPDATA%\inbox-monitor\config.json` to override any default without editing the script, for example:
`{"min_rate_per_hour": 80, "known_senders": ["vamsi.pathakoti@cloudtern.com"], "ignore_domains": ["amazon."]}`
To change a rule itself (the W2, perm, fit or interview patterns), edit the regexes at the top of `inbox_monitor.py`, add a case to `selftest()`, and run `--selftest` before committing.

## Troubleshooting

- No toast: read today's log. A line like `no app password stored` means step 2 was skipped for that account. A line with an error name usually means a wrong app password or IMAP being blocked.
- Missed or wrong category: add the message as a case in `selftest()`, fix the regex, run `--selftest`.
- Never put a password, token or the app password in the repo, the config file, a log or this chat.
