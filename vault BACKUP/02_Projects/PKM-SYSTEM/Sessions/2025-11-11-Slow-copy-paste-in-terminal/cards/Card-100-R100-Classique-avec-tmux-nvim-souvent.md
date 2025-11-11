---
type: chat-card
parent_export: '[[Export]]'
order: 100
role: assistant
created: '2025-11-11T01:06:55.079260Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 100 - Assistant

**ID:** msg-100

## 💬 Content


**ID:** msg-100

Ah oui, classique avec WSL + tmux + nvim ! C'est souvent le bracketed paste mode qui ralentit tout. Voici les fixes rapides :
1. Dans nvim - Désactiver bracketed paste
Ajoute dans ton ~/.config/nvim/init.vim (ou init.lua) :
vim\" Pour init.vim
set t_BE=
ou
lua-- Pour init.lua
vim.opt.t_BE = \"\"
2. Dans tmux - Optimiser le paste
Dans ton ~/.tmux.conf :
bash# Désactiver le délai d'escape (souvent la vraie cause)
set -s escape-time 0

# Augmenter la taille du buffer
set-option -g history-limit 50000

# Optionnel: désactiver bracketed paste si ça ne suffit pas
set -g set-clipboard off
Puis recharge : tmux source ~/.tmux.conf
3. Solution rapide pour les gros textes
Quand tu dois coller un gros bloc, utilise plutôt :

:set paste avant de coller dans nvim (désactive l'auto-indent)
:set nopaste après
Ou mieux : utilise \"+p pour coller directement depuis le clipboard système

4. Si ça lag toujours
Le vrai coupable est souvent WSL qui synchronise le clipboard. Essaie :
bash# Dans ton .bashrc ou .zshrc
export DISPLAY=:0
Quick test : redémarre tmux complètement (tmux kill-server) et réessaie.
Dis-moi laquelle de ces solutions fonctionne pour toi et on ajuste si besoin ! 🚀

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-099-R099-Utilisateur-problème-performance-quand-f]]
- ⬇️ Next: [[Card-101-R101-Pour-init]]
- 📊 MOC: [[_MOC_Slow copy-paste in terminal]]
