---
type: chat-card
parent_export: '[[Export]]'
order: 282
role: assistant
created: '2025-11-10T03:56:32.555221Z'
tags:
- chat-card
- python
- automation
attachments_count: 0
---

# 🤖 Message 282 - Assistant

**ID:** msg-282

## 💬 Content


**ID:** msg-282

javascript// Relay keyboard events to parent
document.addEventListener('keydown', (e) => {
 // Relay Ctrl+1/2/3, Ctrl+B, Ctrl+Arrows to parent
 if (e.ctrlKey && (['1', '2', '3', 'b', 'ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight'].includes(e.key))) {
 window.parent.postMessage({
 type: 'keyboard-event',
 event: {
 key: e.key,
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

- ⬆️ Previous: [[281_assistant_msg-281]]
- ⬇️ Next: [[283_assistant_msg-283]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #automation
