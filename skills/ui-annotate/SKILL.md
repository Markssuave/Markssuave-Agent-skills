---
name: ui-annotate
description: >-
  Inspects live browser UI annotations dispatched via the Codex Annotator bridge and applies targeted modifications to the matching React component or page.
---

# /ui-annotate — Codex UI Element Annotator Workflow

Receives and executes UI element modification requests dispatched directly from the browser overlay (`annotator.js`) via the local Codex Annotator bridge.

## How It Works

1. **In-Browser Annotation**:
   - The user opens their web app in development (`http://localhost:5173`).
   - Clicks `🎯 Annotate` (or presses `Ctrl+Shift+A`).
   - Clicks any UI element, types instructions, and clicks **"⚡ Send to Antigravity"**.

2. **Fetching the Annotation**:
   - **Method A (MCP)**: If the `codex-annotator` MCP server is active, call `get_latest_annotation(pop=True)`.
   - **Method B (File / HTTP Fallback)**:
     - Read `C:\Users\Mark Vasquez\Documents\Agent Skills\codex-annotator\latest_annotation.json`
     - Or query `http://127.0.0.1:3456/latest` via curl/Invoke-RestMethod.

3. **Processing the Instruction**:
   - Inspect the metadata:
     - `componentName`: The identified React component (e.g., `<ExperienceSection />`, `<Navbar />`).
     - `selector`: The CSS selector path.
     - `text`: Text content of the selected element.
     - `outerHTML`: Exact HTML snippet of the element.
     - `instruction`: The user's exact modification prompt.

4. **Applying Modifications**:
   - Locate the source file matching `componentName` or `selector` in `src/`.
   - Apply precise, isolated edits with `replace_file_content`.
   - Preserve existing styling conventions and responsive design.

5. **Verification**:
   - Run `npx tsc --noEmit` and `npm run build` to verify compilation.
