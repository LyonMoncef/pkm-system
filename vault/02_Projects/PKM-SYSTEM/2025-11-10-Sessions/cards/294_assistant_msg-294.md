---
type: chat-card
parent_export: '[[Export]]'
order: 294
role: assistant
created: '2025-11-10T03:56:32.681486Z'
tags:
- chat-card
- python
- automation
attachments_count: 0
---

# 🤖 Message 294 - Assistant

**ID:** msg-294

## 💬 Content


**ID:** msg-294

javascript // === RELAY KEYBOARD EVENTS TO PARENT ===
 document.addEventListener('keydown', (e) => {
 // Relay Ctrl+1/2/3, Ctrl+B, Ctrl+Arrows to parent
 if (e.ctrlKey && ['1', '2', '3', 'b', 'B', 'ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight'].includes(e.key)) {
 e.preventDefault(); // Empêche le comportement par défaut

 window.parent.postMessage({
 type: 'keyboard-event',
 event: {
 key: e.key.toLowerCase(), // Normalise en minuscule
 code: e.code,
 ctrlKey: e.ctrlKey,
 shiftKey: e.shiftKey,
 altKey: e.altKey,
 metaKey: e.metaKey
 }
 }, '*');
 }
 });

 console.log('✅ Keyboard relay active');

---


## 🔗 Navigation

- ⬆️ Previous: [[293_assistant_msg-293]]
- ⬇️ Next: [[295_assistant_msg-295]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #automation
