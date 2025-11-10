---
type: chat-card
parent_export: '[[Export]]'
order: 691
role: assistant
created: '2025-11-10T21:12:14.756560Z'
tags:
- chat-card
- python
- receipts
- code
- automation
attachments_count: 0
---

# 🤖 Message 691 - Assistant

**ID:** msg-691

## 💬 Content


**ID:** msg-691

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

- ⬆️ Previous: [[Card-690-R690-CRITIQUE-AUTO-REFRESH-Putain-watchdog]]
- ⬇️ Next: [[Card-692-R692-Javascript-Anti-freeze-watchdog-DÉSACTIV]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #receipts
- #code
- #automation
