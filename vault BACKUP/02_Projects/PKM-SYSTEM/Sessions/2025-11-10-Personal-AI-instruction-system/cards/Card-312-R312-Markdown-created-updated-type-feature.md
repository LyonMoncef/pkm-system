---
type: chat-card
parent_export: '[[Export]]'
order: 312
role: assistant
created: '2025-11-10T21:46:09.948543Z'
tags:
- chat-card
- python
- obsidian
- code
- automation
attachments_count: 0
---

# 🤖 Message 312 - Assistant

**ID:** msg-312

## 💬 Content


**ID:** msg-312

markdown---
created: 2025-10-24T15:45:00
updated: 2025-11-01T14:30:00
type: feature
status: broken
tags: [feature, shortcut, pkm-system, global, layer-1]
related: [[MOC Raccourcis]], [[smartToggle Function]]
source: \"développement pkm-system\"
---

# Ctrl+Shift+Space - Toggle Capture - BROKEN

## Description

Raccourci global pour afficher/masquer la fenêtre Capture depuis n'importe où dans l'OS.

## Spécifications

**Raccourci:** `Ctrl+Shift+Space`
**Layer:** Global (Layer 1 - OS Level)
**Contexte:** Fonctionne même quand app cachée
**Comportement:**
- App fermée → Créer fenêtre + naviguer Capture
- App cachée → Afficher + naviguer Capture
- App visible sur Capture → Masquer
- App visible sur autre page → Naviguer Capture

## Implémentation

**Fichier:** `src/main/main.js` (ligne 45)
**Fonction:** `registerGlobalShortcuts()`
```javascript
globalShortcut.register('CommandOrControl+Shift+Space', () => {
    smartToggle('capture');
});
```

**Dépendances:**
- [[smartToggle Function]]
- [[IPC Bridge]]

## Problème Actuel

❌ **IPC cassé** - Le relay entre main.js et renderer ne fonctionne pas correctement.

**Causes identifiées:**
- postMessage non configuré correctement
- preload.js manque handlers IPC

## Historique

- `2025-10-20T10:00:00` - Créé (status: planned)
- `2025-10-24T15:45:00` - Implémenté (status: dev)
- `2025-10-24T18:30:00` - IPC cassé détecté (status: broken)
- `2025-10-26T12:00:00` - Fix en cours ([[Backlog]])

## Tests

- [ ] Test: App fermée → Créer + show Capture
- [ ] Test: App cachée → Show Capture
- [ ] Test: Sur Capture → Hide
- [ ] Test: Sur Hub → Navigate Capture

## Liens

- [[MOC Raccourcis]] - Index principal
- [[Ctrl+Shift+F - Toggle Reference]] - Raccourci similaire
- [[Ctrl+Shift+H - Toggle Hub]] - Raccourci similaire
- [[smartToggle Function]] - Implémentation
- [[Phase 1.5 - Refactor]] - Contexte projet

---
**Dernière mise à jour:** 2025-11-01T14:30:00

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-311-R311-Markdown-created-updated-type-tags]]
- ⬇️ Next: [[Card-313-R313-MFon-commence-raccourci-dans-SYSTEM]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #python
- #obsidian
- #code
- #automation
