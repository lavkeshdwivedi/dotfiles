Write and publish one LinkedIn feed post in Lavkesh's voice on the biggest story of the day in his lanes, with a contextual image. Argument (topic or link) skips discovery. Browser steps follow /browser-lean.

Authorized 2026-10-03 to post on its own when every check passes. If any check fails or cannot be verified, stop and hand him the packet: post text in a code block, image path, source link, checklist.

## 0. Never look automated

This rule sits above all others. No repeated phrasings, no template comments, never the same image style twice in a row. Max 3 posts per 7 days, at least 36 hours apart: check `C:\Claude\Projects\lavkesh\data\linkedin-ledger.json` plus his activity page for hand posts; if the cap says not now, stop and say so. Wait a minute or two before the first comment, and write it fresh in his words.

## 1. Find the story

Lanes in order: agentic AI/frameworks, AI security and guardrails, AI in regulated industries (DORA, EU AI Act), forward deployed engineering, then broader engineering/cloud/career. Search the last 24 to 48 hours (WebSearch per lane plus `lavkesh\data\sources.yml`). Pick one story where he has a non-obvious take from his work; no post beats a weak post. Skip anything already posted (https://www.linkedin.com/in/lavkesh/recent-activity/all/, not /in/lavkeshdwivedi; and last week of `lavkesh\articles`). Read the primary source and keep its URL.

## 2. Draft

Read his last few posts first (Sep 30 "software engineering is alive", Oct 2 kognios are the models; the Oct 3 DNS post failed: choppy lines, news recap).

- First person, paragraphs of 3 to 5 sentences, 180 to 300 words, short punchy close allowed. Opinion in the first line, news compressed to a sentence or two as evidence, then what it means from his work (agent escape/guardrail research, kognios, regulated delivery). One idea, take a side.
- Plain text, no links, emojis, em dashes, bullets, employer/client or location names. Only facts on record or from the source; frame anything else as a general pattern.
- Apply banned phrases from `POST_RULES` in `lavkesh\scripts\voice.py` (ignore its 60 to 140 word cap). Run `voice.find_banned_phrases(text)` (must be `[]`) and scan for U+2014.
- Audience is engineers plus hiring managers and leaders (CTO, CIO, CISO, risk): one plain sentence for the technical core, name the business stake (risk, cost, audit, regulator), show him as the person who ships it. Never mention recruiters, hiring or being open to roles. End on a firm statement, never a question. Up to three specific hashtags last (#AgenticAI #AISecurity #AIGovernance), never #Hiring or #OpenToWork.

## 3. Image

Change style every post; check the last post's image first. Options: whiteboard board (mechanisms; refs `scratch\kognios-board.html`, `li-dns-board.html`), hand-drawn doodle (`kognios-doodle.html`), terminal/code window, chart (load `dataviz`, real figures only), annotated source screenshot, incident timeline card, editorial typographic card (weakest, `/blissful-article` style).

Look human-made and bright (paper, ink, marker, a marked-up page; ref `scratch\li-si-dict.html`); no dark neon, glows, gradients or AI-chip art. Must make sense without the post, every number from the source, bold two-line headline, small source credit, corner credit "Lavkesh Dwivedi · agentic AI, AI security, regulated industries", no fake Follow button. 4:3, 1200x900 rendered at 1.5x. Build HTML at `scratch\li-<slug>.html` with fonts from `scratch\fonts`, render with Playwright (`chromium.launch(channel="msedge", headless=True)`), open the PNG and fix overlaps and clipping.

## 4. Human check

Run `/human-check` via a fresh subagent that sees only post text, image, source URL and checklist. Every item must PASS; fix and rerun on FAIL; CAN'T VERIFY means send the packet instead of posting.

## 5. Post through Chrome (not post_linkedin.py)

1. linkedin.com/feed, "Start a post", confirm author is Lavkesh Dwivedi.
2. Image: patch `HTMLInputElement.prototype.click` to capture file inputs, click the media button from JS, `file_upload` the JPEG on the input ref, Next.
3. Text: focus the editor, one `document.execCommand('insertText', false, text)`; never type long text. Check paragraph breaks.
4. Visibility Anyone. Text and image must be final, since "Edited" shows and he deletes edited posts. Click Post.
5. First comment: "Source, <publisher>'s <report>: <url>", blank line, then a fresh follow line ending with https://www.linkedin.com/in/lavkesh/?followMember=lavkesh. Links stay out of the body.
6. Reload his activity page, confirm post, image and comment, then report it with the post link.
