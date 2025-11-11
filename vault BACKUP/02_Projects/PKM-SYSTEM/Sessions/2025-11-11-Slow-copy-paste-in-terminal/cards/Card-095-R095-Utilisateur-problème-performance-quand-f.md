---
type: chat-card
parent_export: '[[Export]]'
order: 95
role: assistant
created: '2025-11-11T01:06:55.036989Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 95 - Assistant

**ID:** msg-95

## 💬 Content


**ID:** msg-95

L'utilisateur a un problème de performance quand il fait copier-coller depuis son navigateur vers son terminal. Il utilise nvim dans tmux sous Ubuntu sous WSL. Le problème semble être lié à la taille du texte copié - plus c'est long, plus c'est lent, et parfois le texte n'est même pas collé en entier.
Il mentionne que sa config tmux et nvim gère le presse-papiers quelque part, et il pense que c'est un problème de taille de cache/tampon.
C'est un problème classique avec WSL + tmux + nvim. Il y a plusieurs causes possibles:

Le bracketed paste mode qui peut ralentir les gros collages
La synchronisation du clipboard entre Windows et WSL
Les plugins vim/nvim qui interceptent le paste
La taille du buffer tmux

Je devrais lui donner des solutions concrètes et rapides pour régler ce problème. Pas besoin de chercher sur le web pour ça, c'est un problème technique connu.
Voici les solutions principales:

Désactiver bracketed paste dans nvim
Ajuster les settings tmux
Utiliser un paste plus direct

Je vais lui donner des solutions pratiques et directes.

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-094-R094-Diagnosed-clipboard-bottleneck-across-tm]]
- ⬇️ Next: [[Card-096-R096-Utilisateur-problème-performance-quand-f]]
- 📊 MOC: [[_MOC_Slow copy-paste in terminal]]
