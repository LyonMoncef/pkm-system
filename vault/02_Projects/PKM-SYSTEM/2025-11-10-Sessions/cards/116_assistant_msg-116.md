---
type: chat-card
parent_export: '[[Export]]'
order: 116
role: assistant
created: '2025-11-10T04:27:17.749330Z'
tags:
- chat-card
- python
- code
- git
attachments_count: 0
---

# 🤖 Message 116 - Assistant

**ID:** msg-116

## 💬 Content

\n\n**ID:** msg-116\n\nOk, on va faire ça proprement avec JetBrainsMono Nerd Font - installation complète !\nInstallation complète\nSur macOS :\nbash# Nettoie les anciennes polices Nerd Font si besoin\nbrew uninstall --cask font-fira-code-nerd-font 2>/dev/null\nbrew uninstall --cask font-fira-mono-nerd-font 2>/dev/null\n\n# Installe JetBrainsMono Nerd Font\nbrew tap homebrew/cask-fonts\nbrew install --cask font-jetbrains-mono-nerd-font\nSur Linux :\nbash# Nettoie les anciennes installations\nrm -rf ~/.local/share/fonts/Fira*\n\n# Télécharge JetBrainsMono Nerd Font (version complète)\ncd /tmp\nwget https://github.com/ryanoasis/nerd-fonts/releases/latest/download/JetBrainsMono.zip\n\n# Extrait et installe\nunzip JetBrainsMono.zip -d JetBrainsMono\nmkdir -p ~/.local/share/fonts\ncp JetBrainsMono/*.ttf ~/.local/share/fonts/\n\n# Rafraîchit le cache\nfc-cache -fv\n\n# Nettoie\nrm -rf JetBrainsMono JetBrainsMono.zip\nConfiguration du terminal\nIMPORTANT : Ferme complètement ton application terminal (Quit, pas juste fermer la fenêtre)\nPuis dans les paramètres :\niTerm2 :\n\n⌘, → Profiles → Text → Font\nSélectionne \"JetBrainsMono Nerd Font Mono\" (pas juste \"JetBrainsMono\")\nTaille : 12-14\n\nAlacritty (~/.config/alacritty/alacritty.yml) :\nyamlfont:\n  normal:\n    family: \"JetBrainsMono Nerd Font Mono\"\n  size: 13.0\nTerminal.app / Gnome Terminal / Autres :\nCherche \"JetBrainsMono Nerd Font Mono\" dans les polices\nTest des icônes\nAprès avoir configuré et relancé ton terminal :\nbash# Test complet des icônes\necho -e \"\\ue0b0 \\ue0b2 \\uf09b \\uf269 \\uf31b \\uf419 \\ue77f \\uf489 \\uf013\"\nTu devrais voir : triangles, GitHub, Python, React, Docker, Vim, engrenage, etc.\nRelance tmux\nbash# Tue toutes les sessions tmux\ntmux kill-server\n\n# Relance\ntmux\nDis-moi quel OS tu es et quel terminal tu utilises, je t'aide à configurer !Réessayer\n\n---\n\n

## 🔗 Navigation

- ⬆️ Previous: [[115_user_msg-115]]
- ⬇️ Next: [[117_assistant_msg-117]]
- 📊 MOC: [[_MOC_Tmux icons missing]]

## 🏷️ Topics

- #python
- #code
- #git
