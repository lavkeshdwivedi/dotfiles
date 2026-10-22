Write and publish one LinkedIn feed post in Lavkesh's voice on the biggest story of the day in his lanes, text only (no image, since 2026-10-13). Argument (topic or link) skips discovery. Browser steps follow /browser-lean.

Authorized 2026-10-03 to post on its own when every check passes. If any check fails or cannot be verified, stop and hand him the packet: post text in a code block, source link, checklist.

## 0. Never look automated

This rule sits above all others. No repeated phrasings, no template comments, vary the opening and shape of each post. Max 3 posts per 7 days, at least 36 hours apart: check `C:\Claude\Projects\lavkesh\data\linkedin-ledger.json` plus his activity page for hand posts; if the cap says not now, stop and say so. Wait a minute or two before the first comment, and write it fresh in his words.

## 1. Find the story

Lanes in order: agentic AI/frameworks, AI security and guardrails, AI in regulated industries (DORA, EU AI Act), forward deployed engineering, then broader engineering/cloud/career. Search the last 24 to 48 hours (WebSearch per lane plus `lavkesh\data\sources.yml`). Pick one story where he has a non-obvious take from his work; no post beats a weak post. Skip anything already posted (https://www.linkedin.com/in/lavkesh/recent-activity/all/, not /in/lavkeshdwivedi; and last week of `lavkesh\articles`). Read the primary source and keep its URL.

## 2. Draft

Read his last few posts first (Sep 30 "software engineering is alive", Oct 2 kognios are the models; the Oct 3 DNS post failed: choppy lines, news recap).

- First person, paragraphs of 3 to 5 sentences, 180 to 300 words, short punchy close allowed. Opinion in the first line, news compressed to a sentence or two as evidence, then what it means from his work (agent escape/guardrail research, kognios, regulated delivery). One idea, take a side.
- Plain text, no links, emojis, em dashes, bullets, employer/client or location names. Only facts on record or from the source; frame anything else as a general pattern.
- Apply banned phrases from `POST_RULES` in `lavkesh\scripts\voice.py` (ignore its 60 to 140 word cap). Run `voice.find_banned_phrases(text)` (must be `[]`) and scan for U+2014.
- Audience is engineers plus hiring managers and leaders (CTO, CIO, CISO, risk): one plain sentence for the technical core, name the business stake (risk, cost, audit, regulator), show him as the person who ships it. Never mention recruiters, hiring or being open to roles. End on a firm statement, never a question. Up to three specific hashtags last (#AgenticAI #AISecurity #AIGovernance), never #Hiring or #OpenToWork.

## 3. No image

Posts are text only from 2026-10-13 (his call). Do not generate, render or attach any image, doodle, chart or card. The old image recipe is gone from this skill; the board and doodle files in `scratch` stay on disk but are unused.

## 4. Human check

Run `/human-check` via a fresh subagent that sees only post text, source URL and checklist. Every item must PASS; fix and rerun on FAIL; CAN'T VERIFY means send the packet instead of posting.

## 5. Post through Chrome (not post_linkedin.py)

1. linkedin.com/feed, "Start a post", confirm author is Lavkesh Dwivedi.
2. Text: focus the editor, one `document.execCommand('insertText', false, text)`; never type long text. Check paragraph breaks. Attach no media.
3. Visibility Anyone. Text must be final, since "Edited" shows and he deletes edited posts. Click Post.
4. First comment: "Source, <publisher>'s <report>: <url>", blank line, then a fresh follow line ending with https://www.linkedin.com/in/lavkesh/?followMember=lavkesh. Links stay out of the body.
5. Reload his activity page, confirm post and comment, then report it with the post link.
