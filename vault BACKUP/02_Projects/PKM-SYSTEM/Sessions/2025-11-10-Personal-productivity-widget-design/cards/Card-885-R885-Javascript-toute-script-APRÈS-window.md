---
type: chat-card
parent_export: '[[Export]]'
order: 885
role: assistant
created: '2025-11-10T22:56:04.547446Z'
tags:
- chat-card
- python
- code
- automation
attachments_count: 0
---

# 🤖 Message 885 - Assistant

**ID:** msg-885

## 💬 Content


**ID:** msg-885

javascript// À la toute fin du script, APRÈS le window.addEventListener('load')

// Force focus dans textarea au chargement
window.addEventListener('load', () => {
 const autosaved = localStorage.getItem('pkm-autosave');
 if (autosaved) {
 editor.value = autosaved;
 updatePreview();
 lastSaved.textContent = 'Restored from autosave';
 }

 // AJOUTE ÇA :
 // Focus automatique dans l'éditeur
 setTimeout(() => {
 editor.focus();
 }, 100);
});

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-884-R884-Javascript-Setup-listeners-window-electr]]
- ⬇️ Next: [[Card-886-R886-Javascript-Anti-freeze-watchdog-lastInte]]
- 📊 MOC: [[_MOC_Personal productivity widget design]]

## 🏷️ Topics

- #python
- #code
- #automation
