---
type: chat-card
parent_export: '[[Export]]'
order: 833
role: assistant
created: '2025-11-10T21:46:17.271238Z'
tags:
- chat-card
- obsidian
- receipts
- code
- git
- automation
attachments_count: 0
---

# 🤖 Message 833 - Assistant

**ID:** msg-833

## 💬 Content


**ID:** msg-833

yamlphase: \"1.5\"
mood: 🔥
```

---

### Principes de Rédaction

**Notes atomiques:**
- Une note = un concept/feature/shortcut
- Contenu concis et précis
- Pas de duplication de code (pointeurs vers fichiers)
- Liens vers notes reliées

**MOCs (Maps of Content):**
- Index avec Dataview queries dynamiques
- PAS de listes en dur
- Vue d'ensemble par catégorie

**Liens fichiers code:**
- Chemin absolu Windows: `C:\\Users\\...\\file.js`
- Pas de duplication du code dans la note
- Juste pointeur + contexte + dépendances

---

## 🛠️ ENVIRONNEMENT TECHNIQUE

### Setup Principal

**Édition (Ubuntu + Nvim + Tmux):**
- Neovim pour édition notes
- Tmux sessions pour organisation
- NAS monté en SMB
- Git via ligne de commande

**Visualisation (Windows + Obsidian):**
- Interface graphique
- Dataview pour queries
- Graph view
- Plugins: Dataview (obligatoire)

### Workflow
```
Ubuntu (création/édition) → NAS (sync) → Windows (visualisation Obsidian)
 ↓
 Git versioning
```

---

## 📂 STRUCTURE VAULT
```
00_Inbox/ # Captures rapides
01_Journal/ # Journal quotidien
02_Projects/ # Projets actifs
 └── PKM-SYSTEM/
 ├── Shortcuts/ # Notes atomiques raccourcis
 ├── Concepts/ # Notes conceptuelles
 └── ...
03_Areas/ # Domaines vie
04_Resources/ # Ressources/références
 └── Environnement/
 ├── Tmux/ # Shortcuts Tmux
 └── Nvim/ # Commandes Nvim
05_Archives/ # Archivé
06_Meta/ # Métadonnées système
 └── TAG_REGISTRY.md # ⚠️ SOURCE DE VÉRITÉ TAGS
```

---

## 🎯 CONTEXTE PROJET PKM SYSTEM

### Stack
- **Frontend:** Vanilla HTML/CSS/JS
- **Framework:** Electron
- **Data:** Vault Obsidian (markdown)
- **Storage:** NAS SMB
- **VCS:** Git

### Philosophie
- **Simplicité** avant tout
- **Vanilla JS** - pas de frameworks lourds
- **Clavier-first** - raccourcis globaux
- **Performance** - app légère

### Architecture
```
Main Process (main.js)
 ↓ IPC
Preload (preload.js)
 ↓ contextBridge
Renderer (app.html + pages)

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-832-R832-Main-preload]]
- ⬇️ Next: [[Card-834-R834-Diff-MANAGEMENT-RÈGLE-ABSOLUE-TOUJOURS]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #obsidian
- #receipts
- #code
- #git
- #automation
