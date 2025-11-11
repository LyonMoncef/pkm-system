---
type: chat-card
parent_export: '[[Export]]'
order: 414
role: assistant
created: '2025-11-11T00:47:17.139117Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 414 - Assistant

**ID:** msg-414

## 💬 Content


**ID:** msg-414

Je vois plusieurs problèmes. Voici les corrections :
🔧 Problème 1 : ZPos qui ne reste pas au premier plan
Pour que les widgets restent vraiment au premier plan, il faut utiliser AlwaysOnTop au lieu de ZPos=2 :
Modifie GlobalVariables.inc :
ini[Variables]
fontName=Trebuchet MS
textSize=10
titleSize=14
smallTextSize=9
Z_STATE=0
ALWAYS_ON_TOP=-2
🔧 Problème 2 : Bouton toggle simplifié (sans émojis buggés)

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-413-R413-Vois-plusieurs-problèmes-Voici-correctio]]
- ⬇️ Next: [[Card-415-R415-Variables-fontName-Trebuchet-textSize-ti]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]
