---
type: chat-card
parent_export: '[[Export]]'
order: 532
role: assistant
created: '2025-11-10T21:46:13.258881Z'
tags:
- chat-card
- obsidian
- receipts
attachments_count: 0
---

# 🤖 Message 532 - Assistant

**ID:** msg-532

## 💬 Content


**ID:** msg-532

---
created: 2025-10-24T15:45:00
updated: 2025-11-01T14:30:00
type: moc
tags:
 - pkm-system
 - shortcuts
 - moc
 - index
related:
 - \"[[Architecture PKM System]]\"
 - \"[[Backlog]]\"
source: développement pkm-system phase 1.5
---
# 🎹 MOC - Raccourcis PKM System
> **Map of Content** - Index des raccourcis clavier du système
---
## 📊 Vue d'Ensemble
### **Raccourcis actifs:**
dataview
LIST
where contains(tags,\"shortcut\") and type=\"feature\"

### **En développement:**
dataview
TABLE shortcut, quicksummary
where type=\"feature\" and status =\"broken\"

### **Cassés:**
dataview
TABLE shortcut, quicksummary
where type=\"feature\" and status =\"broken\"

### **Dépréciés:**
dataview
TABLE shortcut, quicksummary
where type=\"feature\" and status =\"broken\"

---
## 🌍 Layer 1 - Global OS Shortcuts
### Window Management
- [[Ctrl+Shift+Space - Toggle Capture - BROKEN]] - ❌ BROKEN
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
dataview
TABLE status, updated
FROM [[]]
WHERE contains(tags, \"feature\") AND contains(tags, \"shortcut\")
SORT status ASC, updated DESC

---
**Légende Status:**
- ✅ ACTIVE - Fonctionne parfaitement
- 🟡 PARTIAL - Fonctionne partiellement
- ❌ BROKEN - Ne fonctionne pas
- 🔵 PLANNED - Prévu mais pas implémenté
- 🗑️ DEPRECATED - À supprimer
---
**Dernière mise à jour:** 2025-11-01T18:30:00On mets à jour cette note, j'ai commencé vite fait au début, je veux pas que la liste des raccourcis soit en dur, mais en requêtes dynamiques dataviewModifie les requêtes en développement, et dépréciées pour qu'ils soient correctsEnsuite La couche Layer 1, 2, help, layer 3 etc...
ça doit devenir des requêtes dataview qui renvoient la liste de ceux qui matchent ce filtreAfficher plus

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-531-R531-Created-updated-type-tags-system]]
- ⬇️ Next: [[Card-533-S533-ID-msg-533]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #obsidian
- #receipts
