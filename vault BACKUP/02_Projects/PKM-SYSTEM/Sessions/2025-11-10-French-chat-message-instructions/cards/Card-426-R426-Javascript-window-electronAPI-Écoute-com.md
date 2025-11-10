---
type: chat-card
parent_export: '[[Export]]'
order: 426
role: assistant
created: '2025-11-10T21:12:08.196125Z'
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

- ⬆️ Previous: [[Card-425-R425-Javascript-KEYBOARD-SHORTCUTS-INTERNAL-O]]
- ⬇️ Next: [[Card-427-R427-Javascript-Navigation-listeners-onNaviga]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #automation
