---
type: chat-card
parent_export: '[[Export]]'
order: 466
role: assistant
created: '2025-11-10T21:46:12.256370Z'
tags:
- chat-card
- obsidian
attachments_count: 0
---

# 🤖 Message 466 - Assistant

**ID:** msg-466

## 💬 Content


**ID:** msg-466

Diagnosed YAML array syntax issue and prescribed block notation solution.L'utilisateur a un problème avec la syntaxe des propriétés related dans le frontmatter YAML. Il semble que Obsidian n'accepte pas la syntaxe avec virgules pour les liens dans une propriété array.
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

- ⬆️ Previous: [[Card-465-R465-Diagnosed-YAML-array-syntax-issue]]
- ⬇️ Next: [[Card-467-R467-Diagnosed-YAML-array-syntax-issue]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #obsidian
