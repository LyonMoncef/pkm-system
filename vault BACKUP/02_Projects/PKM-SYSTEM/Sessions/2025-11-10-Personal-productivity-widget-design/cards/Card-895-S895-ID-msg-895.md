---
type: chat-card
parent_export: '[[Export]]'
order: 895
role: user
created: '2025-11-10T22:56:04.636696Z'
tags:
- chat-card
- python
- automation
attachments_count: 0
---

# 👤 Message 895 - User

**ID:** msg-895

## 💬 Content


**ID:** msg-895

// Juste après le script qui commence
if (window.electronAPI) {
 // Écoute les commandes de navigation
 window.addEventListener('message', (event) => {
 if (event.data.type === 'navigate-to') {
 navigateToPage(event.data.page);
 }
 if (event.data.type === 'toggle-sidebar') {
 toggleSidebar();
 }
 });
}Je veux pas qu'échap ferme la fenetre
Quand je suis en mode saisie, je veux appuyer échap pour sortir du mode de saisie et agie au clavier dans l'app, façon nvim dans l'accès au mode visuel, copie, normal, saisieJ'en suis à Fix 2
Attends, mieux : utilise l'IPC renderer
Dans preload.js, ajoute :

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-894-R894-Juste-après-script-commence-window]]
- ⬇️ Next: [[Card-896-R896-PARFAIT-choses-faire-ESCAPE-MODE]]
- 📊 MOC: [[_MOC_Personal productivity widget design]]

## 🏷️ Topics

- #python
- #automation
