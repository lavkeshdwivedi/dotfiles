Keep Lavkesh's professional profile consistent everywhere it appears: the tailored resume, LinkedIn, lavkesh.com, the GitHub profile README, and the GitLab profile. Use this whenever any one of them changes (new role, new cloud, new title, new dates) or when asked to tailor a resume for a posting.

## Sources of truth

- **Resume base:** `C:\Users\dlavk\Downloads\Resume_Lavkesh_Dwivedi_latest.docx`. Tailored copies are named `<Name>_Resume_<Role>.docx` (for example `Lavkesh_Dwivedi_Resume_FDE.docx`). Never put tech names like GCP or AWS in a filename.
- **LinkedIn:** linkedin.com/in/lavkesh (headline, About, Experience, top skills).
- **Site:** repo `C:\Claude\Projects\lavkesh` (lavkeshdwivedi/lavkesh). Profile text lives in `index.html` (title, meta/OG/Twitter descriptions, JSON-LD `jobTitle` and description, About bio) and the persona line in `scripts/voice.py`. Articles are never edited for profile changes (timeline rule).
- **GitHub and GitLab:** repo `C:\Claude\Projects\profile-readme` has two remotes, `origin` (GitHub) and `gitlab`. One README change covers both. Account bios: GitHub via `gh api -X PATCH user -f bio=...`; GitLab bio, job title, and organization only through gitlab.com/-/user_settings/profile (the API `PUT /user` returns 404 for non-admins).

## Current career facts (update this list when they change)

- Headline: Forward Deployed Engineer | Forward Deployed AI Lead | Python, .NET, GCP, Azure & AWS | Regulated Industries
- Charles Schwab, Sr. AI Full Stack Engineer, Sep 2024 to Sep 2026: Azure AND Google Cloud together (Azure OpenAI, Vertex AI with Gemini, GKE with Helm, Harness), code across GitHub and BitBucket, CI/CD on Bamboo, Harness, and GitHub Actions during an org pipeline transition. Never replace one cloud with the other.
- Microsoft (Contract), AI Solutions Architect, Apr 2024 to Sep 2024: Azure (Azure OpenAI, Semantic Kernel, LangChain, Cosmos DB vector store, Azure AI Search, Document Intelligence, Video Indexer, Service Bus, Entra ID).
- Philips Healthcare, Jul 2022 to Mar 2024: AWS serverless integrations (Lambda, Step Functions, EventBridge, SQS/SNS, S3 presigned uploads, DynamoDB, CloudWatch, Terraform) plus HL7/DICOM; results 30% throughput, 40% PACS accessibility, 100% DICOM interoperability, 99.8% uptime.
- AINS starts Jul 2011 (CA Technologies internship Feb to Jun 2011).
- Do not name CloudTern as current employer anywhere. PolisIQ and Ansera may appear as projects on the site and README, never on the resume.
- Research: cite SSRN only. The arXiv submissions never published. Do not claim seven attack categories on the resume (C5 to C7 were a local pilot).

## Rules

- Resume is employment only. No personal projects, open source, or research sections or summary mentions; those live on the site and README.
- No em dashes anywhere. No location names in site or post content. Human voice, no AI phrasing.
- Before any destructive file action, inspect the target and use the Recycle Bin, not permanent delete.
- When the user has edited a file themselves, edit it in place. Never regenerate it from a script over their changes.

## Resume checklist

1. Edit the docx in place with python-docx at the run level so formatting survives. Clone existing paragraphs to add bullets.
2. Tech timeline check: every tool named under a role must have existed, under that name, during that role's dates (examples: Azure AI Services not Cognitive Services after Jul 2023; VSTS not Azure DevOps before Sep 2018; Entra ID from Jul 2023; .NET 8 from Nov 2023).
3. ATS check: no tables, text boxes, images, or header/footer text; standard section headings; headline keywords match the target role; each role opens with its strongest outcome; every number used also appears on LinkedIn.
4. Render through Word COM to PDF, confirm page count and that no skills row wraps, and look at the pages.

## LinkedIn checklist (Claude in Chrome)

- Turn "Notify network" off in every edit dialog before saving.
- Adding a position can silently overwrite the headline with "<title> at <company>". Re-check the headline after adding any role and restore it.
- Role descriptions max 2,000 characters; About max 2,600. Count before typing.
- The description and About fields are contenteditable. For a targeted change select the exact text range with JavaScript and use `document.execCommand('insertText', ...)`; plain typing after a JS selection can append instead of replace. Verify by reading the field back after reload.
- Keep 4 to 6 skills per role. The profile is at the 100 skill cap, so only existing skills can be attached. Keep the 5 About top-skill slots filled (currently Agentic AI Development, Enterprise Architecture, Technical Leadership, GCP, Microsoft Azure).
- Respect fields the user cleared on purpose (employment type and location are unset on client roles).

## Site and README

- Work in a git worktree, one squashed commit per logical change, author `Lavkesh Dwivedi <iamlavkesh@gmail.com>`, no Co-Authored-By line.
- Open a PR. Merge only when the user asks. JSON-LD must still parse after edits. Preserve each file's line endings (read and write with `newline=''`).
- Finish by reporting what changed on each surface and what the user must do by hand (for example GitLab profile fields when Chrome is not signed in).
