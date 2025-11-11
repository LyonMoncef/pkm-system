---
type: chat-card
parent_export: '[[Export]]'
order: 216
role: assistant
created: '2025-11-11T01:06:56.212551Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 216 - Assistant

**ID:** msg-216

## 💬 Content


**ID:** msg-216

Ah ! Le problème est clair : la config win32yank n'est pas appliquée, il utilise toujours osc52. Ça veut dire soit :

La config n'est pas dans le bon ordre dans init.lua
Un plugin surcharge la config après

Il faut soit :

Mettre la config clipboard APRÈS les plugins
Ou utiliser autocmd pour forcer après le chargement
Ou vérifier qu'il n'y a pas un plugin qui gère le clipboard

Le fait que ça affiche \"osc52\" montre que quelque chose surcharge la config.

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-215-R215-Problème-clair-config-appliquée-utilise]]
- ⬇️ Next: [[Card-217-R217-Problème-clair-config-appliquée-utilise]]
- 📊 MOC: [[_MOC_Slow copy-paste in terminal]]
