---
type: chat-card
parent_export: '[[Export]]'
order: 134
role: assistant
created: '2025-11-10T21:08:50.840350Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 134 - Assistant

**ID:** msg-134

## 💬 Content


**ID:** msg-134

MFcomment on utilise ce plugin ?
return {
 'yetone/avante.nvim',
 event = 'VeryLazy',
 build = 'make',
 opts = {
 provider = 'claude',
 claude = {
 endpoint = os.getenv 'AVANTE_ANTHROPIC_ENDPOINT' or 'https://api.anthropic.com',
 model = 'claude-3-5-sonnet-20240620',
 timeout = 30000, -- Timeout in milliseconds
 temperature = 0,
 max_tokens = 4096,
 },
 openai = {
 endpoint = os.getenv 'AVANTE_OPENAI_ENDPOINT' or 'https://api.openai.com/v1',
 model = 'gpt-4o',
 timeout = 30000, -- Timeout in milliseconds
 temperature = 0,
 max_tokens = 4096,
 },
 },
 dependencies = {
 'nvim-tree/nvim-web-devicons',
 'stevearc/dressing.nvim',
 'nvim-lua/plenary.nvim',
 'MunifTanjim/nui.nvim',
 --- The below dependencies are optional,
 'echasnovski/mini.pick', -- for file_selector provider mini.pick
 'nvim-telescope/telescope.nvim', -- for file_selector provider telescope
 'hrsh7th/nvim-cmp', -- autocompletion for avante commands and mentions
 'ibhagwan/fzf-lua', -- for file_selector provider fzf
 'nvim-tree/nvim-web-devicons', -- or echasnovski/mini.icons
 'zbirenbaum/copilot.lua', -- for providers='copilot'
 {
 -- support for image pasting
 'HakonHarnes/img-clip.nvim',
 event = 'VeryLazy',
 opts = {
 -- recommended settings
 default = {
 embed_image_as_base64 = false,
 prompt_for_file_name = false,
 drag_and_drop = {
 insert_mode = true,
 },
 -- required for Windows users
 use_absolute_path = true,
 },
 },
 },
 },
}Afficher plus

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-133-R133-Dans-fichier-raccourcis-clavier-sont]]
- ⬇️ Next: [[Card-135-R135-MFcomment-utilise-plugin-return-yetone]]
- 📊 MOC: [[_MOC_Configuring Quarto.lua Plugin for Neovim Jupyter Notebook Simulation]]
