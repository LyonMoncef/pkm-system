---
type: chat-card
parent_export: '[[Export]]'
order: 774
role: assistant
created: '2025-11-10T03:56:38.117535Z'
tags:
- chat-card
- python
- code
- automation
attachments_count: 0
---

# 🤖 Message 774 - Assistant

**ID:** msg-774

## 💬 Content


**ID:** msg-774

javascriptEsc → Normal mode
Ctrl+I → Insert mode
Ctrl+S → Save
Ctrl+K → Clear
Ctrl+1/2/3/B → Relay to parent
```

---

## 🐛 POURQUOI Ctrl+1/2/3 MARCHENT MAIS PAS F1 ?

**Ctrl+1/2/3 = LAYER 2** (internal)
- Gérés directement dans app.html
- Pas d'IPC → Aucune chaîne à casser

**F1/Ctrl+/ = LAYER 1** (global)
- Nécessitent IPC chain complète
- Si 1 maillon cassé → Tout casse

---

## 🔍 DIAGNOSTIC

**La chaîne IPC est cassée quelque part :**
```
✅ main.js capte F1 → logs OK
✅ main.js envoie IPC 'show-shortcuts'
❓ preload.js expose onShowShortcuts ?
❓ app.html écoute l'IPC ?
❓ showKeyboardHints() existe et marche ?

---


## 🔗 Navigation

- ⬆️ Previous: [[773_assistant_msg-773]]
- ⬇️ Next: [[775_assistant_msg-775]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #code
- #automation
