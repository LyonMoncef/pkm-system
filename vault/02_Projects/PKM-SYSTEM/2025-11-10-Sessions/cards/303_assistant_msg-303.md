---
type: chat-card
parent_export: '[[Export]]'
order: 303
role: assistant
created: '2025-11-10T03:56:32.781382Z'
tags:
- chat-card
- python
- code
- automation
attachments_count: 0
---

# 🤖 Message 303 - Assistant

**ID:** msg-303

## 💬 Content


**ID:** msg-303

javascript // === VIM-LIKE MODES ===
 let insertMode = true; // Start in insert mode

 // Esc to exit insert mode
 document.addEventListener('keydown', (e) => {
 if (e.key === 'Escape' && insertMode) {
 e.preventDefault();
 textarea.blur(); // Remove focus
 insertMode = false;
 showNotification('Normal mode', 'info');
 }

 // Ctrl+I to enter insert mode
 if (e.ctrlKey && e.key === 'i' && !insertMode) {
 e.preventDefault();
 textarea.focus();
 insertMode = true;
 showNotification('Insert mode', 'info');
 }
 });

 // Detect when textarea gains/loses focus
 textarea.addEventListener('focus', () => {
 insertMode = true;
 });

 textarea.addEventListener('blur', () => {
 insertMode = false;
 });

---


## 🔗 Navigation

- ⬆️ Previous: [[302_assistant_msg-302]]
- ⬇️ Next: [[304_assistant_msg-304]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #code
- #automation
