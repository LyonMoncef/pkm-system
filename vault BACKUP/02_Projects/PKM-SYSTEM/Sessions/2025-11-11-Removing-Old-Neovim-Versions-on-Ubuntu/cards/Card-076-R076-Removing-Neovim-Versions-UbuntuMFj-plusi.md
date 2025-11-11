---
type: chat-card
parent_export: '[[Export]]'
order: 76
role: assistant
created: '2025-11-11T00:40:04.103869Z'
tags:
- chat-card
- python
attachments_count: 0
---

# 🤖 Message 76 - Assistant

**ID:** msg-76

## 💬 Content


**ID:** msg-76

Removing Old Neovim Versions on UbuntuMFj'ai plusieurs instances de nvim d'installées sur mon ubuntu, comment supprimer les anciennes versions ?Pour supprimer les anciennes versions de Neovim (nvim) sur Ubuntu, voici comment procéder :

Vérifiez d'abord les versions installées avec :

 dpkg -l | grep nvim
ou
 which -a nvim

Si vous avez installé Neovim via apt, supprimez-le avec :

 sudo apt remove neovim
 sudo apt purge neovim

Si vous avez installé via snap :

 sudo snap remove neovim

Pour les versions installées manuellement ou via AppImage, localisez-les (souvent dans /usr/local/bin, ~/.local/bin, ou /opt) puis supprimez-les :

 sudo rm /chemin/vers/nvim

N'oubliez pas de nettoyer les configurations si nécessaire :

 rm -rf ~/.config/nvim
 rm -rf ~/.local/share/nvim
Après la suppression, vous pouvez installer une seule version propre via la méthode de votre choix.
Avez-vous installé vos différentes versions de nvim par des méthodes spécifiques ?RéessayerMFFailed to run config for nvim-lspconfig
/home/tats/.config/nvim/lua/plugins/lsp.lua:118: module 'misc.style' not found:
 no field package.preload['misc.style']
 cache_loader: module 'misc.style' not found
 cache_loader_lib: module 'misc.style' not found
 no file './misc/style.lua'
 no file '/tmp/neovim/.deps/usr/share/luajit-2.1/misc/style.lua'
 no file '/usr/local/share/lua/5.1/misc/style.lua'
 no file '/usr/local/share/lua/5.1/misc/style/init.lua'
 no file '/tmp/neovim/.deps/usr/share/lua/5.1/misc/style.lua'
 no file '/tmp/neovim/.deps/usr/share/lua/5.1/misc/style/init.lua'
 no file './misc/style.so'
 no file '/usr/local/lib/lua/5.1/misc/style.so'
 no file '/tmp/neovim/.deps/usr/lib/lua/5.1/misc/style.so'
 no file '/usr/local/lib/lua/5.1/loadall.so'
 no file './misc.so'
 no file '/usr/local/lib/lua/5.1/misc.so'
 no file '/tmp/neovim/.deps/usr/lib/lua/5.1/misc.so'
 no file '/usr/local/lib/lua/5.1/loadall.so'
# stacktrace:
 - nvim/lua/plugins/lsp.lua:118 *in* **config**
 - nvim/init.lua:30Afficher plusIl semble que vous ayez une erreur liée à un module manquant dans votre configuration Neovim. Le message d'erreur indique que le module 'misc.style' n'est pas trouvé, ce qui provoque l'échec du chargement de nvim-lspconfig.
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
Ce problème est probablement lié à une dépendance manquante ou à un changement dans votre structure de plugins plutôt qu'aux multiples versions de nvim. Pouvez-vous me montrer le contenu de la ligne 118 de votre fichier lsp.lua pour que je puisse vous aider plus précisément ?RéessayerMFvim.lsp.handlers['textDocument/hover'] = vim.lsp.with(vim.lsp.handlers.hover, { border = require('misc.style').border })Je vois le problème. La ligne qui cause l'erreur est celle qui essaie d'appliquer un style de bordure personnalisé aux popups LSP en utilisant un module misc.style qui n'existe pas dans votre configuration.
Voici comment vous pouvez résoudre ce problème :

Créez le module manquant :

bash mkdir -p ~/.config/nvim/lua/misc
 touch ~/.config/nvim/lua/misc/style.lua

Ajoutez le contenu suivant dans le fichier style.lua :

lua local M = {}

 -- Style de bordure par défaut
 M.border = \"rounded\" -- Vous pouvez choisir: 'none', 'single', 'double', 'rounded', 'solid', 'shadow'

 return M

Alternativement, si vous préférez ne pas créer ce module, vous pouvez modifier directement votre fichier lsp.lua pour qu'il n'utilise pas ce module manquant :

