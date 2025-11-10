---
type: chat-card
parent_export: '[[Export]]'
order: 396
role: assistant
created: '2025-11-10T21:46:11.298597Z'
tags:
- chat-card
- python
- obsidian
- receipts
- code
- automation
attachments_count: 0
---

# 🤖 Message 396 - Assistant

**ID:** msg-396

## 💬 Content


**ID:** msg-396

markdown---
created: 2025-10-24T15:45:00
updated: 2025-11-01T15:00:00
type: feature
status: broken
tags: [feature, shortcut, pkm-system, global, layer-1, toggle-window]
related: [[MOC Raccourcis]], [[Ctrl+Shift+Space - Toggle Capture]], [[Ctrl+Shift+F - Toggle Reference]]
source: \"développement pkm-system phase 1.5\"
---

# Ctrl+Shift+H - Toggle Hub - BROKEN

## Description

Raccourci global pour afficher/masquer la fenêtre Hub depuis n'importe où dans l'OS.

## Spécifications

**Raccourci:** `Ctrl+Shift+H`
**Layer:** Global (Layer 1 - OS Level)
**Contexte:** Fonctionne même quand app cachée
**Comportement attendu:**
- App fermée → Créer fenêtre + naviguer Hub
- App cachée → Afficher + naviguer Hub
- App visible sur Hub → Masquer (toggle off)
- App visible sur autre page → Naviguer Hub

## Implémentation

**Fichier:** main.js (fonction `registerGlobalShortcuts()`)
**Chemin:** `C:\\Users\\idsmf\\Projects\\pkm-system\\electron\\src\\main\\main.js`
**Ligne approximative:** ~55
```javascript
globalShortcut.register('CommandOrControl+Shift+H', () => {
    smartToggle('hub');
});
```

**Dépendances conceptuelles:**
- [[smartToggle Function]] - Logique de toggle
- [[IPC Communication]] - Communication main↔renderer
- [[currentPage Variable]] - Tracking état

## Problème Actuel

❌ **Status: BROKEN**

**Symptômes:**
- Raccourci défini mais ne répond pas
- IPC entre main process et renderer cassé
- Communication postMessage non configurée

**Causes identifiées:**
- preload.js manque handlers IPC appropriés
- Relay mechanism postMessage incomplet
- Event listeners non synchronisés

**Solution en cours:**
Voir [[Backlog]] - Fix IPC communication architecture

## Historique

| Date | Heure | Action | Status |
|------|-------|--------|--------|
| 2025-10-20 | 10:00:00 | Design initial | planned |
| 2025-10-24 | 15:45:00 | Implémentation code | dev |
| 2025-10-24 | 18:30:00 | IPC cassé détecté | broken |
| 2025-10-26 | 12:00:00 | Ajouté au backlog | broken |

## Tests à Effectuer

- [ ] **Test 1:** App fermée → Lance app + affiche Hub
- [ ] **Test 2:** App cachée → Affiche fenêtre sur Hub
- [ ] **Test 3:** Sur page Hub → Cache fenêtre
- [ ] **Test 4:** Sur page Capture → Navigate vers Hub
- [ ] **Test 5:** Sur page Reference → Navigate vers Hub

## Notes Techniques

**Architecture visée:**
```
User presse Ctrl+Shift+H
    ↓
OS détecte (Electron globalShortcut)
    ↓
main.js → smartToggle('hub')
    ↓
IPC send → renderer
    ↓
app.html reçoit event
    ↓
Navigation + show/hide window
```

## Liens

- [[MOC Raccourcis]] - Index principal
- [[Ctrl+Shift+Space - Toggle Capture]] - Raccourci similaire (même pattern)
- [[Ctrl+Shift+F - Toggle Reference]] - Raccourci similaire (même pattern)
- [[smartToggle Function]] - Implémentation technique
- [[Phase 1.5 - Refactor]] - Contexte refactoring
- [[Backlog]] - Tâche de fix

---
**Dernière mise à jour:** 2025-11-01T15:00:00
**Priorité:** 🟡 MEDIUM - Raccourci d'accès au hub central

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-395-R395-Markdown-created-updated-type-feature]]
- ⬇️ Next: [[Card-397-R397-MFje-retrouve-tous-tags-pour]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #python
- #obsidian
- #receipts
- #code
- #automation
