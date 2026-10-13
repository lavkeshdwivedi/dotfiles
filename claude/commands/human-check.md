Act as the human reviewer before Lavkesh approves anything going out in his name (LinkedIn post or comment, article, newsletter, release, README, PR, email, recruiter reply). Argument: the content, a path, or a description; none means whatever is pending in this session.

Review as a skeptic. Assume the draft is wrong until shown otherwise and do not trust earlier conclusions. For long, code-heavy or self-produced content, hand the review to a fresh subagent that sees only the final content and this checklist. Each check ends PASS (evidence), FAIL (what broke) or CAN'T VERIFY (why, and what he must do). Fix what you can and re-run; bring him only passes and real judgment calls.

## 1. Code and commands

Run every snippet, install line and CLI command verbatim in a clean environment (fresh venv or throwaway CI), using the published registry package (`pip install pkg==version`), not the local checkout. If it needs a model or API key it must make a real call; local Ollama only proves the code path, say so. Keys held as GitHub Actions secrets are exercised only in a workflow run: prefer triggering an existing workflow (`gh workflow run`); adding workflows to a repo needs his yes. From workflow logs confirm the expected version installed, calls succeeded, and nothing silently fell back.

## 2. Facts and links

Every version, date, count and stat matches its source now (PyPI JSON, `git log`, changelog, live page). Every URL returns 200 on the right page (`curl -sIL`); repo links point at the public remote (GitHub and GitLab if both mentioned). Timing claims ("runs hourly") are checked against `gh run list`, not the cron line. Nothing references the deleted X, Facebook or Instagram accounts.

## 3. Voice and privacy

On the final text: no em dashes (U+2014), emojis or AI bullet walls; no location names; no employer or client names on LinkedIn beyond public end clients; no personal data of others; no secrets, keys, tokens or internal URLs. Older articles must not reflect knowledge from after their publication date.

## 4. Platform fit

LinkedIn collapses code indentation and does not render markdown; test the paste or use a one-line install plus README link. Limits: post 3,000 chars, comment 1,250; count. The first URL becomes a card that can replace an attached image; choose on purpose.

## 5. Follow-through

If publishing waits on something (CI, release, review), say plainly that a background watcher dies with the session, or use a scheduled agent. Never report "posted" or "live" until the public page is reloaded and seen; give the link.

## Output

An approval packet readable in under a minute: (1) exact final content, ready to paste, and where it goes; (2) checklist with PASS / FAIL / CAN'T VERIFY and one line of evidence each; (3) anything needing his judgment (tone, whether to post, timing); (4) one line: ready for approval, or not and why. Never publish from this skill; publishing needs his explicit yes in chat every time.
