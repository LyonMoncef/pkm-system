---
type: chat-card
parent_export: '[[Export]]'
order: 308
role: user
created: '2025-11-10T03:56:32.828526Z'
tags:
- chat-card
attachments_count: 0
---

# 👤 Message 308 - User

**ID:** msg-308

## 💬 Content


**ID:** msg-308

// Keyboard shortcuts
 document.addEventListener('keydown', (e) => {
 // Sort de l'édition
 if (e.key === 'Escape') {
 e.preventDefault(); // Si on est dans le textarea, on blur (sort du mode édition)
 if (document.activeElement === editor) {
 editor.blur();
 showNotification('Mode normal activé');
 }
 // Sinon on ne fait rien (pas de fermeture)
 } // Ctrl/Cmd + S to save
 if ((e.ctrlKey || e.metaKey) && e.key === 's') {
 e.preventDefault();
 saveNote();
 }
 // Ctrl/Cmd + K to clear
 if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
 e.preventDefault();
 clearEditor();
 }
 }); document.addEventListener('keydown', (e) => {
 // Relay Ctrl+1/2/3, Ctrl+B, Ctrl+Arrows to parent
 if (e.ctrlKey && ['1', '2', '3', 'b', 'B', 'ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight'].includes(e.key)) {
 e.preventDefault(); // Empêche le comportement par défaut window.parent.postMessage({
 type: 'keyboard-event',
 event: {
 key: e.key.toLowerCase(), // Normalise en minuscule
 code: e.code,
 ctrlKey: e.ctrlKey,
 shiftKey: e.shiftKey,
 altKey: e.altKey,
 metaKey: e.metaKey
 }
 }, '*');
 }
 });Voila les events listeners dans le capture.html, c'est ici qu'on gérait le mode insertion ?

---


## 🔗 Navigation

- ⬆️ Previous: [[307_assistant_msg-307]]
- ⬇️ Next: [[309_assistant_msg-309]]
- 📊 MOC: [[_MOC_French chat message instructions]]
