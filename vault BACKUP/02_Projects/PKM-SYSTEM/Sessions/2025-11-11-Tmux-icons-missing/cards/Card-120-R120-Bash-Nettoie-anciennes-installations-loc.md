---
type: chat-card
parent_export: '[[Export]]'
order: 120
role: assistant
created: '2025-11-11T00:45:56.338438Z'
tags:
- chat-card
- git
attachments_count: 0
---

# 🤖 Message 120 - Assistant

**ID:** msg-120

## 💬 Content


**ID:** msg-120

bash# Nettoie les anciennes installations
rm -rf ~/.local/share/fonts/Fira*

# Télécharge JetBrainsMono Nerd Font (version complète)
cd /tmp
wget https://github.com/ryanoasis/nerd-fonts/releases/latest/download/JetBrainsMono.zip

# Extrait et installe
unzip JetBrainsMono.zip -d JetBrainsMono
mkdir -p ~/.local/share/fonts
cp JetBrainsMono/*.ttf ~/.local/share/fonts/

# Rafraîchit le cache
fc-cache -fv

# Nettoie
rm -rf JetBrainsMono JetBrainsMono.zip

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-119-R119-Bash-Nettoie-anciennes-polices-Nerd]]
- ⬇️ Next: [[Card-121-R121-Yamlfont-normal-family-JetBrainsMono-Ner]]
- 📊 MOC: [[_MOC_Tmux icons missing]]

## 🏷️ Topics

- #git
