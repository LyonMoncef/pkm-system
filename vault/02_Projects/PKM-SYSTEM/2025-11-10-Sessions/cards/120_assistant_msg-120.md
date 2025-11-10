---
type: chat-card
parent_export: '[[Export]]'
order: 120
role: assistant
created: '2025-11-10T04:27:17.776185Z'
tags:
- chat-card
- git
attachments_count: 0
---

# 🤖 Message 120 - Assistant

**ID:** msg-120

## 💬 Content

\n\n**ID:** msg-120\n\nbash# Nettoie les anciennes installations\nrm -rf ~/.local/share/fonts/Fira*\n\n# Télécharge JetBrainsMono Nerd Font (version complète)\ncd /tmp\nwget https://github.com/ryanoasis/nerd-fonts/releases/latest/download/JetBrainsMono.zip\n\n# Extrait et installe\nunzip JetBrainsMono.zip -d JetBrainsMono\nmkdir -p ~/.local/share/fonts\ncp JetBrainsMono/*.ttf ~/.local/share/fonts/\n\n# Rafraîchit le cache\nfc-cache -fv\n\n# Nettoie\nrm -rf JetBrainsMono JetBrainsMono.zip\n\n---\n\n

## 🔗 Navigation

- ⬆️ Previous: [[119_assistant_msg-119]]
- ⬇️ Next: [[121_assistant_msg-121]]
- 📊 MOC: [[_MOC_Tmux icons missing]]

## 🏷️ Topics

- #git
