/**
 * Codex Annotator Background Service Worker
 * Handles extension shortcuts, toolbar clicks, and proxying annotation requests to localhost.
 */

// Toggle annotator in the current active tab
async function toggleActiveTab(tab) {
  if (!tab || !tab.id) return;
  try {
    await chrome.tabs.sendMessage(tab.id, { action: "toggle" });
  } catch (err) {
    // If content script wasn't injected yet, inject it on-demand
    try {
      await chrome.scripting.executeScript({
        target: { tabId: tab.id },
        files: ["content.js"]
      });
      // Send toggle message after injection
      setTimeout(() => {
        chrome.tabs.sendMessage(tab.id, { action: "toggle" }).catch(() => {});
      }, 100);
    } catch (_) {}
  }
}

// Global shortcut listener (Ctrl+Shift+A)
chrome.commands.onCommand.addListener(async (command) => {
  if (command === "toggle-annotator") {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    toggleActiveTab(tab);
  }
});

// Extension icon click listener
chrome.action.onClicked.addListener((tab) => {
  toggleActiveTab(tab);
});

// Proxy annotation POST requests to avoid page-level CSP or Private Network Access blocks
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "send_annotation") {
    fetch("http://127.0.0.1:3456/annotate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(request.payload)
    })
      .then(async (res) => {
        if (res.ok) {
          sendResponse({ success: true });
        } else {
          const errText = await res.text();
          sendResponse({ success: false, error: errText });
        }
      })
      .catch((err) => {
        sendResponse({ success: false, error: err.message });
      });
    return true; // Keep message channel open for async response
  }
});
