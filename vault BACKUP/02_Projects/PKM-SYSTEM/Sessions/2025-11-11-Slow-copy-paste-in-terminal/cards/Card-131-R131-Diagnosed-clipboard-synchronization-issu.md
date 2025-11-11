---
type: chat-card
parent_export: '[[Export]]'
order: 131
role: assistant
created: '2025-11-11T01:06:55.354518Z'
tags:
- chat-card
- git
attachments_count: 0
---

# 🤖 Message 131 - Assistant

**ID:** msg-131

## 💬 Content


**ID:** msg-131

Diagnosed WSL clipboard synchronization issue, identified win32yank solution.L'utilisateur dit que le registre \"+ est vide. C'est un problème classique avec WSL - le clipboard n'est pas synchronisé entre Windows et Neovim dans WSL.
Il faut :

Vérifier si xsel/wl-clipboard est installé
Vérifier si win32yank est installé (c'est LA solution pour WSL)
Configurer Neovim pour utiliser win32yank

win32yank est l'outil qui permet de faire le pont entre le clipboard Windows et WSL.Ah oui, le clipboard n'est pas synchronisé entre Windows et WSL ! Il faut installer win32yank :
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

- ⬆️ Previous: [[Card-130-R130-Diagnosed-clipboard-synchronization-issu]]
- ⬇️ Next: [[Card-132-R132-Diagnosed-clipboard-synchronization-issu]]
- 📊 MOC: [[_MOC_Slow copy-paste in terminal]]

## 🏷️ Topics

- #git
