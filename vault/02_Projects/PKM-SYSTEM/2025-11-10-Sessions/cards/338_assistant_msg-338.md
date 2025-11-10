---
type: chat-card
parent_export: '[[Export]]'
order: 338
role: assistant
created: '2025-11-10T03:56:33.160088Z'
tags:
- chat-card
- python
- code
- automation
attachments_count: 0
---

# 🤖 Message 338 - Assistant

**ID:** msg-338

## 💬 Content


**ID:** msg-338

javascript // === CTRL+W - Save & Close ===
 if (e.ctrlKey && e.key === 'w') {
 e.preventDefault();

 // Force un dernier save en localStorage
 const content = editor.value;
 if (content.trim()) {
 localStorage.setItem('pkm-quick-note', content);
 localStorage.setItem('pkm-quick-note-timestamp', Date.now());
 showNotification('💾 Note sauvegardée en cache');
 }

 // Demande au main process de cacher/fermer la fenêtre
 setTimeout(() => {
 if (window.electronAPI) {
 // Si on veut juste cacher
 window.parent.postMessage({ type: 'close-window' }, '*');
 }
 }, 300); // Petit délai pour voir la notif
 }

---


## 🔗 Navigation

- ⬆️ Previous: [[337_assistant_msg-337]]
- ⬇️ Next: [[339_assistant_msg-339]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #code
- #automation
