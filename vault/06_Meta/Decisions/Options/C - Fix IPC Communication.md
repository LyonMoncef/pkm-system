---
created: 2025-11-02T21:45:00
updated: 2025-11-02T21:45:00
type: choice-card
tags:
  - choice
  - ipc
  - bug
  - technical
  - urgent
status: deferred
priority: urgent
estimated_time: 2-3h
decision_point: "[[Next Action Choice - Snap 2025-11-02T21-45-00]]"
---

# 🔴 Option C - Fix IPC Communication

## 🎯 Objectif

Réparer la communication IPC entre Main et Renderer pour débloquer raccourcis Layer 1.

## ⏱️ Estimation

**Temps:** 2-3h

## 🔴 Priorité

**URGENT** - Bloque fonctionnalité principale (hotkeys globaux)

## 📋 Actions Détaillées

1. Fixer preload.js (45min)
   - Ajouter handlers IPC
   - contextBridge.exposeInMainWorld
   - ipcRenderer.on events

2. Fixer app.html (45min)
   - Event listeners
   - navigateToPage function
   - Sync currentPage

3. Tests (30min)
   - Test Ctrl+Shift+Space
   - Test Ctrl+Shift+F
   - Test Ctrl+Shift+H

4. Update notes status (15min)
   - Cartes shortcuts → "active"
   - Commit

## ✅ Avantages

- ✅ Débloque feature principale
- ✅ MVP vraiment fonctionnel
- ✅ Valeur utilisateur immédiate

## ❌ Inconvénients

- ❌ Tâche longue (2-3h)
- ❌ Technique, peut bloquer
- ❌ Nécessite focus

## 🌿 Branche Suggérée
```bash
git checkout -b fix/ipc-communication
```

## 🔗 Liens

- [[IPC Communication]] - Note technique
- [[Global Shortcuts System]] - Impacté
- [[TODO]] - Tâche #5
- [[Next Action Choice - Snap 2025-11-02T21-45-00]] - Point décision

---

**Status:** Deferred  
**Chosen:** No  
**Date:** 2025-11-02T21:45:00