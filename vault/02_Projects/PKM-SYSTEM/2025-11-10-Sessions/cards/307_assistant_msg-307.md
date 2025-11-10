---
type: chat-card
parent_export: '[[Export]]'
order: 307
role: assistant
created: '2025-11-10T03:56:32.819510Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 307 - Assistant

**ID:** msg-307

## 💬 Content


**ID:** msg-307

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
 });Voila les events listeners dans le capture.html, c'est ici qu'on gérait le mode insertion ?Afficher plus

---


## 🔗 Navigation

- ⬆️ Previous: [[306_assistant_msg-306]]
- ⬇️ Next: [[308_user_msg-308]]
- 📊 MOC: [[_MOC_French chat message instructions]]
