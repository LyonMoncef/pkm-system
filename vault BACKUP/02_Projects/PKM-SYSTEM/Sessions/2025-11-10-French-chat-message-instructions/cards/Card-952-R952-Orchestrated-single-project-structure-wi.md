---
type: chat-card
parent_export: '[[Export]]'
order: 952
role: assistant
created: '2025-11-10T21:12:18.321884Z'
tags:
- chat-card
- python
- receipts
- code
- git
- automation
attachments_count: 0
---

# 🤖 Message 952 - Assistant

**ID:** msg-952

## 💬 Content


**ID:** msg-952

Orchestrated single-project structure with prefixes and tags.L'utilisateur choisit l'option C : un seul projet avec préfixes [P1], [P2] etc. et tags.
Je vais maintenant lui donner :

Le setup complet Toggl à créer
La liste complète des tâches avec préfixes et tags
Comment démarrer Task 1.1

Pas besoin de web search ici, c'est juste de l'organisation de projet.🎯 SETUP TOGGL - OPTION C ACTIVÉ

📦 CRÉATION PROJET TOGGL
Crée ce projet dans Toggl :
Nom du projet: PKM System - Refactor Plan
Description: Clean architecture refactor - CSS extraction + Shortcuts redesign
Couleur: Violet (#667eea)

🏷️ TAGS À CRÉER
Dans Toggl, crée ces tags :
Phases:
#phase1 #phase2 #phase3 #phase4

Catégories:
#git #doc #css #js #shortcuts #architecture

Actions:
#setup #implementation #test #cleanup #bugfix

UI/UX:
#ui #visual #ux

📋 LISTE COMPLÈTE DES TÂCHES
PHASE 1 - DOCUMENTATION
[P1.1] Commit sauvegarde état actuel
Tags: #phase1 #git #baseline
Durée estimée: 5min

[P1.2] Créer SHORTCUTS.md
Tags: #phase1 #doc #shortcuts
Durée estimée: 5min

[P1.3] Créer REFACTOR.md avec plan
Tags: #phase1 #doc #architecture
Durée estimée: 5min

[P1.4] Merge phase1 dans main
Tags: #phase1 #git
Durée estimée: 2min

PHASE 2 - EXTRACTION CSS/JS
[P2.1] Créer structure /styles et /scripts
Tags: #phase2 #setup #folders
Durée estimée: 5min

[P2.2] Extraire variables CSS → global.css
Tags: #phase2 #css #global
Durée estimée: 10min

[P2.3] Extraire app.html CSS → app.css
Tags: #phase2 #css
Durée estimée: 10min

[P2.4] Extraire capture.html CSS → capture.css
Tags: #phase2 #css
Durée estimée: 10min

[P2.5] Extraire hub.html CSS → hub.css
Tags: #phase2 #css
Durée estimée: 5min

[P2.6] Extraire reference.html CSS → reference.css
Tags: #phase2 #css
Durée estimée: 5min

[P2.7] Update <link> imports dans HTML
Tags: #phase2 #setup
Durée estimée: 5min

[P2.8] Test fonctionnel toutes pages
Tags: #phase2 #test #visual
Durée estimée: 5min

[P2.9] Commit + merge phase2
Tags: #phase2 #git
Durée estimée: 3min

PHASE 3 - REFACTOR SHORTCUTS
[P3.1] Créer scripts/shortcuts.js structure
Tags: #phase3 #setup #js
Durée estimée: 5min

[P3.2] Documenter shortcuts actuels
Tags: #phase3 #doc #shortcuts
Durée estimée: 5min

[P3.3] Supprimer shortcuts de app.html
Tags: #phase3 #cleanup
Durée estimée: 5min

[P3.4] Supprimer shortcuts de capture.html
Tags: #phase3 #cleanup
Durée estimée: 5min

[P3.5] Supprimer shortcuts de hub.html
Tags: #phase3 #cleanup
Durée estimée: 3min

[P3.6] Supprimer shortcuts de reference.html
Tags: #phase3 #cleanup
Durée estimée: 3min

[P3.7] Implémenter Layer 2 navigation
Tags: #phase3 #implementation #shortcuts
Durée estimée: 10min

[P3.8] Test Ctrl+1/2/3/B individuellement
Tags: #phase3 #test
Durée estimée: 5min

[P3.9] Implémenter relay mechanism propre
Tags: #phase3 #implementation #architecture
Durée estimée: 10min

[P3.10] Test relay depuis chaque page
Tags: #phase3 #test
Durée estimée: 5min

[P3.11] Implémenter shortcuts help Ctrl+/
Tags: #phase3 #implementation #ui
Durée estimée: 10min

[P3.12] Fix IPC chain global shortcuts
Tags: #phase3 #bugfix #architecture
Durée estimée: 10min

[P3.13] Test complet matrix shortcuts
Tags: #phase3 #test
Durée estimée: 10min

[P3.14] Commit + merge phase3
Tags: #phase3 #git
Durée estimée: 3min

PHASE 4 - POLISH & CLEANUP
[P4.1] Supprimer code mort (watchdog, debug)
Tags: #phase4 #cleanup
Durée estimée: 5min

[P4.2] Update keyboard hints popup UI
Tags: #phase4 #ui
Durée estimée: 5min

[P4.3] Update status bar raccourcis
Tags: #phase4 #ui
Durée estimée: 3min

[P4.4] Checklist tests manuels complète
Tags: #phase4 #test
Durée estimée: 10min

[P4.5] Update README.md
Tags: #phase4 #doc
Durée estimée: 5min

[P4.6] Commit + merge phase4
Tags: #phase4 #git
Durée estimée: 3min

[P4.7] Tag release v0.2.0-refactor
Tags: #phase4 #git
Durée estimée: 2min

🚀 DÉMARRAGE TASK 1.1
Lance Toggl maintenant :
Timer Toggl:
Projet: PKM System - Refactor Plan
Tâche: [P1.1] Commit sauvegarde état actuel
Tags: #phase1 #git #baseline
Puis exécute dans le terminal :
bashcd ~/pkm-system
git checkout -b refactor/phase1-documentation
git add .
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
Next: [P1.2] Create SHORTCUTS.md\"

git push -u origin refactor/phase1-documentation

✅ CONFIRME
Dis-moi quand:

✅ Projet Toggl créé
✅ Tags créés
✅ Timer [P1.1] lancé
✅ Git commit exécuté

Et on passe à Task 1.2 ! 💪

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-951-R951-Orchestrated-single-project-structure-wi]]
- ⬇️ Next: [[Card-953-R953-Orchestrated-single-project-structure-wi]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #receipts
- #code
- #git
- #automation
