---
type: chat-card
parent_export: '[[Export]]'
order: 847
role: assistant
created: '2025-11-10T21:46:17.426446Z'
tags:
- chat-card
- python
- obsidian
- receipts
- code
- git
- automation
attachments_count: 0
---

# 🤖 Message 847 - Assistant

**ID:** msg-847

## 💬 Content


**ID:** msg-847

MF1 -
On garde, justement regarde cette note : # 📋 Toggl Tasks - Refactor Plan
> **Liste de tâches** - Refactor architecture Phase 1.5
---
## 🎯 Objectif
Clean architecture refactor : Extraction CSS + Redesign Shortcuts
---
## 📊 Configuration Toggl
### Projet
**Nom:** PKM System - Refactor Plan
**Description:** Clean architecture refactor - CSS extraction + Shortcuts redesign
**Couleur:** Violet (#667eea)
### Tags Toggl
**Phases:**
- #phase1 #phase2 #phase3 #phase4
**Catégories:**
- #git #doc #css #js #shortcuts #architecture
**Actions:**
- #setup #implementation #test #cleanup #bugfix
**UI/UX:**
- #ui #visual #ux
---
## 📋 Tasks par Phase
### Phase 1 - Documentation (17min)
- [ ] [P1.1] Commit sauvegarde état actuel (5min) - #phase1 #git #baseline
- [ ] [P1.2] Créer SHORTCUTS.md (5min) - #phase1 #doc #shortcuts
- [ ] [P1.3] Créer REFACTOR.md avec plan (5min) - #phase1 #doc #architecture
- [ ] [P1.4] Merge phase1 dans main (2min) - #phase1 #git
---
### Phase 2 - Extraction CSS/JS (58min)
- [ ] [P2.1] Créer structure /styles et /scripts (5min) - #phase2 #setup #folders
- [ ] [P2.2] Extraire variables CSS → global.css (10min) - #phase2 #css #global
- [ ] [P2.3] Extraire app.html CSS → app.css (10min) - #phase2 #css
- [ ] [P2.4] Extraire capture.html CSS → capture.css (10min) - #phase2 #css
- [ ] [P2.5] Extraire hub.html CSS → hub.css (5min) - #phase2 #css
- [ ] [P2.6] Extraire reference.html CSS → reference.css (5min) - #phase2 #css
- [ ] [P2.7] Update <link> imports dans HTML (5min) - #phase2 #setup
- [ ] [P2.8] Test fonctionnel toutes pages (5min) - #phase2 #test #visual
- [ ] [P2.9] Commit + merge phase2 (3min) - #phase2 #git
---
### Phase 3 - Refactor Shortcuts (92min)
- [ ] [P3.1] Créer scripts/shortcuts.js structure (5min) - #phase3 #setup #js
- [ ] [P3.2] Documenter shortcuts actuels (5min) - #phase3 #doc #shortcuts
- [ ] [P3.3] Supprimer shortcuts de app.html (5min) - #phase3 #cleanup
- [ ] [P3.4] Supprimer shortcuts de capture.html (5min) - #phase3 #cleanup
- [ ] [P3.5] Supprimer shortcuts de hub.html (3min) - #phase3 #cleanup
- [ ] [P3.6] Supprimer shortcuts de reference.html (3min) - #phase3 #cleanup
- [ ] [P3.7] Implémenter Layer 2 navigation (10min) - #phase3 #implementation #shortcuts
- [ ] [P3.8] Test Ctrl+1/2/3/B individuellement (5min) - #phase3 #test
- [ ] [P3.9] Implémenter relay mechanism propre (10min) - #phase3 #implementation #architecture
- [ ] [P3.10] Test relay depuis chaque page (5min) - #phase3 #test
- [ ] [P3.11] Implémenter shortcuts help Ctrl+/ (10min) - #phase3 #implementation #ui
- [ ] [P3.12] Fix IPC chain global shortcuts (10min) - #phase3 #bugfix #architecture
- [ ] [P3.13] Test complet matrix shortcuts (10min) - #phase3 #test
- [ ] [P3.14] Commit + merge phase3 (3min) - #phase3 #git
---
### Phase 4 - Polish & Cleanup (33min)
- [ ] [P4.1] Supprimer code mort (watchdog, debug) (5min) - #phase4 #cleanup
- [ ] [P4.2] Update keyboard hints popup UI (5min) - #phase4 #ui
- [ ] [P4.3] Update status bar raccourcis (3min) - #phase4 #ui
- [ ] [P4.4] Checklist tests manuels complète (10min) - #phase4 #test
- [ ] [P4.5] Update README.md (5min) - #phase4 #doc
- [ ] [P4.6] Commit + merge phase4 (3min) - #phase4 #git
- [ ] [P4.7] Tag release v0.2.0-refactor (2min) - #phase4 #git
---
## 📊 Récapitulatif
**Total estimé:** ~3h20min (200min)
| Phase | Durée | Tâches |
|-------|-------|--------|
| Phase 1 | 17min | 4 |
| Phase 2 | 58min | 9 |
| Phase 3 | 92min | 14 |
| Phase 4 | 33min | 7 |
---
## 🔗 Liens
- [[MOC Raccourcis]] - Documentation shortcuts
- [[Global Shortcuts System]] - Système Layer 1
- [[IPC Communication]] - Architecture IPC
- [[Backlog]] - Backlog général
---
**Dernière mise à jour:** 2025-11-01T20:30:00
**Status:** In Progress - Phase 1.5 Refactor=========================C'est la structure des tasks sur toggle pour le refactor planMais à un embranchement de la conv (si tu peux retrouver quand c'est top) on a dévié sur un autre sujet, un autre concept, une autre rechercheSi tu peux me faire une sorte de schéma comme tu fais avec les cartes UML en .md
pour résumer à partir du moment où on a dévié, tous les embranchements que ça a suivi ?Mais sinon oui il faut garder la mention de toggl, et si j'y fais pas référence comme dans cette session
A chaque task toggl, sa note dans le vault également
On doit s'automatiser pour qu'une tache toggl corresponde à une note
Donc il me faut dans l'arborescence, un dossier qui copie la structure du projet toggl2-
On fait une place aussi pour git aliases on peut le mettre pas loin de nvim et tmux dans les notes (une arbo à recommander pour gérer leurs notes et d'autres sujets environnants ?)3-
Variable se disperse
4- posé v2 sauf ton inverse dans la session locale
5- focus projetAfficher plus

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-846-R846-Garde-justement-regarde-cette-note]]
- ⬇️ Next: [[Card-848-R848-Garde-justement-regarde-cette-note]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #python
- #obsidian
- #receipts
- #code
- #git
- #automation
