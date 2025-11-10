---
type: chat-card
parent_export: '[[Export]]'
order: 889
role: assistant
created: '2025-11-10T21:12:17.483194Z'
tags:
- chat-card
- python
- obsidian
- code
- automation
attachments_count: 0
---

# 🤖 Message 889 - Assistant

**ID:** msg-889

## 💬 Content


**ID:** msg-889

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

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-888-R888-Bashcd-system-commit-Shortcuts-architect]]
- ⬇️ Next: [[Card-890-R890-MFon-adopte-plan-fais-toggle]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #obsidian
- #code
- #automation
