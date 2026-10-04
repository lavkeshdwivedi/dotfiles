Write and publish one LinkedIn feed post in Lavkesh's voice, reacting to the biggest story of the day in the areas he writes about, with a contextual image made for the story. Pass a topic or link as the argument to skip discovery; with no argument, find the story.

Lavkesh authorized this skill on 2026-10-03 to post on its own when every check passes ("post if all good"). If any check fails or can't be verified, stop and hand him the approval packet instead.

## 0. Never look automated, and keep the pace human

Nobody reading his feed may ever be able to tell any of this is automated. That rule sits above every other one here.

- No repeated phrasings across posts or comments, no stock comment template, and never the same image style twice in a row.
- At most 3 posts in any 7 days and at least 36 hours between posts. Check `C:\Claude\Projects\lavkesh\data\linkedin-ledger.json` (every post and comment made through the API is logged there) plus his activity page for anything posted by hand. If the cap says not now, stop and say so.
- Wait a minute or two after posting before adding the first comment, the way a person would.
- Write the first comment fresh each time in his words. Don't reuse "Source:" or "Follow along" as fixed openers.

## 1. Find the story of the day

His lanes, in priority order: agentic AI and agent frameworks, AI security and guardrails (prompt injection, agent escape, red teaming), AI in regulated industries (financial services, healthcare, compliance like DORA or the EU AI Act), forward deployed engineering and how AI work actually ships, then broader engineering, architecture, cloud, and career.

- Search the last 24 to 48 hours: WebSearch for each lane, plus the feeds in `C:\Claude\Projects\lavkesh\data\sources.yml` (Simon Willison, Anthropic, DeepMind, InfoQ, and the rest).
- Pick the one story where he has a real, non-obvious take grounded in his work. A big launch everyone is already summarizing is worth less than a sharper story he can add a spine to. If nothing clears that bar, say so and don't post. No post beats a weak post.
- Skip anything he already posted about. Check his recent activity at https://www.linkedin.com/in/lavkesh/recent-activity/all/ (not /in/lavkeshdwivedi, which is a different person) and the last week of `C:\Claude\Projects\lavkesh\articles`.
- Read the primary source, not just the coverage. Note the source URL.

## 2. Draft in his voice

Model the post on his own best posts, not on generic LinkedIn style. Read his last few posts on the activity page first; the Sep 30 "software engineering is alive" post and the Oct 2 kognios post are the reference. The 2026-10-03 DNS post failed this: choppy one-line paragraphs and a pure news recap with no stake of his own.

- First person, fuller paragraphs of three to five sentences, 180 to 300 words. One short punchy line is fine as the close, not as the shape of the whole post.
- Open with the story and the tension in one or two sentences, explain what actually happened with the concrete details, then say what it means from his own work: his agent escape and guardrail research, kognios, forward deployed delivery in regulated industries. Only tie to things that are true and on record.
- Lead with his opinion in the first line, not the news. The news is evidence for the take, compressed to a sentence or two. A post that reads like a recap gets rewritten.
- Take a side. One idea. Plain text, no links in the body, no emojis, no em dashes, no bullet lists.
- Also apply the banned phrases and rough-edges guidance in `POST_RULES` (`C:\Claude\Projects\lavkesh\scripts\voice.py`), but ignore its 60 to 140 word cap and one-sentence paragraphs.
- Never fabricate anecdotes, numbers, or events. Only facts on record (resume, LinkedIn, the biography in `voice.py`) or from the source. Frame anything else as a general pattern.
- No employer or client names, no location names.
- Run `voice.find_banned_phrases(text)` from the lavkesh repo (must be `[]`) and scan for U+2014.

### Write for the people he wants to reach

Every post has to pull in engineers and also the people who hire and buy: recruiters, hiring managers, and senior leaders (CTOs, CIOs, CISOs, heads of AI, risk and compliance leads), especially in regulated industries.

