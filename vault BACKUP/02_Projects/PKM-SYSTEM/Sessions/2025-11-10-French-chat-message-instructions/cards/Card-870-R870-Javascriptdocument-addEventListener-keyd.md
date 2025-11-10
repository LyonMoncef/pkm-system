---
type: chat-card
parent_export: '[[Export]]'
order: 870
role: assistant
created: '2025-11-10T21:12:17.177433Z'
tags:
- chat-card
- python
- automation
attachments_count: 0
---

# 🤖 Message 870 - Assistant

**ID:** msg-870

## 💬 Content


**ID:** msg-870

javascriptdocument.addEventListener('keydown', (e) => {
 // === ESC ===
 if (e.key === 'Escape') { ... }

 // === CTRL+I ===
 if (e.ctrlKey && e.key === 'i' && !insertMode) { ... }

 // === CTRL+S ===
 if ((e.ctrlKey || e.metaKey) && e.key === 's') { ... }

 // === CTRL+K ===
 if ((e.ctrlKey || e.metaKey) && e.key === 'k') { ... }

 // === TEST - Ctrl+Shift+K ===
 if (e.ctrlKey && e.shiftKey && e.key === 'K') {
 e.preventDefault();
 window.parent.postMessage({
 type: 'show-shortcuts-test',
 event: { key: e.key, ctrlKey: e.ctrlKey, shiftKey: e.shiftKey }
 }, '*');
 }

 // === RELAY TO PARENT - Ctrl+1/2/3, Ctrl+B === ← CETTE SECTION DOIT ÊTRE LÀ !
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

- ⬆️ Previous: [[Card-869-R869-MERDE-CASSÉ-RELAY-EXISTANT-problème]]
- ⬇️ Next: [[Card-871-R871-Javascript-RELAY-PARENT-Ctrl-Ctrl]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #automation
