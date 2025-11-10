---
type: chat-card
parent_export: '[[Export]]'
order: 428
role: assistant
created: '2025-11-10T03:56:34.211328Z'
tags:
- chat-card
- python
- code
- automation
attachments_count: 0
---

# 🤖 Message 428 - Assistant

**ID:** msg-428

## 💬 Content


**ID:** msg-428

javascript // === CTRL+W - Quick save + hide window ===
 if (e.ctrlKey && e.key === 'w') {
 e.preventDefault();

 // Force un dernier save en localStorage
 const content = editor.value;
 if (content.trim()) {
 localStorage.setItem('pkm-quick-note', content);
 localStorage.setItem('pkm-quick-note-timestamp', Date.now());
 showNotification('💾 Sauvegardé + caché');
 } else {
 showNotification('📦 Fenêtre cachée');
 }

 // Hide window via IPC
 setTimeout(() => {
 if (window.electronAPI && window.electronAPI.hideWindow) {
 window.electronAPI.hideWindow();
 }
 }, 300); // Délai pour voir la notif
 }

---


## 🔗 Navigation

- ⬆️ Previous: [[427_assistant_msg-427]]
- ⬇️ Next: [[429_assistant_msg-429]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #code
- #automation
