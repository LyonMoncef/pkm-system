---
type: chat-card
parent_export: '[[Export]]'
order: 618
role: assistant
created: '2025-11-10T21:46:14.297263Z'
tags:
- chat-card
- python
- obsidian
- receipts
- code
- automation
attachments_count: 0
---

# 🤖 Message 618 - Assistant

**ID:** msg-618

## 💬 Content


**ID:** msg-618

markdown---
created: 2025-10-24T15:45:00
updated: 2025-11-01T19:20:00
type: feature
status: broken
priority: medium
shortcut: \"Ctrl+Shift+H\"
quicksummary: \"Toggle fenêtre Hub depuis n'importe où\"
tags: [feature, shortcut, pkm-system, global, layer-1, toggle-window]
tech_stack: [electron, ipc]
dependencies: [smartToggle, currentPage, preload.js]
related:
 - \"[[MOC Raccourcis]]\"
 - \"[[Global Shortcuts System]]\"
 - \"[[Ctrl+Shift+Space - Toggle Capture]]\"
 - \"[[Ctrl+Shift+F - Toggle Reference]]\"
 - \"[[smartToggle Function]]\"
 - \"[[Backlog]]\"
source: \"développement pkm-system phase 1.5\"
---

# Ctrl+Shift+H - Toggle Hub - BROKEN

## Description

Raccourci global pour afficher/masquer la fenêtre Hub depuis n'importe où dans l'OS. Le Hub est le centre de navigation du PKM system, permettant d'accéder rapidement aux différentes sections et vues.

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
- Impossible d'accéder rapidement au Hub
- Navigation entre sections ralentie
- Workflow central du système impacté

## Historique

| Date | Heure | Action | Status |
|------|-------|--------|--------|
| 2025-10-20 | 10:00:00 | Design initial | planned |
| 2025-10-24 | 15:45:00 | Implémentation code | dev |
| 2025-10-24 | 18:30:00 | IPC cassé détecté | broken |
| 2025-10-26 | 12:00:00 | Ajouté au backlog | broken |
| 2025-11-01 | 19:20:00 | Documentation enrichie | broken |

## Tests à Effectuer

- [ ] **Test 1:** App fermée → Lance app + affiche Hub
- [ ] **Test 2:** App cachée → Affiche fenêtre sur Hub
- [ ] **Test 3:** Sur page Hub → Cache fenêtre
- [ ] **Test 4:** Sur page Capture → Navigate vers Hub
- [ ] **Test 5:** Sur page Reference → Navigate vers Hub
- [ ] **Test 6:** Vérifier que navigation cards sont interactives

## Notes Techniques

**Architecture visée:**
```
User presse Ctrl+Shift+H
    ↓
OS détecte (Electron globalShortcut)
    ↓
main.js → smartToggle('hub')
    ↓
Check currentPage variable
    ↓
IPC send → renderer
    ↓
app.html reçoit event
    ↓
Navigate to hub + show/hide window
```

**Considérations futures:**
- Dashboard stats sur le Hub ?
- Quick actions depuis Hub ?
- Dernières notes visitées ?

## Liens

- [[MOC Raccourcis]] - Index principal
- [[Global Shortcuts System]] - Vue complète Layer 1
- [[Ctrl+Shift+Space - Toggle Capture]] - Raccourci similaire (même pattern)
- [[Ctrl+Shift+F - Toggle Reference]] - Raccourci similaire (même pattern)
- [[smartToggle Function]] - Implémentation technique
- [[Phase 1.5 - Refactor]] - Contexte refactoring
- [[Backlog]] - Tâche de fix
- [[IPC Communication]] - Architecture communication

---
**Dernière mise à jour:** 2025-11-01T19:20:00
**Priorité:** 🟡 MEDIUM - Raccourci d'accès au hub central
**Prochaine action:** Fix IPC bridge

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-617-R617-Markdown-created-updated-type-feature]]
- ⬇️ Next: [[Card-619-R619-MFOption-Créer-note-conceptuelle-smartTo]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #python
- #obsidian
- #receipts
- #code
- #automation
