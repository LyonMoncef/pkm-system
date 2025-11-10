---
type: chat-card
parent_export: '[[Export]]'
order: 348
role: assistant
created: '2025-11-10T21:46:10.606604Z'
tags:
- chat-card
- excel
- python
- obsidian
- receipts
- code
- git
- automation
attachments_count: 0
---

# 🤖 Message 348 - Assistant

**ID:** msg-348

## 💬 Content


**ID:** msg-348

🎯 EXCELLENT POINT - ÉVITER L'ENFER DE LA SYNCHRO
⚠️ LE PIÈGE À ÉVITER
Tu as 100% raison : dupliquer le code dans les notes = cauchemar de maintenance.

✅ SOLUTION HYBRIDE INTELLIGENTE
PRINCIPE CLÉ

Le code est la source de vérité. Les notes sont des POINTEURS enrichis.


🏗️ ARCHITECTURE PROPOSÉE
1. Structure Miroir (légère)
04_Resources/
└── Code/
 └── PKM-System/
 ├── main.js.md ← Note légère
 ├── shortcuts.js.md ← Note légère
 ├── preload.js.md ← Note légère
 └── ...
Chaque note de fichier contient :

✅ Métadonnées (créé, modifié, tags)
✅ Description high-level (rôle du fichier)
✅ Lien direct vers le fichier avec protocole file:// ou obsidian://
✅ Liste des fonctions principales (auto-générée plus tard)
✅ Dépendances conceptuelles
❌ PAS de copie du code


2. Liens Intelligents dans les Features
Dans la carte du raccourci :
markdown## Implémentation

**Fichier:** [[main.js]] (ligne ~45)
**Fonction:** `registerGlobalShortcuts()`

→ [Ouvrir le fichier](file:///home/user/pkm-system/src/main/main.js#L45)

**Dépendances conceptuelles:**
- [[smartToggle Function]]
- [[IPC Communication Architecture]]
- [[Global Shortcuts System]]
Au lieu de copier le code.

3. Note main.js (exemple)
markdown---
created: 2025-10-20T10:00:00
updated: 2025-11-01T14:50:00
type: code-file
tags: [code, electron, main-process, pkm-system]
path: \"src/main/main.js\"
language: javascript
---

# main.js - Main Process Entry Point

## Description

Point d'entrée du processus principal Electron. Gère :
- Création de la fenêtre principale
- Enregistrement des raccourcis globaux
- Communication IPC avec le renderer
- Système tray

## Accès Rapide

→ [Ouvrir dans VSCode](vscode://file/home/user/pkm-system/src/main/main.js)
→ [Ouvrir dans Nvim](file:///home/user/pkm-system/src/main/main.js)

## Fonctions Principales

| Fonction | Ligne | Description | Utilisée par |
|----------|-------|-------------|--------------|
| `createMainWindow()` | ~25 | Crée la fenêtre | app.on('ready') |
| `registerGlobalShortcuts()` | ~45 | Configure shortcuts OS | app.on('ready') |
| `smartToggle()` | ~78 | Toggle intelligent | Tous les shortcuts |

## Dépendances

**Imports:**
- `electron` (BrowserWindow, globalShortcut, ipcMain)
- `path`

**Fichiers liés:**
- [[preload.js]] - Bridge IPC
- [[app.html]] - Renderer principal

**Features utilisant ce fichier:**
- [[Ctrl+Shift+Space - Toggle Capture]]
- [[Ctrl+Shift+F - Toggle Reference]]
- [[Ctrl+Shift+H - Toggle Hub]]
- [[Ctrl+W - Quick Save & Hide]]

## Architecture
```
main.js
├── Window Management
│   ├── createMainWindow()
│   └── smartToggle()
├── Global Shortcuts
│   └── registerGlobalShortcuts()
├── IPC Handlers
│   ├── current-page-changed
│   └── hide-window
└── Tray System
    └── createTray()
```

## Notes Techniques

- Utilise `single instance lock` pour éviter multiples instances
- Les shortcuts globaux sont enregistrés au `app.on('ready')`
- Variable `currentPage` track la page active pour smart toggle

## Commits Récents

- `2025-10-24T15:45` - Ajout smartToggle() et tracking currentPage
- `2025-10-20T10:00` - Initial implementation

---

**Source de vérité:** Le fichier code lui-même
**Cette note:** Contexte + navigation + liens conceptuels

🤖 AUTOMATISATION (Phase 2)
Script Python simple qui tourne 1x/jour ou sur commit :
python# sync-code-notes.py

import os
import re
from datetime import datetime

def extract_functions(file_path):
 \"\"\"Extrait les fonctions d'un fichier JS\"\"\"
 with open(file_path, 'r') as f:
 content = f.read()

 # Regex pour fonctions
 functions = re.findall(r'function (\\w+)\\(', content)
 # + arrow functions
 functions += re.findall(r'const (\\w+) = \\(.*\\) =>', content)

 return functions

def update_code_note(js_file, note_file):
 \"\"\"Met à jour la note avec les nouvelles fonctions\"\"\"
 functions = extract_functions(js_file)

 # Lit la note existante
 with open(note_file, 'r') as f:
 note = f.read()

 # Update section \"Fonctions Principales\"
 # (logique de remplacement...)

 # Update \"updated\" timestamp
 # (logique de remplacement...)

# Lance pour tous les fichiers
for js_file in glob('src/**/*.js'):
 note_file = f'vault/04_Resources/Code/{js_file}.md'
 update_code_note(js_file, note_file)
À lancer :

En git pre-commit hook
1x par jour via cron
Ou manuellement quand besoin


🎯 RÉPONSE À TA QUESTION

C'est quoi le mieux ? Accéder au fichier directement ?
Ou bien de le référencer et ajouter des metadonnées autour ?

Les deux !
Option Recommandée : HYBRIDE

Note légère avec métadonnées + contexte
Lien direct vers le fichier source (file://)
Pas de duplication du code
Auto-update des métadonnées basiques (fonctions, lignes)


✅ REFACTO DE LA CARTE RACCOURCI
markdown## Implémentation

**Fichier:** [[main.js]] (fonction `registerGlobalShortcuts()`)
→ [Ouvrir le code](file:///home/moncef/pkm-system/src/main/main.js#L45)

**Ligne approximative:** ~45 (peut changer)

**Dépendances conceptuelles:**
- [[smartToggle Function]] - Logique de toggle
- [[IPC Communication]] - Communication main↔renderer
- [[currentPage Variable]] - Tracking état

**Ne PAS copier le code ici - le code est dans main.js**

🚀 PLAN D'ACTION
Maintenant (Phase 1) :

✅ Finaliser la carte du raccourci avec liens vers fichiers (pas de code dupliqué)
✅ Créer 04_Resources/Code/ structure
✅ Créer note main.js.md (version légère ci-dessus)
✅ Lier les deux

Plus tard (Phase 2) :

Script Python auto-update
Git hooks
Obsidian plugin custom (si besoin)


🤔 QUESTIONS

Le chemin du projet : C'est où exactement ? (pour les liens file://)
Tu veux qu'on crée la note main.js.md maintenant ?
Ou on finit d'abord la carte du raccourci avec les nouveaux principes ?

Ton choix ? 🎯

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-347-R347-Excellente-question-touche-point-crucial]]
- ⬇️ Next: [[Card-349-R349-Code-System-main-Note-légère]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #excel
- #python
- #obsidian
- #receipts
- #code
- #git
- #automation
