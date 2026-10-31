# Antigravity & Codex Agent Workflow Cheat-Sheet
# Usage: .\agy-workflow.ps1 (or 'agy-workflow' once configured in profile)

Clear-Host
Write-Host ""
Write-Host " ======================================================================= " -ForegroundColor Cyan
Write-Host "   === ANTIGRAVITY & CODEX AGENT WORKFLOW CHEAT-SHEET (130 SKILLS) ===   " -ForegroundColor Yellow -BackgroundColor Black
Write-Host " ======================================================================= " -ForegroundColor Cyan
Write-Host ""

# Stage 1: Planning
Write-Host " [STAGE 1] PLANNING & CONFIRMATION GATE" -ForegroundColor Green
Write-Host "   /plan            " -NoNewline -ForegroundColor White
Write-Host "-> (Antigravity) Stops, investigates codebase, mounts native Proceed [Ctrl+Enter] button." -ForegroundColor Gray
Write-Host "   /maxplan         " -NoNewline -ForegroundColor White
Write-Host "-> (Codex/Claude Code) PM coordinator recommends models (flash vs pro) & sub-skills." -ForegroundColor Gray
Write-Host "   /ask-interview   " -NoNewline -ForegroundColor White
Write-Host "-> Stress-tests requirements and uncovers hidden assumptions." -ForegroundColor Gray
Write-Host "   /plan-tickets    " -NoNewline -ForegroundColor White
Write-Host "-> Slices large blueprint into sequential, verifiable tasks." -ForegroundColor Gray
Write-Host ""

# Stage 2: Guardrails
Write-Host " [STAGE 2] ALWAYS-ON ANDREJ KARPATHY GUARDRAILS" -ForegroundColor Green
Write-Host "   /karpathy-guidelines" -NoNewline -ForegroundColor White
Write-Host " -> Enforces 4 core rules:" -ForegroundColor Gray
Write-Host "     1. Think Before Coding (state assumptions, ask when uncertain)" -ForegroundColor DarkCyan
Write-Host "     2. Simplicity First (minimum code, zero speculative abstractions)" -ForegroundColor DarkCyan
Write-Host "     3. Surgical Changes (touch only requested lines, preserve adjacent code)" -ForegroundColor DarkCyan
Write-Host "     4. Goal-Driven Execution (define [Step] -> verify: [check] loops)" -ForegroundColor DarkCyan
Write-Host ""

# Stage 3: Engineering
Write-Host " [STAGE 3] ARCHITECTURE & BACKEND ENGINEERING" -ForegroundColor Green
Write-Host "   /arch-bulletproof" -NoNewline -ForegroundColor White
Write-Host " -> 3-tier Controller -> Service -> Data Access refactor." -ForegroundColor Gray
Write-Host "   /api-validate    " -NoNewline -ForegroundColor White
Write-Host " -> Strict input validation and Zod/Pydantic schemas." -ForegroundColor Gray
Write-Host "   /dev-prisma      " -NoNewline -ForegroundColor White
Write-Host " -> Type-safe database schemas and Prisma models." -ForegroundColor Gray
Write-Host "   /dev-build       " -NoNewline -ForegroundColor White
Write-Host " -> Builds strictly according to plan with no unsolicited extras." -ForegroundColor Gray
Write-Host "   /dev-lean        " -NoNewline -ForegroundColor White
Write-Host " -> Builds minimum viable feature with strict stops." -ForegroundColor Gray
Write-Host ""

# Stage 4: Frontend
Write-Host " [STAGE 4] FRONTEND ART DIRECTION & LIVE ELEMENT ANNOTATION" -ForegroundColor Green
Write-Host "   /taste-skill     " -NoNewline -ForegroundColor White
Write-Host " -> Tasteskill v2 anti-slop art direction distilled from 247 gallery sites." -ForegroundColor Gray
Write-Host "   /ui-ux-pro-max   " -NoNewline -ForegroundColor White
Write-Host " -> Searchable design intelligence: 79 styles, 192 palettes, 74 font pairings." -ForegroundColor Gray
Write-Host "   /ui-annotate     " -NoNewline -ForegroundColor White
Write-Host " -> Connects Codex browser overlay (Ctrl+Shift+A) directly to instant code edits." -ForegroundColor Gray
Write-Host "   /ui-polish       " -NoNewline -ForegroundColor White
Write-Host " -> Final touches to alignment, pixel rhythm, spacing, and visual harmony." -ForegroundColor Gray
Write-Host ""

# Stage 5: Security & Testing
Write-Host " [STAGE 5] TESTING & SECURITY AUDITING" -ForegroundColor Green
Write-Host "   /qa-test-first   " -NoNewline -ForegroundColor White
Write-Host " -> Strict TDD (Red-Green-Refactor loop) before writing implementation." -ForegroundColor Gray
Write-Host "   /sec-skillspector" -NoNewline -ForegroundColor White
Write-Host " -> NVIDIA SkillSpector scanner checking AI skills/MCPs for prompt injection & CVEs." -ForegroundColor Gray
Write-Host "   /sec-audit       " -NoNewline -ForegroundColor White
Write-Host " -> Cloudflare 6-phase offensive & defensive vulnerability discovery harness." -ForegroundColor Gray
Write-Host ""

# Stage 6: Review & Git
Write-Host " [STAGE 6] REVIEW, BLOAT REMOVAL & PR" -ForegroundColor Green
Write-Host "   /audit-bloat     " -NoNewline -ForegroundColor White
Write-Host " -> Scans project for overcomplicated layers, dead files, and unused code." -ForegroundColor Gray
Write-Host "   /caveman         " -NoNewline -ForegroundColor White
Write-Host " -> Ultra-compressed token-saving mode to preserve context during big tasks." -ForegroundColor Gray
Write-Host "   /ops-guardrails  " -NoNewline -ForegroundColor White
Write-Host " -> Blocks destructive git commands (force pushes, hard resets)." -ForegroundColor Gray
Write-Host "   /git-pr          " -NoNewline -ForegroundColor White
Write-Host " -> Generates clean, structured PR descriptions for review." -ForegroundColor Gray
Write-Host "   /show-video      " -NoNewline -ForegroundColor White
Write-Host " -> Creates automated animated launch video for web showcase." -ForegroundColor Gray
Write-Host ""

# Maintenance
Write-Host " [SYSTEM MAINTENANCE]" -ForegroundColor Magenta
Write-Host "   .\\sync-all-skills.ps1" -ForegroundColor Yellow
Write-Host "   -> One-command end-to-end sync: pulls 8 upstream repos, reorganizes 130 skills," -ForegroundColor Gray
Write-Host "      cleans __pycache__, syncs Antigravity/Codex, and rebuilds README tables." -ForegroundColor Gray
Write-Host ""
Write-Host " ======================================================================= " -ForegroundColor Cyan
Write-Host ""
