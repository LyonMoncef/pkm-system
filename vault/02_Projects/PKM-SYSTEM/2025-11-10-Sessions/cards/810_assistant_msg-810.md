---
type: chat-card
parent_export: '[[Export]]'
order: 810
role: assistant
created: '2025-11-10T03:56:38.535820Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 810 - Assistant

**ID:** msg-810

## 💬 Content


**ID:** msg-810

Bonne idée ! Le problème c'est peut-être que :

Le global shortcut en main.js capte F1
Mais l'event ne se propage pas jusqu'à l'iframe
Ou l'iframe ne reçoit jamais l'event parce qu'il est déjà intercepté au niveau OS

Testons avec des raccourcis complètement vierges qui n'existent nulle part pour isoler le problème.
Je vais suggérer :

Ctrl+Shift+K (pas utilisé)
Ctrl+Shift+P (pas utilisé)
F12 (pas utilisé normalement)

Et on les ajoute UNIQUEMENT dans app.html en internal (Layer 2) pour voir si ça marche.

---


## 🔗 Navigation

- ⬆️ Previous: [[809_assistant_msg-809]]
- ⬇️ Next: [[811_assistant_msg-811]]
- 📊 MOC: [[_MOC_French chat message instructions]]
