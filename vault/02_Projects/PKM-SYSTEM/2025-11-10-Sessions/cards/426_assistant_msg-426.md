---
type: chat-card
parent_export: '[[Export]]'
order: 426
role: assistant
created: '2025-11-10T03:56:34.191805Z'
tags:
- chat-card
- python
- automation
attachments_count: 0
---

# 🤖 Message 426 - Assistant

**ID:** msg-426

## 💬 Content


**ID:** msg-426

javascript if (window.electronAPI) {
 // Écoute les commandes de navigation depuis main process
 window.electronAPI.onNavigate((page) => {
 navigateToPage(page);
 });

 window.electronAPI.onToggleSidebar(() => {
 toggleSidebar();
 });

 // NEW: Listen for show shortcuts command
 window.electronAPI.onShowShortcuts(() => {
 showKeyboardHints();
 });
 }

---


## 🔗 Navigation

- ⬆️ Previous: [[425_assistant_msg-425]]
- ⬇️ Next: [[427_assistant_msg-427]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #automation