lua vim.lsp.handlers['textDocument/hover'] = vim.lsp.with(vim.lsp.handlers.hover, { border = \"rounded\" })
Le problème vient du fait que votre configuration essaie d'utiliser un module personnalisé pour les styles qui n'existe pas dans votre installation. Cette erreur n'est pas directement liée aux multiples versions de Neovim, mais plutôt à la configuration de votre instance actuelle.
Préférez-vous créer le module manquant ou simplement modifier la ligne problématique pour utiliser un style de bordure directement?RéessayerMFailed to run config for nvim-lspconfig
/home/tats/.config/nvim/lua/plugins/lsp.lua:120: module 'misc.style' not found:
 no field package.preload['misc.style']
 cache_loader: module 'misc.style' not found
 cache_loader_lib: module 'misc.style' not found
 no file './misc/style.lua'
 no file '/tmp/neovim/.deps/usr/share/luajit-2.1/misc/style.lua'
 no file '/usr/local/share/lua/5.1/misc/style.lua'
 no file '/usr/local/share/lua/5.1/misc/style/init.lua'
 no file '/tmp/neovim/.deps/usr/share/lua/5.1/misc/style.lua'
 no file '/tmp/neovim/.deps/usr/share/lua/5.1/misc/style/init.lua'
 no file '/home/tats/.local/share/nvim/lazy-rocks/nvim-dap-python/share/lua/5.1/misc/style.lua'
 no file '/home/tats/.local/share/nvim/lazy-rocks/nvim-dap-python/share/lua/5.1/misc/style/init.lua'
 no file './misc/style.so'
 no file '/usr/local/lib/lua/5.1/misc/style.so'
 no file '/tmp/neovim/.deps/usr/lib/lua/5.1/misc/style.so'
 no file '/usr/local/lib/lua/5.1/loadall.so'
 no file '/home/tats/.local/share/nvim/lazy-rocks/nvim-dap-python/lib/lua/5.1/misc/style.so'
 no file '/home/tats/.local/share/nvim/lazy-rocks/nvim-dap-python/lib64/lua/5.1/misc/style.so'
 no file './misc.so'
 no file '/usr/local/lib/lua/5.1/misc.so'
 no file '/tmp/neovim/.deps/usr/lib/lua/5.1/misc.so'
 no file '/usr/local/lib/lua/5.1/loadall.so'
 no file '/home/tats/.local/share/nvim/lazy-rocks/nvim-dap-python/lib/lua/5.1/misc.so'
 no file '/home/tats/.local/share/nvim/lazy-rocks/nvim-dap-python/lib64/lua/5.1/misc.so'
# stacktrace:
 - nvim/lua/plugins/lsp.lua:120 *in* **config**
 - nvim/init.lua:30Afficher plusJe vois que l'erreur persiste, mais maintenant à la ligne 120 de votre fichier lsp.lua, toujours liée au module manquant 'misc.style'.
Voici une solution plus complète pour résoudre ce problème :

Créez le module manquant avec tous les chemins nécessaires :

bash mkdir -p ~/.config/nvim/lua/misc

Créez le fichier style.lua dans ce répertoire :

bash nvim ~/.config/nvim/lua/misc/style.lua

Ajoutez ce contenu au fichier :

lua local M = {}

 -- Style de bordure par défaut pour les popups LSP
 M.border = \"rounded\"

 -- Vous pouvez ajouter d'autres styles ici si nécessaire

 return M

Sauvegardez le fichier et redémarrez Neovim.

Si cela ne résout pas le problème, vous pourriez avoir plusieurs utilisations de ce module manquant. Une solution alternative serait de modifier votre fichier lsp.lua pour remplacer toutes les références à 'misc.style' :

Ouvrez votre fichier lsp.lua :

bash nvim ~/.config/nvim/lua/plugins/lsp.lua

Cherchez toutes les occurrences de require('misc.style') et remplacez-les par des valeurs directes. Par exemple, pour la ligne 120 et la ligne 118 précédente :

lua -- Avant :
 vim.lsp.handlers['textDocument/hover'] = vim.lsp.with(vim.lsp.handlers.hover, { border = require('misc.style').border })

 -- Après :
 vim.lsp.handlers['textDocument/hover'] = vim.lsp.with(vim.lsp.handlers.hover, { border = \"rounded\" })
Faites de même pour toutes les autres références à ce module dans votre configuration.RéessayerClaude peut faire des erreurs. Assurez-vous de vérifier ses réponses. Sonnet 4.5Partager

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-075-R075-Moncef-FAFIForfait]]
- ⬇️ Next: [[Card-077-R077-Removing-Neovim-Versions-UbuntuMFj-plusi]]
- 📊 MOC: [[_MOC_Removing Old Neovim Versions on Ubuntu]]

## 🏷️ Topics

- #python
