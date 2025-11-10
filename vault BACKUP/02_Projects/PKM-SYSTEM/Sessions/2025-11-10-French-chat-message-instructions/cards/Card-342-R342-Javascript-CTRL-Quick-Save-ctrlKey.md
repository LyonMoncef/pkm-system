---
type: chat-card
parent_export: '[[Export]]'
order: 342
role: assistant
created: '2025-11-10T21:12:07.217830Z'
tags:
- chat-card
- python
- code
- automation
attachments_count: 0
---

# 🤖 Message 342 - Assistant

**ID:** msg-342

## 💬 Content


**ID:** msg-342

javascript // === CTRL+W - Quick Save ===
 if (e.ctrlKey && e.key === 'w') {
 e.preventDefault();

 const content = editor.value;
 if (content.trim()) {
 localStorage.setItem('pkm-quick-note', content);
 localStorage.setItem('pkm-quick-note-timestamp', Date.now());
 showNotification('💾 Sauvegardé en cache', 'success');
 } else {
 showNotification('⚠️ Rien à sauvegarder', 'info');
 }
 }

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-341-R341-Javascript-Hide-window-ipcMain-hide]]
- ⬇️ Next: [[Card-343-R343-MFattends-attends-avait-déjà-géré]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #code
- #automation
