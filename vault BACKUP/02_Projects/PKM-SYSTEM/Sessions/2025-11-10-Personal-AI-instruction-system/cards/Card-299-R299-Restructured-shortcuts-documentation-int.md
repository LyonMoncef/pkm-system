---
type: chat-card
parent_export: '[[Export]]'
order: 299
role: assistant
created: '2025-11-10T21:46:09.766248Z'
tags:
- chat-card
- excel
- python
- obsidian
- receipts
- code
- automation
attachments_count: 0
---

# 🤖 Message 299 - Assistant

**ID:** msg-299

## 💬 Content


**ID:** msg-299

Restructured shortcuts documentation into indexed, individually-tracked feature cards.Ah excellent point ! Il a totalement raison. Cette note doit être un MOC (Map of Content) qui fait référence à des cartes individuelles pour chaque raccourci, pas une documentation statique.
Chaque raccourci = 1 carte avec:

Son propre statut (active, broken, deprecated, planned)
Son historique
Ses métadonnées
Type: feature

La note principale \"raccourcis.md\" devient un index/hub qui liste et lie vers ces cartes.
Je dois:

Transformer raccourcis.md en MOC
Créer un template pour les cartes de features/raccourcis
Suggérer de créer les cartes individuelles pour chaque raccourci mentionné

C'est une excellente façon de structurer ça - beaucoup plus maintenable et exploitable.🎯 EXACT ! MOC + Cartes Atomiques
📋 NOUVEAU TEMPLATE: FeatureNote.md
yaml---
created: {{date:YYYY-MM-DD}}T{{time:HH:mm:ss}}
updated: {{date:YYYY-MM-DD}}T{{time:HH:mm:ss}}
type: feature
status: [planned|dev|active|broken|deprecated]
tags: [feature, pkm-system]
related: []
source: \"\"
---

# [Shortcut/Feature] - {{title}} - [STATUS]

## Description

[À quoi sert ce raccourci/feature]

## Spécifications

**Raccourci:** `Ctrl+X`
**Layer:** [Global|Internal|Page-specific]
**Contexte:** [Où fonctionne-t-il]

## Implémentation

**Fichier:** `src/main/main.js` (ligne XX)
**Fonction:** `functionName()`
```javascript
// Code pertinent
```

## Historique

- `2025-10-24T15:00:00` - Créé (status: planned)
- `2025-10-25T10:30:00` - Implémenté (status: dev)
- `2025-10-26T14:00:00` - IPC cassé (status: broken)

## Tests

- [ ] Test unitaire
- [ ] Test intégration
- [ ] Test utilisateur

## Liens

- [[MOC Raccourcis]] - Index principal
- [[Feature XYZ]] - Dépendance

---
**Dernière mise à jour:** {{date}}

🗂️ REFACTO: raccourcis.md → MOC
markdown---
created: 2025-10-24T15:45:00
updated: 2025-11-01T14:30:00
type: moc
tags: [pkm-system, shortcuts, moc, index]
related: [[Backlog]], [[VisuMethode]], [[Architecture PKM]]
source: \"développement pkm-system phase 1.5\"
---

# 🎹 MOC - Raccourcis PKM System

> **Map of Content** - Index des raccourcis clavier du système

## 📊 Vue d'Ensemble

**Raccourcis actifs:** 8
**En développement:** 3
**Cassés:** 6
**Dépréciés:** 2

---

## 🌍 Layer 1 - Global OS Shortcuts

### Window Management
- [[Ctrl+Shift+Space - Toggle Capture]] - ❌ BROKEN
- [[Ctrl+Shift+F - Toggle Reference]] - ❌ BROKEN
- [[Ctrl+Shift+H - Toggle Hub]] - ❌ BROKEN
- [[Ctrl+W - Quick Save & Hide]] - ❌ BROKEN
- [[Ctrl+Shift+W - Force Quit]] - ❌ BROKEN

---

## 🎨 Layer 2 - Internal App Shortcuts

