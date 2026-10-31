import os, yaml, re

ROOT_DIR = r"C:\Users\Mark Vasquez\Documents\Agent Skills"
SKILLS_DIR = os.path.join(ROOT_DIR, "skills")
TARGET_README = os.path.join(ROOT_DIR, "README.md")
SUBMODULE_README = os.path.join(ROOT_DIR, "Markssuave-Agent-skills", "README.md")

def get_skill_info(folder):
    p = os.path.join(SKILLS_DIR, folder, "SKILL.md")
    name = folder
    desc = "No description provided."
    if os.path.exists(p):
        with open(p, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
            if match:
                try:
                    data = yaml.safe_load(match.group(1))
                    if isinstance(data, dict):
                        name = data.get("name", folder)
                        desc = str(data.get("description", desc)).replace("\n", " ").strip()
                except Exception:
                    pass
    # Escape pipe characters to maintain clean markdown table format
    desc = desc.replace("|", "\\|")
    return name, desc, folder

def get_origin_badge(name):
    if name == "maxplan":
        return "Codex Protocol"
    if name == "ui-annotate":
        return "Codex Annotator Bridge"
    if name in ["karpathy-guidelines"]:
        return "Andrej Karpathy Skills"
    if name in ["sec-skillspector"]:
        return "NVIDIA SkillSpector"
    if name in ["sec-audit"]:
        return "Cloudflare Security Audit"
    if name in ["taste-skill", "design-taste-frontend"]:
        return "Tasteskill v2"
    if name in ["ui-ux-pro-max", "ui-ux-pro-max-skill"]:
        return "UI/UX Pro Max"
    if name.startswith("ui-") or "impeccable" in name:
        return "Impeccable UI/UX Suite"
    if name.startswith("caveman") or name.startswith("stats-") or name in ["explore-quiet", "delegate-subagents", "git-terse-commit", "docs-compress", "help-caveman", "trace-workflows", "tune-prompts", "manage-experiments", "ops-caveman-gateway", "ops-optimize-eval"]:
        return "Caveman Token Suite"
    if name.startswith("ponytail") or name in ["dev-minimal", "review-bloat", "audit-bloat", "track-debt", "stats-savings", "help-ponytail"]:
        return "Ponytail Minimalist Dev"
    if name in ["api-design", "api-validate", "db-schema", "db-query-opt", "sec-auth", "ops-docker", "ops-ci-cd", "arch-queue", "ops-telemetry", "dev-prisma", "dev-authjs", "dev-bullmq", "arch-bulletproof", "arch-node-best"]:
        return "Backend & Cloud Skills"
    if name.startswith("qa-") or name.startswith("arch-") or name.startswith("plan-") or name.startswith("ask-") or name.startswith("learn-") or name.startswith("dev-") or name in ["sanity-check", "feedback-loop"]:
        return "Matt Pocock Engineering"
    if name.startswith("show-video") or "brag" in name:
        return "Brag Video Suite"
    if name in ["agent-ui-panel", "agent-ui-toggle", "agent-migrate-skills", "agent-customize", "agent-guide", "agent-gen-ui", "ops-schedule", "ops-github", "ops-plugin"]:
        return "Antigravity Built-in"
    return "Custom System Skill"

CATEGORY_DEFINITIONS = [
    (
        "1. 📐 Planning, Product & Architecture",
        "Blueprint creation, ticket breakdown, domain modeling, and high-level architectural boundaries.",
        [
            "maxplan", "plan-tickets", "plan-domain", "arch-design", "arch-improve", 
            "arch-setup-ts", "plan-triage", "plan-map", "plan-orchestrate", "plan-retro", 
            "arch-diagrams", "arch-node-best", "arch-bulletproof"
        ]
    ),
    (
        "2. 💡 Clarification, Interviewing & Teaching",
        "Interactive clarification interviews, devil's advocacy stress-testing, senior heuristics, and technical concept explainers.",
        [
            "ask-interview", "ask-challenge", "ask-docs-interview", "ask-form", 
            "learn-explain", "learn-expert", "sanity-check", "feedback-loop"
        ]
    ),
    (
        "3. ⚡ Core Development & Engineering",
        "Disciplined code implementation, Karpathy guardrails, minimum viable builds, prototypes, migrations, and database patterns.",
        [
            "karpathy-guidelines", "dev-isolated", "dev-prisma", "dev-authjs", 
            "dev-bullmq", "dev-build", "dev-build-spec", "dev-lean", 
            "dev-prototype", "dev-minimal", "dev-migrate", "dev-fix-types"
        ]
    ),
    (
        "4. 🧪 Testing, QA & Debugging",
        "Test-driven development loops, step-by-step scientific deduction, narrow surgical bug patches, and proof verification.",
        [
            "qa-test-first", "qa-diagnose", "qa-investigate", "qa-patch", 
            "qa-verify", "qa-quick-review", "qa-scaffold"
        ]
    ),
    (
        "5. 🎨 Frontend, UI/UX & Design",
        "Visual art direction, anti-slop curation, design intelligence databases, live element annotator bridge, and pixel polish.",
        [
            "ui-master", "taste-skill", "design-taste-frontend", "ui-ux-pro-max", 
            "ui-ux-pro-max-skill", "ui-annotate", "ui-init", "ui-shape", 
            "ui-critique", "ui-audit", "ui-polish", "ui-layout", 
            "ui-responsive", "ui-typography", "ui-colors", "ui-make-bold", 
            "ui-tone-down", "ui-declutter", "ui-animate", "ui-delight", 
            "ui-high-end", "ui-copywrite", "ui-onboard", "ui-harden", 
            "ui-speed", "ui-tokens", "ui-doc-system", "ui-live-tweak", 
            "ui-variants", "ui-craft"
        ]
    ),
    (
        "6. 🧹 Code Review, Refactoring & Cleanup",
        "Overcomplication hunting, safe structural refactoring, dead file scans, and technical debt tracking.",
        [
            "review-deep", "review-bloat", "audit-bloat", "refactor-safe", 
            "track-debt", "stats-savings"
        ]
    ),
    (
        "7. 🗜️ Efficiency, Context & Token Optimization",
        "Ultra-compressed communication shorthand, background subagent delegation, token spend tracking, and prompt tuning.",
        [
            "caveman", "caveman-dense", "caveman-max", "delegate-subagents", 
            "git-terse-commit", "docs-compress", "explore-quiet", "stats-tokens", 
            "help-caveman", "help-ponytail", "stats-spend", "trace-workflows", 
            "tune-prompts", "manage-experiments"
        ]
    ),
    (
        "8. 🚀 DevOps, Automation & Git Operations",
        "Scheduled background automations, Git guardrails, pull request generation, and developer environment wizards.",
        [
            "ops-schedule", "ops-pre-commit", "ops-guardrails", "ops-github", 
            "git-pr", "ops-plugin", "ops-setup-pocock", "ops-caveman-gateway", 
            "ops-optimize-eval", "ops-wizard"
        ]
    ),
    (
        "9. 🎬 Media, Showcase & Video",
        "Automated code-to-video generation for web project launches and animated video showcases.",
        [
            "show-video", "show-video-quick"
        ]
    ),
    (
        "10. ✍️ Writing, Knowledge & Agent Customization",
        "Agent prompt rules, technical prose humanization, Microsoft MarkItDown conversion, and interactive sidecar panels.",
        [
            "write-agent-rules", "write-outline", "write-pacing", "write-snippets", 
            "write-humanize", "humanizer", "doc-markitdown", "markitdown", 
            "knowledge-research", "knowledge-handoff", "knowledge-handoff-claude", 
            "agent-customize", "agent-guide", "agent-gen-ui", "agent-ui-panel", 
            "agent-ui-toggle", "agent-migrate-skills"
        ]
    ),
    (
        "11. 🛡️ Backend, Databases & Cloud Infrastructure",
        "Consistent API endpoints, strict Zod validation, Prisma/Drizzle schemas, Cloudflare 6-phase security audits, and NVIDIA SkillSpector scans.",
        [
            "api-design", "api-validate", "db-schema", "db-query-opt", 
            "sec-auth", "sec-audit", "sec-skillspector", "ops-docker", 
            "ops-ci-cd", "arch-queue", "ops-telemetry"
        ]
    )
]

aliases = {"design-taste-frontend", "ui-ux-pro-max-skill", "humanizer", "markitdown"}

def generate_readme():
    all_categorized = []
    for _, _, skill_list in CATEGORY_DEFINITIONS:
        all_categorized.extend(skill_list)

    total_count = len(all_categorized)
    
    lines = []
    lines.append("# 🧠 Markssuave Agent Skills\n")
    lines.append(f"> A master collection of **{total_count} battle-tested AI agent skills** organized across 11 core engineering roles for **Codex**, **Claude Code**, and **Google Antigravity / Gemini**.\n")
    lines.append("---\n")
    
    lines.append("## 📌 Quick Navigation (By Role Tables)\n")
    for title, _, s_list in CATEGORY_DEFINITIONS:
        anchor = re.sub(r"[^\w\s-]", "", title).strip().replace(" ", "-").lower()
        lines.append(f"- [{title}](#{anchor}) *({len(s_list)} skills)*")
    lines.append("\n---\n")

    lines.append("## 🚀 Quick Setup Guide for Friends\n")
    lines.append("### 1. Which Environment Are You Using?\n")
    lines.append("- **For Codex / Claude Code Users:**")
    lines.append("  - Load [`AGENTS.md`](AGENTS.md) as your project or system rules.")
    lines.append("  - Type `/maxplan` in prompts to trigger the automated project planning coordinator.")
    lines.append("  - Use `/ui-annotate` to receive live element edits directly from the browser overlay bridge (`annotator.js`).\n")
    lines.append("- **For Antigravity / Gemini IDE Users:**")
    lines.append("  - Load [`GEMINI.md`](GEMINI.md) as your project or system rules.")
    lines.append("  - Type `/plan` in prompts to trigger the native IDE confirmation plan gate with interactive choice cards.")
    lines.append("  - Use `/taste-skill` and `/ui-ux-pro-max` for curated frontend art direction and design intelligence.\n")

    lines.append("### 2. Auto-Install All Skills With One Command\n")
    lines.append("To automatically synchronize all skills into your local agent directories (`~/.gemini/config/skills` and `~/.codex/skills`), simply run:\n")
    lines.append("```bash\npython sync_reorganized_skills.py\n```\n")
    lines.append("This script automatically validates frontmatter, strips compiled bytecode (`__pycache__`), maps slash commands, and updates your dropdown menu.\n")
    lines.append("---\n")

    lines.append("## 🔗 Upstream Open Source References & Engines\n")
    lines.append("This repository is powered by and builds upon the following exceptional open-source agent projects:\n")
    lines.append("| Upstream Project | Author / Maintainer | Core Focus | Repository Link |")
    lines.append("| :--- | :--- | :--- | :--- |")
    lines.append("| **Andrej Karpathy Skills** | multica-ai | 4 Coding Guardrails & LLM Pitfall Avoidance | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) |")
    lines.append("| **Cloudflare Security Audit** | Cloudflare | 6-Phase Offensive & Defensive Code Vulnerability Harness | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) |")
    lines.append("| **NVIDIA SkillSpector** | NVIDIA | Static & Taint Analysis Scanner for AI Skills & MCPs | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) |")
    lines.append("| **Tasteskill v2** | Community | Anti-Slop Web Art Direction Distilled from 247 Gallery Sites | [Built-in Engine](skills/taste-skill) |")
    lines.append("| **UI/UX Pro Max** | Community | Design Intelligence: 79 Styles, 192 Palettes, 74 Fonts | [Built-in Engine](skills/ui-ux-pro-max) |")
    lines.append("| **Pocock Skills** | Matt Pocock | Disciplined Software Engineering, TDD, & Architecture | [mattpocock/skills](https://github.com/mattpocock/skills) |")
    lines.append("| **Caveman** | Julius Brussee | Token & Memory Efficiency Compression Protocol | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) |")
    lines.append("| **Impeccable** | Paul Bakaus | Design Director & Frontend Craftsmanship Suite | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |")
    lines.append("| **Ponytail** | Dietrich Gebert | Minimalist Senior Engineering & Bloat Removal | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) |")
    lines.append("\n---\n")

    lines.append("## 🗂️ Complete Directory of Skills by Role\n")

    for cat_title, cat_desc, skill_list in CATEGORY_DEFINITIONS:
        lines.append(f"### {cat_title}\n")
        lines.append(f"*{cat_desc}*\n")
        lines.append("| Slash Command | Origin / Suite | What It Does (In Layman's Terms) | Folder |")
        lines.append("| :--- | :--- | :--- | :--- |")
        
        for folder in skill_list:
            name, desc, f_path = get_skill_info(folder)
            origin = get_origin_badge(name)
            badge = " `[Alias]`" if name in aliases else ""
            if name == "maxplan":
                badge = " `[Codex Protocol]`"
            elif name == "ui-annotate":
                badge = " `[Codex Bridge]`"
            
            lines.append(f"| `/{name}`{badge} | {origin} | {desc} | [`skills/{f_path}`](skills/{f_path}) |")
        lines.append("\n")

    output_content = "\n".join(lines)
    
    with open(TARGET_README, "w", encoding="utf-8") as f:
        f.write(output_content)
    print(f"Generated {TARGET_README} with {total_count} skills.")

    if os.path.exists(os.path.dirname(SUBMODULE_README)):
        with open(SUBMODULE_README, "w", encoding="utf-8") as f:
            f.write(output_content)
        print(f"Mirrored {SUBMODULE_README} with {total_count} skills.")

if __name__ == "__main__":
    generate_readme()
