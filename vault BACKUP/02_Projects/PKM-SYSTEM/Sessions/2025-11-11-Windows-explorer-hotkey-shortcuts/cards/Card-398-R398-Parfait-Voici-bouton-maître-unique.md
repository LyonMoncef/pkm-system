---
type: chat-card
parent_export: '[[Export]]'
order: 398
role: assistant
created: '2025-11-11T00:47:16.956575Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 398 - Assistant

**ID:** msg-398

## 💬 Content


**ID:** msg-398

Parfait ! Voici le bouton maître unique. Maintenant il faut configurer tes autres skins pour qu'ils réagissent :
📋 Étapes d'installation :
1️⃣ Créer le fichier ToggleZPos.ini
Sauvegarde le code ci-dessus dans ton dossier Rainmeter (par exemple dans YourSuite\\ToggleZPos\\ToggleZPos.ini)
2️⃣ Modifier Disk.ini (et tous tes autres skins)
ini[Rainmeter]
Update=1000
Background=#@#Background.png
BackgroundMode=3
BackgroundMargins=0,50,0,30
@include=#@#GlobalVariables.inc
ZPos=#Z_STATE#
Group=AllSkins

; ... reste de ton code Disk.ini sans le bouton toggle ...
3️⃣ Modifier Shortcuts.ini
ini[Rainmeter]
Update=1000
Background=#@#Background.png
BackgroundMode=3
BackgroundMargins=0,50,0,30
@include=#@#GlobalVariables.inc
ZPos=#Z_STATE#
Group=AllSkins

; ... reste de ton code ...
4️⃣ Vérifier GlobalVariables.inc
ini[Variables]
fontName=Trebuchet MS
textSize=10
titleSize=14
smallTextSize=9
Z_STATE=0
🎯 Comment ça fonctionne :

Le bouton toggle change la valeur de Z_STATE dans GlobalVariables.inc
Il utilise [!RefreshGroup \"AllSkins\"] qui rafraîchit tous les skins du groupe
Tous les skins qui ont Group=AllSkins et ZPos=#Z_STATE# basculent ensemble

Résultat : Un seul clic sur le bouton et TOUS tes widgets passent au premier plan (ou reviennent en mode normal) simultanément ! 🚀
Tu veux que je te prépare les versions complètes de Disk.ini et Shortcuts.ini sans leurs anciens boutons toggle ?

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-397-R397-ToggleZPos-Bouton-Maître-pour-tous]]
- ⬇️ Next: [[Card-399-R399-Rainmeter-Update-Background-Background-B]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]
