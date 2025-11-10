---
type: chat-card
parent_export: '[[Export]]'
order: 886
role: assistant
created: '2025-11-10T22:56:04.556528Z'
tags:
- chat-card
- python
- receipts
- code
- automation
attachments_count: 0
---

# 🤖 Message 886 - Assistant

**ID:** msg-886

## 💬 Content


**ID:** msg-886

javascript// Anti-freeze watchdog
let lastInteraction = Date.now();

document.addEventListener('mousemove', () => {
 lastInteraction = Date.now();
});

document.addEventListener('keydown', () => {
 lastInteraction = Date.now();
});

// Check toutes les 5 secondes
setInterval(() => {
 const timeSinceInteraction = Date.now() - lastInteraction;

 // Si pas d'interaction depuis 30 sec ET app active
 if (timeSinceInteraction > 30000 && document.hasFocus()) {
 console.warn('Possible freeze detected, reloading active iframe');
 const activeIframe = document.querySelector('.view-page.active iframe');
 if (activeIframe) {
 activeIframe.src = activeIframe.src; // Force reload
 }
 }
}, 5000);

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-885-R885-Javascript-toute-script-APRÈS-window]]
- ⬇️ Next: [[Card-887-R887-Javascript-Toggle-sidebar-function-toggl]]
- 📊 MOC: [[_MOC_Personal productivity widget design]]

## 🏷️ Topics

- #python
- #receipts
- #code
- #automation
