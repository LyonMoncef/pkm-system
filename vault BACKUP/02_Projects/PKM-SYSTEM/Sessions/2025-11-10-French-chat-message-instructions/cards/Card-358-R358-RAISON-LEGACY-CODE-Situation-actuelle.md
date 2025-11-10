---
type: chat-card
parent_export: '[[Export]]'
order: 358
role: assistant
created: '2025-11-10T21:12:07.396398Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 358 - Assistant

**ID:** msg-358

## 💬 Content


**ID:** msg-358

🎯 T'AS RAISON, ON A DU LEGACY CODE !
Situation actuelle :
Shortcuts qui existent :

Ctrl+Shift+Space → Toggle window + go to Capture (global, marche app fermée)
Ctrl+Shift+F → Toggle window + go to Reference (global, marche app fermée)
Ctrl+1/2/3 → Navigate pages (interne app seulement)
Ctrl+B → Toggle sidebar (interne app)

Le problème :

Ctrl+Shift+Space et Ctrl+1 font presque la même chose (vont sur Capture)
Ctrl+Shift+F et Ctrl+3 font presque la même chose (vont sur Reference)
MAIS les Ctrl+Shift marchent app fermée (global OS), les Ctrl+chiffres app ouverte seulement


🔧 REFACTOR PROPOSAL
Garder la logique suivante :
Global OS shortcuts (app fermée/ouverte) :

Ctrl+Shift+Space → Toggle Capture (show/hide + go to capture)
Ctrl+Shift+F → Toggle Reference (show/hide + go to reference)
Ctrl+Shift+H → Toggle Hub (NEW - show/hide + go to hub)

Internal app shortcuts (app ouverte seulement) :

Ctrl+1/2/3 → Quick navigate pages (pas de toggle, juste switch)
Ctrl+B → Toggle sidebar
Ctrl+I → Insert mode
Esc → Normal mode
Ctrl+S → Save note to file
Ctrl+K → Clear editor
? → Show shortcuts (à fixer)

Smart behavior :

Si app visible + tu fais Ctrl+Shift+Space → Hide
Si app cachée + tu fais Ctrl+Shift+Space → Show + Capture
Si app visible sur Reference + tu fais Ctrl+Shift+Space → Go to Capture (pas hide)


🗂️ OÙ SONT DÉFINIS LES SHORTCUTS ACTUELLEMENT

main.js → Global OS shortcuts (Ctrl+Shift+Space/F, Ctrl+1/2/3, Ctrl+B)
app.html → Internal keyboard listener (reçoit les relays)
capture.html → Relay + shortcuts locaux (Esc, Ctrl+I, Ctrl+S/K)
reference.html → Relay
hub.html → Relay


🎯 PROPOSITION DE REFACTOR
Je peux créer :
Option A - Centralisé (PROPRE)
Un fichier shortcuts.js qui documente et gère TOUS les shortcuts de manière centralisée avec commentaires clairs.
Option B - Cleanup actuel (RAPIDE)
On garde la structure actuelle mais on :

Nettoie les doublons
Ajoute des commentaires clairs partout
Documente dans un README.md

Option C - Plus tard (BACKLOG)
On note ça dans le backlog et on finit les bugs critiques d'abord.

💬 TON CALL
Tu veux qu'on :

A) Refactor propre maintenant (30min)
B) Quick cleanup + doc (10min)
C) Backlog + on continue bugs

Et pour Ctrl+W, actuellement ça fait quoi ? Rien ? Ou ça ferme ?
Balance ton choix ! 💪

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-357-R357-RAISON-LEGACY-CODE-Situation-actuelle]]
- ⬇️ Next: [[Card-359-R359-MFGo-refactor-note-reflexions-sous]]
- 📊 MOC: [[_MOC_French chat message instructions]]
