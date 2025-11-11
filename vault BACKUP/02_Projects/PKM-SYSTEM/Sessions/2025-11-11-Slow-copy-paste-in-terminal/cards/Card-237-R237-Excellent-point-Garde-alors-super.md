---
type: chat-card
parent_export: '[[Export]]'
order: 237
role: assistant
created: '2025-11-11T01:06:56.451682Z'
tags:
- chat-card
- excel
attachments_count: 0
---

# 🤖 Message 237 - Assistant

**ID:** msg-237

## 💬 Content


**ID:** msg-237

Ah excellent point ! Garde OSC52 alors, c'est super pratique.
Le vrai problème c'est le PASTE qui est lent, pas le copy. Donc :
Solution : Garde OSC52 + Fix tmux uniquement

Enlève la config win32yank de ton init.lua (garde OSC52)
Vérifie que tu as bien mis ça dans ton ~/.tmux.conf :

bashset -s escape-time 0
set -g history-limit 50000

Redémarre tmux complètement :

bashtmux kill-server
# Puis relance tmux

Teste : copie un gros bloc de texte depuis Windows et colle avec Ctrl+Shift+V dans nvim

Ça devrait être beaucoup plus rapide maintenant. Le escape-time 0 est la clé.
Si c'est encore lent
Le problème vient peut-être du terminal Windows. Tu utilises quoi ? Windows Terminal, WSL natif, autre ?
Dans Windows Terminal, vérifie dans les paramètres que tu n'as pas un énorme historique qui ralentit tout.
Teste déjà avec le fix tmux et dis-moi ! 🚀

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-236-R236-Excellent-point-utilisateur-raison-très]]
- ⬇️ Next: [[Card-238-R238-Bashset-escape-time-history-limit]]
- 📊 MOC: [[_MOC_Slow copy-paste in terminal]]

## 🏷️ Topics

- #excel
