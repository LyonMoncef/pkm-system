---
type: chat-card
parent_export: '[[Export]]'
order: 351
role: assistant
created: '2025-11-10T21:46:10.665871Z'
tags:
- chat-card
- python
- obsidian
- code
- git
- automation
attachments_count: 0
---

# 🤖 Message 351 - Assistant

**ID:** msg-351

## 💬 Content


**ID:** msg-351

markdown---
created: 2025-10-20T10:00:00
updated: 2025-11-01T14:50:00
type: code-file
tags: [code, electron, main-process, pkm-system]
path: \"src/main/main.js\"
language: javascript
---

# main.js - Main Process Entry Point

## Description

Point d'entrée du processus principal Electron. Gère :
- Création de la fenêtre principale
- Enregistrement des raccourcis globaux
- Communication IPC avec le renderer
- Système tray

## Accès Rapide

→ [Ouvrir dans VSCode](vscode://file/home/user/pkm-system/src/main/main.js)
→ [Ouvrir dans Nvim](file:///home/user/pkm-system/src/main/main.js)

## Fonctions Principales

| Fonction | Ligne | Description | Utilisée par |
|----------|-------|-------------|--------------|
| `createMainWindow()` | ~25 | Crée la fenêtre | app.on('ready') |
| `registerGlobalShortcuts()` | ~45 | Configure shortcuts OS | app.on('ready') |
| `smartToggle()` | ~78 | Toggle intelligent | Tous les shortcuts |

## Dépendances

**Imports:**
- `electron` (BrowserWindow, globalShortcut, ipcMain)
- `path`

**Fichiers liés:**
- [[preload.js]] - Bridge IPC
- [[app.html]] - Renderer principal

**Features utilisant ce fichier:**
- [[Ctrl+Shift+Space - Toggle Capture]]
- [[Ctrl+Shift+F - Toggle Reference]]
- [[Ctrl+Shift+H - Toggle Hub]]
- [[Ctrl+W - Quick Save & Hide]]

## Architecture
```
main.js
├── Window Management
│   ├── createMainWindow()
│   └── smartToggle()
├── Global Shortcuts
│   └── registerGlobalShortcuts()
├── IPC Handlers
│   ├── current-page-changed
│   └── hide-window
└── Tray System
    └── createTray()
```

## Notes Techniques

- Utilise `single instance lock` pour éviter multiples instances
- Les shortcuts globaux sont enregistrés au `app.on('ready')`
- Variable `currentPage` track la page active pour smart toggle

## Commits Récents

- `2025-10-24T15:45` - Ajout smartToggle() et tracking currentPage
- `2025-10-20T10:00` - Initial implementation

---

**Source de vérité:** Le fichier code lui-même
**Cette note:** Contexte + navigation + liens conceptuels

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-350-R350-Markdown-Implémentation-Fichier-main-lig]]
- ⬇️ Next: [[Card-352-R352-Python-sync-code-notes-import]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #python
- #obsidian
- #code
- #git
- #automation
