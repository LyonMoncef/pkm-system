---
type: chat-card
parent_export: '[[Export]]'
order: 588
role: assistant
created: '2025-11-10T21:46:13.934197Z'
tags:
- chat-card
- obsidian
attachments_count: 0
---

# 🤖 Message 588 - Assistant

**ID:** msg-588

## 💬 Content


**ID:** msg-588

Ah oui, c'est une bonne question. Il veut utiliser FROM pour cibler un dossier spécifique, pas juste un tag. En Dataview, pour référencer un dossier, il y a plusieurs syntaxes possibles :

Sans guillemets si pas d'espaces/caractères spéciaux
Avec guillemets si espaces/tirets
Le problème c'est que \"PKM-SYSTEM\" a un tiret, ce qui peut causer des soucis

Les syntaxes possibles en Dataview pour les dossiers :

FROM \"02_Projects/PKM-SYSTEM/Shortcuts\"
FROM \"02_Projects/PKM-SYSTEM/Shortcuts/\"
Sans guillemets si ça marche : FROM 02_Projects/PKM-SYSTEM/Shortcuts

Le tiret dans \"PKM-SYSTEM\" est probablement ce qui pose problème. Quelques solutions :

Essayer sans guillemets
Essayer avec des guillemets normales
Vérifier que le chemin est exact (case-sensitive)
Utiliser un chemin relatif
Combiner dossier + tags

Laisse-moi lui donner les bonnes syntaxes et des solutions de debug.

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-587-R587-Bonne-question-veut-utiliser-FROM]]
- ⬇️ Next: [[Card-589-R589-Bonne-question-veut-utiliser-FROM]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #obsidian
