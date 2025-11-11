---
type: chat-card
parent_export: '[[Export]]'
order: 220
role: assistant
created: '2025-11-11T01:06:56.264509Z'
tags:
- chat-card
- code
attachments_count: 0
---

# 🤖 Message 220 - Assistant

**ID:** msg-220

## 💬 Content


**ID:** msg-220

luavim.api.nvim_create_autocmd(\"VimEnter\", {
 callback = function()
 vim.g.clipboard = {
 name = 'WslClipboard',
 copy = {
 ['+'] = 'win32yank.exe -i --crlf',
 ['*'] = 'win32yank.exe -i --crlf',
 },
 paste = {
 ['+'] = 'win32yank.exe -o --lf',
 ['*'] = 'win32yank.exe -o --lf',
 },
 cache_enabled = 0,
 }
 end
})

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-219-R219-Force-APRÈS-tout-reste-schedule]]
- ⬇️ Next: [[Card-221-R221-Print-inspect-clipboard]]
- 📊 MOC: [[_MOC_Slow copy-paste in terminal]]

## 🏷️ Topics

- #code