- Explain the technical core in one plain sentence a non-engineer can follow, then go deep.
- Name the business stake out loud: risk, cost, audit, downtime, a regulator asking questions. Leaders share posts that give them a line to repeat in their own meeting.
- Show him as the person who ships and leads this work. Show it through what he built, studied, or decided, never by saying he's open to work or asking for roles. Never mention recruiters, hiring, job searching, or being open to roles.
- End on a firm statement both a practitioner and an executive could repeat in their own meeting. Never end with a question.
- Up to three specific hashtags at the very end (for example #AgenticAI #AISecurity #AIGovernance). Specific ones only, never #Hiring, #OpenToWork, or a pile of generic tags.

## 3. Contextual image

Make an image that explains the story, and switch the style every post so the feed never looks templated. Check the image on his previous post and pick a different style that fits this story's content:

- Whiteboard board (FigJam look: dotted grid, sticky notes, cursors, arrows, a stamp, a comment pin): for mechanisms, architectures, how something broke or got around a control. Reference: `C:\Claude\Projects\scratch\kognios-board.html` and `li-dns-board.html`.
- Hand-drawn doodle (Caveat / Patrick Hand fonts, sketchy lines): for a personal lesson or a simple before/after. Reference: `kognios-doodle.html`.
- Terminal or code window: when the story is a command, config, log line, or API change.
- Chart: when the story is a number or trend. Load the `dataviz` skill first, and plot real figures from the source only.
- Annotated screenshot of the source (page, product, or paper figure) with arrows and callouts: when the artifact itself is the news.
- Incident timeline or postmortem card: for outages and security incidents with timestamps.
- Editorial typographic card (Blissful Bytes house style from `/blissful-article`): only for pure opinion pieces with nothing to diagram. It's the weakest option.

Look human-made and bright: paper, ink, marker, whiteboard, a marked-up page. No dark neon, glows, gradients, or stock "AI chip" art; if it could pass for AI-generated, redo it. Reference: `scratch\li-si-dict.html` (a dictionary page edited in red pen).

Rules for every style: the image has to make sense to someone who never reads the post, every number and label on it comes from the source, a bold two-line headline, a small source credit, 4:3 landscape at 1200x900 (rendered at 1.5x). LinkedIn's profile activity carousel shows images in a roughly 4:3 frame and pads anything else with black bars, so 16:9 and square both look awkward there; 4:3 fills it and also shows full size in the feed. Every image carries a small credit line in a corner ("Lavkesh Dwivedi · agentic AI, AI security, regulated industries") so reshares still carry his name. Never draw a fake Follow button: nothing in a LinkedIn image is clickable. Build it as HTML in `C:\Claude\Projects\scratch\li-<slug>.html` with the local fonts in `scratch\fonts`, render it with Playwright (`chromium.launch(channel="msedge", headless=True)`), then open the PNG and look at it. Fix overlaps, clipped text, and crowding before using it.

## 4. Human check

Run `/human-check` on the final post, the rendered image, and the source link, every time, before anything goes out. Hand the review to a fresh subagent that sees only the post text, the image file, the source URL, and the human-check checklist, not the drafting. It must check every number and claim in both the text and the image against the source, read the post the way a recruiter and a CTO would, and look at the image for overlaps, clipped text, and unreadable labels. Every item must PASS. Fix and re-run on any FAIL; a CAN'T VERIFY means stop and send Lavkesh the packet instead of posting.

## 5. Post through Chrome

Use Claude in Chrome. Don't use the repo's `post_linkedin.py`; the web UI is what he trusts.

1. Open https://www.linkedin.com/feed/, click "Start a post", and confirm the author shows as Lavkesh Dwivedi (not a page).
2. Image: patch `HTMLInputElement.prototype.click` in the page to capture file inputs without opening the native picker, click the media button from JS, find the input ref, `file_upload` the JPEG, then Next in the editor dialog.
3. Text: focus the post editor and run `document.execCommand('insertText', false, text)` once. Never type long text with keystrokes. Check the blank lines between paragraphs survived.
4. Visibility is Anyone. Get the text and image final before clicking Post: LinkedIn shows "Edited" to every visitor, and Lavkesh won't keep an edited post (fixing one means he deletes it and you repost). Click Post.
5. Add the first comment: the source link, a blank line, then a follow line with the real follow link, for example:
   "Source, <publisher>'s <report>: <url>

   I'll keep breaking down <topic> like this one. Follow along: https://www.linkedin.com/in/lavkesh/?followMember=lavkesh"
   Links stay out of the post body (they cut reach); the comment is where they go. His profile already has "Make follow primary" on and followers set to Everyone, so the real Follow button shows next to his name for non-connections.
6. Reload https://www.linkedin.com/in/lavkesh/recent-activity/all/ and confirm the post is there with the image and the comment. Only then report it as posted, with the post link.

If he hasn't authorized posting (a check failed, or he asked for a draft), stop after step 4 and hand him the packet: post text in a plain code block, image path, source link, checklist.
