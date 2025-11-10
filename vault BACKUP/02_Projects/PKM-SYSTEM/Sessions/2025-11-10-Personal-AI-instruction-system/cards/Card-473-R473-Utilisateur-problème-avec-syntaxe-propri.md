---
type: chat-card
parent_export: '[[Export]]'
order: 473
role: assistant
created: '2025-11-10T21:46:12.361854Z'
tags:
- chat-card
- obsidian
attachments_count: 0
---

# 🤖 Message 473 - Assistant

**ID:** msg-473

## 💬 Content


**ID:** msg-473

L'utilisateur a un problème avec la syntaxe des propriétés related dans le frontmatter YAML. Il semble que Obsidian n'accepte pas la syntaxe avec virgules pour les liens dans une propriété array.
En YAML, pour les arrays, il y a plusieurs syntaxes possibles :

related: [item1, item2, item3] - syntaxe inline
related: suivi de lignes avec - item - syntaxe block

Le problème ici est que les [[liens]] dans un array inline avec virgules peuvent poser problème. Il faut soit :

Utiliser la syntaxe block (avec des tirets)
Ou mettre les liens entre guillemets dans l'array inline

La meilleure solution pour Obsidian est la syntaxe block :
yamlrelated:
 - \"[[MOC Raccourcis]]\"
 - \"[[Ctrl+Shift+F - Toggle Reference]]\"
 - \"[[Ctrl+Shift+H - Toggle Hub]]\"
Ou sans guillemets si Obsidian les accepte :
yamlrelated:
 - [[MOC Raccourcis]]
 - [[Ctrl+Shift+F - Toggle Reference]]
 - [[Ctrl+Shift+H - Toggle Hub]]

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-472-R472-Utilisateur-problème-avec-syntaxe-propri]]
- ⬇️ Next: [[Card-474-R474-Yamlrelated-Raccourcis-Ctrl-Shift-Toggle]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #obsidian
