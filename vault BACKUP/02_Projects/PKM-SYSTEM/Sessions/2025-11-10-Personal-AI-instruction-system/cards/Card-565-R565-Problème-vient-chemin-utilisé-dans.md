---
type: chat-card
parent_export: '[[Export]]'
order: 565
role: assistant
created: '2025-11-10T21:46:13.627582Z'
tags:
- chat-card
- obsidian
- code
attachments_count: 0
---

# 🤖 Message 565 - Assistant

**ID:** msg-565

## 💬 Content


**ID:** msg-565

Le problème vient du chemin utilisé dans la requête Dataview. Il y a plusieurs possibilités :

Le chemin exact n'est pas correct (espaces, underscores, etc.)
Dataview nécessite une syntaxe différente pour les chemins avec underscores/espaces
Il faut peut-être utiliser des guillemets simples ou pas de guillemets du tout

Regardons la structure qu'il a donnée plus tôt :
02_Projects/PKM-SYSTEM/Shortcuts/
Donc le chemin semble correct. Le problème peut venir de :

Les underscores dans PKM-SYSTEM
Les tirets
Les espaces potentiels
La syntaxe Dataview elle-même

En Dataview, pour les chemins :

Avec guillemets doubles : FROM \"path/to/folder\"
Sans guillemets si pas d'espaces : FROM path/to/folder
Avec des backslashes si nécessaire

Essayons différentes solutions :

Sans guillemets
Avec des guillemets simples
Avec le chemin complet depuis la racine
En utilisant des tags à la place

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-564-R564-Problème-vient-chemin-utilisé-dans]]
- ⬇️ Next: [[Card-566-R566-Problème-vient-chemin-utilisé-dans]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #obsidian
- #code
