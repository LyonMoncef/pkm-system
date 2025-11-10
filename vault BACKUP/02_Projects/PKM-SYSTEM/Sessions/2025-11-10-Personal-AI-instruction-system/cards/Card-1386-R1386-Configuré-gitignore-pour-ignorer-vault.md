---
type: chat-card
parent_export: '[[Export]]'
order: 1386
role: assistant
created: '2025-11-10T21:46:24.115189Z'
tags:
- chat-card
- obsidian
- git
attachments_count: 0
---

# 🤖 Message 1386 - Assistant

**ID:** msg-1386

## 💬 Content


**ID:** msg-1386

Ah oui ! On a configuré le .gitignore pour ignorer vault/* avec des exceptions seulement pour:

vault/06_Meta/TAG_REGISTRY.md
vault/06_Meta/Claude-Instructions.md
vault/04_Resources/Templates/

Mais pas pour vault/06_Meta/Decisions/ !
Il faut soit:

Ajouter une exception pour vault/06_Meta/Decisions/ dans le .gitignore
Ou décider si on veut vraiment versionner les cartes de décision

Je pense que les cartes de décision DOIVENT être versionnées car:

C'est de la documentation système
Pas de données personnelles
Important pour comprendre l'évolution du projet
Snapshots sont justement là pour l'historique

Donc il faut modifier le .gitignore pour ajouter l'exception.

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-1385-R1385-Configuré-gitignore-pour-ignorer-vault]]
- ⬇️ Next: [[Card-1387-R1387-Configuré-gitignore-pour-ignorer-vault]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #obsidian
- #git
