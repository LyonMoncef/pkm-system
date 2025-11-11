---
type: chat-card
parent_export: '[[Export]]'
order: 105
role: assistant
created: '2025-11-11T00:45:56.200169Z'
tags:
- chat-card
- git
attachments_count: 0
---

# 🤖 Message 105 - Assistant

**ID:** msg-105

## 💬 Content


**ID:** msg-105

Ah ok, il faut probablement installer la police complète avec tous les glyphes. Essaie ça :
Installation complète de FiraCode Nerd Font
Sur macOS :
bash# Désinstalle l'ancienne version
brew uninstall --cask font-fira-code-nerd-font

# Réinstalle
brew install --cask font-fira-code-nerd-font

# Ou installe toutes les variantes
brew install --cask font-fira-mono-nerd-font
Sur Linux :
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
Vérification
Après installation, ferme complètement ton terminal (pas juste la fenêtre, quitte l'app) et rouvre-le.
Dans les paramètres de ton terminal, assure-toi de sélectionner :

\"FiraCode Nerd Font Mono\" (pas juste \"FiraCode\")
ou \"FiraMono Nerd Font\"

Test rapide
Dans ton terminal, tape ça pour tester les icônes :
bashecho -e \"\\ue0b0 \\ue0b2 \\uf09b \\uf269 \\uf31b\"
Tu devrais voir des triangles et des icônes. Si ça affiche des carrés ou des \"?\", c'est que la police n'est pas bien configurée dans le terminal.
C'est quel terminal que tu utilises ? (iTerm2, Terminal.app, Alacritty, autre ?)Réessayer

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-104-S104-ID-msg-104]]
- ⬇️ Next: [[Card-106-R106-Faut-probablement-installer-police-compl]]
- 📊 MOC: [[_MOC_Tmux icons missing]]

## 🏷️ Topics

- #git
