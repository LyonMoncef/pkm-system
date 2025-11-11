---
type: chat-card
parent_export: '[[Export]]'
order: 162
role: assistant
created: '2025-11-11T00:45:56.732349Z'
tags:
- chat-card
- git
attachments_count: 0
---

# 🤖 Message 162 - Assistant

**ID:** msg-162

## 💬 Content


**ID:** msg-162

Pas de souci ! Tes alias ne sont probablement pas dans .zshrc directement. Selon ta config Oh My Zsh, ils devraient être dans un fichier séparé.
Recherche des alias
1. Cherche dans les fichiers custom Oh My Zsh :
bash# Cherche tous les fichiers .zsh dans le dossier custom
ls -la ~/.oh-my-zsh/custom/*.zsh

# Affiche le contenu de chaque fichier
cat ~/.oh-my-zsh/custom/*.zsh
2. Cherche dans les fichiers de config courants :
bash# Vérifie ces fichiers
cat ~/.zsh_aliases 2>/dev/null
cat ~/.aliases 2>/dev/null
cat ~/.bash_aliases 2>/dev/null
3. Recherche globale de tes alias :
bash# Cherche tous les alias définis
grep -r \"^alias\" ~ --include=\"*.zsh\" --include=\"*.sh\" 2>/dev/null | grep -v \".oh-my-zsh/plugins\"
4. Vérifie les alias actuellement chargés :
bash# Liste tous les alias actifs dans ta session
alias
Où les mettre ?
Selon ta config, tu devrais les mettre dans :
bash# Crée ou édite ce fichier
nvim ~/.oh-my-zsh/custom/aliases.zsh
Exemple :
bashalias ll='ls -alh'
alias v='nvim'
alias gs='git status'
Puis recharge :
bashsource ~/.zshrc
Dis-moi ce que tu trouves avec ces commandes ! On va les retrouver 👍

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-161-R161-Souci-alias-sont-probablement-dans]]
- ⬇️ Next: [[Card-163-R163-Bash-Cherche-tous-fichiers-dans]]
- 📊 MOC: [[_MOC_Tmux icons missing]]

## 🏷️ Topics

- #git
