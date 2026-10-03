Write and publish one LinkedIn feed post in Lavkesh's voice, reacting to the biggest story of the day in the areas he writes about, with a contextual image from the story itself. Pass a topic or link as the argument to skip discovery; with no argument, find the story.

Lavkesh authorized this skill on 2026-10-03 to post on its own when every check passes ("post if all good"). If any check fails or can't be verified, stop and hand him the approval packet instead.

## 1. Find the story of the day

His lanes, in priority order: agentic AI and agent frameworks, AI security and guardrails (prompt injection, agent escape, red teaming), AI in regulated industries (financial services, healthcare, compliance like DORA or the EU AI Act), forward deployed engineering and how AI work actually ships, then broader engineering, architecture, cloud, and career.

- Search the last 24 to 48 hours: WebSearch for each lane, plus the feeds in `C:\Claude\Projects\lavkesh\data\sources.yml` (Simon Willison, Anthropic, DeepMind, InfoQ, and the rest).
- Pick the one story where he has a real, non-obvious take grounded in his work. A big launch everyone is already summarizing is worth less than a sharper story he can add a spine to. If nothing clears that bar, say so and don't post. No post beats a weak post.
- Skip anything he already posted about. Check his recent activity at https://www.linkedin.com/in/lavkeshdwivedi/recent-activity/all/ and the last week of `C:\Claude\Projects\lavkesh\articles`.
- Read the primary source, not just the coverage. Note the source URL.

## 2. Draft in his voice

- Rules: `POST_RULES` and `_REACTIVE_SLOT_GUIDANCE` in `C:\Claude\Projects\lavkesh\scripts\voice.py`. In short: scroll-stopping first line, short paragraphs with blank lines between them, take a side, one idea, 50 to 140 words, plain text, no links in the body, no hashtags, no emojis, no em dashes, no bullet lists.
- Name the source and story within the first two lines. He is reacting, not reporting.
- Never fabricate anecdotes, numbers, or events. Only facts on record (resume, LinkedIn, the biography in `voice.py`) or from the source. Frame anything else as a general pattern.
- No employer or client names, no location names.
- Run `voice.find_banned_phrases(text)` from the lavkesh repo (must be `[]`) and scan for U+2014.

## 3. Contextual image

The image comes from the story, so the reader sees what he's reacting to.

1. First choice: the source page's own preview image (`og:image` / `twitter:image`). Download it to the session scratchpad.
2. If missing, tiny (under 800px wide), a logo-only tile, or a paywall placeholder: use a relevant openly licensed photo (Wikimedia Commons, Unsplash, or the vendor's press kit) that actually depicts the subject.
3. Last resort: an editorial typographic card in the Blissful Bytes house style (see `/blissful-article`, cover image section), with a short punchy headline about the story.

Open the image and look at it before using it. Reject anything with someone else's watermark, a face that isn't central to the story, or text that contradicts the post. Convert to JPEG under 5 MB.

## 4. Human check

Run `/human-check` on the final post, the image, and the source link. Every item must PASS. The source URL must return 200 and say what the post claims.

## 5. Post through Chrome

Use Claude in Chrome. Don't use the repo's `post_linkedin.py`; the web UI is what he trusts.

1. Open https://www.linkedin.com/feed/, click "Start a post", and confirm the author shows as Lavkesh Dwivedi (not a page).
2. Image: patch `HTMLInputElement.prototype.click` in the page to capture file inputs without opening the native picker, click the media button from JS, find the input ref, `file_upload` the JPEG, then Next in the editor dialog.
3. Text: focus the post editor and run `document.execCommand('insertText', false, text)` once. Never type long text with keystrokes. Check the blank lines between paragraphs survived.
4. Visibility is Anyone. Click Post.
5. Add the source URL as the first comment on the post, with one short line of lead-in (for example "Source:" plus the link).
6. Reload his recent activity and confirm the post is there with the image and the comment. Only then report it as posted, with the post link.

If he hasn't authorized posting (a check failed, or he asked for a draft), stop after step 4 and hand him the packet: post text in a plain code block, image path, source link, checklist.
