---
type: chat-card
parent_export: '[[Export]]'
order: 1004
role: assistant
created: '2025-11-10T21:12:18.944284Z'
tags:
- chat-card
- python
- obsidian
- receipts
- code
- automation
attachments_count: 0
---

# 🤖 Message 1004 - Assistant

**ID:** msg-1004

## 💬 Content


**ID:** msg-1004

markdown# 🎹 PKM System - Keyboard Shortcuts Reference

> **Documentation Date:** 2025-10-26
> **Version:** Pre-Refactor Baseline
> **Status:** 🚧 In Refactor - Architecture being redesigned

---

## 📊 Current State (Before Refactor)

### ✅ Working Shortcuts

#### **Sidebar & Navigation (Layer 2 - Internal)**
| Shortcut | Action | Status | Location |
|----------|--------|--------|----------|
| `Ctrl+B` | Toggle sidebar collapse | ✅ Working | app.html |
| `Ctrl+1` | Navigate to Capture | ⚠️ Partial | app.html (relay from iframes) |
| `Ctrl+2` | Navigate to Hub | ⚠️ Partial | app.html (relay from iframes) |
| `Ctrl+3` | Navigate to Reference | ⚠️ Partial | app.html (relay from iframes) |

#### **Capture Page (Layer 3 - Local)**
| Shortcut | Action | Status | Location |
|----------|--------|--------|----------|
| `Esc` | Exit insert mode (blur textarea) | ✅ Working | capture.html |
| `Ctrl+I` | Enter insert mode (focus textarea) | ✅ Working | capture.html |
| `Ctrl+S` | Save to vault + clear editor | ✅ Working | capture.html |
| `Ctrl+K` | Clear editor | ✅ Working | capture.html |

#### **Auto-behaviors**
| Behavior | Description | Status |
|----------|-------------|--------|
| Auto-save | Save to localStorage every 2s while typing | ✅ Working |
| Auto-load | Load from localStorage once on startup | ✅ Working |

---

### ❌ Broken Shortcuts

#### **Global Shortcuts (Layer 1 - OS Level)**
| Shortcut | Action | Status | Issue |
|----------|--------|--------|-------|
| `Ctrl+Shift+Space` | Toggle Capture window | ❌ Broken | IPC chain broken |
| `Ctrl+Shift+F` | Toggle Reference window | ❌ Broken | IPC chain broken |
| `Ctrl+Shift+H` | Toggle Hub window | ❌ Broken | IPC chain broken |
| `Ctrl+W` | Quick save + hide | ❌ Broken | IPC chain broken |
| `Ctrl+Shift+W` | Force quit app | ❌ Broken | IPC chain broken |
| `F1` | Show shortcuts help | ❌ Broken | IPC chain broken |
| `Ctrl+/` | Show shortcuts help | ❌ Broken | IPC chain broken |
| `Ctrl+Shift+I` | Show shortcuts help | ❌ Broken | Conflicts with DevTools |

---

### 🧪 Test Shortcuts (To Remove After Refactor)
| Shortcut | Purpose | Status |
|----------|---------|--------|
| `Ctrl+Shift+K` | Test relay mechanism | ✅ Working |
| `Ctrl+Shift+P` | Test local shortcut | ❌ Not working |
| `F12` | Test local shortcut | ❌ Not working |

---

## 🎯 Target Architecture (After Refactor)

### **3-Layer Architecture**
```
┌─────────────────────────────────────────────────────────┐
│ Layer 1: Global OS Shortcuts (main.js)                 │
│ - Work when app is hidden/minimized                    │
│ - Registered via globalShortcut.register()             │
│ - Communication: main.js → IPC → preload → renderer    │
└─────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────┐
│ Layer 2: Internal App Shortcuts (shortcuts.js)         │
│ - Work only when app is focused                        │
│ - Registered via addEventListener('keydown')           │
│ - Direct communication (no IPC)                        │
└─────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────┐
│ Layer 3: Page-Specific Shortcuts (page files)          │
│ - Local to each iframe                                 │
│ - Relayed to parent via postMessage when needed        │
└─────────────────────────────────────────────────────────┘
```

---

### **Layer 1 - Global OS Shortcuts** (main.js)
```javascript
// Toggle windows (work when app hidden)
Ctrl+Shift+Space → smartToggle('capture')  // Show/hide capture window
Ctrl+Shift+F     → smartToggle('reference') // Show/hide reference window
Ctrl+Shift+H     → smartToggle('hub')       // Show/hide hub window

// Window management
Ctrl+W           → quickSaveAndHide()       // Save current content + hide window
Ctrl+Shift+W     → app.quit()               // Quit app completely
```

