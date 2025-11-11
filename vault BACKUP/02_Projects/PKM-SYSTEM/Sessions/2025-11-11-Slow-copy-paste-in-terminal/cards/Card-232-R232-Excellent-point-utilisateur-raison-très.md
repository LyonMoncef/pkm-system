---
type: chat-card
parent_export: '[[Export]]'
order: 232
role: assistant
created: '2025-11-11T01:06:56.403466Z'
tags:
- chat-card
- excel
attachments_count: 0
---

# 🤖 Message 232 - Assistant

**ID:** msg-232

## 💬 Content


**ID:** msg-232

Ah excellent point ! L'utilisateur a raison - OSC52 est très utile pour copier DEPUIS nvim/tmux vers Windows, surtout en SSH. Le problème c'est juste le PASTE qui est lent.
Donc la vraie solution c'est :

Garder OSC52 pour le COPY (nvim -> Windows)
Utiliser win32yank pour le PASTE (Windows -> nvim)

Ou mieux encore, peut-être que le vrai problème c'est juste le fix tmux qu'on a fait au début. Peut-être qu'avec set -s escape-time 0 dans tmux, le paste normal (Ctrl+Shift+V) va être rapide maintenant ?
Je devrais lui demander s'il a bien appliqué le fix tmux et testé. Parce que si OSC52 fonctionne bien pour lui, peut-être que le problème initial était juste le escape-time de tmux.

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-231-R231-Reconcilié-pour-copie-avec-solution]]
- ⬇️ Next: [[Card-233-R233-Excellent-point-utilisateur-raison-très]]
- 📊 MOC: [[_MOC_Slow copy-paste in terminal]]

## 🏷️ Topics

- #excel
