---
type: chat-card
parent_export: '[[Export]]'
order: 851
role: assistant
created: '2025-11-10T21:12:16.879815Z'
tags:
- chat-card
- python
- automation
attachments_count: 0
---

# 🤖 Message 851 - Assistant

**ID:** msg-851

## 💬 Content


**ID:** msg-851

javascript document.addEventListener('keydown', (e) => {
 // === ESC, Ctrl+I, Ctrl+S, Ctrl+K (inchangés) ===
 if (e.key === 'Escape') {
 e.preventDefault();
 if (document.activeElement === editor) {
 editor.blur();
 insertMode = false;
 showNotification('Mode normal activé', 'info');
 }
 }

 if (e.ctrlKey && e.key === 'i' && !insertMode) {
 e.preventDefault();
 editor.focus();
 insertMode = true;
 showNotification('Mode insertion activé', 'info');
 }

 if ((e.ctrlKey || e.metaKey) && e.key === 's') {
 e.preventDefault();
 saveNote();
 }

 if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
 e.preventDefault();
 clearEditor();
 }

 // === TEST MINIMAL - Ctrl+Shift+K → Relay au parent ===
 if (e.ctrlKey && e.shiftKey && e.key === 'K') {
 e.preventDefault();
 console.log('🧪 Ctrl+Shift+K - Relaying to parent');

 window.parent.postMessage({
 type: 'show-shortcuts-test',
 event: {
 key: e.key,
 ctrlKey: e.ctrlKey,
 shiftKey: e.shiftKey
 }
 }, '*');
 }

 // === RELAY TO PARENT - Ctrl+1/2/3, Ctrl+B (inchangés) ===
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

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-850-R850-MINIMAL-SEUL-RACCOURCI-teste-Ctrl]]
- ⬇️ Next: [[Card-852-R852-Javascript-FOCUS-MANAGEMENT-TEST-SHORTCU]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #automation
