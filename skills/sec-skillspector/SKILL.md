---
name: sec-skillspector
description: >-
  Scans AI agent skills, MCP servers, and GitHub repositories for prompt injection, data exfiltration, malicious code, and supply-chain CVEs using NVIDIA SkillSpector.
---

# /sec-skillspector

Scan an AI agent skill, MCP configuration, `.zip` archive, or GitHub repository for 71 security vulnerability patterns using **NVIDIA SkillSpector** before installing or trusting it.

## Binary Path
```powershell
$skillspector = "C:\Users\Mark Vasquez\Documents\Agent Skills\SkillSpector\.venv\Scripts\skillspector.exe"
```

## Critical Windows Rule
- **NEVER pass `-o` or `--output` on Windows.** SkillSpector's file writer requires POSIX `O_NOFOLLOW` directory operations and intentionally fails on Windows. Always omit `--output` so results stream to `stdout`.

## Execution Workflow

1. **Fast Static + OSV.dev Scan (Default, Zero Cost)**:
   Run static AST, regex, taint-tracking, YARA, and live OSV.dev CVE checks without sending files to an external LLM:
   ```powershell
   & "C:\Users\Mark Vasquez\Documents\Agent Skills\SkillSpector\.venv\Scripts\skillspector.exe" scan "<target-path-or-url>" --no-llm --format json
   ```

2. **Recursive Collection Scan** (for multi-skill repos):
   ```powershell
   & "C:\Users\Mark Vasquez\Documents\Agent Skills\SkillSpector\.venv\Scripts\skillspector.exe" scan "<target-dir>" --recursive --max-skills 100 --no-llm --format terminal
   ```

3. **Optional Semantic LLM Pass** (only when static findings need disambiguation):
   Set `SKILLSPECTOR_PROVIDER` (`gemini_cli`, `claude_cli`, `openai`, or `anthropic`) and omit `--no-llm`:
   ```powershell
   $env:SKILLSPECTOR_PROVIDER = "gemini_cli"
   & "C:\Users\Mark Vasquez\Documents\Agent Skills\SkillSpector\.venv\Scripts\skillspector.exe" scan "<target-path-or-url>" --format json
   ```

4. **Gate Policy**:
   - `SAFE` (Score `0-20`): Safe to install.
   - `CAUTION` (Score `21-50`): Review flagged lines and explain trade-offs to the user before installing.
   - `DO_NOT_INSTALL` (Score `51-100`): Block installation immediately and report exact findings (`id`, `severity`, `location`, `explanation`).
