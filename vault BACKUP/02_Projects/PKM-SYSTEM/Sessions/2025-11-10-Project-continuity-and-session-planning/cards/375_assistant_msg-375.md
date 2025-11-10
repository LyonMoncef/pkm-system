---
type: chat-card
parent_export: '[[Export]]'
order: 375
role: assistant
created: '2025-11-10T23:13:24.737953Z'
tags:
- chat-card
- python
- obsidian
- automation
attachments_count: 0
---

# 🤖 Message 375 - Assistant

**ID:** msg-375

## 💬 Content


**ID:** msg-375

Bonne question sur l'organisation des scripts. Il faut penser à :

Ces scripts sont des outils/utilitaires pour le PKM
Ils seront réutilisés régulièrement
D'autres scripts viendront
Besoin d'une structure claire et consultable

Options :

Dans le vault Obsidian avec documentation
Dans un dossier séparé du projet
Mixte : code externe + doc dans vault

Je pense la meilleure approche :

Scripts dans /scripts ou /tools à la racine du projet
Documentation dans 04_Resources/Tools/ dans le vault
MOC pour référencer tous les outils

Structure proposée :
pkm-system/
├── vault/
│ └── 04_Resources/
│ └── Tools/
│ ├── MOC - Tools.md
│ ├── chat-exporter-guide.md
│ └── ...
├── scripts/
│ ├── README.md
│ ├── chat-exporter.js
│ └── ...
└── ...
Garde ça court et structuré comme demandé.

---


## 🔗 Navigation

- ⬆️ Previous: [[374_assistant_msg-374]]
- ⬇️ Next: [[376_assistant_msg-376]]
- 📊 MOC: [[_MOC_Project continuity and session planning]]

## 🏷️ Topics

- #python
- #obsidian
- #automation
