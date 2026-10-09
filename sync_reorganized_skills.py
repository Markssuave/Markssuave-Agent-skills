import os
import shutil
import re
import json

ROOT_DIR = r"C:\Users\Mark Vasquez\Documents\Agent Skills"
GLOBAL_SKILLS_DIR = r"C:\Users\Mark Vasquez\.gemini\config\skills"
BUILTIN_DIR = r"C:\Users\Mark Vasquez\.gemini\antigravity\builtin\skills"

# Master 102 Reorganized Skills Map: (old_name -> (new_name, layman_description))
SKILL_MAP = {
    # 1. Planning, Product & Architecture (10)
    "to-spec": ("plan-spec", "Turns your rough idea into a complete, clear blueprint before building."),
    "to-tickets": ("plan-tickets", "Breaks a large blueprint down into bite-sized, sequential to-do tasks."),
    "domain-modeling": ("plan-domain", "Defines the business vocabulary and real-world concepts your project uses so everyone is aligned."),
    "codebase-design": ("arch-design", "Designs clean boundaries between components so code stays simple to update and test later."),
    "improve-codebase-architecture": ("arch-improve", "Restructures the system’s big-picture foundations so it doesn't become messy."),
    "setup-ts-deep-modules": ("arch-setup-ts", "Sets up strict, modular TypeScript architecture boundaries."),
    "triage": ("plan-triage", "Sorts incoming bugs and feature requests by urgency and priority."),
    "wayfinder": ("plan-map", "Maps out how different parts of your codebase connect to each other."),
    "chief-of-staff": ("plan-orchestrate", "Coordinates complex, multi-stage project milestones like an executive assistant."),
    "retro": ("plan-retro", "Looks back at what went well and what went wrong after finishing a milestone."),
    "arch-diagrams": ("arch-diagrams", "Generates clean, rendered system charts, flowcharts, and Data Flow Diagrams (DFDs) using Mermaid.js."),
    "arch-node-best": ("arch-node-best", "Audits the codebase against the massive Node.js best practices compendium (security, error handling, performance)."),
    "arch-bulletproof": ("arch-bulletproof", "Scaffolds or refactors APIs into a clean 3-tier architecture (Controllers -> Services -> Data Access) with proper Dependency Injection."),
    "dev-prisma": ("dev-prisma", "Designs type-safe relational database schemas and queries using Prisma best practices."),
    "dev-authjs": ("dev-authjs", "Implements secure, industry-standard authentication flows and session management using NextAuth/Auth.js."),
    "dev-bullmq": ("dev-bullmq", "Sets up reliable background job queues and worker processes for async tasks."),

    # 2. Clarification, Interviewing & Teaching (8)
    "grill-me": ("ask-interview", "Interviews you with sharp questions to uncover hidden assumptions in your ideas."),
    "grilling": ("ask-challenge", "Plays devil's advocate to stress-test your thinking and decisions."),
    "grill-with-docs": ("ask-docs-interview", "Interviews you while actively cross-referencing your project's existing documentation."),
    "to-questionnaire": ("ask-form", "Converts open-ended decisions into simple multiple-choice questionnaires."),
    "teach": ("learn-explain", "Explains complex technical concepts in plain, easy-to-understand language."),
    "ask-matt": ("learn-expert", "Asks senior TypeScript engineer heuristics for tricky problems."),
    "wait-what": ("sanity-check", "Rapidly double-checks weird or confusing code to see if it actually makes sense."),
    "loop-me": ("feedback-loop", "Keeps you in the loop with continuous feedback checkpoints as work progresses."),

    # 3. Core Development & Engineering (7)
    "implement": ("dev-build", "Builds code strictly according to an agreed plan without adding unnecessary extras."),
    "implement-spec": ("dev-build-spec", "Builds a full feature straight from an approved technical blueprint."),
    "lean-build": ("dev-lean", "Builds the minimum viable version of a feature with strict stops to prevent over-engineering."),
    "prototype": ("dev-prototype", "Builds a quick throwaway experiment to test if an idea works before committing to it."),
    "ponytail": ("dev-minimal", "Solves problems using the absolute fewest lines of native code possible."),
    "migration": ("dev-migrate", "Safely moves databases, configurations, or APIs to a new version without downtime."),
    "migrate-to-shoehorn": ("dev-fix-types", "Cleans up sloppy type shortcuts in test files so they are rock solid."),
    "dev-isolated": ("dev-isolated", "Applies precise, isolated modifications to any part of the system (UI, Backend, Data) without causing collateral damage."),

    # 4. Testing, QA & Debugging (7)
    "tdd": ("qa-test-first", "Writes tests before writing code to guarantee everything works from the ground up."),
    "diagnosing-bugs": ("qa-diagnose", "Tracks down stubborn bugs and slowdowns using step-by-step scientific deduction."),
    "investigate-first": ("qa-investigate", "Investigates confusing glitches with evidence before touching any code."),
    "surgical-patch": ("qa-patch", "Applies precise, narrow bug fixes without breaking other parts of the system."),
    "verify-and-stop": ("qa-verify", "Runs rigorous proof checks to confirm work meets requirements, then stops immediately."),
    "caveman-review": ("qa-quick-review", "Delivers an ultra-brief, one-line-per-finding quality check on code changes."),
    "scaffold-exercises": ("qa-scaffold", "Generates structured test exercises, problems, and solutions for learning repos."),

    # 5. Frontend, UI/UX & Design (25)
    "impeccable": ("ui-master", "Master design director for elevating visual design, usability, and UX."),
    "impeccable-init": ("ui-init", "Discovers brand identity and sets up design guidelines (PRODUCT.md & DESIGN.md)."),
    "impeccable-shape": ("ui-shape", "Plans screen layouts and user flows before writing any frontend code."),
    "impeccable-critique": ("ui-critique", "Evaluates screens from a human user’s perspective for clunkiness and visual clutter."),
    "impeccable-audit": ("ui-audit", "Inspects a web interface for accessibility, speed, and design mistakes."),
    "impeccable-polish": ("ui-polish", "Adds final touches to alignment, pixel spacing, and visual harmony before shipping."),
    "impeccable-layout": ("ui-layout", "Fixes cramped spacing, awkward grids, and unbalanced screen rhythm."),
    "impeccable-adapt": ("ui-responsive", "Makes websites look flawless on mobile, tablets, and desktops."),
    "impeccable-typeset": ("ui-typography", "Fixes font pairings, text hierarchy, line spacing, and readability."),
    "impeccable-colorize": ("ui-colors", "Replaces boring gray screens with intentional, attractive color palettes."),
    "impeccable-bolder": ("ui-make-bold", "Gives dull, generic designs more punch, contrast, and strong personality."),
    "impeccable-quieter": ("ui-tone-down", "Softens loud, chaotic, or overly bright designs into calm, elegant interfaces."),
    "impeccable-distill": ("ui-declutter", "Strips away clutter and unnecessary buttons so users can focus on what matters."),
    "impeccable-animate": ("ui-animate", "Adds smooth button hovers, page transitions, and subtle motion."),
    "impeccable-delight": ("ui-delight", "Adds delightful details and playful moments that make software fun to use."),
    "impeccable-overdrive": ("ui-high-end", "Builds high-end effects like 3D graphics, spring physics, and fluid animations."),
    "impeccable-clarify": ("ui-copywrite", "Rewrites confusing buttons, error messages, and onboarding text into plain English."),
    "impeccable-onboard": ("ui-onboard", "Designs first-time welcome screens and empty states that guide new users."),
    "impeccable-harden": ("ui-harden", "Makes UI bulletproof against weird screen sizes, long text overflows, and network glitches."),
    "impeccable-optimize": ("ui-speed", "Speeds up slow-loading pages, laggy animations, and heavy web files."),
    "impeccable-extract": ("ui-tokens", "Gathers repeated buttons, colors, and fonts into reusable design tokens."),
    "impeccable-document": ("ui-doc-system", "Writes down your project's visual rules into a shareable DESIGN.md guide."),
    "impeccable-live": ("ui-live-tweak", "Lets you see and test AI design changes live in your running web browser."),
    "impeccable-generate": ("ui-variants", "Generates multiple design options for a component so you can pick the best one."),
    "impeccable-craft": ("ui-craft", "Ensures designs meet strict senior craftsmanship standards."),

    # 6. Code Review, Refactoring & Cleanup (6)
    "code-review": ("review-deep", "Runs thorough parallel checks to ensure code matches requirements and high standards."),
    "ponytail-review": ("review-bloat", "Hunts down overcomplicated code and deletes unnecessary layers."),
    "ponytail-audit": ("audit-bloat", "Scans your entire project for useless code, dead files, and security risks."),
    "safe-refactor": ("refactor-safe", "Cleans up messy code structure while guaranteeing zero change to how it functions."),
    "ponytail-debt": ("track-debt", "Catalogs temporary shortcuts and 'fix this later' notes into a clear to-do list."),
    "ponytail-gain": ("stats-savings", "Measures how much code, memory, and money was saved by keeping things simple."),

    # 7. Efficiency, Context & Token Optimization (14)
    "caveman": ("caveman", "Keeps our interactions short to save token usage and efficiency."),
    "megacave": ("caveman-dense", "Compresses answers into dense shorthand to preserve AI memory during huge tasks."),
    "ultracave": ("caveman-max", "Maximum possible compression mode for emergency context conservation."),
    "cavecrew": ("delegate-subagents", "Hands off background tasks to sub-agents so our main conversation doesn't get clogged."),
    "caveman-commit": ("git-terse-commit", "Writes short, meaningful commit messages with zero fluff."),
    "caveman-compress": ("docs-compress", "Shrinks large notes and memory files to save AI memory while keeping the facts."),
    "caveman-explore": ("explore-quiet", "Searches the codebase silently in the background without spamming the chat."),
    "caveman-stats": ("stats-tokens", "Shows how many tokens and cache reads we have used so far."),
    "caveman-help": ("help-caveman", "Displays a quick summary of token-saving commands."),
    "ponytail-help": ("help-ponytail", "Displays a quick cheat-sheet for minimalist coding commands."),
    "caveman-evidence-review": ("stats-spend", "Shows where your AI token budget is actually being spent."),
    "caveman-discover": ("trace-workflows", "Finds and labels all AI workflows in your project so costs can be tracked."),
    "caveman-learn": ("tune-prompts", "Finds wasteful prompt habits and applies fixes to permanently lower AI costs."),
    "caveman-manage": ("manage-experiments", "Manages and approves experiments to test AI cost reductions."),

    # 8. DevOps, Automation & Git Operations (10)
    "automation": ("ops-schedule", "Sets up background recurring automations and timers (cron jobs)."),
    "setup-pre-commit": ("ops-pre-commit", "Automatically checks code formatting and tests every time you make a git commit."),
    "git-guardrails-claude-code": ("ops-guardrails", "Blocks accidentally running destructive git commands like force pushes or deletions."),
    "permissioned-github": ("ops-github", "Handles secure, scoped access to GitHub repositories and pull requests."),
    "pr": ("git-pr", "Writes clean, well-structured pull request summaries for code review."),
    "plugin": ("ops-plugin", "Installs, manages, or creates plugins that package skills and tools together."),
    "setup-matt-pocock-skills": ("ops-setup-pocock", "Sets up Matt Pocock’s engineering skill pack environment."),
    "caveman-setup": ("ops-caveman-gateway", "Connects your project to an observability gateway to track AI efficiency."),
    "caveman-optimize": ("ops-optimize-eval", "Evaluates token optimization experiments against baseline tests."),
    "wizard": ("ops-wizard", "Creates an interactive terminal assistant that guides you step-by-step through manual setup."),

    # 9. Media, Showcase & Video (2)
    "brag": ("show-video", "Automatically turns your web project into a polished, animated showcase launch video."),
    "brag-slim": ("show-video-quick", "Creates a fast, lightweight showcase video with music and copy with no external assets needed."),

    # 10. Writing, Knowledge & Agent Customization (13)
    "writing-for-agents": ("write-agent-rules", "Writes crystal-clear instructions for AI agents so they follow your rules."),
    "writing-shape": ("write-outline", "Plans out the structural outline for long technical articles or documentation."),
    "writing-beats": ("write-pacing", "Plans the narrative flow and key highlights for technical explainers."),
    "writing-fragments": ("write-snippets", "Drafts self-contained modular paragraphs and snippets for documentation."),
    "research": ("knowledge-research", "Digs through authoritative documentation and saves a research summary in markdown."),
    "handoff": ("knowledge-handoff", "Summarizes current work state so another agent or session can take over seamlessly."),
    "claude-handoff": ("knowledge-handoff-claude", "Packages session notes formatted specifically for Claude Code transitions."),
    "agy-customizations": ("agent-customize", "Guide for building custom skills, rules, hooks, and MCP servers in Antigravity."),
    "antigravity_guide": ("agent-guide", "Complete guide and cheatsheet for using Antigravity features, IDE shortcuts, and CLI."),
    "generative_ui": ("agent-gen-ui", "Renders interactive visual widgets and dashboards right inside our chat window."),
    "ui-extension": ("agent-ui-panel", "Builds interactive web side panels that live right in the Antigravity workspace."),
    "ui-plugin-navigation": ("agent-ui-toggle", "Adds one-click buttons in chat to open relevant side panels."),
    "migrate-workflows": ("agent-migrate-skills", "Converts legacy workflow scripts into modern agent skills."),

    # 11. Backend, Databases & Cloud Infrastructure (10)
    "api-design": ("api-design", "Designs clean, standardized REST/GraphQL endpoints with consistent envelopes."),
    "api-validate": ("api-validate", "Implements strict input validation, sanitization, and Zod/Pydantic schemas."),
    "db-schema": ("db-schema", "Generates relational database schemas, migrations, and Prisma/Drizzle models."),
    "db-query-opt": ("db-query-opt", "Analyzes query execution plans, indexes, and eliminates N+1 query bottlenecks."),
    "sec-auth": ("sec-auth", "Implements secure auth flows like JWT rotation, session cookies, and OAuth."),
    "sec-audit": ("sec-audit", "Audits endpoints and configurations against OWASP Top 10 security risks."),
    "ops-docker": ("ops-docker", "Crafts minimal, multi-stage Dockerfiles and local compose environments."),
    "ops-ci-cd": ("ops-ci-cd", "Builds automated GitHub Actions CI/CD test and deployment pipelines."),
    "arch-queue": ("arch-queue", "Designs background worker jobs, queue retries, and scheduled workers."),
    "ops-telemetry": ("ops-telemetry", "Sets up structured JSON logging, correlation IDs, and Sentry error monitoring."),
}

