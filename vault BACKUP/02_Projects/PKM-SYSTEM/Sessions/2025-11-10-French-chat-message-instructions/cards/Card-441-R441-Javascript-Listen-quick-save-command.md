---
type: chat-card
parent_export: '[[Export]]'
order: 441
role: assistant
created: '2025-11-10T21:12:08.445967Z'
tags:
- chat-card
- python
- code
- automation
attachments_count: 0
---

# 🤖 Message 441 - Assistant

**ID:** msg-441

## 💬 Content


**ID:** msg-441

javascript // Listen for quick save command from parent
 window.addEventListener('message', (event) => {
 if (event.data.type === 'quick-save-and-hide') {
 // Force save to localStorage
 const content = editor.value;
 if (content.trim()) {
 localStorage.setItem('pkm-quick-note', content);
 localStorage.setItem('pkm-quick-note-timestamp', Date.now());
 showNotification('💾 Sauvegardé + caché');
 } else {
 showNotification('📦 Fenêtre cachée');
 }
 }
 });

 console.log('✅ Keyboard relay active');

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-440-R440-Javascript-Quick-save-hide-listener]]
- ⬇️ Next: [[Card-442-R442-Devenu-très-moche-ecran-shortcuts]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #code
- #automation
