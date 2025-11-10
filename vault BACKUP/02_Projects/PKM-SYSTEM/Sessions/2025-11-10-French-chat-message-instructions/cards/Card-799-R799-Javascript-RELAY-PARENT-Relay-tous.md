---
type: chat-card
parent_export: '[[Export]]'
order: 799
role: assistant
created: '2025-11-10T21:12:16.139252Z'
tags:
- chat-card
- python
- code
- automation
attachments_count: 0
---

# 🤖 Message 799 - Assistant

**ID:** msg-799

## 💬 Content


**ID:** msg-799

javascript// === RELAY TO PARENT ===
// Relay tous les raccourcis SAUF ceux gérés localement
const localShortcuts = [
 { key: 'Escape' },
 { ctrl: true, key: 'i' },
 { ctrl: true, key: 's' },
 { ctrl: true, key: 'k' }
];

// Check si c'est un shortcut local
const isLocalShortcut = localShortcuts.some(s => {
 if (s.key === e.key) {
 if (s.ctrl && !e.ctrlKey) return false;
 return true;
 }
 return false;
});

// Si c'est pas un shortcut local, relay au parent
if (!isLocalShortcut && (e.ctrlKey || e.shiftKey || e.altKey || e.metaKey || ['F1', 'F2', 'F3', 'F4'].includes(e.key))) {
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

- ⬆️ Previous: [[Card-798-R798-Javascript-RELAY-PARENT-Ctrl-Ctrl]]
- ⬇️ Next: [[Card-800-R800-MFdans-marche-toujours-parce-sont]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #code
- #automation
