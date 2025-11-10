---
type: chat-card
parent_export: '[[Export]]'
order: 439
role: assistant
created: '2025-11-10T03:56:34.321519Z'
tags:
- chat-card
- python
- code
- automation
attachments_count: 0
---

# 🤖 Message 439 - Assistant

**ID:** msg-439

## 💬 Content


**ID:** msg-439

javascript if (window.electronAPI) {
 // Écoute les commandes de navigation depuis main process
 window.electronAPI.onNavigate((page) => {
 navigateToPage(page);
 });

 window.electronAPI.onToggleSidebar(() => {
 toggleSidebar();
 });

 // Listen for show shortcuts command
 window.electronAPI.onShowShortcuts(() => {
 showKeyboardHints();
 });

 // NEW: Listen for quick save and hide
 window.electronAPI.onQuickSaveAndHide(() => {
 // Forward to active iframe (capture page)
 const activeIframe = document.querySelector('.view-page.active iframe');
 if (activeIframe && activeIframe.contentWindow) {
 activeIframe.contentWindow.postMessage({ type: 'quick-save-and-hide' }, '*');
 }

 // Hide window after short delay
 setTimeout(() => {
 if (window.electronAPI && window.electronAPI.hideWindow) {
 window.electronAPI.hideWindow();
 }
 }, 300);
 });
 }

---


## 🔗 Navigation

- ⬆️ Previous: [[438_assistant_msg-438]]
- ⬇️ Next: [[440_assistant_msg-440]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #code
- #automation
