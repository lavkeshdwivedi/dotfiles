# dotfiles

Personal configuration and Claude Code skills for [@lavkeshdwivedi](https://github.com/lavkeshdwivedi).

## Claude Code skills

Slash commands that install into `~/.claude/commands/` and work in every Claude Code session.

| Command | What it does |
|---|---|
| `/autopilot` | Runs the session autonomously with minimal prompting |
| `/blissful-article` | Writes a Blissful Bytes article for lavkesh.com and publishes it to the LinkedIn newsletter with a cover image |
| `/deep-research` | Expands a research paper in the conversation with academic literature and documented real-world incidents |
| `/human-check` | Reviews anything going out in my name (posts, comments, articles, emails, recruiter replies) the way a careful colleague would, before it reaches me for approval |
| `/inbox-replies` | Replies to recruiters and DMs without repeating or contradicting what I already did, with the checks that run before anything is sent |
| `/journal-reviewer` | Full structured peer review of a paper in the conversation, at the standard of venues like IEEE TSE |
| `/keep-awake` | Keeps Windows from sleeping or locking; pass `stop` to turn it off |
| `/linkedin-post` | Finds the day's story in my areas, writes a LinkedIn post in my voice with a contextual 4:3 image, reviews it, and posts at a human pace |
| `/linkedin-comments` | Writes and posts feed comments and replies in my voice, spaced out and shown to me first |
| `/profile-sync` | Keeps my resume, LinkedIn, site, GitHub and GitLab profiles, and job boards consistent |
| `/style-fix` | Fixes language and voice: strips AI-sounding patterns and enforces terse writing |

## Install

**Mac / Linux**

```bash
git clone https://github.com/lavkeshdwivedi/dotfiles.git
cd dotfiles
bash install.sh
```

**Windows (PowerShell)**

```powershell
git clone https://github.com/lavkeshdwivedi/dotfiles.git
cd dotfiles
.\install.ps1
```

Both scripts copy all skills to `~/.claude/commands/` (or `%USERPROFILE%\.claude\commands\` on Windows). After install, restart Claude Code and the commands are available.

## My repos

### Original projects

| Repo | Description |
|---|---|
| [kogniOS](https://github.com/lavkeshdwivedi/kogniOS) | Personal AI operating system |
| [geo-pulse](https://github.com/lavkeshdwivedi/geo-pulse) | Automatic geopolitics newsletter with hourly summaries to GitHub Pages |
| [agent-escalation-eval](https://github.com/lavkeshdwivedi/agent-escalation-eval) | Inspect AI eval for autonomous agent constraint escalation (C4) |
| [agent-escape-lab](https://github.com/lavkeshdwivedi/agent-escape-lab) | Guardrail bypass experiment lab: four bypass classes tested across 29 models from 8 providers |
| [openclaw](https://github.com/lavkeshdwivedi/openclaw) | Personal AI assistant, cross-platform |
| [career-ops-fork](https://github.com/lavkeshdwivedi/career-ops-fork) | AI-powered job search system built on Claude Code: 14 skill modes, Go dashboard, PDF generation, batch processing |
| [planning-poker](https://github.com/lavkeshdwivedi/planning-poker) | Real-time Planning Poker for agile teams; single HTML file, Firebase backend, no build step |
| [awesome-design-md](https://github.com/lavkeshdwivedi/awesome-design-md) | DESIGN.md files capturing design systems from popular sites, for use with coding agents |
| [skills](https://github.com/lavkeshdwivedi/skills) | Claude Code skill collection |
| [dotfiles](https://github.com/lavkeshdwivedi/dotfiles) | This repo |

### Open-source forks

Projects I follow, contribute to, or use in my own work.

| Repo | Description |
|---|---|
| [agno](https://github.com/lavkeshdwivedi/agno) | Build, run, and manage agent platforms |
| [deepeval](https://github.com/lavkeshdwivedi/deepeval) | LLM evaluation framework |
| [garak](https://github.com/lavkeshdwivedi/garak) | LLM vulnerability scanner |
| [promptfoo](https://github.com/lavkeshdwivedi/promptfoo) | Red teaming and evaluation for prompts, agents, and RAGs |
| [inspect_ai](https://github.com/lavkeshdwivedi/inspect_ai) | Framework for large language model evaluations |
| [inspect_evals](https://github.com/lavkeshdwivedi/inspect_evals) | Community eval collection for Inspect AI |
| [llm-guard](https://github.com/lavkeshdwivedi/llm-guard) | Security toolkit for LLM interactions |
| [OpenHands](https://github.com/lavkeshdwivedi/OpenHands) | AI-driven software development |
| [dify](https://github.com/lavkeshdwivedi/dify) | Production-ready platform for agentic workflow development |
| [guardrails](https://github.com/lavkeshdwivedi/guardrails) | Adding guardrails to LLMs |
| [Guardrails-1](https://github.com/lavkeshdwivedi/Guardrails-1) | NeMo Guardrails: programmable guardrails for conversational LLM systems |
| [mlflow](https://github.com/lavkeshdwivedi/mlflow) | Open-source AI engineering platform for agents and ML models |
| [anthropic-sdk-python](https://github.com/lavkeshdwivedi/anthropic-sdk-python) | Anthropic Python SDK |
| [awesome-copilot](https://github.com/lavkeshdwivedi/awesome-copilot) | Community instructions and skills for GitHub Copilot |
| [postgrest](https://github.com/lavkeshdwivedi/postgrest) | REST API for any Postgres database |
| [influxdb](https://github.com/lavkeshdwivedi/influxdb) | Scalable datastore for metrics, events, and real-time analytics |
| [eShopOnDapr](https://github.com/lavkeshdwivedi/eShopOnDapr) | .NET distributed application built on Dapr |
| [coolstore-microservices](https://github.com/lavkeshdwivedi/coolstore-microservices) | Full-stack .NET microservices with Dapr and Tye |
| [Hangfire](https://github.com/lavkeshdwivedi/Hangfire) | Background job processing for .NET |
| [IdentityServer4](https://github.com/lavkeshdwivedi/IdentityServer4) | OpenID Connect and OAuth 2.0 framework for ASP.NET Core |
| [AppMetrics](https://github.com/lavkeshdwivedi/AppMetrics) | Cross-platform .NET metrics library |
| [minio-dotnet](https://github.com/lavkeshdwivedi/minio-dotnet) | MinIO client SDK for .NET |
| [swagger-ui](https://github.com/lavkeshdwivedi/swagger-ui) | Swagger UI |
| [client-python](https://github.com/lavkeshdwivedi/client-python) | Mistral AI Python client |
| [code-connect](https://github.com/lavkeshdwivedi/code-connect) | Connect design system components in code with Figma |
