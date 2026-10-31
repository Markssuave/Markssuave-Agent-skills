# 🧠 Markssuave Agent Skills

> A master collection of **130 battle-tested AI agent skills** organized across 11 core engineering roles for **Codex**, **Claude Code**, and **Google Antigravity / Gemini**.

---

## 📌 Quick Navigation (By Role Tables)

- [1. 📐 Planning, Product & Architecture](#1--planning-product--architecture) *(13 skills)*
- [2. 💡 Clarification, Interviewing & Teaching](#2--clarification-interviewing--teaching) *(8 skills)*
- [3. ⚡ Core Development & Engineering](#3--core-development--engineering) *(12 skills)*
- [4. 🧪 Testing, QA & Debugging](#4--testing-qa--debugging) *(7 skills)*
- [5. 🎨 Frontend, UI/UX & Design](#5--frontend-uiux--design) *(30 skills)*
- [6. 🧹 Code Review, Refactoring & Cleanup](#6--code-review-refactoring--cleanup) *(6 skills)*
- [7. 🗜️ Efficiency, Context & Token Optimization](#7--efficiency-context--token-optimization) *(14 skills)*
- [8. 🚀 DevOps, Automation & Git Operations](#8--devops-automation--git-operations) *(10 skills)*
- [9. 🎬 Media, Showcase & Video](#9--media-showcase--video) *(2 skills)*
- [10. ✍️ Writing, Knowledge & Agent Customization](#10--writing-knowledge--agent-customization) *(17 skills)*
- [11. 🛡️ Backend, Databases & Cloud Infrastructure](#11--backend-databases--cloud-infrastructure) *(11 skills)*

---

## 🚀 Quick Setup Guide for Friends

### 1. Which Environment Are You Using?

- **For Codex / Claude Code Users:**
  - Load [`AGENTS.md`](AGENTS.md) as your project or system rules.
  - Type `/maxplan` in prompts to trigger the automated project planning coordinator.
  - Use `/ui-annotate` to receive live element edits directly from the browser overlay bridge (`annotator.js`).

- **For Antigravity / Gemini IDE Users:**
  - Load [`GEMINI.md`](GEMINI.md) as your project or system rules.
  - Type `/plan` in prompts to trigger the native IDE confirmation plan gate with interactive choice cards.
  - Use `/taste-skill` and `/ui-ux-pro-max` for curated frontend art direction and design intelligence.

### 2. Auto-Install All Skills With One Command

To automatically synchronize all skills into your local agent directories (`~/.gemini/config/skills` and `~/.codex/skills`), simply run:

```bash
python sync_reorganized_skills.py
```

This script automatically validates frontmatter, strips compiled bytecode (`__pycache__`), maps slash commands, and updates your dropdown menu.

---

## 🔗 Upstream Open Source References & Engines

This repository is powered by and builds upon the following exceptional open-source agent projects:

| Upstream Project | Author / Maintainer | Core Focus | Repository Link |
| :--- | :--- | :--- | :--- |
| **Andrej Karpathy Skills** | multica-ai | 4 Coding Guardrails & LLM Pitfall Avoidance | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) |
| **Cloudflare Security Audit** | Cloudflare | 6-Phase Offensive & Defensive Code Vulnerability Harness | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) |
| **NVIDIA SkillSpector** | NVIDIA | Static & Taint Analysis Scanner for AI Skills & MCPs | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) |
| **Tasteskill v2** | Community | Anti-Slop Web Art Direction Distilled from 247 Gallery Sites | [Built-in Engine](skills/taste-skill) |
| **UI/UX Pro Max** | Community | Design Intelligence: 79 Styles, 192 Palettes, 74 Fonts | [Built-in Engine](skills/ui-ux-pro-max) |
| **Pocock Skills** | Matt Pocock | Disciplined Software Engineering, TDD, & Architecture | [mattpocock/skills](https://github.com/mattpocock/skills) |
| **Caveman** | Julius Brussee | Token & Memory Efficiency Compression Protocol | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) |
| **Impeccable** | Paul Bakaus | Design Director & Frontend Craftsmanship Suite | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| **Ponytail** | Dietrich Gebert | Minimalist Senior Engineering & Bloat Removal | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) |

---

## 🗂️ Complete Directory of Skills by Role

### 1. 📐 Planning, Product & Architecture

*Blueprint creation, ticket breakdown, domain modeling, and high-level architectural boundaries.*

| Slash Command | Origin / Suite | What It Does (In Layman's Terms) | Folder |
| :--- | :--- | :--- | :--- |
| `/maxplan` `[Codex Protocol]` | Codex Protocol | Plans the requested work and recommends the relevant skills when the user invokes /maxplan. | [`skills/maxplan`](skills/maxplan) |
| `/plan-tickets` | Matt Pocock Engineering | Breaks a large blueprint down into bite-sized, sequential to-do tasks. | [`skills/plan-tickets`](skills/plan-tickets) |
| `/plan-domain` | Matt Pocock Engineering | Defines the business vocabulary and real-world concepts your project uses so everyone is aligned. | [`skills/plan-domain`](skills/plan-domain) |
| `/arch-design` | Matt Pocock Engineering | Designs clean boundaries between components so code stays simple to update and test later. | [`skills/arch-design`](skills/arch-design) |
| `/arch-improve` | Matt Pocock Engineering | Restructures the system’s big-picture foundations so it doesn't become messy. | [`skills/arch-improve`](skills/arch-improve) |
| `/arch-setup-ts` | Matt Pocock Engineering | Sets up strict, modular TypeScript architecture boundaries. | [`skills/arch-setup-ts`](skills/arch-setup-ts) |
| `/plan-triage` | Matt Pocock Engineering | Sorts incoming bugs and feature requests by urgency and priority. | [`skills/plan-triage`](skills/plan-triage) |
| `/plan-map` | Matt Pocock Engineering | Maps out how different parts of your codebase connect to each other. | [`skills/plan-map`](skills/plan-map) |
| `/plan-orchestrate` | Matt Pocock Engineering | Coordinates complex, multi-stage project milestones like an executive assistant. | [`skills/plan-orchestrate`](skills/plan-orchestrate) |
| `/plan-retro` | Matt Pocock Engineering | Looks back at what went well and what went wrong after finishing a milestone. | [`skills/plan-retro`](skills/plan-retro) |
| `/arch-diagrams` | Matt Pocock Engineering | Generates clean, rendered system charts, flowcharts, and Data Flow Diagrams (DFDs) using Mermaid.js. | [`skills/arch-diagrams`](skills/arch-diagrams) |
| `/arch-node-best` | Backend & Cloud Skills | Audits the codebase against the massive Node.js best practices compendium (security, error handling, performance). | [`skills/arch-node-best`](skills/arch-node-best) |
| `/arch-bulletproof` | Backend & Cloud Skills | Scaffolds or refactors APIs into a clean 3-tier architecture (Controllers -> Services -> Data Access) with proper Dependency Injection. | [`skills/arch-bulletproof`](skills/arch-bulletproof) |


### 2. 💡 Clarification, Interviewing & Teaching

*Interactive clarification interviews, devil's advocacy stress-testing, senior heuristics, and technical concept explainers.*

| Slash Command | Origin / Suite | What It Does (In Layman's Terms) | Folder |
| :--- | :--- | :--- | :--- |
| `/ask-interview` | Matt Pocock Engineering | Interviews you with sharp questions to uncover hidden assumptions in your ideas. | [`skills/ask-interview`](skills/ask-interview) |
| `/ask-challenge` | Matt Pocock Engineering | Plays devil's advocate to stress-test your thinking and decisions. | [`skills/ask-challenge`](skills/ask-challenge) |
| `/ask-docs-interview` | Matt Pocock Engineering | Interviews you while actively cross-referencing your project's existing documentation. | [`skills/ask-docs-interview`](skills/ask-docs-interview) |
| `/ask-form` | Matt Pocock Engineering | Converts open-ended decisions into simple multiple-choice questionnaires. | [`skills/ask-form`](skills/ask-form) |
| `/learn-explain` | Matt Pocock Engineering | Explains complex technical concepts in plain, easy-to-understand language. | [`skills/learn-explain`](skills/learn-explain) |
| `/learn-expert` | Matt Pocock Engineering | Asks senior TypeScript engineer heuristics for tricky problems. | [`skills/learn-expert`](skills/learn-expert) |
| `/sanity-check` | Matt Pocock Engineering | Rapidly double-checks weird or confusing code to see if it actually makes sense. | [`skills/sanity-check`](skills/sanity-check) |
| `/feedback-loop` | Matt Pocock Engineering | Keeps you in the loop with continuous feedback checkpoints as work progresses. | [`skills/feedback-loop`](skills/feedback-loop) |


### 3. ⚡ Core Development & Engineering

*Disciplined code implementation, Karpathy guardrails, minimum viable builds, prototypes, migrations, and database patterns.*

| Slash Command | Origin / Suite | What It Does (In Layman's Terms) | Folder |
| :--- | :--- | :--- | :--- |
| `/karpathy-guidelines` | Andrej Karpathy Skills | Enforces Andrej Karpathy's 4 coding guardrails: think before coding, simplicity first, surgical changes, and goal-driven execution. | [`skills/karpathy-guidelines`](skills/karpathy-guidelines) |
| `/dev-isolated` | Matt Pocock Engineering | Applies precise, isolated modifications to any part of the system (UI, Backend, Data) without causing collateral damage. | [`skills/dev-isolated`](skills/dev-isolated) |
| `/dev-prisma` | Backend & Cloud Skills | Designs type-safe relational database schemas and queries using Prisma best practices. | [`skills/dev-prisma`](skills/dev-prisma) |
| `/dev-authjs` | Backend & Cloud Skills | Implements secure, industry-standard authentication flows and session management using NextAuth/Auth.js. | [`skills/dev-authjs`](skills/dev-authjs) |
| `/dev-bullmq` | Backend & Cloud Skills | Sets up reliable background job queues and worker processes for async tasks. | [`skills/dev-bullmq`](skills/dev-bullmq) |
| `/dev-build` | Matt Pocock Engineering | Builds code strictly according to an agreed plan without adding unnecessary extras. | [`skills/dev-build`](skills/dev-build) |
| `/dev-build-spec` | Matt Pocock Engineering | Builds a full feature straight from an approved technical blueprint. | [`skills/dev-build-spec`](skills/dev-build-spec) |
| `/dev-lean` | Matt Pocock Engineering | Builds the minimum viable version of a feature with strict stops to prevent over-engineering. | [`skills/dev-lean`](skills/dev-lean) |
| `/dev-prototype` | Matt Pocock Engineering | Builds a quick throwaway experiment to test if an idea works before committing to it. | [`skills/dev-prototype`](skills/dev-prototype) |
| `/dev-minimal` | Ponytail Minimalist Dev | Solves problems using the absolute fewest lines of native code possible. | [`skills/dev-minimal`](skills/dev-minimal) |
| `/dev-migrate` | Matt Pocock Engineering | Safely moves databases, configurations, or APIs to a new version without downtime. | [`skills/dev-migrate`](skills/dev-migrate) |
| `/dev-fix-types` | Matt Pocock Engineering | Cleans up sloppy type shortcuts in test files so they are rock solid. | [`skills/dev-fix-types`](skills/dev-fix-types) |


### 4. 🧪 Testing, QA & Debugging

*Test-driven development loops, step-by-step scientific deduction, narrow surgical bug patches, and proof verification.*

| Slash Command | Origin / Suite | What It Does (In Layman's Terms) | Folder |
| :--- | :--- | :--- | :--- |
| `/qa-test-first` | Matt Pocock Engineering | Writes tests before writing code to guarantee everything works from the ground up. | [`skills/qa-test-first`](skills/qa-test-first) |
| `/qa-diagnose` | Matt Pocock Engineering | Tracks down stubborn bugs and slowdowns using step-by-step scientific deduction. | [`skills/qa-diagnose`](skills/qa-diagnose) |
| `/qa-investigate` | Matt Pocock Engineering | Investigates confusing glitches with evidence before touching any code. | [`skills/qa-investigate`](skills/qa-investigate) |
| `/qa-patch` | Matt Pocock Engineering | Applies precise, narrow bug fixes without breaking other parts of the system. | [`skills/qa-patch`](skills/qa-patch) |
| `/qa-verify` | Matt Pocock Engineering | Runs rigorous proof checks to confirm work meets requirements, then stops immediately. | [`skills/qa-verify`](skills/qa-verify) |
| `/qa-quick-review` | Matt Pocock Engineering | Delivers an ultra-brief, one-line-per-finding quality check on code changes. | [`skills/qa-quick-review`](skills/qa-quick-review) |
| `/qa-scaffold` | Matt Pocock Engineering | Generates structured test exercises, problems, and solutions for learning repos. | [`skills/qa-scaffold`](skills/qa-scaffold) |


### 5. 🎨 Frontend, UI/UX & Design

*Visual art direction, anti-slop curation, design intelligence databases, live element annotator bridge, and pixel polish.*

| Slash Command | Origin / Suite | What It Does (In Layman's Terms) | Folder |
| :--- | :--- | :--- | :--- |
| `/ui-master` | Impeccable UI/UX Suite | Master design director for elevating visual design, usability, and UX. | [`skills/ui-master`](skills/ui-master) |
| `/taste-skill` | Tasteskill v2 | tasteskill v2, the anti-slop frontend skill for intentional art direction and curated layouts. | [`skills/taste-skill`](skills/taste-skill) |
| `/design-taste-frontend` `[Alias]` | Tasteskill v2 | Alias for /taste-skill. Tasteskill v2, the anti-slop frontend skill for intentional art direction and curated layouts. | [`skills/design-taste-frontend`](skills/design-taste-frontend) |
| `/ui-ux-pro-max` | UI/UX Pro Max | UI/UX design intelligence database with 79 UI styles, 192 color palettes, 74 font pairings, 119 UX guidelines, and 25 chart types. | [`skills/ui-ux-pro-max`](skills/ui-ux-pro-max) |
| `/ui-ux-pro-max-skill` `[Alias]` | UI/UX Pro Max | Alias for /ui-ux-pro-max. Design intelligence database with 79 UI styles, 192 color palettes, 74 font pairings, 119 UX guidelines, and 25 chart types. | [`skills/ui-ux-pro-max-skill`](skills/ui-ux-pro-max-skill) |
| `/ui-annotate` `[Codex Bridge]` | Codex Annotator Bridge | Inspects live browser UI annotations dispatched via the Codex Annotator bridge and applies targeted modifications to the matching React component or page. | [`skills/ui-annotate`](skills/ui-annotate) |
| `/ui-init` | Impeccable UI/UX Suite | Discovers brand identity and sets up design guidelines (PRODUCT.md & DESIGN.md). | [`skills/ui-init`](skills/ui-init) |
| `/ui-shape` | Impeccable UI/UX Suite | Plans screen layouts and user flows before writing any frontend code. | [`skills/ui-shape`](skills/ui-shape) |
| `/ui-critique` | Impeccable UI/UX Suite | Evaluates screens from a human user’s perspective for clunkiness and visual clutter. | [`skills/ui-critique`](skills/ui-critique) |
| `/ui-audit` | Impeccable UI/UX Suite | Inspects a web interface for accessibility, speed, and design mistakes. | [`skills/ui-audit`](skills/ui-audit) |
| `/ui-polish` | Impeccable UI/UX Suite | Adds final touches to alignment, pixel spacing, and visual harmony before shipping. | [`skills/ui-polish`](skills/ui-polish) |
| `/ui-layout` | Impeccable UI/UX Suite | Fixes cramped spacing, awkward grids, and unbalanced screen rhythm. | [`skills/ui-layout`](skills/ui-layout) |
| `/ui-responsive` | Impeccable UI/UX Suite | Makes websites look flawless on mobile, tablets, and desktops. | [`skills/ui-responsive`](skills/ui-responsive) |
| `/ui-typography` | Impeccable UI/UX Suite | Fixes font pairings, text hierarchy, line spacing, and readability. | [`skills/ui-typography`](skills/ui-typography) |
| `/ui-colors` | Impeccable UI/UX Suite | Replaces boring gray screens with intentional, attractive color palettes. | [`skills/ui-colors`](skills/ui-colors) |
| `/ui-make-bold` | Impeccable UI/UX Suite | Gives dull, generic designs more punch, contrast, and strong personality. | [`skills/ui-make-bold`](skills/ui-make-bold) |
| `/ui-tone-down` | Impeccable UI/UX Suite | Softens loud, chaotic, or overly bright designs into calm, elegant interfaces. | [`skills/ui-tone-down`](skills/ui-tone-down) |
| `/ui-declutter` | Impeccable UI/UX Suite | Strips away clutter and unnecessary buttons so users can focus on what matters. | [`skills/ui-declutter`](skills/ui-declutter) |
| `/ui-animate` | Impeccable UI/UX Suite | Adds smooth button hovers, page transitions, and subtle motion. | [`skills/ui-animate`](skills/ui-animate) |
| `/ui-delight` | Impeccable UI/UX Suite | Adds delightful details and playful moments that make software fun to use. | [`skills/ui-delight`](skills/ui-delight) |
| `/ui-high-end` | Impeccable UI/UX Suite | Builds high-end effects like 3D graphics, spring physics, and fluid animations. | [`skills/ui-high-end`](skills/ui-high-end) |
| `/ui-copywrite` | Impeccable UI/UX Suite | Rewrites confusing buttons, error messages, and onboarding text into plain English. | [`skills/ui-copywrite`](skills/ui-copywrite) |
| `/ui-onboard` | Impeccable UI/UX Suite | Designs first-time welcome screens and empty states that guide new users. | [`skills/ui-onboard`](skills/ui-onboard) |
| `/ui-harden` | Impeccable UI/UX Suite | Makes UI bulletproof against weird screen sizes, long text overflows, and network glitches. | [`skills/ui-harden`](skills/ui-harden) |
| `/ui-speed` | Impeccable UI/UX Suite | Speeds up slow-loading pages, laggy animations, and heavy web files. | [`skills/ui-speed`](skills/ui-speed) |
| `/ui-tokens` | Impeccable UI/UX Suite | Gathers repeated buttons, colors, and fonts into reusable design tokens. | [`skills/ui-tokens`](skills/ui-tokens) |
| `/ui-doc-system` | Impeccable UI/UX Suite | Writes down your project's visual rules into a shareable DESIGN.md guide. | [`skills/ui-doc-system`](skills/ui-doc-system) |
| `/ui-live-tweak` | Impeccable UI/UX Suite | Lets you see and test AI design changes live in your running web browser. | [`skills/ui-live-tweak`](skills/ui-live-tweak) |
| `/ui-variants` | Impeccable UI/UX Suite | Generates multiple design options for a component so you can pick the best one. | [`skills/ui-variants`](skills/ui-variants) |
| `/ui-craft` | Impeccable UI/UX Suite | Ensures designs meet strict senior craftsmanship standards. | [`skills/ui-craft`](skills/ui-craft) |


### 6. 🧹 Code Review, Refactoring & Cleanup

*Overcomplication hunting, safe structural refactoring, dead file scans, and technical debt tracking.*

| Slash Command | Origin / Suite | What It Does (In Layman's Terms) | Folder |
| :--- | :--- | :--- | :--- |
| `/review-deep` | Custom System Skill | Runs thorough parallel checks to ensure code matches requirements and high standards. | [`skills/review-deep`](skills/review-deep) |
| `/review-bloat` | Ponytail Minimalist Dev | Hunts down overcomplicated code and deletes unnecessary layers. | [`skills/review-bloat`](skills/review-bloat) |
| `/audit-bloat` | Ponytail Minimalist Dev | Scans your entire project for useless code, dead files, and security risks. | [`skills/audit-bloat`](skills/audit-bloat) |
| `/refactor-safe` | Custom System Skill | Cleans up messy code structure while guaranteeing zero change to how it functions. | [`skills/refactor-safe`](skills/refactor-safe) |
| `/track-debt` | Ponytail Minimalist Dev | Catalogs temporary shortcuts and 'fix this later' notes into a clear to-do list. | [`skills/track-debt`](skills/track-debt) |
| `/stats-savings` | Caveman Token Suite | Measures how much code, memory, and money was saved by keeping things simple. | [`skills/stats-savings`](skills/stats-savings) |


### 7. 🗜️ Efficiency, Context & Token Optimization

*Ultra-compressed communication shorthand, background subagent delegation, token spend tracking, and prompt tuning.*

| Slash Command | Origin / Suite | What It Does (In Layman's Terms) | Folder |
| :--- | :--- | :--- | :--- |
| `/caveman` | Caveman Token Suite | Keeps our interactions short to save token usage and efficiency. | [`skills/caveman`](skills/caveman) |
| `/caveman-dense` | Caveman Token Suite | Compresses answers into dense shorthand to preserve AI memory during huge tasks. | [`skills/caveman-dense`](skills/caveman-dense) |
| `/caveman-max` | Caveman Token Suite | Maximum possible compression mode for emergency context conservation. | [`skills/caveman-max`](skills/caveman-max) |
| `/delegate-subagents` | Caveman Token Suite | Hands off background tasks to sub-agents so our main conversation doesn't get clogged. | [`skills/delegate-subagents`](skills/delegate-subagents) |
| `/git-terse-commit` | Caveman Token Suite | Writes short, meaningful commit messages with zero fluff. | [`skills/git-terse-commit`](skills/git-terse-commit) |
| `/docs-compress` | Caveman Token Suite | Shrinks large notes and memory files to save AI memory while keeping the facts. | [`skills/docs-compress`](skills/docs-compress) |
| `/explore-quiet` | Caveman Token Suite | Searches the codebase silently in the background without spamming the chat. | [`skills/explore-quiet`](skills/explore-quiet) |
| `/stats-tokens` | Caveman Token Suite | Shows how many tokens and cache reads we have used so far. | [`skills/stats-tokens`](skills/stats-tokens) |
| `/help-caveman` | Caveman Token Suite | Displays a quick summary of token-saving commands. | [`skills/help-caveman`](skills/help-caveman) |
| `/help-ponytail` | Ponytail Minimalist Dev | Displays a quick cheat-sheet for minimalist coding commands. | [`skills/help-ponytail`](skills/help-ponytail) |
| `/stats-spend` | Caveman Token Suite | Shows where your AI token budget is actually being spent. | [`skills/stats-spend`](skills/stats-spend) |
| `/trace-workflows` | Caveman Token Suite | Finds and labels all AI workflows in your project so costs can be tracked. | [`skills/trace-workflows`](skills/trace-workflows) |
| `/tune-prompts` | Caveman Token Suite | Finds wasteful prompt habits and applies fixes to permanently lower AI costs. | [`skills/tune-prompts`](skills/tune-prompts) |
| `/manage-experiments` | Caveman Token Suite | Manages and approves experiments to test AI cost reductions. | [`skills/manage-experiments`](skills/manage-experiments) |


### 8. 🚀 DevOps, Automation & Git Operations

*Scheduled background automations, Git guardrails, pull request generation, and developer environment wizards.*

| Slash Command | Origin / Suite | What It Does (In Layman's Terms) | Folder |
| :--- | :--- | :--- | :--- |
| `/ops-schedule` | Antigravity Built-in | Sets up background recurring automations and timers (cron jobs). | [`skills/ops-schedule`](skills/ops-schedule) |
| `/ops-pre-commit` | Custom System Skill | Automatically checks code formatting and tests every time you make a git commit. | [`skills/ops-pre-commit`](skills/ops-pre-commit) |
| `/ops-guardrails` | Custom System Skill | Blocks accidentally running destructive git commands like force pushes or deletions. | [`skills/ops-guardrails`](skills/ops-guardrails) |
| `/ops-github` | Antigravity Built-in | Handles secure, scoped access to GitHub repositories and pull requests. | [`skills/ops-github`](skills/ops-github) |
| `/git-pr` | Custom System Skill | Writes clean, well-structured pull request summaries for code review. | [`skills/git-pr`](skills/git-pr) |
| `/ops-plugin` | Antigravity Built-in | Installs, manages, or creates plugins that package skills and tools together. | [`skills/ops-plugin`](skills/ops-plugin) |
| `/ops-setup-pocock` | Custom System Skill | Sets up Matt Pocock’s engineering skill pack environment. | [`skills/ops-setup-pocock`](skills/ops-setup-pocock) |
| `/ops-caveman-gateway` | Caveman Token Suite | Connects your project to an observability gateway to track AI efficiency. | [`skills/ops-caveman-gateway`](skills/ops-caveman-gateway) |
| `/ops-optimize-eval` | Caveman Token Suite | Evaluates token optimization experiments against baseline tests. | [`skills/ops-optimize-eval`](skills/ops-optimize-eval) |
| `/ops-wizard` | Custom System Skill | Creates an interactive terminal assistant that guides you step-by-step through manual setup. | [`skills/ops-wizard`](skills/ops-wizard) |


### 9. 🎬 Media, Showcase & Video

*Automated code-to-video generation for web project launches and animated video showcases.*

| Slash Command | Origin / Suite | What It Does (In Layman's Terms) | Folder |
| :--- | :--- | :--- | :--- |
| `/show-video` | Brag Video Suite | Automatically turns your web project into a polished, animated showcase launch video. | [`skills/show-video`](skills/show-video) |
| `/show-video-quick` | Brag Video Suite | Creates a fast, lightweight showcase video with music and copy with no external assets needed. | [`skills/show-video-quick`](skills/show-video-quick) |


### 10. ✍️ Writing, Knowledge & Agent Customization

*Agent prompt rules, technical prose humanization, Microsoft MarkItDown conversion, and interactive sidecar panels.*

| Slash Command | Origin / Suite | What It Does (In Layman's Terms) | Folder |
| :--- | :--- | :--- | :--- |
| `/write-agent-rules` | Custom System Skill | Writes crystal-clear instructions for AI agents so they follow your rules. | [`skills/write-agent-rules`](skills/write-agent-rules) |
| `/write-outline` | Custom System Skill | Plans out the structural outline for long technical articles or documentation. | [`skills/write-outline`](skills/write-outline) |
| `/write-pacing` | Custom System Skill | Plans the narrative flow and key highlights for technical explainers. | [`skills/write-pacing`](skills/write-pacing) |
| `/write-snippets` | Custom System Skill | Drafts self-contained modular paragraphs and snippets for documentation. | [`skills/write-snippets`](skills/write-snippets) |
| `/write-humanize` | Custom System Skill | Rewrites AI-sounding prose and documentation to read with natural, human cadence without altering core facts. | [`skills/write-humanize`](skills/write-humanize) |
| `/humanizer` `[Alias]` | Custom System Skill | Alias for /write-humanize to strip AI writing tells and restore natural human cadence. | [`skills/humanizer`](skills/humanizer) |
| `/doc-markitdown` | Custom System Skill | Converts documents (PDF, Word, Excel, PowerPoint, audio, HTML) into clean, structured Markdown using Microsoft MarkItDown. | [`skills/doc-markitdown`](skills/doc-markitdown) |
| `/markitdown` `[Alias]` | Custom System Skill | Alias for /doc-markitdown to convert Office docs and PDFs into Markdown. | [`skills/markitdown`](skills/markitdown) |
| `/knowledge-research` | Custom System Skill | Digs through authoritative documentation and saves a research summary in markdown. | [`skills/knowledge-research`](skills/knowledge-research) |
| `/knowledge-handoff` | Custom System Skill | Summarizes current work state so another agent or session can take over seamlessly. | [`skills/knowledge-handoff`](skills/knowledge-handoff) |
| `/knowledge-handoff-claude` | Custom System Skill | Packages session notes formatted specifically for Claude Code transitions. | [`skills/knowledge-handoff-claude`](skills/knowledge-handoff-claude) |
| `/agent-customize` | Antigravity Built-in | Guide for building custom skills, rules, hooks, and MCP servers in Antigravity. | [`skills/agent-customize`](skills/agent-customize) |
| `/agent-guide` | Antigravity Built-in | Complete guide and cheatsheet for using Antigravity features, IDE shortcuts, and CLI. | [`skills/agent-guide`](skills/agent-guide) |
| `/agent-gen-ui` | Antigravity Built-in | Renders interactive visual widgets and dashboards right inside our chat window. | [`skills/agent-gen-ui`](skills/agent-gen-ui) |
| `/agent-ui-panel` | Antigravity Built-in | Builds interactive web side panels that live right in the Antigravity workspace. | [`skills/agent-ui-panel`](skills/agent-ui-panel) |
| `/agent-ui-toggle` | Antigravity Built-in | Adds one-click buttons in chat to open relevant side panels. | [`skills/agent-ui-toggle`](skills/agent-ui-toggle) |
| `/agent-migrate-skills` | Antigravity Built-in | Converts legacy workflow scripts into modern agent skills. | [`skills/agent-migrate-skills`](skills/agent-migrate-skills) |


### 11. 🛡️ Backend, Databases & Cloud Infrastructure

*Consistent API endpoints, strict Zod validation, Prisma/Drizzle schemas, Cloudflare 6-phase security audits, and NVIDIA SkillSpector scans.*

| Slash Command | Origin / Suite | What It Does (In Layman's Terms) | Folder |
| :--- | :--- | :--- | :--- |
| `/api-design` | Backend & Cloud Skills | Designs clean, standardized REST/GraphQL endpoints with consistent envelopes. | [`skills/api-design`](skills/api-design) |
| `/api-validate` | Backend & Cloud Skills | Implements strict input validation, sanitization, and Zod/Pydantic schemas. | [`skills/api-validate`](skills/api-validate) |
| `/db-schema` | Backend & Cloud Skills | Generates relational database schemas, migrations, and Prisma/Drizzle models. | [`skills/db-schema`](skills/db-schema) |
| `/db-query-opt` | Backend & Cloud Skills | Analyzes query execution plans, indexes, and eliminates N+1 query bottlenecks. | [`skills/db-query-opt`](skills/db-query-opt) |
| `/sec-auth` | Backend & Cloud Skills | Implements secure auth flows like JWT rotation, session cookies, and OAuth. | [`skills/sec-auth`](skills/sec-auth) |
| `/sec-audit` | Cloudflare Security Audit | Runs Cloudflare's 6-phase security audit and vulnerability discovery harness across codebases (reconnaissance, hunting, adversarial verification, and guidance). | [`skills/sec-audit`](skills/sec-audit) |
| `/sec-skillspector` | NVIDIA SkillSpector | Scans AI agent skills, MCP servers, and GitHub repositories for prompt injection, data exfiltration, malicious code, and supply-chain CVEs using NVIDIA SkillSpector. | [`skills/sec-skillspector`](skills/sec-skillspector) |
| `/ops-docker` | Backend & Cloud Skills | Crafts minimal, multi-stage Dockerfiles and local compose environments. | [`skills/ops-docker`](skills/ops-docker) |
| `/ops-ci-cd` | Backend & Cloud Skills | Builds automated GitHub Actions CI/CD test and deployment pipelines. | [`skills/ops-ci-cd`](skills/ops-ci-cd) |
| `/arch-queue` | Backend & Cloud Skills | Designs background worker jobs, queue retries, and scheduled workers. | [`skills/arch-queue`](skills/arch-queue) |
| `/ops-telemetry` | Backend & Cloud Skills | Sets up structured JSON logging, correlation IDs, and Sentry error monitoring. | [`skills/ops-telemetry`](skills/ops-telemetry) |

