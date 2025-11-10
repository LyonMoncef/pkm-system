---
type: chat-card
parent_export: '[[Export]]'
order: 160
role: assistant
created: '2025-11-10T04:27:18.012057Z'
tags:
- chat-card
- git
attachments_count: 0
---

# 🤖 Message 160 - Assistant

**ID:** msg-160

## 💬 Content

\n\n**ID:** msg-160\n\nPas de souci ! Tes alias ne sont probablement pas dans .zshrc directement. Selon ta config Oh My Zsh, ils devraient être dans un fichier séparé.\nRecherche des alias\n1. Cherche dans les fichiers custom Oh My Zsh :\nbash# Cherche tous les fichiers .zsh dans le dossier custom\nls -la ~/.oh-my-zsh/custom/*.zsh\n\n# Affiche le contenu de chaque fichier\ncat ~/.oh-my-zsh/custom/*.zsh\n2. Cherche dans les fichiers de config courants :\nbash# Vérifie ces fichiers\ncat ~/.zsh_aliases 2>/dev/null\ncat ~/.aliases 2>/dev/null\ncat ~/.bash_aliases 2>/dev/null\n3. Recherche globale de tes alias :\nbash# Cherche tous les alias définis\ngrep -r \"^alias\" ~ --include=\"*.zsh\" --include=\"*.sh\" 2>/dev/null | grep -v \".oh-my-zsh/plugins\"\n4. Vérifie les alias actuellement chargés :\nbash# Liste tous les alias actifs dans ta session\nalias\nOù les mettre ?\nSelon ta config, tu devrais les mettre dans :\nbash# Crée ou édite ce fichier\nnvim ~/.oh-my-zsh/custom/aliases.zsh\nExemple :\nbashalias ll='ls -alh'\nalias v='nvim'\nalias gs='git status'\nPuis recharge :\nbashsource ~/.zshrc\nDis-moi ce que tu trouves avec ces commandes ! On va les retrouver 👍Réessayer\n\n---\n\n

## 🔗 Navigation

- ⬆️ Previous: [[159_user_msg-159]]
- ⬇️ Next: [[161_assistant_msg-161]]
- 📊 MOC: [[_MOC_Tmux icons missing]]

## 🏷️ Topics

- #git