def update_skill_frontmatter(skill_md_path, new_name, layman_desc):
    if not os.path.exists(skill_md_path):
        return
    with open(skill_md_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    frontmatter_pattern = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
    match = frontmatter_pattern.match(content)

    new_frontmatter = f"---\nname: {new_name}\ndescription: >-\n  {layman_desc}\n---\n\n"

    if match:
        body = content[match.end():]
        new_content = new_frontmatter + body
    else:
        new_content = new_frontmatter + content

    with open(skill_md_path, "w", encoding="utf-8") as f:
        f.write(new_content)

def find_source_skill_dirs():
    sources = {}

    # 1. Pocock skills
    pocock_dir = os.path.join(ROOT_DIR, "pocock-skills", "skills")
    if os.path.exists(pocock_dir):
        for root, dirs, files in os.walk(pocock_dir):
            if "SKILL.md" in files and "deprecated" not in root and "node_modules" not in root:
                name = os.path.basename(root)
                sources[name] = root

    # 2. Ponytail skills
    ponytail_dir = os.path.join(ROOT_DIR, "ponytail", "skills")
    if os.path.exists(ponytail_dir):
        for item in os.listdir(ponytail_dir):
            p = os.path.join(ponytail_dir, item)
            if os.path.isdir(p) and os.path.exists(os.path.join(p, "SKILL.md")):
                sources[item] = p

    # 3. Brag skills
    brag_dir = os.path.join(ROOT_DIR, "brag", "skills")
    if os.path.exists(brag_dir):
        for item in os.listdir(brag_dir):
            p = os.path.join(brag_dir, item)
            if os.path.isdir(p) and os.path.exists(os.path.join(p, "SKILL.md")):
                sources[item] = p

    # 4. Caveman skills
    caveman_dir = os.path.join(ROOT_DIR, "caveman", "skills")
    if os.path.exists(caveman_dir):
        for root, dirs, files in os.walk(caveman_dir):
            if "SKILL.md" in files and "generated" not in root and "node_modules" not in root:
                name = os.path.basename(root)
                sources[name] = root

    # 5. Impeccable base
    impeccable_src = os.path.join(ROOT_DIR, "impeccable", ".gemini", "skills", "impeccable")
    if os.path.exists(impeccable_src):
        sources["impeccable"] = impeccable_src

    # 6. Builtin skills
    if os.path.exists(BUILTIN_DIR):
        for item in os.listdir(BUILTIN_DIR):
            p = os.path.join(BUILTIN_DIR, item)
            if os.path.isdir(p) and os.path.exists(os.path.join(p, "SKILL.md")):
                sources[item] = p

    # 7. Backend & Cloud skills
    backend_dir = os.path.join(ROOT_DIR, "backend-cloud-skills", "skills")
    if os.path.exists(backend_dir):
        for item in os.listdir(backend_dir):
            p = os.path.join(backend_dir, item)
            if os.path.isdir(p) and os.path.exists(os.path.join(p, "SKILL.md")):
                sources[item] = p

    # 8. Arch Diagrams
    arch_diag_dir = os.path.join(ROOT_DIR, "arch-diagrams")
    if os.path.exists(arch_diag_dir):
        sources["arch-diagrams"] = arch_diag_dir

    # 9. Backend Reference Skills
    ref_dir = os.path.join(ROOT_DIR, "backend-reference-skills")
    if os.path.exists(ref_dir):
        for item in os.listdir(ref_dir):
            p = os.path.join(ref_dir, item)
            if os.path.isdir(p) and os.path.exists(os.path.join(p, "SKILL.md")):
                sources[item] = p

    # 10. Dev Isolated
    iso_dir = os.path.join(ROOT_DIR, "dev-isolated")
    if os.path.exists(iso_dir):
        sources["dev-isolated"] = iso_dir

    return sources

def main():
    print("=== Reorganizing and Syncing Skills for IDE Dropdown ===")
    os.makedirs(GLOBAL_SKILLS_DIR, exist_ok=True)
    sources = find_source_skill_dirs()

    # Read impeccable metadata for subcommands
    impeccable_src = os.path.join(ROOT_DIR, "impeccable", ".gemini", "skills", "impeccable")
    impeccable_meta = {}
    meta_file = os.path.join(impeccable_src, "scripts", "command-metadata.json")
    if os.path.exists(meta_file):
        with open(meta_file, "r", encoding="utf-8") as f:
            impeccable_meta = json.load(f)

    # Clean out old directories from GLOBAL_SKILLS_DIR that don't match our new target names
    expected_new_names = set(v[0] for v in SKILL_MAP.values())
    for item in os.listdir(GLOBAL_SKILLS_DIR):
        item_path = os.path.join(GLOBAL_SKILLS_DIR, item)
        if os.path.isdir(item_path) and item not in expected_new_names:
            print(f"Removing old unmapped skill folder: {item}")
            shutil.rmtree(item_path, ignore_errors=True)

    synced_count = 0
    for old_name, (new_name, layman_desc) in SKILL_MAP.items():
        dest_path = os.path.join(GLOBAL_SKILLS_DIR, new_name)

        if old_name in sources:
            src_path = sources[old_name]
            # Copy source directory to target
            if os.path.exists(dest_path):
                shutil.rmtree(dest_path, ignore_errors=True)
            shutil.copytree(src_path, dest_path)
            # Update SKILL.md frontmatter
            skill_md = os.path.join(dest_path, "SKILL.md")
            update_skill_frontmatter(skill_md, new_name, layman_desc)
            synced_count += 1
            print(f"Synced: {old_name} -> {new_name}")

        elif old_name.startswith("impeccable-"):
            cmd = old_name.replace("impeccable-", "")
            os.makedirs(dest_path, exist_ok=True)
            skill_md = os.path.join(dest_path, "SKILL.md")

            native_ref = ""
            impeccable_dest = os.path.join(GLOBAL_SKILLS_DIR, "ui-master")
            if os.path.exists(os.path.join(impeccable_src, "reference", f"{cmd}.native.md")):
                native_ref = f" (on native platforms: [reference/{cmd}.native.md](file:///C:/Users/Mark%20Vasquez/.gemini/config/skills/ui-master/reference/{cmd}.native.md))"

            content = f"""---
name: {new_name}
description: >-
  {layman_desc}
---

# /{new_name}

Execute Impeccable's **{cmd}** command workflow.

## Instructions

1. **Context & Setup**:
   - Read `PRODUCT.md` and `DESIGN.md` directly from the project root.
   - Before applying any frontend code edits, review [reference/craft-floor.md](file:///C:/Users/Mark%20Vasquez/.gemini/config/skills/ui-master/reference/craft-floor.md) to uphold the craftsmanship floor.

2. **Playbook Execution**:
   - Follow the primary playbook for this command:
     [reference/{cmd}.md](file:///C:/Users/Mark%20Vasquez/.gemini/config/skills/ui-master/reference/{cmd}.md){native_ref}
   - Execute the steps specified in the playbook for the target component, page, or feature.
"""
            with open(skill_md, "w", encoding="utf-8") as f:
                f.write(content)
            synced_count += 1
            print(f"Generated Impeccable Command: {old_name} -> {new_name}")

    print(f"\nSuccessfully reorganized and synced {synced_count} skills into {GLOBAL_SKILLS_DIR}!")

if __name__ == "__main__":
    main()
