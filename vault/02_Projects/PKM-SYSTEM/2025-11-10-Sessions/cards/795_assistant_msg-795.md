---
type: chat-card
parent_export: '[[Export]]'
order: 795
role: assistant
created: '2025-11-10T03:56:38.375822Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 795 - Assistant

**ID:** msg-795

## 💬 Content


**ID:** msg-795

Ah ! Le problème est clair maintenant !
Dans capture.html, il y a un listener qui RELAY certains raccourcis au parent via postMessage, mais il ne relay QUE Ctrl+1/2/3/B.
Donc quand l'utilisateur est focused dans l'iframe capture.html (ce qui est le cas par défaut puisque le textarea a l'auto-focus), les raccourcis F1, Ctrl+/, etc. sont captés par l'iframe mais PAS relayés au parent app.html.
C'est pour ça que:

Ctrl+1/2/3 marchent → Ils sont relayés
F1/Ctrl+/ ne marchent pas → Ils ne sont PAS relayés

Solution: Ajouter F1 (et les autres raccourcis help) à la liste des raccourcis relayés dans capture.html, hub.html, et reference.html.
OU mieux encore: Relay TOUS les raccourcis sauf ceux qui sont gérés localement (Esc, Ctrl+I, Ctrl+S, Ctrl+K).

---


## 🔗 Navigation

- ⬆️ Previous: [[794_assistant_msg-794]]
- ⬇️ Next: [[796_assistant_msg-796]]
- 📊 MOC: [[_MOC_French chat message instructions]]
