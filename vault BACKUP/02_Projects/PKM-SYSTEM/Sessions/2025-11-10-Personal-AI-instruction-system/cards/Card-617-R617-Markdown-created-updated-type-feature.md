---
type: chat-card
parent_export: '[[Export]]'
order: 617
role: assistant
created: '2025-11-10T21:46:14.286327Z'
tags:
- chat-card
- python
- obsidian
- receipts
- code
- automation
attachments_count: 0
---

# 🤖 Message 617 - Assistant

**ID:** msg-617

## 💬 Content


**ID:** msg-617

markdown---
created: 2025-10-24T15:45:00
updated: 2025-11-01T19:20:00
type: feature
status: broken
priority: medium
shortcut: \"Ctrl+Shift+F\"
quicksummary: \"Toggle fenêtre Reference depuis n'importe où\"
tags: [feature, shortcut, pkm-system, global, layer-1, toggle-window]
tech_stack: [electron, ipc]
dependencies: [smartToggle, currentPage, preload.js]
related:
 - \"[[MOC Raccourcis]]\"
 - \"[[Global Shortcuts System]]\"
 - \"[[Ctrl+Shift+Space - Toggle Capture]]\"
 - \"[[Ctrl+Shift+H - Toggle Hub]]\"
 - \"[[smartToggle Function]]\"
 - \"[[Backlog]]\"
source: \"développement pkm-system phase 1.5\"
---

# Ctrl+Shift+F - Toggle Reference - BROKEN

## Description

Raccourci global pour afficher/masquer la fenêtre Reference depuis n'importe où dans l'OS. Permet un accès rapide à la page de référence pour consulter des notes ou rechercher de l'information.

## Spécifications

**Raccourci:** `Ctrl+Shift+F`
**Layer:** Global (Layer 1 - OS Level)
**Contexte:** Fonctionne même quand app cachée
**Comportement attendu:**
- App fermée → Créer fenêtre + naviguer Reference
- App cachée → Afficher + naviguer Reference
- App visible sur Reference → Masquer (toggle off)
- App visible sur autre page → Naviguer Reference

## Implémentation

**Fichier:** main.js (fonction `registerGlobalShortcuts()`)
**Chemin:** `C:\\Users\\idsmf\\Projects\\pkm-system\\electron\\src\\main\\main.js`
**Ligne approximative:** ~50
```javascript
globalShortcut.register('CommandOrControl+Shift+F', () => {
    smartToggle('reference');
});
```

**Dépendances conceptuelles:**
- [[smartToggle Function]] - Logique de toggle window
- [[IPC Communication]] - Communication main↔renderer
- [[currentPage Variable]] - Tracking état page active

## Problème Actuel

❌ **Status: BROKEN**

**Symptômes:**
- Raccourci défini mais ne répond pas
- IPC entre main process et renderer cassé
- Communication postMessage non configurée
- Aucune réaction au keypress global

**Causes identifiées:**
- preload.js manque handlers IPC appropriés
- Relay mechanism postMessage incomplet
- Event listeners non synchronisés
- Bridge IPC non fonctionnel

**Solution en cours:**
Voir [[Backlog]] - Fix IPC communication architecture

**Impact utilisateur:**
- Impossible d'accéder rapidement à Reference
- Workflow de recherche ralenti
- Navigation manuelle nécessaire

## Historique

| Date | Heure | Action | Status |
|------|-------|--------|--------|
| 2025-10-20 | 10:00:00 | Design initial | planned |
| 2025-10-24 | 15:45:00 | Implémentation code | dev |
| 2025-10-24 | 18:30:00 | IPC cassé détecté | broken |
| 2025-10-26 | 12:00:00 | Ajouté au backlog | broken |
| 2025-11-01 | 19:20:00 | Documentation enrichie | broken |

## Tests à Effectuer

- [ ] **Test 1:** App fermée → Lance app + affiche Reference
- [ ] **Test 2:** App cachée → Affiche fenêtre sur Reference
- [ ] **Test 3:** Sur page Reference → Cache fenêtre
- [ ] **Test 4:** Sur page Capture → Navigate vers Reference
- [ ] **Test 5:** Sur page Hub → Navigate vers Reference
- [ ] **Test 6:** Vérifier focus sur search bar si implémenté

## Notes Techniques

**Architecture visée:**
```
User presse Ctrl+Shift+F
    ↓
OS détecte (Electron globalShortcut)
    ↓
main.js → smartToggle('reference')
    ↓
Check currentPage variable
    ↓
IPC send → renderer
    ↓
app.html reçoit event
    ↓
Navigate to reference + show/hide window
```

**Considérations futures:**
- Auto-focus sur search bar au toggle ?
- Mémoriser dernière position dans Reference ?
- Animation de transition ?

## Liens

- [[MOC Raccourcis]] - Index principal
- [[Global Shortcuts System]] - Vue complète Layer 1
- [[Ctrl+Shift+Space - Toggle Capture]] - Raccourci similaire (même pattern)
- [[Ctrl+Shift+H - Toggle Hub]] - Raccourci similaire (même pattern)
- [[smartToggle Function]] - Implémentation technique
- [[Phase 1.5 - Refactor]] - Contexte refactoring
- [[Backlog]] - Tâche de fix
- [[IPC Communication]] - Architecture communication

---
**Dernière mise à jour:** 2025-11-01T19:20:00
**Priorité:** 🟡 MEDIUM - Raccourci d'accès rapide à la référence
**Prochaine action:** Fix IPC bridge

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-616-R616-CARTES-CTRL-SHIFT-CTRL-SHIFT]]
- ⬇️ Next: [[Card-618-R618-Markdown-created-updated-type-feature]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #python
- #obsidian
- #receipts
- #code
- #automation