### Navigation
- [[Ctrl+1 - Navigate to Capture]] - 🟡 PARTIAL
- [[Ctrl+2 - Navigate to Hub]] - 🟡 PARTIAL
- [[Ctrl+3 - Navigate to Reference]] - 🟡 PARTIAL
- [[Ctrl+B - Toggle Sidebar]] - ✅ ACTIVE

### Help
- [[F1 - Show Shortcuts Help]] - ❌ BROKEN
- [[Ctrl+Slash - Show Shortcuts Help]] - ❌ BROKEN

---

## 📄 Layer 3 - Page-Specific Shortcuts

### Capture Page
- [[Esc - Exit Insert Mode]] - ✅ ACTIVE
- [[Ctrl+I - Enter Insert Mode]] - ✅ ACTIVE
- [[Ctrl+S - Save to Vault]] - ✅ ACTIVE
- [[Ctrl+K - Clear Editor]] - ✅ ACTIVE

### Hub Page
- [[Ctrl+N - New Note]] - 🔵 PLANNED

### Reference Page
- [[Ctrl+F - Search in Reference]] - 🔵 PLANNED

---

## 🧪 Test Shortcuts (À Supprimer)

- [[Ctrl+Shift+K - Test Relay]] - 🗑️ DEPRECATED
- [[Ctrl+Shift+P - Test]] - 🗑️ DEPRECATED
- [[F12 - Test]] - 🗑️ DEPRECATED

---

## 📋 Actions

### Priorité 1 - Fix Layer 1
- [ ] Débugger IPC pour global shortcuts
- [ ] Implémenter smartToggle()
- [ ] Tester chaque raccourci global

### Priorité 2 - Compléter Layer 2
- [ ] Finaliser navigation Ctrl+1/2/3
- [ ] Fix shortcuts help

### Priorité 3 - Nettoyer
- [ ] Supprimer test shortcuts
- [ ] Documenter architecture finale

---

## 🔗 Liens Projet

- [[Architecture PKM System]] - Vue d'ensemble
- [[Backlog]] - Tâches en attente
- [[Phase 1.5 - Refactor]] - Contexte actuel

---

## 📊 Dataview - Raccourcis par Status
```dataview
TABLE status, updated
FROM [[]]
WHERE contains(tags, \"feature\") AND contains(tags, \"shortcut\")
SORT status ASC, updated DESC
```

---

**Légende Status:**
- ✅ ACTIVE - Fonctionne parfaitement
- 🟡 PARTIAL - Fonctionne partiellement
- ❌ BROKEN - Ne fonctionne pas
- 🔵 PLANNED - Prévu mais pas implémenté
- 🗑️ DEPRECATED - À supprimer

---
**Dernière mise à jour:** 2025-11-01T14:30:00

🎯 EXEMPLE: Carte Individuelle
Fichier: Ctrl+Shift+Space - Toggle Capture.md
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

✅ PLAN D'ACTION
1. Crée le template FeatureNote.md (je te le donne prêt)
2. Remplace raccourcis.md par le MOC (version ci-dessus)
3. Ensuite (optionnel maintenant, obligatoire plus tard):

Créer les 19 cartes individuelles pour chaque raccourci
Ou on le fait progressivement quand tu touches à un raccourci


🤔 QUESTIONS

On crée toutes les cartes de raccourcis maintenant ou plus tard ?

Maintenant = 30-45 min mais complet
Plus tard = Au fur et à mesure que tu travailles dessus


Où stocker ces cartes ?

02_Projects/PKM-SYSTEM/Features/Shortcuts/ ?
02_Projects/PKM-SYSTEM/Shortcuts/ ?


Le MOC te convient ?

Dis-moi et on passe à l'action ! 🚀Réessayer

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-298-S298-ID-msg-298]]
- ⬇️ Next: [[Card-300-R300-Restructured-shortcuts-documentation-int]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #excel
- #python
- #obsidian
- #receipts
- #code
- #automation
