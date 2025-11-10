---
type: chat-card
parent_export: '[[Export]]'
order: 834
role: assistant
created: '2025-11-10T03:56:38.804555Z'
tags:
- chat-card
- python
- automation
attachments_count: 0
---

# 🤖 Message 834 - Assistant

**ID:** msg-834

## 💬 Content


**ID:** msg-834

javascript document.addEventListener('keydown', (e) => {
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

 // === TEST RACCOURCIS LOCAUX ===
 // Ctrl+Shift+K - Test 1
 if (e.ctrlKey && e.shiftKey && e.key === 'K') {
 e.preventDefault();
 console.log('🧪 Ctrl+Shift+K caught LOCAL in capture.html');
 showNotification('🧪 TEST: Ctrl+Shift+K works!', 'info');
 }

 // Ctrl+Shift+P - Test 2
 if (e.ctrlKey && e.shiftKey && e.key === 'P') {
 e.preventDefault();
 console.log('🧪 Ctrl+Shift+P caught LOCAL in capture.html');
 showNotification('🧪 TEST: Ctrl+Shift+P works!', 'info');
 }

 // F12 - Test 3
 if (e.key === 'F12') {
 e.preventDefault();
 console.log('🧪 F12 caught LOCAL in capture.html');
 showNotification('🧪 TEST: F12 works!', 'info');
 }

 // === CTRL+S - Save ===
 if ((e.ctrlKey || e.metaKey) && e.key === 's') {
 e.preventDefault();
 saveNote();
 }

 // ... reste du code ...

---


## 🔗 Navigation

- ⬆️ Previous: [[833_assistant_msg-833]]
- ⬇️ Next: [[835_assistant_msg-835]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #automation
