---
type: chat-card
parent_export: '[[Export]]'
order: 1550
role: assistant
created: '2025-11-10T21:46:25.888949Z'
tags:
- chat-card
- python
- obsidian
- code
- automation
attachments_count: 0
---

# 🤖 Message 1550 - Assistant

**ID:** msg-1550

## 💬 Content


**ID:** msg-1550

markdown---
created: 2025-10-18T00:00:00
updated: 2025-11-02T12:10:00
type: backlog-item
category: bug
priority: urgent
status: todo
tags: [bug, ipc, electron, hotkeys, layer-1]
estimated_time: \"2-3h\"
estimated_time_minutes: 150
blocked_by: []
related:
 - \"[[IPC Communication]]\"
 - \"[[Global Shortcuts System]]\"
 - \"[[TODO]]\"
---

# Fix IPC Hotkeys - Layer 1

## 🎯 Description

Les raccourcis Layer 1 (Ctrl+Shift+Space/F/H) ne fonctionnent pas - problème IPC entre Main et Renderer.

## 📋 Contexte

**Problème:**
Communication IPC cassée entre process Main et Renderer.

**Symptômes:**
- ❌ Ctrl+Shift+Space ne toggle pas Capture
- ❌ Ctrl+Shift+F ne toggle pas Reference
- ❌ Ctrl+Shift+H ne toggle pas Hub
- ✅ Hotkeys enregistrés dans Main OK
- ❌ Events pas reçus dans Renderer

**Use Case:**
MVP non fonctionnel sans hotkeys globaux.

**Inspiration:**
Phase 1.5 - Feature principale cassée

## 🔧 Solutions Possibles

### Fix preload.js + app.html

**Fichiers à modifier:**
- `electron/preload.js` - Ajouter handlers IPC
- `electron/app.html` - Ajouter listeners

**Code preload.js:**
```javascript
contextBridge.exposeInMainWorld('electron', {
  onNavigate: (callback) => {
    ipcRenderer.on('navigate-to', callback);
  }
});
```

**Code app.html:**
```javascript
window.electron.onNavigate((event, page) => {
  navigateToPage(page);
});
```

## 📊 Critères Acceptation

- [ ] Ctrl+Shift+Space fonctionne
- [ ] Ctrl+Shift+F fonctionne
- [ ] Ctrl+Shift+H fonctionne
- [ ] Tests sur chaque window
- [ ] Status cartes updated (BROKEN → ACTIVE)

## 🔗 Ressources

**Notes techniques:**
- [[IPC Communication]]
- [[Global Shortcuts System]]
- [[Ctrl+Shift+Space - Toggle Capture]]

**Electron Docs:**
- [IPC Tutorial](https://www.electronjs.org/docs/latest/tutorial/ipc)

---

## 📝 Notes

**Priorité URGENTE** - Bloque feature principale MVP.

---

**Créé:** 2025-10-18
**Session:** Phase 1.5 - Post migration Electron

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-1549-R1549-Bashnvim-vault-SYSTEM-BackLog-Items]]
- ⬇️ Next: [[Card-1551-R1551-Bashcd-system-Tout-ajouter-vault]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #python
- #obsidian
- #code
- #automation
