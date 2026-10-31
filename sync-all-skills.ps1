# Master Skills Sync: Matt Pocock + Ponytail + Brag + Impeccable + Caveman + Karpathy + SkillSpector + Cloudflare
Write-Host "=== Master Agent Skills End-to-End Sync ===" -ForegroundColor Cyan

$rootDir = $PSScriptRoot
$globalSkillsDir = "C:\Users\Mark Vasquez\.gemini\config\skills"

# 1. Update Pocock Skills
$pocockDir = "$rootDir\pocock-skills"
if (Test-Path "$pocockDir\.git") {
    Write-Host "`nUpdating Pocock Skills..." -ForegroundColor Yellow
    git -C $pocockDir pull origin main
}

# 2. Update Ponytail
$ponytailDir = "$rootDir\ponytail"
if (Test-Path "$ponytailDir\.git") {
    Write-Host "`nUpdating Ponytail..." -ForegroundColor Yellow
    git -C $ponytailDir pull origin main
}

# 3. Update Brag Skills
$bragDir = "$rootDir\brag"
if (Test-Path "$bragDir\.git") {
    Write-Host "`nUpdating Brag Skills..." -ForegroundColor Yellow
    git -C $bragDir pull origin main
}

# 4. Update Impeccable Skills
$impeccableDir = "$rootDir\impeccable"
if (Test-Path "$impeccableDir\.git") {
    Write-Host "`nUpdating Impeccable Skills..." -ForegroundColor Yellow
    git -C $impeccableDir pull origin main
}

# 5. Update Caveman Skills
$cavemanDir = "$rootDir\caveman"
if (Test-Path "$cavemanDir\.git") {
    Write-Host "`nUpdating Caveman Skills..." -ForegroundColor Yellow
    git -C $cavemanDir pull origin main
}

# 5b. Update Andrej Karpathy Skills
$karpathyDir = "$rootDir\andrej-karpathy-skills"
if (Test-Path "$karpathyDir\.git") {
    Write-Host "`nUpdating Andrej Karpathy Skills..." -ForegroundColor Yellow
    git -C $karpathyDir pull origin main
}

# 5c. Update NVIDIA SkillSpector
$skillspectorDir = "$rootDir\SkillSpector"
if (Test-Path "$skillspectorDir\.git") {
    Write-Host "`nUpdating NVIDIA SkillSpector..." -ForegroundColor Yellow
    git -C $skillspectorDir pull origin main
}

# 5d. Update Cloudflare Security Audit Skill
$cfAuditDir = "$rootDir\cloudflare-security-audit"
if (Test-Path "$cfAuditDir\.git") {
    Write-Host "`nUpdating Cloudflare Security Audit Skill..." -ForegroundColor Yellow
    git -C $cfAuditDir pull origin main
}

# 6. Ensure global skills directory exists
if (!(Test-Path $globalSkillsDir)) {
    New-Item -ItemType Directory -Path $globalSkillsDir | Out-Null
}

# Remove existing junctions / links so clean real folders can be created
Write-Host "`nCleaning up old junctions..." -ForegroundColor Yellow
Get-ChildItem -Path $globalSkillsDir | ForEach-Object {
    if ($_.LinkType -or ($_.Attributes -band [System.IO.FileAttributes]::ReparsePoint)) {
        cmd /c rmdir "$($_.FullName)"
    }
}

# 7. Reorganize & Sync All 130 Skills with Role-Based Slash Commands
Write-Host "`nReorganizing & Syncing All 130 Skills across Antigravity & Codex..." -ForegroundColor Yellow
python "$rootDir\sync_reorganized_skills.py"

# 8. Ensure Global Rules (GEMINI.md & AGENTS.md) stay in sync across Antigravity & Codex
Write-Host "`nSyncing Global Rules (GEMINI.md & AGENTS.md) to Antigravity and Codex..." -ForegroundColor Yellow
$globalConfigDir = "C:\Users\Mark Vasquez\.gemini\config"
$codexConfigDir = "C:\Users\Mark Vasquez\.codex"
if (Test-Path "$rootDir\GEMINI.md") {
    Copy-Item "$rootDir\GEMINI.md" "$globalConfigDir\GEMINI.md" -Force
}
if (Test-Path "$rootDir\AGENTS.md") {
    Copy-Item "$rootDir\AGENTS.md" "$globalConfigDir\AGENTS.md" -Force
    if (Test-Path $codexConfigDir) {
        Copy-Item "$rootDir\AGENTS.md" "$codexConfigDir\AGENTS.md" -Force
    }
}

# 9. Rebuild Table-Based Master Documentation (README.md)
Write-Host "`nRebuilding Master Documentation Tables (README.md)..." -ForegroundColor Yellow
$readmeBuilder = "$rootDir\repo_export\build_table_readme.py"
if (Test-Path $readmeBuilder) {
    python $readmeBuilder
}

# 10. Mirror changes to nested repository if present
$submoduleDir = "$rootDir\Markssuave-Agent-skills"
if (Test-Path $submoduleDir) {
    Write-Host "`nMirroring to nested repository..." -ForegroundColor Yellow
    Copy-Item "$rootDir\README.md" "$submoduleDir\README.md" -Force
    Copy-Item "$rootDir\AGENTS.md" "$submoduleDir\AGENTS.md" -Force
    Copy-Item "$rootDir\GEMINI.md" "$submoduleDir\GEMINI.md" -Force
    Copy-Item "$rootDir\sync_reorganized_skills.py" "$submoduleDir\sync_reorganized_skills.py" -Force
    Copy-Item "$rootDir\sync-all-skills.ps1" "$submoduleDir\sync-all-skills.ps1" -Force
    if (Test-Path "$rootDir\agy-workflow.ps1") {
        Copy-Item "$rootDir\agy-workflow.ps1" "$submoduleDir\agy-workflow.ps1" -Force
    }
}

$totalActive = (Get-ChildItem $globalSkillsDir -Directory).Count
Write-Host "`n=== Master Sync Complete! Total Active Skills: $totalActive ===" -ForegroundColor Green
Write-Host "All 130 skills, slash commands, rules, and README tables are fully synchronized." -ForegroundColor Cyan
