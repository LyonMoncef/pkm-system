---
type: chat-card
parent_export: '[[Export]]'
order: 1385
role: assistant
created: '2025-11-10T21:46:24.104153Z'
tags:
- chat-card
- obsidian
- git
attachments_count: 0
---

# 🤖 Message 1385 - Assistant

**ID:** msg-1385

## 💬 Content


**ID:** msg-1385

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

- ⬆️ Previous: [[Card-1384-R1384-Identified-gitignore-conflict-advocated-]]
- ⬇️ Next: [[Card-1386-R1386-Configuré-gitignore-pour-ignorer-vault]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #obsidian
- #git
