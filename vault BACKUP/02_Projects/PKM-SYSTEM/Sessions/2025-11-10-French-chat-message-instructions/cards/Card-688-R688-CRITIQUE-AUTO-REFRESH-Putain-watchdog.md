---
type: chat-card
parent_export: '[[Export]]'
order: 688
role: assistant
created: '2025-11-10T21:12:14.723275Z'
tags:
- chat-card
- python
- receipts
- code
- automation
attachments_count: 0
---

# 🤖 Message 688 - Assistant

**ID:** msg-688

## 💬 Content


**ID:** msg-688

🚨 BUG CRITIQUE - AUTO-REFRESH
Putain oui, le watchdog anti-freeze !

🐛 LE PROBLÈME
Dans app.html, il y a un watchdog qui reload les iframes toutes les 30 secondes.
Cherche cette section dans le JavaScript de app.html :
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

🔧 FIX IMMÉDIAT
SUPPRIME COMPLÈTEMENT cette section watchdog dans app.html.
OU si tu veux le garder pour debug :
javascript// Anti-freeze watchdog (DÉSACTIVÉ - causait des refreshs)
/*
let lastInteraction = Date.now();
... toute la section ...
*/

🚀 APPLIQUE + TESTE

Supprime le watchdog dans app.html
Restart
Tape du texte et attends 1-2 minutes
Vérifie que ça ne refresh plus

Confirme-moi quand c'est fixé ! 💪Réessayer

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-687-S687-ID-msg-687]]
- ⬇️ Next: [[Card-689-R689-CRITIQUE-AUTO-REFRESH-Putain-watchdog]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #receipts
- #code
- #automation
