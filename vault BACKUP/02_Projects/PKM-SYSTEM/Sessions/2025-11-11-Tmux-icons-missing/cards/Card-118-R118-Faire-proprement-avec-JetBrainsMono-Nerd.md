---
type: chat-card
parent_export: '[[Export]]'
order: 118
role: assistant
created: '2025-11-11T00:45:56.321271Z'
tags:
- chat-card
- python
- code
- git
attachments_count: 0
---

# 🤖 Message 118 - Assistant

**ID:** msg-118

## 💬 Content


**ID:** msg-118

Ok, on va faire ça proprement avec JetBrainsMono Nerd Font - installation complète !
Installation complète
Sur macOS :
bash# Nettoie les anciennes polices Nerd Font si besoin
brew uninstall --cask font-fira-code-nerd-font 2>/dev/null
brew uninstall --cask font-fira-mono-nerd-font 2>/dev/null

# Installe JetBrainsMono Nerd Font
brew tap homebrew/cask-fonts
brew install --cask font-jetbrains-mono-nerd-font
Sur Linux :
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
Configuration du terminal
IMPORTANT : Ferme complètement ton application terminal (Quit, pas juste fermer la fenêtre)
Puis dans les paramètres :
iTerm2 :

⌘, → Profiles → Text → Font
Sélectionne \"JetBrainsMono Nerd Font Mono\" (pas juste \"JetBrainsMono\")
Taille : 12-14

Alacritty (~/.config/alacritty/alacritty.yml) :
yamlfont:
 normal:
 family: \"JetBrainsMono Nerd Font Mono\"
 size: 13.0
Terminal.app / Gnome Terminal / Autres :
Cherche \"JetBrainsMono Nerd Font Mono\" dans les polices
Test des icônes
Après avoir configuré et relancé ton terminal :
bash# Test complet des icônes
echo -e \"\\ue0b0 \\ue0b2 \\uf09b \\uf269 \\uf31b \\uf419 \\ue77f \\uf489 \\uf013\"
Tu devrais voir : triangles, GitHub, Python, React, Docker, Vim, engrenage, etc.
Relance tmux
bash# Tue toutes les sessions tmux
tmux kill-server

# Relance
tmux
Dis-moi quel OS tu es et quel terminal tu utilises, je t'aide à configurer !

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-117-R117-Faire-proprement-avec-JetBrainsMono-Nerd]]
- ⬇️ Next: [[Card-119-R119-Bash-Nettoie-anciennes-polices-Nerd]]
- 📊 MOC: [[_MOC_Tmux icons missing]]

## 🏷️ Topics

- #python
- #code
- #git
