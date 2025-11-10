---
type: chat-card
parent_export: '[[Export]]'
order: 877
role: assistant
created: '2025-11-10T21:12:17.308029Z'
tags:
- chat-card
- python
- obsidian
- receipts
- code
- git
- automation
attachments_count: 0
---

# 🤖 Message 877 - Assistant

**ID:** msg-877

## 💬 Content


**ID:** msg-877

Orchestrated comprehensive refactoring strategy with documentation and architectural cleanup.L'utilisateur a raison, c'est devenu du code spaghetti avec les raccourcis qui ne fonctionnent plus. Il veut:

Commit de sauvegarde
Documenter tous les raccourcis actuels
Refactor complet avec architecture propre
CSS séparé
Raccourcis centralisés

C'est le bon moment pour faire un vrai refactor propre. Je vais:

Créer un commit
Créer un fichier SHORTCUTS.md avec tous les raccourcis documentés
Proposer une architecture propre pour le refactor
Lister les autres refactors nécessaires
🎯 COMMIT + REFACTOR PROPRE
T'as raison, on arrête le bricolage. On refactor CLEAN ! 💪

📦 ÉTAPE 1 - COMMIT DE SAUVEGARDE
bashcd ~/pkm-system
git add .
git commit -m \"WIP: Shortcuts architecture debug - before major refactor

Features working:
- Sidebar toggle (Ctrl+B) ✅
- Page navigation (Ctrl+1/2/3) partially working
- Capture auto-save/load ✅
- Vim modes (Esc/Ctrl+I) ✅
- Dark theme coherent ✅

Issues:
- Global shortcuts IPC chain broken
- Shortcuts relay inconsistent between pages
- Code spaghetti with shortcuts scattered everywhere

Next: Clean refactor with modular architecture\"

git push origin main

📝 ÉTAPE 2 - DOCUMENTATION SHORTCUTS
Je vais créer SHORTCUTS.md pour référence :
markdown# 🎹 PKM System - Keyboard Shortcuts Reference

## 📊 Current State (Before Refactor)

### ✅ Working Shortcuts

**Sidebar & Navigation (Layer 2 - Internal):**
- `Ctrl+B` - Toggle sidebar collapse
- `Ctrl+1` - Navigate to Capture (partial)
- `Ctrl+2` - Navigate to Hub (partial)
- `Ctrl+3` - Navigate to Reference (partial)

**Capture Page (Local):**
- `Esc` - Exit insert mode (blur textarea)
- `Ctrl+I` - Enter insert mode (focus textarea)
- `Ctrl+S` - Save to vault + clear editor
- `Ctrl+K` - Clear editor

**Auto-behaviors:**
- Auto-save to cache every 2s while typing
- Load from cache once on startup

### ❌ Broken Shortcuts

**Global Shortcuts (Layer 1 - OS Level):**
- `Ctrl+Shift+Space` - Toggle Capture window (defined but IPC broken)
- `Ctrl+Shift+F` - Toggle Reference window (defined but IPC broken)
- `Ctrl+Shift+H` - Toggle Hub window (defined but IPC broken)
- `Ctrl+W` - Quick save + hide (defined but IPC broken)
- `Ctrl+Shift+W` - Force quit (defined but IPC broken)
- `F1` / `Ctrl+/` / `Ctrl+Shift+I` - Show shortcuts help (IPC broken)

### 🧪 Test Shortcuts (To Remove)
- `Ctrl+Shift+K` - Test relay (working)
- `Ctrl+Shift+P` - Test (not working)
- `F12` - Test (not working)

---

## 🎯 Target Architecture (After Refactor)

### Layer 1 - Global OS Shortcuts (main.js)
```javascript
// Toggle windows (work when app hidden)
Ctrl+Shift+Space → smartToggle('capture')
Ctrl+Shift+F → smartToggle('reference')
Ctrl+Shift+H → smartToggle('hub')

// Window management
Ctrl+W → quickSaveAndHide()
Ctrl+Shift+W → app.quit()
```

