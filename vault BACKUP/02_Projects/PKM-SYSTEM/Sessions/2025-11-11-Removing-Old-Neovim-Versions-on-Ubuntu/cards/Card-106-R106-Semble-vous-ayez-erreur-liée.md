---
type: chat-card
parent_export: '[[Export]]'
order: 106
role: assistant
created: '2025-11-11T00:40:04.629573Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 106 - Assistant

**ID:** msg-106

## 💬 Content


**ID:** msg-106

Il semble que vous ayez une erreur liée à un module manquant dans votre configuration Neovim. Le message d'erreur indique que le module 'misc.style' n'est pas trouvé, ce qui provoque l'échec du chargement de nvim-lspconfig.
Voici comment vous pouvez résoudre ce problème :

Vérifiez votre fichier /home/tats/.config/nvim/lua/plugins/lsp.lua qui essaie d'importer le module 'misc.style' à la ligne 118.
Vous avez trois options principales :

Créer le module manquant en ajoutant un fichier misc/style.lua dans l'un des chemins de recherche Lua
Modifier votre configuration pour ne plus dépendre de ce module
Vérifier si le module fait partie d'un plugin que vous avez désinstallé ou oublié d'installer


Solution rapide : créez le module manquant

bash mkdir -p ~/.config/nvim/lua/misc
 touch ~/.config/nvim/lua/misc/style.lua
Puis ajoutez le contenu nécessaire à ce fichier.

Ou examinez le fichier lsp.lua à la ligne 118 et commentez temporairement cette ligne pour voir si le reste de votre configuration fonctionne correctement :

lua -- require('misc.style') -- commentez cette ligne pour tester
Ce problème est probablement lié à une dépendance manquante ou à un changement dans votre structure de plugins plutôt qu'aux multiples versions de nvim. Pouvez-vous me montrer le contenu de la ligne 118 de votre fichier lsp.lua pour que je puisse vous aider plus précisément ?Réessayer

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-105-S105-ID-msg-105]]
- ⬇️ Next: [[Card-107-R107-Semble-vous-ayez-erreur-liée]]
- 📊 MOC: [[_MOC_Removing Old Neovim Versions on Ubuntu]]
