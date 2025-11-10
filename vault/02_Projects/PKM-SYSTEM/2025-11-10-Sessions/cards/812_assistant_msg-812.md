---
type: chat-card
parent_export: '[[Export]]'
order: 812
role: assistant
created: '2025-11-10T03:56:38.557269Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 812 - Assistant

**ID:** msg-812

## 💬 Content


**ID:** msg-812

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

- ⬆️ Previous: [[811_assistant_msg-811]]
- ⬇️ Next: [[813_assistant_msg-813]]
- 📊 MOC: [[_MOC_French chat message instructions]]
