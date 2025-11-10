---
type: chat-card
parent_export: '[[Export]]'
order: 922
role: assistant
created: '2025-11-10T21:12:17.947841Z'
tags:
- chat-card
- python
- receipts
- code
- git
- automation
attachments_count: 0
---

# 🤖 Message 922 - Assistant

**ID:** msg-922

## 💬 Content


**ID:** msg-922

🚀 REFACTOR PLAN - TOGGLE TASKS AVEC TAGS

📋 PHASE 1 - COMMIT + DOCUMENTATION
Branch: refactor/phase1-documentation
Durée estimée: 15min
Tags: #refactor #phase1 #documentation

 Task 1.1 - Commit sauvegarde état actuel #git #baseline
 Task 1.2 - Créer SHORTCUTS.md avec état actuel #doc #shortcuts
 Task 1.3 - Créer REFACTOR.md avec plan complet #doc #architecture
 Task 1.4 - Merge phase1 dans main #git #merge


📋 PHASE 2 - EXTRACTION CSS/JS
Branch: refactor/phase2-extraction
Durée estimée: 1h
Tags: #refactor #phase2 #css #modularization

 Task 2.1 - Créer structure /styles et /scripts #setup #folders
 Task 2.2 - Extraire variables CSS → styles/global.css #css #global
 Task 2.3 - Extraire app.html CSS → styles/app.css #css #app
 Task 2.4 - Extraire capture.html CSS → styles/capture.css #css #capture
 Task 2.5 - Extraire hub.html CSS → styles/hub.css #css #hub
 Task 2.6 - Extraire reference.html CSS → styles/reference.css #css #reference
 Task 2.7 - Update <link> imports dans tous les HTML #html #imports
 Task 2.8 - Test fonctionnel toutes les pages #test #visual
 Task 2.9 - Commit + merge phase2 dans main #git #merge


📋 PHASE 3 - REFACTOR SHORTCUTS
Branch: refactor/phase3-shortcuts
Durée estimée: 1h
Tags: #refactor #phase3 #shortcuts #architecture

 Task 3.1 - Créer scripts/shortcuts.js structure vide #setup #js
 Task 3.2 - Documenter shortcuts actuels dans le code #doc #audit
 Task 3.3 - Supprimer shortcuts inline de app.html #cleanup #app
 Task 3.4 - Supprimer shortcuts inline de capture.html #cleanup #capture
 Task 3.5 - Supprimer shortcuts inline de hub.html #cleanup #hub
 Task 3.6 - Supprimer shortcuts inline de reference.html #cleanup #reference
 Task 3.7 - Implémenter Layer 2 navigation dans shortcuts.js #implementation #layer2
 Task 3.8 - Test Ctrl+1/2/3/B individuellement #test #navigation
 Task 3.9 - Implémenter relay mechanism propre (postMessage) #implementation #relay
 Task 3.10 - Test relay depuis capture/hub/reference #test #relay
 Task 3.11 - Implémenter shortcuts help Ctrl+/ #implementation #help
 Task 3.12 - Fix IPC chain pour global shortcuts #bugfix #ipc
 Task 3.13 - Test complet matrix tous shortcuts #test #comprehensive
 Task 3.14 - Commit + merge phase3 dans main #git #merge


📋 PHASE 4 - POLISH & CLEANUP
Branch: refactor/phase4-polish
Durée estimée: 30min
Tags: #refactor #phase4 #polish #cleanup

 Task 4.1 - Supprimer code mort (watchdog, debug logs) #cleanup #deadcode
 Task 4.2 - Update keyboard hints popup UI #ui #hints
 Task 4.3 - Update status bar avec bons raccourcis #ui #statusbar
 Task 4.4 - Checklist tests manuels complète #test #manual
 Task 4.5 - Update README.md avec nouvelle archi #doc #readme
 Task 4.6 - Commit + merge phase4 dans main #git #merge
 Task 4.7 - Tag release v0.2.0-refactor #git #release


🎯 TASK 1.1 EN COURS
Commit sauvegarde état actuel
Tags: #git #baseline #save
Branch: refactor/phase1-documentation
bashcd ~/pkm-system

# Checkout nouvelle branche
git checkout -b refactor/phase1-documentation

# Add tout
git add .

# Commit état actuel
git commit -m \"save: pre-refactor state - working features baseline

✅ Working:
- Sidebar toggle (Ctrl+B)
- Capture auto-save/load to localStorage
- Vim modes (Esc/Ctrl+I) in capture
- Dark theme coherent across pages
- Page navigation (Ctrl+1/2/3) partial

⚠️ Issues:
- Global shortcuts IPC chain broken
- Shortcuts relay inconsistent
- Code scattered across files (spaghetti)

Tags: #baseline #pre-refactor
Next: Task 1.2 - Create SHORTCUTS.md\"

# Push branche
git push -u origin refactor/phase1-documentation

✅ EXÉCUTE + CONFIRME
Lance ces commandes et dis-moi quand c'est fait pour passer à Task 1.2 ! 💪

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-921-R921-Utilisateur-raison-oublié-formater-corre]]
- ⬇️ Next: [[Card-923-R923-Bashcd-system-Checkout-nouvelle-branche]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #receipts
- #code
- #git
- #automation
