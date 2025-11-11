---
type: chat-card
parent_export: '[[Export]]'
order: 424
role: assistant
created: '2025-11-11T00:47:17.233973Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 424 - Assistant

**ID:** msg-424

## 💬 Content


**ID:** msg-424

🔧 Problème 3 : Modifier TOUS tes skins
Remplace dans CHAQUE skin (Clock, Network, Shortcuts, System, Disk) :
ini[Rainmeter]
Update=1000
Background=#@#Background.png
BackgroundMode=3
BackgroundMargins=0,50,0,30
@include=#@#GlobalVariables.inc
AlwaysOnTop=#ALWAYS_ON_TOP#
Group=AllSkins
Note : Remplace ZPos=#Z_STATE# par AlwaysOnTop=#ALWAYS_ON_TOP#
📋 Valeurs AlwaysOnTop expliquées :

-2 = Toujours au premier plan (même au-dessus des fenêtres en plein écran)
-1 = Normal (mode fenêtre classique)
0 = Toujours en arrière-plan
1 = Au-dessus des fenêtres normales
2 = Mode \"topmost\" (reste devant mais peut être recouvert)

✅ Résumé des modifications :

GlobalVariables.inc - Ajoute ALWAYS_ON_TOP=-2
ToggleZPos.ini - Version simplifiée sans émojis
Tous les skins - Remplace ZPos=#Z_STATE# par AlwaysOnTop=#ALWAYS_ON_TOP#

Avec ces changements, le bouton devrait :

✅ S'afficher correctement (pas de caractères buggés)
✅ Vraiment garder les widgets au premier plan
✅ Fonctionner pour TOUS les skins

Teste et dis-moi si ça fonctionne ! 🎯

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-423-R423-ToggleZPos-Bouton-Maître-Simplifié-Rainm]]
- ⬇️ Next: [[Card-425-R425-Rainmeter-Update-Background-Background-B]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]
