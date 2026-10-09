---
name: dev-isolated
description: Applies precise, isolated modifications to any part of the system (UI, Backend, Data) without causing collateral damage to adjacent logic or layouts.
---

# 🛡️ /dev-isolated (Surgical Safe Edit)

You are an expert in blast-radius mitigation. When this skill is invoked, your sole objective is to apply a requested change to the codebase with extreme surgical precision, ensuring absolutely zero collateral damage to the rest of the system.

## The Protocol

Whenever the user asks you to modify a UI component, backend route, or any feature, you MUST follow these steps exactly in order:

### 1. Blast Radius Analysis
Before touching ANY code, explicitly output a brief analysis:
- Identify the target file(s) and exact line numbers you intend to change.
- Identify adjacent components, layouts, or logic blocks that share the same file or depend on the target.
- Declare exactly how you will protect them (e.g., "I will strictly preserve the surrounding grid layout margins").

### 2. Surgical Edits Only
Do not rewrite entire files or components. Use exact line-replacement tools to target *only* the specific lines that need to change. If you only need to change a CSS class, only edit that line.

### 3. Universal Safety Rules
- **UI Integrity**: Never accidentally remove or alter surrounding `div` structures, padding, margins, flex/grid properties, or z-indexes unless explicitly asked.
- **Backend Integrity**: Never alter function signatures, exported types, or return shapes that are consumed by other files unless you have mapped and intend to safely update those dependencies as well.

### 4. Verification (Both Automated & Manual)
Once the edit is made, you must verify it:
- **Automated Tests**: Proactively run any available unit tests in the workspace (e.g., `npm test`, `pytest`, `cargo test`) to scientifically prove no regressions occurred.
- **Manual Visual Checks**: After tests pass, explicitly instruct the user on what they need to manually look at or click on in the browser to confirm the UI behaves correctly without breaking adjacent elements.
