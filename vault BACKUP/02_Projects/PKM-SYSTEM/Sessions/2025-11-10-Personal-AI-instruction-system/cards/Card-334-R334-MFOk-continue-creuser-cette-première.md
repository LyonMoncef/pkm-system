---
type: chat-card
parent_export: '[[Export]]'
order: 334
role: assistant
created: '2025-11-10T21:46:10.316446Z'
tags:
- chat-card
- python
- obsidian
- receipts
- code
- automation
attachments_count: 0
---

# 🤖 Message 334 - Assistant

**ID:** msg-334

## 💬 Content


**ID:** msg-334

MFOk on continue à creuser cette première note
on oublie pas d'ajouter le statut dans le titre, pour qu'il soit lisible depuis le MOCCtrl+Shift+Space - Toggle Capture - BROKEN---
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
**Raccourci:** Ctrl+Shift+Space
**Layer:** Global (Layer 1 - OS Level)
**Contexte:** Fonctionne même quand app cachée
**Comportement attendu:**
- App fermée → Créer fenêtre + naviguer Capture
- App cachée → Afficher + naviguer Capture
- App visible sur Capture → Masquer (toggle off)
- App visible sur autre page → Naviguer Capture
## Implémentation
**Fichier:** src/main/main.js (ligne ~45)
**Fonction:** registerGlobalShortcuts()
javascript
globalShortcut.register('CommandOrControl+Shift+Space', () => {
 smartToggle('capture');
});

**Dépendances:**
- Fonction smartToggle(targetPage) dans main.js
- Variable currentPage pour tracking état
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

## Liens
- [[MOC Raccourcis]] - Index principal
- [[Ctrl+Shift+F - Toggle Reference]] - Raccourci similaire (même pattern)
- [[Ctrl+Shift+H - Toggle Hub]] - Raccourci similaire (même pattern)
- [[smartToggle Function]] - Implémentation technique
- [[Phase 1.5 - Refactor]] - Contexte refactoring
- [[Backlog]] - Tâche de fix
---
**Dernière mise à jour:** 2025-11-01T14:45:00
**Priorité:** 🔴 HIGH - Raccourci principal du systèmeDans cette note, on fait référence à un fichier main.js où il est implémenté, ça tombe bienon va avoir besoin d'une structure qui épouse la structure du code
Donc la même arborescence que les projet, et une note par fichierC'est quoi le mieux ? Accéder au fichier directement ?
Par exemple main.js
Ou bien de le référencer et ajouter des metadonnées autour ?Peu importe la forme, le but, c'est quand je pense à \"raccourci, je vais pas chercher dans main.js ou raccourcis.js ou que sais-jeJe vais dans la carte obsidian des raccourcis, je navigue cers ctrl space, puis j'accède à l'endroit ou il est implémenté avec en un clin d'oeil son contexte et dépendances, ses tests unitaires (pourquoi pas pour la suite)
Pour que l'ensemble reste à jour ça va demander une gymnastique impossible si je dois mettre à jour les cartes à chaque modifsTu conseilles quoi ?Afficher plus

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-333-R333-MFOk-continue-creuser-cette-première]]
- ⬇️ Next: [[Card-335-R335-MFOk-continue-creuser-cette-première]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #python
- #obsidian
- #receipts
- #code
- #automation
