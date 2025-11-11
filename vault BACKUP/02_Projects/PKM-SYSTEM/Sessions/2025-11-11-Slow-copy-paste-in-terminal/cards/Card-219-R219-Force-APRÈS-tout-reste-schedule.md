---
type: chat-card
parent_export: '[[Export]]'
order: 219
role: assistant
created: '2025-11-11T01:06:56.253869Z'
tags:
- chat-card
- code
attachments_count: 0
---

# 🤖 Message 219 - Assistant

**ID:** msg-219

## 💬 Content


**ID:** msg-219

lua-- Force win32yank APRÈS tout le reste
vim.schedule(function()
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
end)

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-218-R218-Config-écrasée-probablement-plugin-faut]]
- ⬇️ Next: [[Card-220-R220-Luavim-VimEnter-callback-function-clipbo]]
- 📊 MOC: [[_MOC_Slow copy-paste in terminal]]

## 🏷️ Topics

- #code
