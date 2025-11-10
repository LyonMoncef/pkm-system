---
type: chat-card
parent_export: '[[Export]]'
order: 624
role: assistant
created: '2025-11-10T21:12:13.899373Z'
tags:
- chat-card
- python
- code
- automation
attachments_count: 0
---

# 🤖 Message 624 - Assistant

**ID:** msg-624

## 💬 Content


**ID:** msg-624

javascript // === VIM-LIKE MODES ===
 let insertMode = true;

 document.addEventListener('keydown', (e) => {
 // === ESC - Sort du mode édition ===
 if (e.key === 'Escape') {
 e.preventDefault();

 if (document.activeElement === editor) {
 editor.blur();
 insertMode = false;
 showNotification('Mode normal activé', 'info');
 }
 }

 // === CTRL+I - Entre en mode édition ===
 if (e.ctrlKey && e.key === 'i' && !insertMode) {
 e.preventDefault();
 editor.focus();
 insertMode = true;
 showNotification('Mode insertion activé', 'info');
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

 // === RELAY TO PARENT - Ctrl+1/2/3, Ctrl+B ===
 if (e.ctrlKey && ['1', '2', '3', 'b', 'B'].includes(e.key)) {
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

 console.log('✅ Quick Capture loaded - Dark theme');
 console.log('✅ Keyboard relay active');
 </script>
</body>
</html>

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-623-R623-PARTIE-Modes-Keyboard-Shortcuts-FINALE]]
- ⬇️ Next: [[Card-625-R625-DOCTYPE-html-html-lang-head]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #code
- #automation
