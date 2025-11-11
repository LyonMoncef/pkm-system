---
type: chat-card
parent_export: '[[Export]]'
order: 375
role: assistant
created: '2025-11-11T00:47:16.593022Z'
tags:
- chat-card
- excel
- receipts
- code
attachments_count: 0
---

# 🤖 Message 375 - Assistant

**ID:** msg-375

## 💬 Content


**ID:** msg-375

Excellente question ! Il y a deux approches possibles :
✅ Solution recommandée : Un bouton par skin (intégré)
Avantages :

Chaque skin contrôle son propre état (indépendant)
Plus simple à gérer
Pas de skin supplémentaire à charger

Comment faire :
Copie le code du bouton toggle à la fin de chaque skin (Disk.ini, Shortcuts.ini, etc.). Tu auras un petit bouton sur chaque widget pour l'épingler individuellement.
ini; Dans Disk.ini - à la fin du fichier
[measureToggleState]
Measure=Calc
Formula=#Z_STATE#
DynamicVariables=1

[MeterToggleBackground]
Meter=Shape
X=10
Y=10
; ... reste du code ...
Important : Dans LeftMouseUpAction, change le nom du skin :
ini; Pour Disk.ini
LeftMouseUpAction=[!SetVariable Z_STATE ([&Z_STATE]=0 ? 2 : 0)][!WriteKeyValue Variables Z_STATE [&Z_STATE] \"#@#GlobalVariables.inc\"][!UpdateMeasure *][!UpdateMeter *][!Redraw]

; ⚠️ Attention : chaque skin doit avoir sa PROPRE variable Z_STATE
; Dans GlobalVariables.inc :
Z_STATE_DISK=0
Z_STATE_SHORTCUTS=0
Z_STATE_CPU=0

❌ Problème avec l'approche \"skin unique\"
Si tu fais un ToggleZPos.ini séparé, il ne pourra contrôler qu'un seul skin à la fois, pas tous. Ce n'est pas pratique.

🎯 Ma recommandation finale
Utilise des variables séparées pour chaque skin :
Dans GlobalVariables.inc :
ini[Variables]
fontName=Trebuchet MS
textSize=10
titleSize=14
smallTextSize=9

; États Z pour chaque skin
Z_STATE_DISK=0
Z_STATE_SHORTCUTS=0
Z_STATE_CPU=0
Dans Disk.ini :
ini[Rainmeter]
Update=1000
Background=#@#Background.png
BackgroundMode=3
BackgroundMargins=0,50,0,30
@include=#@#GlobalVariables.inc
ZPos=#Z_STATE_DISK#

; ... ton contenu ...

; Bouton toggle spécifique à Disk
[MeterToggleClick]
Meter=Image
X=10
Y=10
W=50
H=24
SolidColor=0,0,0,1
LeftMouseUpAction=[!SetVariable Z_STATE_DISK ([#Z_STATE_DISK#]=0 ? 2 : 0)][!WriteKeyValue Variables Z_STATE_DISK [#Z_STATE_DISK#] \"#@#GlobalVariables.inc\"][!UpdateMeasure *][!UpdateMeter *][!Redraw]
DynamicVariables=1
Dans Shortcuts.ini :
ini[Rainmeter]
ZPos=#Z_STATE_SHORTCUTS#
; ...

[MeterToggleClick]
LeftMouseUpAction=[!SetVariable Z_STATE_SHORTCUTS ([#Z_STATE_SHORTCUTS#]=0 ? 2 : 0)][!WriteKeyValue Variables Z_STATE_SHORTCUTS [#Z_STATE_SHORTCUTS#] \"#@#GlobalVariables.inc\"][!UpdateMeasure *][!UpdateMeter *][!Redraw]
Comme ça chaque widget peut être épinglé indépendamment ! 📌
Tu veux que je te prépare le code complet pour Disk et Shortcuts avec cette approche ?

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-374-R374-Excellente-question-deux-approches-possi]]
- ⬇️ Next: [[Card-376-R376-Excellente-question-deux-approches-possi]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]

## 🏷️ Topics

- #excel
- #receipts
- #code
