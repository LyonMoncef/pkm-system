---
type: chat-card
parent_export: '[[Export]]'
order: 109
role: assistant
created: '2025-11-11T00:45:56.239010Z'
tags:
- chat-card
- git
attachments_count: 0
---

# 🤖 Message 109 - Assistant

**ID:** msg-109

## 💬 Content


**ID:** msg-109

bash# Télécharge depuis le dépôt officiel
cd /tmp
wget https://github.com/ryanoasis/nerd-fonts/releases/latest/download/FiraCode.zip
unzip FiraCode.zip -d FiraCode

# Copie toutes les variantes
mkdir -p ~/.local/share/fonts
cp FiraCode/*.ttf ~/.local/share/fonts/

# Rafraîchir
fc-cache -fv

# Nettoyer
rm -rf FiraCode FiraCode.zip

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-108-R108-Bash-Désinstalle-ancienne-version-brew]]
- ⬇️ Next: [[Card-110-R110-Bashecho]]
- 📊 MOC: [[_MOC_Tmux icons missing]]

## 🏷️ Topics

- #git
