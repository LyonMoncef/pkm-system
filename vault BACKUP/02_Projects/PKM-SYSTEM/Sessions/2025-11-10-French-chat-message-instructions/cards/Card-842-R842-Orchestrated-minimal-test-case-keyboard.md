---
type: chat-card
parent_export: '[[Export]]'
order: 842
role: assistant
created: '2025-11-10T21:12:16.745459Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 842 - Assistant

**ID:** msg-842

## 💬 Content


**ID:** msg-842

Orchestrated minimal test case for keyboard shortcuts relay.OK, on a confirmé que les raccourcis locaux marchent dans capture.html. Maintenant il veut tester l'affichage du popup de shortcuts (keyboardHint).
Le problème c'est que capture.html n'a PAS le popup keyboardHint - c'est dans app.html !
Donc on a 2 options :

Tester le relay vers app.html avec UN seul raccourci simple
Ajouter le popup keyboardHint dans capture.html pour tester en local

Je pense qu'il veut tester le relay vers app.html pour afficher le popup de shortcuts. On va faire simple : un seul raccourci qui relay vers app.html et déclenche showKeyboardHints().
On va garder Ctrl+Shift+K comme raccourci de test.

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-841-R841-Orchestrated-minimal-test-case-keyboard]]
- ⬇️ Next: [[Card-843-R843-Orchestrated-minimal-test-case-keyboard]]
- 📊 MOC: [[_MOC_French chat message instructions]]
