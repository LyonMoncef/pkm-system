---
type: chat-card
parent_export: '[[Export]]'
order: 104
role: assistant
created: '2025-11-10T21:42:07.782088Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 104 - Assistant

**ID:** msg-104

## 💬 Content


**ID:** msg-104

Je vois que vous avez exécuté la commande :NullLsInfo (ou son équivalent) et il semble qu'aucune source ne soit attachée à votre buffer actuel.
Le problème que vous rencontrez est probablement lié à une configuration incorrecte ou incomplète de none-ls.nvim (la version maintenue par nvimtools, qui est un fork du projet null-ls original).
Voici quelques étapes pour résoudre ce problème :

Vérifiez votre configuration dans votre fichier init.lua ou dans les fichiers spécifiques à none-ls.nvim. Assurez-vous que vous avez bien configuré et enregistré des sources.
Un exemple de configuration basique pourrait ressembler à ceci :

lualocal null_ls = require(\"null-ls\")

null_ls.setup({
 sources = {
 -- Ajoutez ici vos sources, par exemple :
 null_ls.builtins.formatting.prettier,
 null_ls.builtins.diagnostics.eslint,
 -- etc.
 },
})

Assurez-vous que les dépendances externes pour vos sources sont bien installées (comme prettier, eslint, etc. si vous les utilisez).
Vérifiez les conflits possibles avec d'autres plugins LSP.
Essayez de recharger votre configuration Neovim avec :source % si vous êtes dans votre fichier de configuration, ou redémarrez complètement Neovim.
Si le problème persiste, vous pourriez avoir besoin de mettre à jour none-ls.nvim et ses dépendances.

L'erreur spécifique que vous avez partagée indique un problème interne dans le client none-ls, ce qui pourrait être dû à une initialisation incorrecte ou à un bug dans le plugin lui-même.
Si vous partagez votre configuration actuelle de none-ls.nvim, je pourrais vous aider à identifier le problème plus précisément.

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-103-R103-Vois-vous-avez-exécuté-commande]]
- ⬇️ Next: [[Card-105-R105-Lualocal-require-null-setup-sources]]
- 📊 MOC: [[_MOC_Neovim Error with null-ls Plugin]]
