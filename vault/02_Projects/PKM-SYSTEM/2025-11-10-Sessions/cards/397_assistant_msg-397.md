---
type: chat-card
parent_export: '[[Export]]'
order: 397
role: assistant
created: '2025-11-10T03:56:33.788238Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 397 - Assistant

**ID:** msg-397

## 💬 Content


**ID:** msg-397

yaml---
title: \"Refactor - Step 1: Cleanup main.js Global Shortcuts\"
date: 2025-10-24
timestamp: 2025-10-24T15:45:00Z
type: refactor-card
status: completed
project: pkm-system
phase: phase-1.5
tags: [shortcuts, main-process, global-shortcuts, smart-toggle]
related: [keyboard-shortcuts-refactor, phase-1.5-ninja-mode]
author: claude-moncef-collab
---

## ✅ Changements Appliqués

### Supprimé
- `setupGlobalKeyboardShortcuts()` → Ctrl+1/2/3/B ne sont plus globaux
- Doublons shortcuts entre global et internal

### Ajouté
- Variable `currentPage` pour tracking état
- Fonction `smartToggle(targetPage)` avec logique intelligente
- `Ctrl+Shift+H` pour toggle Hub
- IPC handlers: `current-page-changed`, `hide-window`

### Modifié
- `registerShortcuts()` → `registerGlobalShortcuts()`
- Tous les global shortcuts utilisent `smartToggle()`
- Tray menu utilise `smartToggle()`

## 🎯 Smart Toggle Logic

**Comportement:**
- App fermée → Create + navigate
- App cachée → Show + navigate
- App visible sur même page → Hide (toggle off)
- App visible sur autre page → Navigate

## ✅ Tests Validés
- Ctrl+Shift+Space/F/H fonctionnent
- Smart toggle marche correctement
- Tray menu fonctionne avec smart toggle

## 📊 Status
✅ COMPLETED - 2025-10-24T15:45:00Z

---


## 🔗 Navigation

- ⬆️ Previous: [[396_assistant_msg-396]]
- ⬇️ Next: [[398_assistant_msg-398]]
- 📊 MOC: [[_MOC_French chat message instructions]]
