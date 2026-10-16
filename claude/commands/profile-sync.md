Keep Lavkesh's profile consistent on every surface (resume, LinkedIn, lavkesh.com, GitHub/GitLab README, Indeed, Dice, Monster). Use when any one changes (role, cloud, title, dates) or when tailoring a resume. Browser steps follow /browser-lean. Audit read-only first, change only what drifted, report each surface as in sync, changed, or needs the user.

## Sources of truth

- Resume base: `C:\Users\dlavk\Downloads\Resume_Lavkesh_Dwivedi_latest.docx`. Tailored copies: `<Name>_Resume_<Role>.docx`, no tech names in filenames. The long `Lavkesh_Dwivedi_Resume` (docx+PDF) is the default for boards and recruiters. `_Short` (docx+PDF, trimmed, no HackerRank certs) only when asked. Never swap or upload the short one to a board. Apply every change to both.
- LinkedIn: linkedin.com/in/lavkesh. Site: repo `C:\Claude\Projects\lavkesh`, profile text in `index.html` (title, meta/OG/Twitter, JSON-LD `jobTitle`, About) and persona in `scripts/voice.py`; never edit articles (timeline rule); check `origin/main`.
- GitHub/GitLab: repo `C:\Claude\Projects\profile-readme`, remotes `origin` and `gitlab`; pull first, local can be stale. Read published README with `gh api -H "Accept: application/vnd.github.raw" repos/lavkeshdwivedi/lavkeshdwivedi/readme`; bio via `gh api user --jq .bio` / `-X PATCH user -f bio=...`. GitLab bio, job title (Forward Deployed Engineer), organization (blank) only at gitlab.com/-/user_settings/profile, bio matching GitHub.
- Boards: Indeed (profile.indeed.com), Dice (dice.com/profile), Monster (monster.com/profile/detail). Each carries the current resume plus a structured summary and work history that must match it. May need the user to log in.

## Current facts

- Headline: Forward Deployed Engineer | Forward Deployed AI Lead | Python, .NET, GCP, Azure & AWS | Regulated Industries
- Schwab, Sr. AI Full Stack Engineer, Sep 2024 to Sep 2026: Azure AND Google Cloud together (Azure OpenAI, Vertex AI with Gemini, GKE with Helm, Harness), GitHub and BitBucket, CI/CD on Bamboo, Harness, GitHub Actions. Never replace one cloud with the other.
- Microsoft (Contract), AI Solutions Architect, Apr 2024 to Sep 2024: Azure OpenAI, Semantic Kernel, LangChain, Cosmos DB vector store, Azure AI Search, Document Intelligence, Video Indexer, Service Bus, Entra ID.
- Philips Healthcare, Jul 2022 to Mar 2024: AWS serverless (Lambda, Step Functions, EventBridge, SQS/SNS, S3, DynamoDB, CloudWatch, Terraform), HL7/DICOM; 30% throughput, 40% PACS accessibility, 100% DICOM interoperability, 99.8% uptime.
- AINS from Jul 2011 (CA Technologies internship Feb to Jun 2011).
- Contract only, C2C through his employer. Never name the employer/vendor (CloudTern, Accionlabs, Cognizant) anywhere. The C2C availability line was removed from resume, boards and LinkedIn About on 2026-10-08, do not re-add. PolisIQ and Ansera only on site/README, never the resume.
- Research: cite SSRN only; arXiv never published; do not claim seven attack categories (C5 to C7 were a local pilot).

## Rules

- Resume is employment only: no personal projects, open source or research. No em dashes, no location names, human voice, plain AI (no SI wording).
- Recycle Bin, not permanent delete. If the user edited a file, edit in place, never regenerate over it.
- Site/README: git worktree, one squashed commit, author `Lavkesh Dwivedi <iamlavkesh@gmail.com>`, no Co-Authored-By, open a PR, merge only when asked, JSON-LD must parse, preserve line endings (`newline=''`).

## Resume checklist

1. Edit docx in place with python-docx at run level; clone paragraphs for new bullets.
2. Tech timeline: every tool must exist under that name in that role's dates (Azure AI Services after Jul 2023; VSTS before Sep 2018; Entra ID from Jul 2023; .NET 8 from Nov 2023).
3. ATS: no tables, text boxes, images, header/footer text; standard headings; strongest outcome first; every number also on LinkedIn.
4. Render to PDF via Word COM; confirm page count, no wrapped skills row.

## LinkedIn (Chrome)

- Prefs: Open to work Recruiters only, Remote+Hybrid+On-site, Contract, relocation, US + DFW; no Forward Deployed Engineer in title list, use Software Engineer. Decline job-alert prompts.
- About names no clients or employers ("a major US brokerage", "a large enterprise software company", "a global healthcare technology company", "CRM platforms"); no C2C line. Client names stay in Experience. Read About at `/in/lavkesh/edit/forms/summary/new/`, Experience at `/in/lavkesh/details/experience/`, leave without saving.
- Turn "Notify network" off before saving. Adding a position can overwrite the headline, recheck. Limits: role 2,000 chars, About 2,600. Skills at the 100 cap, 4 to 6 per role, five About top skills (Agentic AI Development, Enterprise Architecture, Technical Leadership, GCP, Microsoft Azure). Leave fields the user cleared (employment type, location on client roles).
- Edits: description and About are contenteditable. Select the range in JS and `execCommand('insertText')`, then press a real key and confirm the counter changed, or the save drops it. Reload and re-read after saving.

## Boards (Chrome)

- Keep one resume (latest long). `file_upload` only accepts the job tmp folder or an /add-dir folder, so copy the file there. To avoid the native picker, patch `HTMLInputElement.prototype.click` and `showPicker` before clicking upload. Dice: File options, Replace, Upload works; 2 MB cap (use PDF). Monster upload does not replace; user uploads by hand. Indeed freezes screenshots, check by hand.
- Structured profile equals resume: same summary, title Forward Deployed Engineer, each role with title, client, dates, bullets.
- Prefs: contract only (Dice: Contract - Corp-to-Corp, rate $95/hr, one short preferred title with .NET and Python; never W2, C2H, full-time), Remote+Hybrid+On-site, relocation. Schwab title on Dice is Sr. AI Full Stack Engineer.
- No visa hook: Dice work authorization "Prefer not to answer", Monster empty, Indeed has none.
- Dice "Scan and upload" adds junk skill chips (Typing, Drafting, AWS Secrets Manager), prune; preference chips need real clicks. Indeed: one skill per form; Claude's skill deletes do not persist, leave to user; keep "Open to all jobs". Monster: no Contract type (use Remote), native value setter plus input/change events for text, comboboxes need real typing (state before city), never script skill deletes, cookie banner covers lower left; three titles: Forward Deployed Engineer, Solutions Architect, .NET Python AI Engineer; relocation Yes.
- Reload each site after saving and re-read fields.

Finish by reporting what changed per surface and what the user must do by hand.
