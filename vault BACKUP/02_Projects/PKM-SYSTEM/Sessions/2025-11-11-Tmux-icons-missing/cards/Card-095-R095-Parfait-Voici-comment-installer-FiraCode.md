---
type: chat-card
parent_export: '[[Export]]'
order: 95
role: assistant
created: '2025-11-11T00:45:56.112412Z'
tags:
- chat-card
- git
attachments_count: 0
---

# 🤖 Message 95 - Assistant

**ID:** msg-95

## 💬 Content


**ID:** msg-95

Parfait ! Voici comment installer FiraCode Nerd Font :
Installation
Sur macOS :
bashbrew tap homebrew/cask-fonts
brew install --cask font-fira-code-nerd-font
Sur Linux :
bash# Créer le dossier des polices
mkdir -p ~/.local/share/fonts

# Télécharger FiraCode Nerd Font
cd ~/.local/share/fonts
wget https://github.com/ryanoasis/nerd-fonts/releases/download/v3.1.1/FiraCode.zip

# Décompresser et nettoyer
unzip FiraCode.zip
rm FiraCode.zip

# Rafraîchir le cache
fc-cache -fv
Configuration du terminal
iTerm2 :

⌘, → Profiles → Text → Font → \"FiraCode Nerd Font\"

Alacritty :
yamlfont:
 normal:
 family: \"FiraCode Nerd Font\"
 size: 12.0
Autres terminaux :
Cherche \"FiraCode Nerd Font\" ou \"FiraMono Nerd Font\" dans les paramètres de police.
Après avoir changé la police dans ton terminal, relance tmux ou détache/rattache ta session :
bashtmux detach # Ctrl+b puis d
tmux attach
Ça devrait afficher les icônes correctement ! 🎯

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-094-R094-Parfait-Voici-comment-installer-FiraCode]]
- ⬇️ Next: [[Card-096-R096-Bashbrew-homebrew-cask-fonts-brew]]
- 📊 MOC: [[_MOC_Tmux icons missing]]

## 🏷️ Topics

- #git
