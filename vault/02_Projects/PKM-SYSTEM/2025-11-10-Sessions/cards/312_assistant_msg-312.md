---
type: chat-card
parent_export: '[[Export]]'
order: 312
role: assistant
created: '2025-11-10T03:56:32.868192Z'
tags:
- chat-card
- python
- code
- automation
attachments_count: 0
---

# 🤖 Message 312 - Assistant

**ID:** msg-312

## 💬 Content


**ID:** msg-312

javascript // === VIM-LIKE MODES ===
 let insertMode = true; // Start in insert mode (focus auto au démarrage)

 // Keyboard shortcuts
 document.addEventListener('keydown', (e) => {
 // === ESC - Sort du mode édition ===
 if (e.key === 'Escape') {
 e.preventDefault();

 // Si on est dans le textarea, on blur (sort du mode édition)
 if (document.activeElement === editor) {
 editor.blur();
 insertMode = false;
 showNotification('Mode normal activé');
 }
 }

 // === CTRL+I - Entre en mode édition ===
 if (e.ctrlKey && e.key === 'i' && !insertMode) {
 e.preventDefault();
 editor.focus();
 insertMode = true;
 showNotification('Mode insertion activé');
 }

 // === CTRL+S - Save ===
 if ((e.ctrlKey || e.metaKey) && e.key === 's') {
 e.preventDefault();
 saveNote();
 }

 // === CTRL+K - Clear ===
 if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
 e.preventDefault();
 clearEditor();
 }

 // === RELAY TO PARENT - Ctrl+1/2/3, Ctrl+B, Ctrl+Arrows ===
 if (e.ctrlKey && ['1', '2', '3', 'b', 'B', 'ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight'].includes(e.key)) {
 e.preventDefault();

 window.parent.postMessage({
 type: 'keyboard-event',
 event: {
 key: e.key.toLowerCase(),
 code: e.code,
 ctrlKey: e.ctrlKey,
 shiftKey: e.shiftKey,
 altKey: e.altKey,
 metaKey: e.metaKey
 }
 }, '*');
 }
 });

 // Sync insertMode avec le focus du textarea
 editor.addEventListener('focus', () => {
 insertMode = true;
 });

 editor.addEventListener('blur', () => {
 insertMode = false;
 });

---


## 🔗 Navigation

- ⬆️ Previous: [[311_assistant_msg-311]]
- ⬇️ Next: [[313_assistant_msg-313]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #code
- #automation
