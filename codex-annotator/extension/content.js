/**
 * Codex Annotator Content Script
 * Runs in isolated extension world: bypasses page CSP and provides visual element inspector.
 */
(function () {
  if (window.__CODEX_ANNOTATOR_EXTENSION_ACTIVE__) return;
  window.__CODEX_ANNOTATOR_EXTENSION_ACTIVE__ = true;

  let isActive = false;
  let hoveredEl = null;
  let selectedEl = null;

  // 1. Create Shadow DOM Container
  const container = document.createElement("div");
  container.id = "codex-annotator-ext-root";
  const shadow = container.attachShadow({ mode: "open" });

  const style = document.createElement("style");
  style.textContent = `
    * { box-sizing: border-box; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
    
    /* Active indicator banner */
    .active-pill {
      position: fixed;
      top: 16px;
      right: 20px;
      z-index: 2147483647;
      background: #1e1e2e;
      color: #89b4fa;
      border: 1px solid #89b4fa;
      padding: 8px 16px;
      border-radius: 9999px;
      font-size: 13px;
      font-weight: 700;
      display: none;
      align-items: center;
      gap: 10px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.5);
      cursor: pointer;
    }
    .active-pill .dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #a6e3a1;
      box-shadow: 0 0 8px #a6e3a1;
    }
    .active-pill .close {
      opacity: 0.6;
      font-size: 11px;
      margin-left: 6px;
    }

    /* Highlight Box */
    .highlight-overlay {
      position: fixed;
      pointer-events: none;
      z-index: 2147483645;
      border: 2px solid #89b4fa;
      background: rgba(137, 180, 250, 0.15);
      border-radius: 4px;
      display: none;
      transition: all 0.06s ease-out;
    }
    .highlight-tag {
      position: absolute;
      top: -24px;
      left: 0;
      background: #89b4fa;
      color: #11111b;
      font-size: 11px;
      font-weight: 700;
      padding: 2px 7px;
      border-radius: 4px 4px 0 0;
      white-space: nowrap;
    }

    /* Modal Card */
    .modal-backdrop {
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(0,0,0,0.45);
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
      width: 480px;
      max-width: 90vw;
      box-shadow: 0 20px 40px rgba(0,0,0,0.6);
      padding: 20px;
      animation: popIn 0.12s ease-out;
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
      padding: 3px 8px;
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
      height: 95px;
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

  // Active Pill
  const activePill = document.createElement("div");
  activePill.className = "active-pill";
  activePill.innerHTML = `<span class="dot"></span><span>🎯 Annotation Mode Active</span><span class="close">(Esc to exit)</span>`;
  shadow.appendChild(activePill);

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
        <div class="badge-target" id="modal-tag">element</div>
      </div>
      <div class="meta-box" id="modal-meta">Selector: #element</div>
      <textarea id="modal-input" placeholder="What should Antigravity change on this element? (e.g. Change color to indigo, adjust padding, fix alignment)..."></textarea>
      <div class="card-actions">
        <button class="btn btn-cancel" id="btn-cancel">Cancel</button>
        <button class="btn btn-copy" id="btn-copy">📋 Copy Prompt</button>
        <button class="btn btn-send" id="btn-send">⚡ Send to Antigravity</button>
      </div>
      <div class="status-msg" id="status-msg"></div>
    </div>
  `;
  shadow.appendChild(modalBackdrop);

  // Mount into page safely
  function mount() {
    if (document.body) {
      document.body.appendChild(container);
    } else {
      window.addEventListener("DOMContentLoaded", () => document.body.appendChild(container));
    }
  }
  mount();

  // Helper: Inspect element details
  function getElementDetails(el) {
    let selector = el.tagName.toLowerCase();
    if (el.id) {
      selector += `#${el.id}`;
    } else if (el.className && typeof el.className === "string") {
      const classes = el.className.trim().split(/\s+/).filter(Boolean);
      if (classes.length) selector += `.${classes.slice(0, 3).join(".")}`;
    }

    // Detect React Component
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
      activePill.style.display = "flex";
      document.body.style.cursor = "crosshair";
    } else {
      activePill.style.display = "none";
      highlight.style.display = "none";
      modalBackdrop.style.display = "none";
      document.body.style.cursor = "";
      hoveredEl = null;
      selectedEl = null;
    }
  }

  activePill.addEventListener("click", () => setMode(false));

  // Toggle from extension command (Ctrl+Shift+A) or message
  chrome.runtime.onMessage.addListener((msg) => {
    if (msg.action === "toggle") {
      setMode(!isActive);
    }
  });

  // Also support direct in-page keydown
  window.addEventListener("keydown", (e) => {
    if ((e.ctrlKey || e.metaKey) && e.shiftKey && (e.key === "A" || e.key === "a")) {
      e.preventDefault();
      setMode(!isActive);
    } else if (e.key === "Escape" && isActive) {
      setMode(false);
    }
  });

  // Mousemove inspection
  window.addEventListener("mousemove", (e) => {
    if (!isActive || modalBackdrop.style.display === "flex") return;
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

  // Click inspection
  window.addEventListener("click", (e) => {
    if (!isActive || modalBackdrop.style.display === "flex") return;
    if (e.target === container || container.contains(e.target)) return;

    e.preventDefault();
    e.stopPropagation();

    if (!hoveredEl) return;
    selectedEl = hoveredEl;
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

  // Close modal
  shadow.querySelector("#btn-cancel").addEventListener("click", () => {
    modalBackdrop.style.display = "none";
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
      setTimeout(() => { modalBackdrop.style.display = "none"; setMode(false); }, 1200);
    });
  });

  // Send to Antigravity bridge via background worker (100% immune to page CSP)
  shadow.querySelector("#btn-send").addEventListener("click", () => {
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

    chrome.runtime.sendMessage({ action: "send_annotation", payload }, (res) => {
      if (res && res.success) {
        statusMsg.style.color = "#a6e3a1";
        statusMsg.textContent = "🚀 Sent to Antigravity successfully!";
        setTimeout(() => {
          modalBackdrop.style.display = "none";
          setMode(false);
        }, 1200);
      } else {
        statusMsg.style.color = "#f38ba8";
        statusMsg.textContent = "⚠️ Bridge not running on port 3456. Use 'Copy Prompt' instead!";
      }
    });
  });
})();
