---
type: chat-card
parent_export: '[[Export]]'
order: 93
role: assistant
created: '2025-11-10T04:27:17.579717Z'
tags:
- chat-card
- git
attachments_count: 0
---

# 🤖 Message 93 - Assistant

**ID:** msg-93

## 💬 Content

\n\n**ID:** msg-93\n\nParfait ! Voici comment installer FiraCode Nerd Font :\nInstallation\nSur macOS :\nbashbrew tap homebrew/cask-fonts\nbrew install --cask font-fira-code-nerd-font\nSur Linux :\nbash# Créer le dossier des polices\nmkdir -p ~/.local/share/fonts\n\n# Télécharger FiraCode Nerd Font\ncd ~/.local/share/fonts\nwget https://github.com/ryanoasis/nerd-fonts/releases/download/v3.1.1/FiraCode.zip\n\n# Décompresser et nettoyer\nunzip FiraCode.zip\nrm FiraCode.zip\n\n# Rafraîchir le cache\nfc-cache -fv\nConfiguration du terminal\niTerm2 :\n\n⌘, → Profiles → Text → Font → \"FiraCode Nerd Font\"\n\nAlacritty :\nyamlfont:\n  normal:\n    family: \"FiraCode Nerd Font\"\n  size: 12.0\nAutres terminaux :\nCherche \"FiraCode Nerd Font\" ou \"FiraMono Nerd Font\" dans les paramètres de police.\nAprès avoir changé la police dans ton terminal, relance tmux ou détache/rattache ta session :\nbashtmux detach  # Ctrl+b puis d\ntmux attach\nÇa devrait afficher les icônes correctement ! 🎯Réessayer\n\n---\n\n

## 🔗 Navigation

- ⬆️ Previous: [[092_assistant_msg-92]]
- ⬇️ Next: [[094_assistant_msg-94]]
- 📊 MOC: [[_MOC_Tmux icons missing]]

## 🏷️ Topics

- #git
