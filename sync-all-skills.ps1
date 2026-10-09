# Master Skills Sync: Matt Pocock + Ponytail + Brag + Impeccable + Caveman
Write-Host "=== Syncing Global Agent Skills ===" -ForegroundColor Cyan

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

# 7. Reorganize & Sync All 102 Skills with Role-Based Slash Commands
Write-Host "Reorganizing & Syncing All 102 Skills with Slash Commands..." -ForegroundColor Yellow
python "$rootDir\sync_reorganized_skills.py"

# 12. Ensure Global Rules (GEMINI.md & AGENTS.md) stay in sync
Write-Host "Syncing Global Rules (GEMINI.md & AGENTS.md)..." -ForegroundColor Yellow
$globalConfigDir = "C:\Users\Mark Vasquez\.gemini\config"
if (Test-Path "$rootDir\GEMINI.md") {
    Copy-Item "$rootDir\GEMINI.md" "$globalConfigDir\GEMINI.md" -Force
}
if (Test-Path "$rootDir\AGENTS.md") {
    Copy-Item "$rootDir\AGENTS.md" "$globalConfigDir\AGENTS.md" -Force
}

$totalActive = (Get-ChildItem $globalSkillsDir -Directory).Count
Write-Host "`n=== Sync Complete! Total Global Skills Active: $totalActive ===" -ForegroundColor Green
