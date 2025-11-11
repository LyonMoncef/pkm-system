---
type: chat-card
parent_export: '[[Export]]'
order: 86
role: assistant
created: '2025-11-11T00:45:56.034772Z'
tags:
- chat-card
- git
attachments_count: 0
---

# 🤖 Message 86 - Assistant

**ID:** msg-86

## 💬 Content


**ID:** msg-86

Pas de souci ! Pour les icônes dans tmux, tu as probablement besoin d'une Nerd Font. Voici comment réinstaller :
Installation rapide
Sur macOS :
bashbrew tap homebrew/cask-fonts
brew install --cask font-hack-nerd-font
Sur Linux :
bash# Créer le dossier des polices si nécessaire
mkdir -p ~/.local/share/fonts

# Télécharger et installer (exemple avec Hack Nerd Font)
cd ~/.local/share/fonts
curl -fLo \"Hack Bold Nerd Font Complete.ttf\" \\
 https://github.com/ryanoasis/nerd-fonts/raw/master/patched-fonts/Hack/Bold/HackNerdFont-Bold.ttf

# Rafraîchir le cache des polices
fc-cache -fv
Configuration du terminal
Après l'installation, tu dois configurer ton terminal pour utiliser cette police :

iTerm2 : Preferences → Profiles → Text → Font → \"Hack Nerd Font\"
Terminal.app : Préférences → Profils → Police
Alacritty : Dans ~/.config/alacritty/alacritty.yml

yaml font:
 normal:
 family: \"Hack Nerd Font\"
Autres Nerd Fonts populaires
Si Hack ne te plaît pas :

FiraCode Nerd Font
JetBrainsMono Nerd Font
Meslo Nerd Font

Tu te souviens quelle police tu utilisais avant ? Ou tu veux juste repartir avec Hack ?

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-085-R085-Souci-Pour-icônes-dans-tmux]]
- ⬇️ Next: [[Card-087-R087-Bashbrew-homebrew-cask-fonts-brew]]
- 📊 MOC: [[_MOC_Tmux icons missing]]

## 🏷️ Topics

- #git
