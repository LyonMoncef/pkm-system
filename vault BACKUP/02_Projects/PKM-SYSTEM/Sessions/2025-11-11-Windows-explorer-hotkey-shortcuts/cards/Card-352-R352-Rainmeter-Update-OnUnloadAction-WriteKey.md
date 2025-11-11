---
type: chat-card
parent_export: '[[Export]]'
order: 352
role: assistant
created: '2025-11-11T00:47:16.371042Z'
tags:
- chat-card
- receipts
attachments_count: 0
---

# 🤖 Message 352 - Assistant

**ID:** msg-352

## 💬 Content


**ID:** msg-352

MF[Rainmeter]
Update=100
OnUnloadAction=[!WriteKeyValue Variables Z_STATE 0 \"#@#GlobalVariables.inc\"][!RefreshApp]
@include=#@#GlobalVariables.inc
; ------------------------------------
; MESURE: Calcul du prochain état
; ------------------------------------
[measureZNextState]
Measure=Calc
; Si l'état actuel (Z_STATE) est 0 (Normal), le prochain état est 2 (1er plan), et vice-versa.
Formula=(#Z_STATE# = 0 ? 2 : 0)
DynamicVariables=1
; ------------------------------------
; MÈTRES: Le Bouton Discret (10x10 pixels)
; ------------------------------------
; Fond du cercle (gris)
[MeterToggleDotBg]
Meter=Shape
X=0
Y=0
W=10
H=10
Shape=Circle 5,5,5 | Fill Color 150,150,150,50
; Point indicateur de statut (Couleur dynamique: Vert si ON, Gris si OFF)
[MeterStatusColor]
Meter=Shape
X=0
Y=0
W=10
H=10
Shape=Circle 5,5,3 | Fill Color ([&Z_STATE]=0 ? 100,100,100,255 : 50,255,50,255)
DynamicVariables=1
; Zone cliquable et Tooltip
[MeterClickAction]
Meter=String
X=0
Y=0
W=10
H=10
SolidColor=0,0,0,1
LeftMouseUpAction=[!SetVariable Z_STATE ([&Z_STATE]=0 ? 2 : 0)]
 [!SetOption \"Disk\" \"ZPos\" [&Z_STATE]]
 [!UpdateMeter *]
 [!Redraw]
DynamicVariables=1
[MeterTooltip]
Meter=String
X=0
Y=0
W=10
H=10
SolidColor=0,0,0,1
ToolTipText=[&Z_STATE]=0 ? \"Affichage normal\" : \"Passage au 1er plan\"
DynamicVariables=1J'aime pas du tout le résultat de ce bouton toggle, c'est buggé, ça ne fait pas switcher l'état normal de l'état 1er plan
Il est très peu visible et mocheFais moi un joli bouton toggle stp qui fonctionne idéalementAfficher plus

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-351-R351-Rainmeter-Update-OnUnloadAction-WriteKey]]
- ⬇️ Next: [[Card-353-R353-Rainmeter-Update-OnUnloadAction-WriteKey]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]

## 🏷️ Topics

- #receipts
