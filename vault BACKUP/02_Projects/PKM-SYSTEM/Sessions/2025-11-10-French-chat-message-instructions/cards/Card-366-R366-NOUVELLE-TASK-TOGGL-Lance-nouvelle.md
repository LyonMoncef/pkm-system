---
type: chat-card
parent_export: '[[Export]]'
order: 366
role: assistant
created: '2025-11-10T21:12:07.482728Z'
tags:
- chat-card
- python
- obsidian
- receipts
- code
- automation
attachments_count: 0
---

# 🤖 Message 366 - Assistant

**ID:** msg-366

## 💬 Content


**ID:** msg-366

⏱️ NOUVELLE TASK TOGGL
Lance ta nouvelle tâche Toggl :
Nom:
PKM System - Refactor Keyboard Shortcuts Architecture
Description:
- Audit all keyboard shortcuts (global vs internal)
- Clean duplicates and conflicts
- Centralize shortcuts documentation
- Implement smart toggle behavior
Projet: PKM System
Tags: refactor, shortcuts, architecture, phase-1.5

🗂️ CARTE #1 - AUDIT SHORTCUTS ACTUELS
📊 ÉTAT DES LIEUX
Global OS Shortcuts (dans main.js)
javascript// registerShortcuts()
Ctrl+Shift+Space → Toggle window + navigate to Capture
Ctrl+Shift+F → Toggle window + navigate to Reference

// setupGlobalKeyboardShortcuts()
Ctrl+1 → Send IPC 'navigate-to' capture
Ctrl+2 → Send IPC 'navigate-to' hub
Ctrl+3 → Send IPC 'navigate-to' reference
Ctrl+B → Send IPC 'toggle-sidebar'
Internal App Shortcuts (dans app.html)
javascript// Reçoit via IPC
navigate-to → Change page
toggle-sidebar → Collapse sidebar

// Reçoit via postMessage (relay des iframes)
Ctrl+1/2/3 → Navigate pages
Ctrl+B → Toggle sidebar
Ctrl+Arrows → (supprimé, était prévu)

// Direct listeners
? → Show keyboard hints (bug, needs Shift)
Capture Page Shortcuts (dans capture.html)
javascriptEsc → Exit insert mode (blur textarea)
Ctrl+I → Enter insert mode (focus textarea)
Ctrl+S → Save note to file
Ctrl+K → Clear editor
Ctrl+W → (pas implémenté, à décider)

// Relay to parent
Ctrl+1/2/3/B → postMessage to app.html
Reference & Hub Pages
javascript// Relay to parent
Ctrl+1/2/3/B → postMessage to app.html

🗂️ CARTE #2 - PROBLÈMES IDENTIFIÉS
🐛 Issues
1. Doublons Global vs Internal

Ctrl+1/2/3 définis 2x : global (main.js) + internal (app.html relay)
Ctrl+B défini 2x : global (main.js) + internal (app.html relay)
Risque: Conflits, double-trigger

2. Toggle Logic Simpliste
javascript// Actuel dans main.js
if (mainWindow.isVisible()) {
 mainWindow.hide();
} else {
 mainWindow.show();
 navigate to page;
}
Problème: Si visible sur Hub et tu fais Ctrl+Shift+Space, ça hide au lieu d'aller sur Capture
3. Shortcuts Manquants

Pas de Ctrl+Shift+H pour Hub
Ctrl+W pas défini (comportement natif browser)
? shortcut bugué (needs Shift detection)

4. Documentation Dispersée

Shortcuts définis dans 5 fichiers différents
Pas de doc centralisée
Keyboard hints dans app.html obsolètes


🗂️ CARTE #3 - ARCHITECTURE PROPOSÉE
🎯 Principe de Séparation
LAYER 1 - Global OS (main.js)
Rôle: Toggle window visibility + set initial page
javascriptCtrl+Shift+Space → Toggle + Capture
Ctrl+Shift+F → Toggle + Reference
Ctrl+Shift+H → Toggle + Hub (NEW)
Logique smart toggle:
javascriptif (!mainWindow) {
 createMainWindow();
 navigate(page);
} else if (!mainWindow.isVisible()) {
 mainWindow.show();
 navigate(page);
} else {
 // App déjà visible
 const currentPage = getCurrentPage(); // À implémenter
 if (currentPage === page) {
 mainWindow.hide(); // Toggle off si déjà sur la page
 } else {
 navigate(page); // Change de page si différent
 }
}
LAYER 2 - Internal Navigation (app.html)
Rôle: Navigation entre pages, UI controls
javascriptCtrl+1 → Navigate Capture
Ctrl+2 → Navigate Hub
Ctrl+3 → Navigate Reference
Ctrl+B → Toggle Sidebar
Shift+? → Show Shortcuts
Supprimé de main.js: Les Ctrl+1/2/3/B ne sont PLUS des global shortcuts, seulement internal
LAYER 3 - Page-Specific (capture/reference/hub.html)
Rôle: Actions spécifiques à chaque page
javascript// capture.html
Esc → Normal mode
Ctrl+I → Insert mode
Ctrl+S → Save to file
Ctrl+K → Clear
Ctrl+W → Save cache + hide (NEW)

