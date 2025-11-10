---
type: chat-card
parent_export: '[[Export]]'
order: 495
role: assistant
created: '2025-11-10T03:56:34.932946Z'
tags:
- chat-card
- git
- automation
attachments_count: 0
---

# 🤖 Message 495 - Assistant

**ID:** msg-495

## 💬 Content


**ID:** msg-495

🔧 ALIAS comt POUR ZSH

📝 AJOUTER L'ALIAS DANS .zshrc
Ouvre ton fichier de config ZSH :
bashnano ~/.zshrc
Ajoute cette ligne à la fin du fichier :
bash# PKM System - Quick commit alias
comt() {
 git add -A && git commit -m \"${1:-Quick save}\" && git push
}
Sauvegarde et quitte :

Ctrl+O (save)
Enter (confirm)
Ctrl+X (exit)

Recharge la config :
bashsource ~/.zshrc

🚀 USAGE
bash# Commit rapide sans message
comt

# Commit avec message custom
comt \"Fix save behaviors in capture.html\"

# Multi-ligne si besoin
comt \"Major refactor

- Fix shortcuts popup styling
- Implement save behaviors
- Add vim modes\"

✅ VÉRIFIE QUE ÇA MARCHE
bash# Test l'alias
cd ~/Projects/pkm-system
comt \"Test alias comt from zsh\"
Si ça push bien, t'es good ! 💪

📋 BONUS - AUTRES ALIAS UTILES
Si tu veux d'autres alias Git pour ton workflow :
bash# Status rapide
alias gs='git status'

# Log pretty
alias gl='git log --oneline --graph --decorate -10'

# Diff rapide
alias gd='git diff'

# Pull rapide
alias gpl='git pull'

# Annuler dernier commit (garde les changements)
alias gundo='git reset --soft HEAD~1'
Ajoute-les dans ton .zshrc si tu veux ! 🔥

---


## 🔗 Navigation

- ⬆️ Previous: [[494_assistant_msg-494]]
- ⬇️ Next: [[496_assistant_msg-496]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #git
- #automation
