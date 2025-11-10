---
type: chat-card
parent_export: '[[Export]]'
order: 817
role: assistant
created: '2025-11-10T21:12:16.385431Z'
tags:
- chat-card
- python
- automation
attachments_count: 0
---

# 🤖 Message 817 - Assistant

**ID:** msg-817

## 💬 Content


**ID:** msg-817

javascript// === RELAY TO PARENT ===
if (
 (e.ctrlKey && ['1', '2', '3', 'b', 'B'].includes(e.key)) ||
 (e.ctrlKey && e.shiftKey && ['K', 'P'].includes(e.key)) ||
 ['F12'].includes(e.key)
) {
 e.preventDefault();

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

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-816-R816-Javascript-TEST-RACCOURCIS-VIERGES-Layer]]
- ⬇️ Next: [[Card-818-R818-MFnope-fonctionne-plus-tester-autrement]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #automation
