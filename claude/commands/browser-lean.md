Token-lean rules for Chrome and computer use. Apply to every browser task (LinkedIn, job boards, any site). Screenshots and page dumps are the biggest token cost, so read as text first.

## Order of preference (cheapest first)

1. API or MCP connector (Gmail, Calendar, Drive) beats the browser. Use the browser only when no connector covers it, or when a connector errors.
2. javascript_tool with a narrow query: return `innerText` of one element, or a short JSON of the few fields you need. Never return `document.body.innerText` for a feed. Cap length with `.slice(0, 1500)`.
3. find or read_page filtered to interactive elements, then act by ref.
4. get_page_text only on pages that are mostly one article or thread.
5. Screenshot last, and only to confirm identity before a send, a delete or a post. Zoom into the region, never full-page on a long list.

## Habits

- Load tools once: ToolSearch `select:` with every tool you expect (browser_batch, tabs_context_mcp, tabs_create_mcp, navigate, find, javascript_tool, get_page_text, computer) in one call.
- Batch with browser_batch: click, type, key, wait in one call instead of one call each. One call per thread, not per action.
- Reuse the open tab. Do not open new tabs per item. Never reuse tab ids from an earlier session.
- No polling screenshots. After a click, read the one value that proves it worked (JS), not the whole page.
- Lists: read the top N rows once through JS, note ids, and do not re-read the list after each action. The LinkedIn list reorders after a send, so re-find by name, not by position.
- Heavy scroll plus screenshots froze the LinkedIn tab before. Read with JS instead of scrolling and capturing.
- Stop after 2 or 3 failures of the same action and report, do not loop.
- Avoid clicking checkbox refs (caused an accidental multi-select).

## Session hygiene

- For multi-thread jobs, keep a plain list in chat (name, status) and update it once per batch. Use TaskCreate only for jobs with 5 or more distinct steps.
- Do not re-state tool output at length. Report decisions and results in a few lines.
- Do not re-read memory or skill files already in context. Do not spawn subagents unless asked.
- Prefer a fresh short session over a very long one. Summaries drop detail, and long contexts re-bill every turn.
