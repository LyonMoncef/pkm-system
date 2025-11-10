---
type: chat-card
parent_export: '[[Export]]'
order: 798
role: assistant
created: '2025-11-10T21:12:16.119200Z'
tags:
- chat-card
- python
- automation
attachments_count: 0
---

# 🤖 Message 798 - Assistant

**ID:** msg-798

## 💬 Content


**ID:** msg-798

javascript// === RELAY TO PARENT - Ctrl+1/2/3, Ctrl+B, F1 ===
if (
 (e.ctrlKey && ['1', '2', '3', 'b', 'B', '/'].includes(e.key)) ||
 (e.ctrlKey && e.shiftKey && e.key === 'L') ||
 e.key === 'F1'
) {
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

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-797-R797-Javascript-RELAY-PARENT-Ctrl-Ctrl]]
- ⬇️ Next: [[Card-799-R799-Javascript-RELAY-PARENT-Relay-tous]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #automation
