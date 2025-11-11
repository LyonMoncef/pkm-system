---
type: chat-card
parent_export: '[[Export]]'
order: 140
role: assistant
created: '2025-11-11T01:06:55.451424Z'
tags:
- chat-card
- git
attachments_count: 0
---

# 🤖 Message 140 - Assistant

**ID:** msg-140

## 💬 Content


**ID:** msg-140

Ah oui, le clipboard n'est pas synchronisé entre Windows et WSL ! Il faut installer win32yank :
Solution : win32yank pour WSL
bash# Télécharge win32yank
curl -sLo /tmp/win32yank.zip https://github.com/equalsraf/win32yank/releases/download/v0.1.1/win32yank-x64.zip

# Extrait et installe
sudo unzip -p /tmp/win32yank.zip win32yank.exe > /usr/local/bin/win32yank.exe
sudo chmod +x /usr/local/bin/win32yank.exe
Puis dans ton ~/.config/nvim/init.lua, ajoute :
lua-- Configuration clipboard pour WSL
if vim.fn.has('wsl') == 1 then
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
Redémarre Neovim et teste :

Copie du texte dans Windows (navigateur, etc.)
Dans Neovim en mode normal : \"+p
Ça devrait coller instantanément !

Alternative rapide : Si tu veux pas installer win32yank tout de suite, utilise temporairement :
bash# En mode insertion dans Neovim, fais :
Ctrl+Shift+V
Mais avec le fix tmux (set -s escape-time 0) ça devrait déjà être beaucoup plus rapide qu'avant.
Teste et dis-moi ! 🚀

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-139-R139-Utilisateur-registre-vide-problème-class]]
- ⬇️ Next: [[Card-141-R141-Bash-Télécharge-curl-https-github]]
- 📊 MOC: [[_MOC_Slow copy-paste in terminal]]

## 🏷️ Topics

- #git
