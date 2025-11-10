---
type: chat-card
parent_export: '[[Export]]'
order: 770
role: assistant
created: '2025-11-10T21:12:15.741211Z'
tags:
- chat-card
- receipts
attachments_count: 0
---

# 🤖 Message 770 - Assistant

**ID:** msg-770

## 💬 Content


**ID:** msg-770

L'utilisateur a un problème : les raccourcis globaux (F1, Ctrl+/, Ctrl+Shift+L) sont bien captés par main.js (logs affichés) mais ne déclenchent aucune action dans l'app.
Par contre, Ctrl+1/2/3 marchent sans problème partout.
Il demande un rappel de l'architecture shortcuts globaux vs internes.
Laisse-moi faire un rappel clair de l'architecture qu'on a mise en place :
ARCHITECTURE SHORTCUTS - RAPPEL
Layer 1 - Global OS Shortcuts (main.js)

Registered via globalShortcut.register()
Fonctionnent MÊME quand app fermée/cachée
Envoyent des messages IPC vers renderer process
Exemples actuels :

Ctrl+Shift+Space → Toggle Capture
Ctrl+Shift+F → Toggle Reference
Ctrl+Shift+H → Toggle Hub
Ctrl+W → Quick save + hide
Ctrl+Shift+W → Force quit
F1, Ctrl+/, Ctrl+Shift+L → Show shortcuts (en test)


Layer 2 - Internal App Shortcuts (app.html)

Registered via document.addEventListener('keydown')
Fonctionnent SEULEMENT quand app ouverte et focused
Gérés directement dans le renderer process
Exemples :

Ctrl+1/2/3 → Navigate pages (marchent bien)
Ctrl+B → Toggle sidebar


Layer 3 - Page-Specific Shortcuts (capture.html, etc.)

Dans chaque iframe
Relayés vers parent via postMessage
Exemples :

Esc, Ctrl+I → Vim modes
Ctrl+S, Ctrl+K → Save, Clear


Je vois un problème de communication entre les couches de raccourcis. Les raccourcis globaux sont correctement interceptés par main.js, mais ne semblent pas atteindre le renderer process. Le point critique est probablement la configuration du listener IPC dans app.html ou l'implémentation de la fonction showKeyboardHints(). Il faut vérifier que le canal IPC est ouvert et que la fonction de gestion des raccourcis est correctement définie.
La différence entre Layer 1 et Layer 2 révèle une faiblesse dans la chaîne de transmission. Les raccourcis internes (Ctrl+1/2/3) fonctionnent directement, tandis que les raccourcis globaux (F1/Ctrl+/) nécessitent une transmission complexe via main.js et preload.js.
Pour diagnostiquer, je vais tester en convertissant temporairement le raccourci show-shortcuts en événement local dans app.html, ce qui permettra de confirmer si le problème est lié à la transmission IPC.
Un refactoring futur impliquera une architecture plus modulaire, avec une séparation nette du CSS et une optimisation du code.

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-769-R769-Utilisateur-problème-raccourcis-globaux-]]
- ⬇️ Next: [[Card-771-R771-RAPPEL-ARCHITECTURE-SHORTCUTS-ARCHITECTU]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #receipts
