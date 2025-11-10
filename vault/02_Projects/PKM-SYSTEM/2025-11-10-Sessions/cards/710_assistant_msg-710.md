---
type: chat-card
parent_export: '[[Export]]'
order: 710
role: assistant
created: '2025-11-10T03:56:37.450537Z'
tags:
- chat-card
- python
- automation
attachments_count: 0
---

# 🤖 Message 710 - Assistant

**ID:** msg-710

## 💬 Content


**ID:** msg-710

🔍 DEBUG CTRL+SHIFT+I
Pas de research nécessaire, c'est un bug d'event handling.

🐛 PROBABLE CAUSE
Le shortcut est peut-être capturé par Electron DevTools (Ctrl+Shift+I = Toggle DevTools par défaut).

🔧 FIX - 2 OPTIONS
Option A - Changer le raccourci
Dans main.js, change pour Ctrl+Shift+H (Help) :
javascript // Ctrl+Shift+H - Show keyboard shortcuts (Help)
 globalShortcut.register('CommandOrControl+Shift+H', () => {
 if (mainWindow && mainWindow.isVisible()) {
 mainWindow.webContents.send('show-shortcuts');
 } else if (mainWindow) {
 mainWindow.show();
 setTimeout(() => {
 mainWindow.webContents.send('show-shortcuts');
 }, 300);
 } else {
 createMainWindow();
 setTimeout(() => {
 mainWindow.webContents.send('show-shortcuts');
 }, 800);
 }
 });
MAIS ATTENDS - tu utilises déjà Ctrl+Shift+H pour Hub !

Option B - Utiliser F1 (standard)
Change pour F1 (raccourci help universel) :
javascript // F1 - Show keyboard shortcuts (Help)
 globalShortcut.register('F1', () => {
 if (mainWindow && mainWindow.isVisible()) {
 mainWindow.webContents.send('show-shortcuts');
 } else if (mainWindow) {
 mainWindow.show();
 setTimeout(() => {
 mainWindow.webContents.send('show-shortcuts');
 }, 300);
 } else {
 createMainWindow();
 setTimeout(() => {
 mainWindow.webContents.send('show-shortcuts');
 }, 800);
 }
 });

🎯 RECOMMANDATION
Je suggère F1 car :

Standard dans toutes les apps
Pas de conflit
Facile à retenir

Ou alors Ctrl+/ (comme Discord, Slack, etc.)

💬 TON CALL
Quel raccourci tu préfères ?

A) F1 (standard help)
B) Ctrl+/ (moderne)
C) Autre chose

Dis-moi et je te donne le code ! 💪

---


## 🔗 Navigation

- ⬆️ Previous: [[709_assistant_msg-709]]
- ⬇️ Next: [[711_assistant_msg-711]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #automation
