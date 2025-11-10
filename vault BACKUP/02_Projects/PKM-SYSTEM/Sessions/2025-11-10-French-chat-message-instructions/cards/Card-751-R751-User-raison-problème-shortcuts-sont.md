---
type: chat-card
parent_export: '[[Export]]'
order: 751
role: assistant
created: '2025-11-10T21:12:15.504323Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 751 - Assistant

**ID:** msg-751

## 💬 Content


**ID:** msg-751

Ah ! Le user a raison. Le problème c'est que:

Les shortcuts sont bien enregistrés dans main.js ✅
Les shortcuts sont bien capturés (on voit les logs) ✅
Mais la popup ne s'affiche pas ❌

Le problème est probablement dans la chaîne IPC:

main.js envoie show-shortcuts via IPC ✅
preload.js doit exposer onShowShortcuts ✅
app.html doit écouter avec window.electronAPI.onShowShortcuts() ❌ (peut-être manquant)
app.html doit appeler showKeyboardHints() ❌ (peut-être la fonction n'existe pas)

Il faut vérifier:

Est-ce que la fonction showKeyboardHints() existe dans app.html ?
Est-ce que le listener IPC est bien connecté ?
Est-ce que le HTML du keyboard hint popup existe dans app.html ?

Le user demande aussi si les raccourcis sont transmis aux pages. Non, les global shortcuts dans main.js ne sont PAS automatiquement transmis aux iframes. Il faut explicitement envoyer via IPC.

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-750-R750-User-raison-problème-shortcuts-sont]]
- ⬇️ Next: [[Card-752-R752-PROBLÈME-DANS-CHAÎNE-logs-montrent]]
- 📊 MOC: [[_MOC_French chat message instructions]]