### Layer 2 - Internal App Shortcuts (shortcuts.js)
```javascript
// Navigation
Ctrl+1/2/3 → navigateToPage()
Ctrl+B → toggleSidebar()
Ctrl+/ → showShortcutsHelp()

// Relayed from iframes via postMessage
```

### Layer 3 - Page-Specific Shortcuts
```javascript
// Capture page
Esc → normalMode()
Ctrl+I → insertMode()
Ctrl+S → saveToVault()
Ctrl+K → clearEditor()

// Hub page
(none - all navigation via Layer 2)

// Reference page
Ctrl+F → searchInReference()
```

---

## 📋 Implementation Checklist

- [ ] Extract CSS to separate files
- [ ] Create shortcuts.js module
- [ ] Centralize IPC handlers in preload.js
- [ ] Fix relay mechanism (postMessage)
- [ ] Test each shortcut individually
- [ ] Remove test/debug shortcuts
- [ ] Update UI hints with final shortcuts
```

---

## 🏗️ ÉTAPE 3 - NOUVELLE ARCHITECTURE
```
/pkm-system
├── src/
│ ├── main/
│ │ ├── main.js (process principal)
│ │ └── shortcuts.js (global shortcuts centralisés)
│ │
│ ├── preload/
│ │ └── preload.js (IPC bridge)
│ │
│ └── renderer/
│ ├── app.html (wrapper principal)
│ │
│ ├── pages/
│ │ ├── capture.html
│ │ ├── hub.html
│ │ └── reference.html
│ │
│ ├── styles/
│ │ ├── global.css (reset, variables)
│ │ ├── app.css (sidebar, header, status)
│ │ ├── capture.css
│ │ ├── hub.css
│ │ └── reference.css
│ │
│ └── scripts/
│ ├── shortcuts.js (internal shortcuts)
│ ├── navigation.js (page switching)
│ ├── ipc-handlers.js (IPC listeners)
│ └── utils.js (helpers)
│
├── SHORTCUTS.md (documentation)
└── REFACTOR.md (plan + progress)

🔧 AUTRES REFACTORS NÉCESSAIRES
High Priority:

✅ Séparer CSS dans /styles
✅ Centraliser shortcuts dans /scripts/shortcuts.js
✅ Fix IPC chain proprement
✅ Supprimer code mort (tests, watchdog, etc.)

Medium Priority:

Modulariser navigation (page switching logic)
Créer utils.js (notifications, localStorage helpers)
Settings menu (vault location config)
Error handling proper (try/catch partout)

Low Priority:

Tests (au moins manuels avec checklist)
Documentation (README, ARCHITECTURE.md)
Build process (webpack/vite optionnel)


🚀 PLAN DE REFACTOR
Phase 1 - Commit + Doc (15min)

✅ Commit sauvegarde
✅ Créer SHORTCUTS.md
✅ Créer REFACTOR.md

Phase 2 - Extraction (1h)

Créer structure /styles et /scripts
Extraire CSS de app.html → app.css
Extraire CSS des pages → capture.css, etc.
Créer shortcuts.js avec tous les raccourcis
Commit: \"refactor: extract CSS and scripts to modules\"

Phase 3 - Fix Shortcuts (1h)

Réimplémenter shortcuts Layer par Layer
Tester chaque shortcut individuellement
Fix relay mechanism proprement
Commit: \"fix: reimplemented shortcuts with clean architecture\"

Phase 4 - Polish (30min)

Supprimer code mort
Update UI hints
Tests manuels complets
Commit: \"polish: cleanup and final tests\"


💬 TON CALL
On fait :

Le commit maintenant
Je crée SHORTCUTS.md
On lance Phase 2 (extraction CSS/JS) ?

Ou tu veux autre chose en priorité ?
Dis-moi et on y va ! 🔥Réessayer

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-876-S876-ID-msg-876]]
- ⬇️ Next: [[Card-878-R878-Orchestrated-comprehensive-refactoring-s]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #obsidian
- #receipts
- #code
- #git
- #automation
