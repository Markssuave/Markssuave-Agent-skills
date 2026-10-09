/**
 * Codex-Style In-Browser Annotator for Antigravity
 * Injects a floating inspector that lets you click UI elements,
 * write a prompt, and instantly dispatch it to Antigravity via local bridge.
 */
(function () {
  if (window.__CODEX_ANNOTATOR_LOADED__) {
    console.log("[Codex Annotator] Already loaded. Press Ctrl+Shift+A to toggle.");
    window.__toggleCodexAnnotator && window.__toggleCodexAnnotator();
    return;
  }
  window.__CODEX_ANNOTATOR_LOADED__ = true;

  const BRIDGE_URL = "http://127.0.0.1:3456/annotate";
  let isActive = false;
  let hoveredEl = null;
  let selectedEl = null;

  // 1. Create Overlay Elements
  const container = document.createElement("div");
  container.id = "codex-annotator-root";
  const shadow = container.attachShadow({ mode: "open" });

  const style = document.createElement("style");
  style.textContent = `
    * { box-sizing: border-box; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
    
    /* Toggle Button */
    .toggle-badge {
      position: fixed;
      bottom: 20px;
      right: 20px;
      z-index: 2147483647;
      background: #1e1e2e;
      color: #cdd6f4;
      border: 1px solid #45475a;
      padding: 10px 16px;
      border-radius: 9999px;
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 4px 14px rgba(0,0,0,0.35);
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .toggle-badge:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(0,0,0,0.45);
      border-color: #89b4fa;
    }
    .toggle-badge.active {
      background: #89b4fa;
      color: #11111b;
      border-color: #b4befe;
    }
    .indicator-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #a6adc8;
    }
    .toggle-badge.active .indicator-dot {
      background: #a6e3a1;
      box-shadow: 0 0 8px #a6e3a1;
    }

    /* Highlight Box */
    .highlight-overlay {
      position: fixed;
      pointer-events: none;
      z-index: 2147483645;
      border: 2px solid #89b4fa;
      background: rgba(137, 180, 250, 0.12);
      border-radius: 4px;
      display: none;
      transition: all 0.08s ease-out;
    }
    .highlight-tag {
      position: absolute;
      top: -24px;
      left: 0;
      background: #89b4fa;
      color: #11111b;
      font-size: 11px;
      font-weight: 700;
      padding: 2px 6px;
      border-radius: 4px 4px 0 0;
      white-space: nowrap;
    }

    /* Modal Card */
    .modal-backdrop {
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(0,0,0,0.4);
      backdrop-filter: blur(2px);
      z-index: 2147483646;
      display: none;
      align-items: center;
      justify-content: center;
    }
    .card {
      background: #181825;
      color: #cdd6f4;
      border: 1px solid #313244;
      border-radius: 12px;
      width: 460px;
      max-width: 90vw;
      box-shadow: 0 20px 40px rgba(0,0,0,0.6);
      padding: 18px;
      animation: popIn 0.15s ease-out;
    }
    @keyframes popIn {
      from { opacity: 0; transform: scale(0.96); }
      to { opacity: 1; transform: scale(1); }
    }
    .card-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
    }
    .card-title {
      font-size: 14px;
      font-weight: 700;
      color: #cdd6f4;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .badge-target {
      background: #313244;
      color: #89b4fa;
      padding: 2px 8px;
      border-radius: 6px;
      font-family: monospace;
      font-size: 12px;
    }
    .meta-box {
      background: #11111b;
      border: 1px solid #313244;
      border-radius: 6px;
      padding: 8px 10px;
      font-family: monospace;
      font-size: 11px;
      color: #a6adc8;
      margin-bottom: 12px;
      max-height: 80px;
      overflow-y: auto;
      word-break: break-all;
    }
    textarea {
      width: 100%;
      height: 90px;
      background: #11111b;
      border: 1px solid #45475a;
      border-radius: 8px;
      padding: 10px;
      color: #cdd6f4;
      font-size: 13px;
      resize: vertical;
      outline: none;
      margin-bottom: 14px;
    }
    textarea:focus {
      border-color: #89b4fa;
    }
    .card-actions {
      display: flex;
      justify-content: flex-end;
      gap: 8px;
    }
    button.btn {
      padding: 8px 14px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      border: none;
      transition: opacity 0.15s;
    }
    button.btn:hover { opacity: 0.88; }
    .btn-cancel { background: #313244; color: #cdd6f4; }
    .btn-copy { background: #45475a; color: #cdd6f4; }
    .btn-send { background: #89b4fa; color: #11111b; font-weight: 700; }
    .status-msg {
      font-size: 11px;
      margin-top: 8px;
      text-align: right;
      color: #a6e3a1;
      display: none;
    }
  `;

  shadow.appendChild(style);

  // Toggle button
  const toggleBtn = document.createElement("button");
  toggleBtn.className = "toggle-badge";
  toggleBtn.innerHTML = `<span class="indicator-dot"></span><span>🎯 Annotate</span> <kbd style="opacity:0.6;font-size:10px;">Ctrl+Shift+A</kbd>`;
  shadow.appendChild(toggleBtn);

  // Highlight Box
  const highlight = document.createElement("div");
  highlight.className = "highlight-overlay";
  highlight.innerHTML = `<div class="highlight-tag"></div>`;
  shadow.appendChild(highlight);
  const tagLabel = highlight.querySelector(".highlight-tag");

  // Modal Backdrop
  const modalBackdrop = document.createElement("div");
  modalBackdrop.className = "modal-backdrop";
  modalBackdrop.innerHTML = `
    <div class="card">
      <div class="card-header">
        <div class="card-title"><span>🎯 Annotate Element</span></div>
        <div class="badge-target" id="modal-tag">button</div>
      </div>
      <div class="meta-box" id="modal-meta">Selector: #submit-btn</div>
      <textarea id="modal-input" placeholder="What should Antigravity change on this element? (e.g. Change color to deep indigo, add subtle drop shadow on hover, fix alignment)..."></textarea>
      <div class="card-actions">
        <button class="btn btn-cancel" id="btn-cancel">Cancel</button>
        <button class="btn btn-copy" id="btn-copy">📋 Copy Prompt</button>
        <button class="btn btn-send" id="btn-send">⚡ Send to Antigravity</button>
      </div>
      <div class="status-msg" id="status-msg"></div>
    </div>
  `;
  shadow.appendChild(modalBackdrop);

  if (document.body) {
    document.body.appendChild(container);
  } else {
    window.addEventListener("DOMContentLoaded", () => {
      document.body.appendChild(container);
    });
  }

  // Helper: Inspect element details
  function getElementDetails(el) {
    let selector = el.tagName.toLowerCase();
    if (el.id) {
      selector += `#${el.id}`;
    } else if (el.className && typeof el.className === "string") {
      const classes = el.className.trim().split(/\s+/).filter(Boolean);
      if (classes.length) selector += `.${classes.slice(0, 3).join(".")}`;
    }

    // Try finding React component name
    let componentName = "Unknown Component";
    try {
      const fiberKey = Object.keys(el).find(k => k.startsWith("__reactFiber$") || k.startsWith("__reactInternalInstance$"));
      if (fiberKey) {
        let curr = el[fiberKey];
        while (curr) {
          if (curr.type && typeof curr.type === "function") {
            componentName = curr.type.displayName || curr.type.name || "Anonymous Component";
            break;
          }
          curr = curr.return;
        }
      }
    } catch (_) {}

    return {
      selector,
      componentName,
      tagName: el.tagName.toLowerCase(),
      text: (el.innerText || el.textContent || "").trim().slice(0, 100),
      outerHTML: el.outerHTML ? el.outerHTML.slice(0, 400) : "",
      url: window.location.href
    };
  }

  // Toggle Mode
  function setMode(active) {
    isActive = active;
    if (isActive) {
      toggleBtn.classList.add("active");
      document.body.style.cursor = "crosshair";
    } else {
      toggleBtn.classList.remove("active");
      highlight.style.display = "none";
      modalBackdrop.style.display = "none";
      document.body.style.cursor = "";
      hoveredEl = null;
      selectedEl = null;
    }
  }

  window.__toggleCodexAnnotator = () => setMode(!isActive);
  toggleBtn.addEventListener("click", () => setMode(!isActive));

  // Shortcut Ctrl+Shift+A
  window.addEventListener("keydown", (e) => {
    if ((e.ctrlKey || e.metaKey) && e.shiftKey && (e.key === "A" || e.key === "a")) {
      e.preventDefault();
      setMode(!isActive);
    }
  });

  // Mouse Over inspection
  window.addEventListener("mousemove", (e) => {
    if (!isActive || modalBackdrop.style.display === "flex") return;
    
    // Ignore clicks on our own shadow root
    if (e.target === container || container.contains(e.target)) return;

    const el = document.elementFromPoint(e.clientX, e.clientY);
    if (!el || el === container || container.contains(el)) return;

    hoveredEl = el;
    const rect = el.getBoundingClientRect();
    highlight.style.display = "block";
    highlight.style.top = `${rect.top}px`;
    highlight.style.left = `${rect.left}px`;
    highlight.style.width = `${rect.width}px`;
    highlight.style.height = `${rect.height}px`;

    const details = getElementDetails(el);
    tagLabel.textContent = details.componentName !== "Unknown Component" 
      ? `<${details.componentName} /> (${details.selector})`
      : details.selector;
  }, { passive: true });

  // Click Element
  window.addEventListener("click", (e) => {
    if (!isActive || modalBackdrop.style.display === "flex") return;
    if (e.target === container || container.contains(e.target)) return;

    e.preventDefault();
    e.stopPropagation();

    const el = hoveredEl || document.elementFromPoint(e.clientX, e.clientY);
    if (!el || el === container || container.contains(el)) return;

    selectedEl = el;
    const details = getElementDetails(selectedEl);

    shadow.querySelector("#modal-tag").textContent = details.componentName !== "Unknown Component" 
      ? `<${details.componentName} />` 
      : details.selector;
      
    shadow.querySelector("#modal-meta").textContent = 
      `Selector: ${details.selector}\nText: "${details.text}"\nComponent: ${details.componentName}`;
    
    const input = shadow.querySelector("#modal-input");
    input.value = "";
    const statusMsg = shadow.querySelector("#status-msg");
    statusMsg.style.display = "none";

    modalBackdrop.style.display = "flex";
    setTimeout(() => input.focus(), 50);
  }, true);

  // Close modal on cancel or backdrop click
  shadow.querySelector("#btn-cancel").addEventListener("click", () => {
    modalBackdrop.style.display = "none";
  });

  modalBackdrop.addEventListener("click", (e) => {
    if (e.target === modalBackdrop) {
      modalBackdrop.style.display = "none";
    }
  });

  const card = shadow.querySelector(".card");
  if (card) {
    card.addEventListener("click", (e) => e.stopPropagation());
  }

  // Close on Escape or submit on Ctrl+Enter
  window.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && modalBackdrop.style.display === "flex") {
      modalBackdrop.style.display = "none";
    }
  });

  shadow.querySelector("#modal-input").addEventListener("keydown", (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key === "Enter") {
      e.preventDefault();
      shadow.querySelector("#btn-send").click();
    }
  });

  // Copy prompt button
  shadow.querySelector("#btn-copy").addEventListener("click", () => {
    if (!selectedEl) return;
    const details = getElementDetails(selectedEl);
    const instruction = shadow.querySelector("#modal-input").value.trim();
    const prompt = 
`🎯 **UI Annotation Request**
- **Page URL**: ${details.url}
- **Component**: \`${details.componentName}\`
- **Selector**: \`${details.selector}\`
- **Text Preview**: "${details.text}"
- **Instruction**: ${instruction || "Please inspect and refactor this element."}
- **HTML Snippet**:
\`\`\`html
${details.outerHTML}
\`\`\``;

    navigator.clipboard.writeText(prompt).then(() => {
      const statusMsg = shadow.querySelector("#status-msg");
      statusMsg.style.color = "#a6e3a1";
      statusMsg.textContent = "✓ Prompt copied to clipboard! Paste into Antigravity.";
      statusMsg.style.display = "block";
      setTimeout(() => { modalBackdrop.style.display = "none"; }, 1200);
    });
  });

  // Send directly to Antigravity Bridge
  shadow.querySelector("#btn-send").addEventListener("click", async () => {
    if (!selectedEl) return;
    const details = getElementDetails(selectedEl);
    const instruction = shadow.querySelector("#modal-input").value.trim();
    const statusMsg = shadow.querySelector("#status-msg");

    const payload = {
      ...details,
      instruction: instruction || "Update this UI element",
      timestamp: new Date().toISOString()
    };

    statusMsg.style.color = "#89b4fa";
    statusMsg.textContent = "Sending to Antigravity bridge...";
    statusMsg.style.display = "block";

    try {
      let res;
      // Try local Vite proxy (/api/annotate) first to comply with strict CSP
      try {
        res = await fetch("/api/annotate", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(payload)
        });
      } catch (_) {
        // Fallback to direct port 3456
        res = await fetch("http://127.0.0.1:3456/annotate", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(payload)
        });
      }

      if (res && res.ok) {
        statusMsg.style.color = "#a6e3a1";
        statusMsg.textContent = "🚀 Sent to Antigravity successfully!";
        setTimeout(() => {
          modalBackdrop.style.display = "none";
          setMode(false);
        }, 1200);
      } else {
        throw new Error("Bridge responded with error");
      }
    } catch (err) {
      statusMsg.style.color = "#f38ba8";
      statusMsg.textContent = "⚠️ Bridge not reachable. Use '📋 Copy Prompt' instead!";
    }
  });

  console.log("%c[Codex Annotator Loaded]%c Click '🎯 Annotate' or press Ctrl+Shift+A", "background: #89b4fa; color: #111; font-weight: bold; padding: 2px 6px; border-radius: 4px;", "");
})();
