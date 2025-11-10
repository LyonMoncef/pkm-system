---
type: chat-card
parent_export: '[[Export]]'
order: 288
role: assistant
created: '2025-11-10T21:46:09.592371Z'
tags:
- chat-card
- python
- obsidian
- receipts
- code
- automation
attachments_count: 0
---

# 🤖 Message 288 - Assistant

**ID:** msg-288

## 💬 Content


**ID:** msg-288

✅ TEMPLATES AVEC DATE + HEURE
📋 NOUVEAUX STANDARDS
QuickNote.md
yaml---
created: {{date:YYYY-MM-DD}}T{{time:HH:mm:ss}}
updated: {{date:YYYY-MM-DD}}T{{time:HH:mm:ss}}
type: fleeting
tags: [inbox]
status: to-process
---

# {{title}}

[ton idée ici]

---
À traiter: classer + lier + enrichir
ConceptNote.md
yaml---
created: {{date:YYYY-MM-DD}}T{{time:HH:mm:ss}}
updated: {{date:YYYY-MM-DD}}T{{time:HH:mm:ss}}
type: concept
tags: []
related: []
source: \"\"
---

# {{title}}

## Idée principale

[résumé en 2-3 phrases]

## Développement

[détails]

## Liens

- [[Note reliée]]
ProjectNote.md
yaml---
created: {{date:YYYY-MM-DD}}T{{time:HH:mm:ss}}
updated: {{date:YYYY-MM-DD}}T{{time:HH:mm:ss}}
type: project
status: active
tags: [project]
---

# {{title}}

## État actuel

- [ ] Tâche 1
- [ ] Tâche 2

## Prochaine action

[quoi faire maintenant]

## Contexte

[[Lien vers discussions]]
ChatCardNote.md
yaml---
created: {{date:YYYY-MM-DD}}T{{time:HH:mm:ss}}
updated: {{date:YYYY-MM-DD}}T{{time:HH:mm:ss}}
type: chat-card
tags: []
related: []
source: \"chat-claude-YYYY-MM-DD\"
chat_url: \"\"
chat_timestamp: \"YYYY-MM-DDTHH:mm:ss\"
---

# {{title}}

## Contexte

[Où en était la discussion]

## Contenu

[Le sujet/concept extrait]

## Liens

- [[Note reliée]]

---
**Extrait de:** [Chat du {{date}}]({{chat_url}})

📝 REFACTO: raccourcis.md
Analyse rapide:

Type: concept (documentation des raccourcis)
Créé: ~2025-10-24 (phase refactor)
Tags: pkm-system, shortcuts, electron, keyboard, architecture

Voici la version refactorisée:
markdown---
created: 2025-10-24T15:45:00
updated: 2025-11-01T14:30:00
type: concept
tags: [pkm-system, shortcuts, electron, keyboard, architecture]
related: []
source: \"développement pkm-system phase 1.5\"
---

# 🎹 PKM System - Keyboard Shortcuts Reference

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

---

## 🗂️ Architecture Finale
```
/pkm-system
├── src/
│   ├── main/
│   │   ├── main.js (process principal)
│   │   └── shortcuts.js (global shortcuts centralisés)
│   │
│   ├── preload/
│   │   └── preload.js (IPC bridge)
│   │
│   └── renderer/
│       ├── app.html (wrapper principal)
│       │
│       ├── pages/
│       │   ├── capture.html
│       │   ├── hub.html
│       │   └── reference.html
│       │
│       ├── styles/
│       │   ├── global.css (reset, variables)
│       │   ├── app.css (sidebar, header, status)
│       │   ├── capture.css
│       │   ├── hub.css
│       │   └── reference.css
│       │
│       └── scripts/
│           ├── shortcuts.js (internal shortcuts)
│           ├── navigation.js (page switching)
│           ├── ipc-handlers.js (IPC listeners)
│           └── utils.js (helpers)
│
├── SHORTCUTS.md (documentation)
└── REFACTOR.md (plan + progress)
```

## Liens

- [[Backlog]] - Tâches en cours
- [[VisuMethode]] - Méthodologie de visualisation

---
**Phase:** 1.5 - Refactor Architecture
**Status:** En cours

✅ ACTIONS
1. Remplace le fichier raccourcis.md par cette version
2. Questions pour affiner:

Cette note devrait être liée à quoi ? (j'ai mis [[Backlog]] et [[VisuMethode]] au pif)
La date de création 2025-10-24T15:45:00 te semble correcte ?
Tags OK ou tu veux en ajouter/retirer ?

3. Prochaine note à traiter:

VisuMethode.md ?
Backlog.md ?
Autre ?

Dis-moi si la refacto est OK et on passe à la suivante ! 🚀

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-287-R287-Utilisateur-veut-Date-heure-dans]]
- ⬇️ Next: [[Card-289-R289-Yaml-created-date-YYYY-time]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #python
- #obsidian
- #receipts
- #code
- #automation
