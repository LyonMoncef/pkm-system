---
type: chat-card
parent_export: '[[Export]]'
order: 135
role: assistant
created: '2025-11-11T01:06:55.400546Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 135 - Assistant

**ID:** msg-135

## 💬 Content


**ID:** msg-135

L'utilisateur dit que le registre \"+ est vide. C'est un problème classique avec WSL - le clipboard n'est pas synchronisé entre Windows et Neovim dans WSL.
Il faut :

Vérifier si xsel/wl-clipboard est installé
Vérifier si win32yank est installé (c'est LA solution pour WSL)
Configurer Neovim pour utiliser win32yank

win32yank est l'outil qui permet de faire le pont entre le clipboard Windows et WSL.

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-134-R134-Diagnosed-clipboard-synchronization-issu]]
- ⬇️ Next: [[Card-136-R136-Utilisateur-registre-vide-problème-class]]
- 📊 MOC: [[_MOC_Slow copy-paste in terminal]]
