---
type: chat-card
parent_export: '[[Export]]'
order: 338
role: assistant
created: '2025-11-10T21:12:07.169861Z'
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

- ⬆️ Previous: [[Card-337-R337-CTRL-AUTO-SAVE-CLOSE-Parfait]]
- ⬇️ Next: [[Card-339-R339-Javascript-Close-window-request-event]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #code
- #automation
