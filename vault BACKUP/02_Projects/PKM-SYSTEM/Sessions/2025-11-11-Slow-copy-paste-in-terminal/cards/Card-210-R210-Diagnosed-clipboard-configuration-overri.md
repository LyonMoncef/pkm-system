---
type: chat-card
parent_export: '[[Export]]'
order: 210
role: assistant
created: '2025-11-11T01:06:56.124328Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 210 - Assistant

**ID:** msg-210

## 💬 Content


**ID:** msg-210

Diagnosed clipboard configuration override issue in Neovim.Ah ! Le problème est clair : la config win32yank n'est pas appliquée, il utilise toujours osc52. Ça veut dire soit :

La config n'est pas dans le bon ordre dans init.lua
Un plugin surcharge la config après

Il faut soit :

Mettre la config clipboard APRÈS les plugins
Ou utiliser autocmd pour forcer après le chargement
Ou vérifier qu'il n'y a pas un plugin qui gère le clipboard

Le fait que ça affiche \"osc52\" montre que quelque chose surcharge la config.

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-209-R209-Diagnosed-clipboard-configuration-overri]]
- ⬇️ Next: [[Card-211-R211-Diagnosed-clipboard-configuration-overri]]
- 📊 MOC: [[_MOC_Slow copy-paste in terminal]]
