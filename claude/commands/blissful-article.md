Write and publish a hand-written Blissful Bytes article on lavkesh.com, then cross-post to the Blissful Bytes LinkedIn newsletter. Use when he gives a topic or angle (the weekly generator is for LLM-drafted pieces). Browser steps follow /browser-lean.

## 1. Draft

- Read `scripts/voice.py` (`ARTICLE_RULES`, `TITLE_RULES`, `BANNED_PHRASES`) and the Writing Voice and Timeline sections of the site repo `CLAUDE.md`.
- First person, concrete hook, real opinions, technical detail. No numbered lists posing as prose, no conclusion paragraph, never end on a question or a moral. No fabricated anecdotes or numbers: only facts on record, anything else framed as a general pattern. No current employer, no location names, no em dashes.
- Title 45 to 80 chars, no colon, semicolon, parentheses, em dash or banned formula. Write `{"title","excerpt","cats","body_paragraphs"}` JSON to the job tmp dir, 700 to 1,100 words, 8 to 10 paragraphs.

## 2. Check

From the site repo root: `sys.path.insert(0,"scripts"); sys.argv=["x"]; import voice, generate_article as g`. Need `voice.find_banned_phrases(text) == []`, `voice.check_excerpt(excerpt) is None`, `g._title_looks_aiish(title) is None`, zero em dashes, and a last paragraph not matching the generator's conclusion regex (question ending, "not X but Y", "reminder that", leading "perhaps").

## 3. Build (git worktree off origin/main)

- Slug: short form + `-lavkesh-dwivedi-<YYYY-MM-DD>`, set explicitly (`g.slugify` truncates mid-word).
- Use a small script file (inline Python gets blocked in worktrees): load JSON, build the article dict (`slug`, `title`, `date` `%b %d, %Y`, `date_iso`, `excerpt`, `cats`, `read_time` at 230 wpm, `body_paragraphs`), write `g.build_article_html(article, len(existing)+1, existing[-1]["slug"])` to `articles/<slug>.html`, append the catalog entry, `g.save_articles(...)`, `g.rebuild_indexes()`. Then `python scripts/generate_sitemap.py`. "pattern not found, skipping" lines are normal.
- Prev/next links are fixed by `fix_article_nav.py` in Deploy Pages; do not hand-edit older articles. To retitle later, rebuild the page from JSON (keeps the hero SVG in sync), keep the slug.
- Ship: one commit, author `Lavkesh Dwivedi <iamlavkesh@gmail.com>`, no Co-Authored-By, push branch, open PR, merge only when he asks, check `gh run list` for Deploy Pages.

## 4. LinkedIn newsletter (by hand in Chrome)

Never use the repo crosspost scripts (unreliable, no cover, they taskkill every Edge window). Newsletter: https://www.linkedin.com/newsletters/blissful-bytes-7173171984510468097/

No cover image on any LinkedIn article (his rule 2026-10-13, repeated 2026-10-15). Skip cover generation and upload entirely.

Format (modelled on https://www.linkedin.com/pulse/how-do-large-language-models-work-university-of-phoenix-ponmc/, his request 2026-10-16): sentence-case title, often a plain question; no subtitle; a short two-paragraph intro that opens on one concrete image or analogy; then `<h3>` section headings (some phrased as questions, later ones short topic labels), one to three short paragraphs each, uneven lengths. Use one bulleted list with a bold label before a colon only where the content is a real list (the article's uses, stages, options), not to chop prose. End on the last section, then the `Also on lavkesh.com` line. Keep the voice rules from step 1; the site version stays plain paragraphs.

Publish:
1. https://www.linkedin.com/article/new/, confirm author "Blissful Bytes".
2. Title: `#article-editor-headline__textarea` (not the first textarea, that is the caption) via native value setter plus `input` and `change` events; caption stays empty. Never type long text with keystrokes.
3. Body: `document.execCommand('insertHTML', false, html)` once on the "Article editor content" contenteditable, `<h3>` per heading, `<p>` per paragraph, `<ul><li><b>Label:</b> text</li></ul>` for the list, final paragraph `Also on lavkesh.com: <link>`.
4. Wait for autosave, reload `/article/edit/<id>/`, verify title, headings, paragraph count, no em dashes, no cover.
5. Next from JS; in the dialog insert a 2 to 3 sentence intro in his voice (`execCommand('insertText')`), audience "Anyone + Subscribers", Publish. Confirm "Published Just now" on the newsletter page.
