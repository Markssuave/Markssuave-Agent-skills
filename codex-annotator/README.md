# 🎯 Codex-Style UI Annotator for Antigravity

A zero-dependency, open-source bridge that brings OpenAI Codex's in-browser annotation workflow to **Antigravity**.

Click any live UI element in your browser, type what you want changed, and dispatch it directly to Antigravity without copying, pasting, or guessing CSS selectors.

---

## ⚡ How It Works

1. **In-Browser Overlay (`annotator.js`)**:
   - Injects a small floating button (`🎯 Annotate`) or press `Ctrl+Shift+A`.
   - Hovering highlights DOM elements with an outline showing tag, CSS selector, and React/Vue component names.
   - Clicking an element pops up a floating card where you type your instruction.
   - Click **"⚡ Send to Antigravity"** to dispatch the annotation directly to the local bridge.
   - Click **"📋 Copy Prompt"** to copy a markdown-formatted prompt to your clipboard as a fallback.

2. **Local Bridge & MCP Server (`server.py`)**:
   - Written in 100% Python standard library (no `pip install` required).
   - Listens on `http://127.0.0.1:3456` to receive annotations from your browser.
   - Exposes standard Model Context Protocol (MCP) tools (`get_latest_annotation`, `clear_annotations`) so Antigravity can directly pull annotations.

---

## 🚀 Quick Setup (Choose 1 or Both)

### Method A: One-Click Browser Bookmarklet (Recommended - Zero Project Changes)
You can use the annotator on **any** web app (localhost:3000, Vite, Next.js, or production pages) without modifying any project code:

1. Open your browser's Bookmarks bar (`Ctrl+Shift+O` or `Ctrl+Shift+B`).
2. Create a new bookmark named **"🎯 Annotate"**.
3. Set the URL to:
```javascript
javascript:(function(){const s=document.createElement('script');s.src='http://127.0.0.1:3456/annotator.js';document.body.appendChild(s);})();
```
4. Whenever you are testing your web app, click the bookmark (or open `demo.html` to drag and drop it).

---

### Method B: Add to Your Project HTML (Dev Only)
If you prefer the button to be automatically present during development, add this line right before `</body>`:
```html
<script src="http://127.0.0.1:3456/annotator.js"></script>
```

---

## 🔌 Connecting to Antigravity via MCP

To let Antigravity automatically launch and listen to annotations:

Add this to `C:\Users\Mark Vasquez\.gemini\config\mcp_config.json`:

```json
{
  "mcpServers": {
    "codex-annotator": {
      "command": "python",
      "args": [
        "C:\\Users\\Mark Vasquez\\Documents\\Agent Skills\\codex-annotator\\server.py"
      ]
    }
  }
}
```

Whenever Antigravity starts, it will launch the bridge server automatically.

---

## 🧪 Testing Right Now

1. Start the server manually to test:
   ```powershell
   python "C:\Users\Mark Vasquez\Documents\Agent Skills\codex-annotator\server.py" --http-only
   ```
2. Open `http://127.0.0.1:3456/demo.html` in your browser.
3. Click **"🎯 Annotate"** or press `Ctrl+Shift+A`.
4. Click on any button or input, write an instruction, and click **"⚡ Send to Antigravity"**!
