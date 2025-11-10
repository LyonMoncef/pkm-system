---
type: chat-card
parent_export: '[[Export]]'
order: 319
role: assistant
created: '2025-11-10T21:46:10.039985Z'
tags:
- chat-card
- python
- obsidian
- receipts
- code
- automation
attachments_count: 0
---

# 🤖 Message 319 - Assistant

**ID:** msg-319

## 💬 Content


**ID:** msg-319

Orchestrated création du premier raccourci clavier.Parfait, on va créer la première carte de raccourci. Je vais prendre le premier de la liste du MOC : \"Ctrl+Shift+Space - Toggle Capture\" qui a le status BROKEN.
Je vais créer le fichier dans le bon format avec toutes les métadonnées nécessaires.🎯 CRÉATION 1ÈRE CARTE RACCOURCI
📁 Structure à créer
bash02_Projects/PKM-SYSTEM/Shortcuts/
└── Ctrl+Shift+Space - Toggle Capture.md

📝 CONTENU DE LA CARTE
markdown---
created: 2025-10-24T15:45:00
updated: 2025-11-01T14:45:00
type: feature
status: broken
tags: [feature, shortcut, pkm-system, global, layer-1, toggle-window]
related: [[MOC Raccourcis]], [[Ctrl+Shift+F - Toggle Reference]], [[Ctrl+Shift+H - Toggle Hub]]
source: \"développement pkm-system phase 1.5\"
---

# Ctrl+Shift+Space - Toggle Capture - BROKEN

## Description

Raccourci global pour afficher/masquer la fenêtre Capture depuis n'importe où dans l'OS.

## Spécifications

**Raccourci:** `Ctrl+Shift+Space`
**Layer:** Global (Layer 1 - OS Level)
**Contexte:** Fonctionne même quand app cachée
**Comportement attendu:**
- App fermée → Créer fenêtre + naviguer Capture
- App cachée → Afficher + naviguer Capture
- App visible sur Capture → Masquer (toggle off)
- App visible sur autre page → Naviguer Capture

## Implémentation

**Fichier:** `src/main/main.js` (ligne ~45)
**Fonction:** `registerGlobalShortcuts()`
```javascript
globalShortcut.register('CommandOrControl+Shift+Space', () => {
    smartToggle('capture');
});
```

**Dépendances:**
- Fonction `smartToggle(targetPage)` dans main.js
- Variable `currentPage` pour tracking état
- IPC handlers pour communication main ↔ renderer

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

- [ ] **Test 1:** App fermée → Lance app + affiche Capture
- [ ] **Test 2:** App cachée → Affiche fenêtre sur Capture
- [ ] **Test 3:** Sur page Capture → Cache fenêtre
- [ ] **Test 4:** Sur page Hub → Navigate vers Capture
- [ ] **Test 5:** Sur page Reference → Navigate vers Capture

## Notes Techniques

**Architecture visée:**
```
User presse Ctrl+Shift+Space
    ↓
OS détecte (Electron globalShortcut)
    ↓
main.js → smartToggle('capture')
    ↓
IPC send → renderer
    ↓
app.html reçoit event
    ↓
Navigation + show/hide window
```

## Liens

- [[MOC Raccourcis]] - Index principal
- [[Ctrl+Shift+F - Toggle Reference]] - Raccourci similaire (même pattern)
- [[Ctrl+Shift+H - Toggle Hub]] - Raccourci similaire (même pattern)
- [[smartToggle Function]] - Implémentation technique
- [[Phase 1.5 - Refactor]] - Contexte refactoring
- [[Backlog]] - Tâche de fix

---
**Dernière mise à jour:** 2025-11-01T14:45:00
**Priorité:** 🔴 HIGH - Raccourci principal du système

✅ ACTIONS
1. Crée le dossier:
bashmkdir -p 02_Projects/PKM-SYSTEM/Shortcuts
2. Crée le fichier:
bashnvim \"02_Projects/PKM-SYSTEM/Shortcuts/Ctrl+Shift+Space - Toggle Capture.md\"
3. Colle le contenu ci-dessus
4. Ensuite on fait quoi ?

A. On crée les 2 suivants (Ctrl+Shift+F et Ctrl+Shift+H) qui sont similaires
B. On passe à un raccourci différent (genre Ctrl+B - Toggle Sidebar qui fonctionne)
C. On fait le template FeatureNote.md d'abord
D. Autre chose

Ton choix ? 🚀

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-318-R318-Orchestrated-création-premier-raccourci-]]
- ⬇️ Next: [[Card-320-R320-Orchestrated-création-premier-raccourci-]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #python
- #obsidian
- #receipts
- #code
- #automation