// reference.html
Ctrl+F → Search (native)
Ctrl+L → Toggle language

// hub.html
(à définir)
Relay system: Toutes les pages relayent Ctrl+1/2/3/B vers parent

🗂️ CARTE #4 - PLAN D'IMPLÉMENTATION
🔧 Étapes
STEP 1: Cleanup main.js

❌ Supprimer setupGlobalKeyboardShortcuts() (Ctrl+1/2/3/B globaux)
✅ Garder registerShortcuts() (Ctrl+Shift+Space/F)
✅ Ajouter Ctrl+Shift+H pour Hub
✅ Implémenter smart toggle logic

STEP 2: Refactor app.html

✅ Ctrl+1/2/3/B restent internal seulement
✅ Fix shortcut ? → Shift+?
✅ Mettre à jour keyboard hints text
✅ Ajouter tracking de currentPage pour smart toggle

STEP 3: Enhance capture.html

✅ Ajouter Ctrl+W → Save cache + hide window
✅ Garder relay system intact

STEP 4: Documentation

✅ Créer SHORTCUTS.md avec table complète
✅ Ajouter commentaires inline dans chaque fichier
✅ Mettre à jour handoff doc


🗂️ CARTE #5 - SHORTCUTS.md (DRAFT)
markdown# 🎹 PKM SYSTEM - KEYBOARD SHORTCUTS

## 🌍 Global Shortcuts (work when app is closed)

| Shortcut | Action | Layer |
|----------|--------|-------|
| `Ctrl+Shift+Space` | Toggle Capture | OS Global |
| `Ctrl+Shift+F` | Toggle Reference | OS Global |
| `Ctrl+Shift+H` | Toggle Hub | OS Global |

**Smart Toggle Behavior:**
- If app hidden → Show + navigate to page
- If app visible on same page → Hide app
- If app visible on different page → Navigate to page

---

## 🏠 Internal Navigation (app must be open)

| Shortcut | Action | Context |
|----------|--------|---------|
| `Ctrl+1` | Go to Capture | Anywhere in app |
| `Ctrl+2` | Go to Hub | Anywhere in app |
| `Ctrl+3` | Go to Reference | Anywhere in app |
| `Ctrl+B` | Toggle Sidebar | Anywhere in app |
| `Shift+?` | Show Shortcuts | Anywhere in app |

---

## ✍️ Capture Page Shortcuts

| Shortcut | Action | Context |
|----------|--------|---------|
| `Esc` | Exit insert mode | When focused on textarea |
| `Ctrl+I` | Enter insert mode | When not in textarea |
| `Ctrl+S` | Save note to vault | Anytime |
| `Ctrl+K` | Clear editor | Anytime |
| `Ctrl+W` | Quick save + hide | Anytime |

---

## ⚡ Reference Page Shortcuts

| Shortcut | Action | Context |
|----------|--------|---------|
| `Ctrl+F` | Search (native) | Anytime |
| `Ctrl+L` | Toggle language | Anytime |

---

## 🏠 Hub Page Shortcuts

(To be defined)

🚀 PRÊT POUR LE CODE ?
Je te sors le code refactoré pour :

main.js (cleanup + smart toggle)
app.html (fix ? + tracking currentPage)
capture.html (add Ctrl+W)
SHORTCUTS.md (doc complète)

Go ? Balance \"go\" et je balance la sauce ! 💪

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-365-R365-NOUVELLE-TASK-TOGGL-Lance-nouvelle]]
- ⬇️ Next: [[Card-367-R367-System-Refactor-Keyboard-Shortcuts-Archi]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #obsidian
- #receipts
- #code
- #automation