---

### **Layer 2 - Internal App Shortcuts** (shortcuts.js)
```javascript
// Navigation
Ctrl+1           → navigateToPage('capture')
Ctrl+2           → navigateToPage('hub')
Ctrl+3           → navigateToPage('reference')

// UI Controls
Ctrl+B           → toggleSidebar()          // Show/hide sidebar
Ctrl+/           → showShortcutsHelp()      // Show this help popup

// Relayed from iframes via postMessage
// (handled automatically by relay mechanism)
```

---

### **Layer 3 - Page-Specific Shortcuts**

#### **Capture Page** (capture.html)
```javascript
// Vim-like modes
Esc              → normalMode()             // Exit insert mode (blur textarea)
Ctrl+I           → insertMode()             // Enter insert mode (focus textarea)

// Actions
Ctrl+S           → saveToVault()            // Save to vault + clear editor
Ctrl+K           → clearEditor()            // Clear editor content

// Auto-behaviors
// - Auto-save to localStorage every 2s while typing
// - Auto-load from localStorage once on startup
```

#### **Hub Page** (hub.html)
```javascript
// All navigation handled by Layer 2
// No page-specific shortcuts
```

#### **Reference Page** (reference.html)
```javascript
// Future shortcuts
Ctrl+F           → searchInReference()      // Search in reference content
```

---

## 🔧 Known Issues & Technical Debt

### **Critical Issues**
1. **IPC Chain Broken** - Global shortcuts (Layer 1) don't communicate with renderer
 - `main.js` captures shortcuts ✅
 - `main.js` sends IPC message ✅
 - `preload.js` exposes listener ❓
 - `app.html` receives message ❌
 - `showKeyboardHints()` called ❌

2. **Relay Mechanism Inconsistent** - postMessage relay works for some shortcuts, not others
 - Ctrl+1/2/3/B → Sometimes work, sometimes don't
 - Depends on focus state and timing

3. **Code Scattered** - Shortcuts defined in multiple files
 - app.html has some shortcuts
 - capture.html has some shortcuts
 - hub.html has relay code
 - reference.html has relay code
 - No single source of truth

### **Medium Priority**
4. **No Centralized Documentation** - This file is the first attempt
5. **Test Shortcuts Left Behind** - Debug shortcuts still in code
6. **No Error Handling** - Shortcuts fail silently

---

## 📋 Refactor Checklist

- [ ] Extract all shortcuts to centralized `scripts/shortcuts.js`
- [ ] Fix IPC chain for global shortcuts
- [ ] Implement clean relay mechanism
- [ ] Remove test/debug shortcuts
- [ ] Add error handling
- [ ] Update UI hints to match final shortcuts
- [ ] Test matrix of all shortcuts across all states

---

## 🧪 Testing Matrix (To Complete After Refactor)

| Shortcut | Capture Focused | Hub Focused | Reference Focused | App Unfocused | App Hidden |
|----------|----------------|-------------|-------------------|---------------|------------|
| Ctrl+Shift+Space | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| Ctrl+Shift+F | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| Ctrl+Shift+H | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| Ctrl+W | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| Ctrl+1/2/3 | ⬜ | ⬜ | ⬜ | ⬜ | N/A |
| Ctrl+B | ⬜ | ⬜ | ⬜ | ⬜ | N/A |
| Ctrl+/ | ⬜ | ⬜ | ⬜ | ⬜ | N/A |
| Esc (capture) | ⬜ | N/A | N/A | N/A | N/A |
| Ctrl+I (capture) | ⬜ | N/A | N/A | N/A | N/A |
| Ctrl+S (capture) | ⬜ | N/A | N/A | N/A | N/A |

Legend: ✅ Works | ❌ Broken | ⚠️ Partial | ⬜ Not tested | N/A Not applicable

---

## 📝 Notes

- Last updated: 2025-10-26
- This document will be updated after each refactor phase
- See `REFACTOR.md` for implementation plan
- See `ARCHITECTURE.md` for system design (to be created)

---

**End of SHORTCUTS.md**

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-1003-R1003-Projet-System-Refactor-Plan-Tâche]]
- ⬇️ Next: [[Card-1005-R1005-Bashcd-system-Créer-fichier-SHORTCUTS]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #obsidian
- #receipts
- #code
- #automation
