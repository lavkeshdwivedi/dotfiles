Write and publish a hand-written Blissful Bytes article on lavkesh.com, then cross-post it to the Blissful Bytes LinkedIn newsletter. Use when the user gives a topic or angle for a post (the automated weekly generator is for LLM-drafted pieces; this is for articles written in the session).

## 1. Draft in Lavkesh's voice

- Read the rules first: `scripts/voice.py` (`ARTICLE_RULES`, `TITLE_RULES`, `BANNED_PHRASES`) and the Writing Voice and Timeline sections of the repo `CLAUDE.md`.
- First person, opens on a concrete hook, real opinions, concrete technical detail. No numbered lists posing as prose, no conclusion paragraph, never end on a question to the reader or a moral.
- Never fabricate anecdotes, numbers, or events. Use only facts on record (resume, LinkedIn, the biography in `voice.py`). Frame anything else as a general pattern, not a story that happened.
- Do not name the current employer. Past industries are fine. No specific location names. No em dashes.
- Title: 45 to 80 characters, no colon, semicolon, parentheses, or em dash, none of the banned title formulas.
- Write `{"title", "excerpt", "cats", "body_paragraphs"}` to a JSON file in the job tmp directory. Aim for 700 to 1,100 words across 8 to 10 paragraphs.

## 2. Check before building

From the site repo root:

```python
import sys; sys.path.insert(0, "scripts"); sys.argv = ["x"]
import voice, generate_article as g
voice.find_banned_phrases(text)      # must be []
voice.check_excerpt(excerpt)          # must be None
g._title_looks_aiish(title)           # must be None
```

Also confirm zero em dashes and that the last paragraph does not match the generator's conclusion-ending regex (question mark ending, "not X but Y", "reminder that", leading "perhaps").

## 3. Build into the site (in a git worktree off origin/main)

- Slug: short form plus `-lavkesh-dwivedi-<YYYY-MM-DD>` (for example `forward-deployed-still-software-engineer-lavkesh-dwivedi-2026-09-30`). Set it explicitly; `g.slugify` truncates long titles mid-word.
- Write a small script (complex inline Python gets blocked in worktree sessions) that loads the JSON, builds the article dict (`slug`, `title`, `date` as `%b %d, %Y`, `date_iso`, `excerpt`, `cats`, `read_time` at 230 wpm, `body_paragraphs`), writes `g.build_article_html(article, len(existing) + 1, existing[-1]["slug"])` to `articles/<slug>.html`, appends the catalog entry, then `g.save_articles(...)` and `g.rebuild_indexes()`.
- Run `python scripts/generate_sitemap.py` (feed.xml, sitemap.xml, stats.json). The "pattern not found, skipping" lines from rebuild are normal.
- Previous/next links are fixed by `fix_article_nav.py` in the Deploy Pages workflow, so do not hand-edit older articles.
- To change a title later, rebuild the whole page from the JSON with `build_article_html` so the inline hero SVG updates too; keep the slug.

## 4. Ship

- One commit, author `Lavkesh Dwivedi <iamlavkesh@gmail.com>`, no Co-Authored-By. Push the branch, open a PR, merge when the user asks. Check `gh run list` for the Deploy Pages run.

## 5. LinkedIn newsletter

- Use `python scripts/crosspost_linkedin_newsletter.py --slug <slug> --dry-run` first, then without `--dry-run`. It records the post in `data/crosspost-history.json`; commit that file afterwards.
- WARNING: the script runs `taskkill /f /im msedge.exe` to relaunch Edge with remote debugging on the user's profile. Check `tasklist` for msedge and get the user's OK before the real run, because it closes every open Edge window.
