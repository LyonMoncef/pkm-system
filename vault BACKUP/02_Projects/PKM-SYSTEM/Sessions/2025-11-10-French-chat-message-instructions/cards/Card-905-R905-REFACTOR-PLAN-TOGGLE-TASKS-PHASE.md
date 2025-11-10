---
type: chat-card
parent_export: '[[Export]]'
order: 905
role: assistant
created: '2025-11-10T21:12:17.717109Z'
tags:
- chat-card
- python
- receipts
- code
- git
- automation
attachments_count: 0
---

# 🤖 Message 905 - Assistant

**ID:** msg-905

## 💬 Content


**ID:** msg-905

🚀 REFACTOR PLAN - TOGGLE TASKS

📋 PHASE 1 - COMMIT + DOCUMENTATION (15min)
Branche: refactor/phase1-documentation

 Task 1.1 - Commit sauvegarde état actuel
 Task 1.2 - Créer SHORTCUTS.md
 Task 1.3 - Créer REFACTOR.md avec plan complet
 Task 1.4 - Merge dans main


📋 PHASE 2 - EXTRACTION CSS/JS (1h)
Branche: refactor/phase2-extraction

 Task 2.1 - Créer structure dossiers /styles et /scripts
 Task 2.2 - Extraire CSS global → styles/global.css
 Task 2.3 - Extraire CSS app.html → styles/app.css
 Task 2.4 - Extraire CSS capture.html → styles/capture.css
 Task 2.5 - Extraire CSS hub.html → styles/hub.css
 Task 2.6 - Extraire CSS reference.html → styles/reference.css
 Task 2.7 - Update imports dans HTML
 Task 2.8 - Test fonctionnel
 Task 2.9 - Merge dans main


📋 PHASE 3 - REFACTOR SHORTCUTS (1h)
Branche: refactor/phase3-shortcuts

 Task 3.1 - Créer scripts/shortcuts.js vide
 Task 3.2 - Documenter tous les shortcuts actuels
 Task 3.3 - Supprimer shortcuts de app.html
 Task 3.4 - Supprimer shortcuts de capture.html
 Task 3.5 - Supprimer shortcuts de hub.html
 Task 3.6 - Supprimer shortcuts de reference.html
 Task 3.7 - Implémenter Layer 2 (internal) dans shortcuts.js
 Task 3.8 - Tester Ctrl+1/2/3/B individuellement
 Task 3.9 - Implémenter relay mechanism propre
 Task 3.10 - Tester relay depuis chaque page
 Task 3.11 - Implémenter shortcuts help (Ctrl+/)
 Task 3.12 - Fix IPC chain pour global shortcuts
 Task 3.13 - Test complet tous shortcuts
 Task 3.14 - Merge dans main


📋 PHASE 4 - POLISH & CLEANUP (30min)
Branche: refactor/phase4-polish

 Task 4.1 - Supprimer code mort (watchdog, tests debug)
 Task 4.2 - Update keyboard hints UI
 Task 4.3 - Update status bar text
 Task 4.4 - Tests manuels checklist complète
 Task 4.5 - Update README.md
 Task 4.6 - Merge dans main
 Task 4.7 - Tag release v0.2.0-refactor


🔥 TASK 1.1 - COMMIT SAUVEGARDE
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

📋 Next: Phase 1 - Documentation (SHORTCUTS.md, REFACTOR.md)\"

# Push branche
git push -u origin refactor/phase1-documentation

✅ EXÉCUTE TASK 1.1
Lance ces commandes et confirme-moi quand c'est fait ! 💪

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-904-R904-Utilisateur-veut-adopte-plan-refactor]]
- ⬇️ Next: [[Card-906-R906-Bashcd-system-Checkout-nouvelle-branche]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #receipts
- #code
- #git
- #automation
