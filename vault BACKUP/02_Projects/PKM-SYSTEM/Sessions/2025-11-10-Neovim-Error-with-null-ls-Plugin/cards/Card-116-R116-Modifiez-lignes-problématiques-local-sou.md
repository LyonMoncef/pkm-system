---
type: chat-card
parent_export: '[[Export]]'
order: 116
role: assistant
created: '2025-11-10T21:42:07.993174Z'
tags:
- chat-card
- obsidian
attachments_count: 0
---

# 🤖 Message 116 - Assistant

**ID:** msg-116

## 💬 Content


**ID:** msg-116

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

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-115-R115-Luarequire-none-extras-formatting-ruff]]
- ⬇️ Next: [[Card-117-R117-Setup-debug-true-Décommentez-cette]]
- 📊 MOC: [[_MOC_Neovim Error with null-ls Plugin]]

## 🏷️ Topics

- #obsidian
