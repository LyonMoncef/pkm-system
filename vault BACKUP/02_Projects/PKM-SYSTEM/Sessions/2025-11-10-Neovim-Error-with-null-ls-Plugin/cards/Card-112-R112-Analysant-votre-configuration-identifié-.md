---
type: chat-card
parent_export: '[[Export]]'
order: 112
role: assistant
created: '2025-11-10T21:42:07.902800Z'
tags:
- chat-card
- obsidian
attachments_count: 0
---

# 🤖 Message 112 - Assistant

**ID:** msg-112

## 💬 Content


**ID:** msg-112

En analysant votre configuration, j'ai identifié un problème potentiel qui pourrait causer l'erreur que vous rencontrez. Voici ce que j'ai remarqué :

Vous importez les formateurs Ruff d'une manière qui semble incorrecte :

luarequire('none-ls.formatting.ruff').with { extra_args = { '--extend-select', 'I' } },
require 'none-ls.formatting.ruff_format',
La structure correcte pour importer des sources depuis none-ls-extras serait plutôt :
luarequire('none-ls-extras.formatting.ruff').with { extra_args = { '--extend-select', 'I' } },
require('none-ls-extras.formatting.ruff_format'),
Notez que vous devez utiliser none-ls-extras au lieu de none-ls pour ces sources spécifiques.

Assurez-vous que les versions de vos plugins sont compatibles entre elles. Le plugin mason-null-ls.nvim a été conçu pour null-ls original et pourrait ne pas être entièrement compatible avec none-ls.
Pour résoudre votre problème :

lua-- Modifiez les lignes problématiques
local sources = {
 diagnostics.checkmake,
 formatting.prettier.with { filetypes = { 'html', 'json', 'yaml', 'markdown' } },
 formatting.stylua,
 formatting.shfmt.with { args = { '-i', '4' } },
 formatting.terraform_fmt,
 -- Utilisez la structure correcte pour none-ls-extras
 require('none-ls-extras.formatting.ruff').with { extra_args = { '--extend-select', 'I' } },
 require('none-ls-extras.formatting.ruff_format'),
}

Activez le mode debug pour obtenir plus d'informations :

luanull_ls.setup {
 debug = true, -- Décommentez cette ligne
 sources = sources,
 -- reste de votre configuration
}

Vérifiez également si terraform_fmt est bien disponible dans les formateurs intégrés de none-ls. Si ce n'est pas le cas, vous devrez peut-être l'importer d'une manière différente ou l'installer séparément.

Après avoir effectué ces modifications, redémarrez Neovim et vérifiez si l'erreur persiste. Vous pouvez également consulter les logs avec :NullLsLog pour obtenir plus d'informations sur le problème.

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-111-R111-Analysant-votre-configuration-identifié-]]
- ⬇️ Next: [[Card-113-R113-Analysant-votre-configuration-identifié-]]
- 📊 MOC: [[_MOC_Neovim Error with null-ls Plugin]]

## 🏷️ Topics

- #obsidian
