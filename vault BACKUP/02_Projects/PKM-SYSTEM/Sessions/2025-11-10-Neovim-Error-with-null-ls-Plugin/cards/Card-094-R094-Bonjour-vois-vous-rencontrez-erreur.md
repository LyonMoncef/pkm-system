---
type: chat-card
parent_export: '[[Export]]'
order: 94
role: assistant
created: '2025-11-10T21:42:07.658635Z'
tags:
- chat-card
- git
attachments_count: 0
---

# 🤖 Message 94 - Assistant

**ID:** msg-94

## 💬 Content


**ID:** msg-94

Bonjour ! Je vois que vous rencontrez une erreur avec Neovim, plus précisément avec le plugin none-ls.nvim (anciennement null-ls). Voici l'analyse de votre erreur:
L'erreur se produit lors du traitement des événements CursorHoldI (quand le curseur reste immobile en mode insertion). Le problème spécifique est:
attempt to index field '_request_name_to_capability' (a nil value)
Cette erreur signifie que le code essaie d'accéder à une propriété _request_name_to_capability qui n'existe pas ou est nil.
Le problème se situe dans:

Fichier: null-ls/client.lua, ligne 77, dans la fonction capability_is_disabled
Cette fonction est appelée par supports_method
Qui est ensuite utilisée par la fonction buf_request de l'API LSP de Neovim

Pour résoudre ce problème, vous pourriez essayer:

Mettre à jour none-ls.nvim et Neovim à leurs dernières versions
Vérifier si vos configurations de none-ls sont compatibles avec votre version actuelle
Essayer de réinitialiser le plugin: :NullLsLog pour voir les logs, puis :NullLsInfo pour vérifier l'état

Si le problème persiste, vous pourriez temporairement désactiver none-ls ou signaler le bug sur le dépôt GitHub du plugin.
Avez-vous modifié récemment votre configuration Neovim ou mis à jour vos plugins?Réessayer

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-093-S093-ID-msg-93]]
- ⬇️ Next: [[Card-095-R095-Bonjour-vois-vous-rencontrez-erreur]]
- 📊 MOC: [[_MOC_Neovim Error with null-ls Plugin]]

## 🏷️ Topics

- #git
