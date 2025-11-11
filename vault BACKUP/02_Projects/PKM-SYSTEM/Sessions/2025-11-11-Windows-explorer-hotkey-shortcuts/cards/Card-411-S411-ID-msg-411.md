---
type: chat-card
parent_export: '[[Export]]'
order: 411
role: user
created: '2025-11-11T00:47:17.092279Z'
tags:
- chat-card
- power-bi
- receipts
attachments_count: 0
---

# 👤 Message 411 - User

**ID:** msg-411

## 💬 Content


**ID:** msg-411

le bouton fonctionne à peu près dans 2 cas :
Disk
System
Pour ces 2, l'appui du toggle les passe au 1er plan mais un clic sunr une fenêtre active et ils repassent en arrièrePour les 3 autres, le toggle ne fonctionne pas
Clock
Raccourcis
NetworkL'affichage du toggle est buggé comme pour des caractères non reconnus, fais quelque chose dep lus simple pour l'instant; Clock avec couleur par jour - Formatage aligné sur Disk
; ----------------------------------
[Rainmeter]
Update=1000
Background=#@#Background.png
BackgroundMode=3
BackgroundMargins=0,50,0,30
@include=#@#GlobalVariables.inc
ZPos=#Z_STATE#
Group=AllSkins
[Variables]
; Couleurs des jours (R,G,B,A)
color0=255,50,50,205
color1=50,200,50,205
color2=255,165,0,205
color3=255,220,50,205
color4=150,50,200,205
color5=50,130,255,205
color6=255,140,0,205
[Metadata]
Name=Clock
Information=Horloge avec couleur par jour
Version=2.1.0
; ----------------------------------
; MEASURES
; ----------------------------------
[measureTime]
Measure=Time
Format=%H:%M
[measureDate]
Measure=Time
Format=%d/%m/%Y
[measureDay]
Measure=Time
Format=%A
Substitute=\"Monday\":\"Lundi\",\"Tuesday\":\"Mardi\",\"Wednesday\":\"Mercredi\",\"Thursday\":\"Jeudi\",\"Friday\":\"Vendredi\",\"Saturday\":\"Samedi\",\"Sunday\":\"Dimanche\"
[measureDayNumber]
Measure=Time
Format=%w
; ----------------------------------
; METERS
; ----------------------------------
[meterTitle]
Meter=String
MeasureName=measureTime
X=100
Y=8
W=190
H=30
StringAlign=Center
StringCase=Upper
StringStyle=Bold
StringEffect=Shadow
FontEffectColor=0,0,0,120
FontFace=Trebuchet MS
FontSize=14
FontColor=[#color[&measureDayNumber]]
AntiAlias=1
DynamicVariables=1
Text=%1
[meterDay]
Meter=String
MeasureName=measureDay
X=10
Y=42
W=190
H=16
StringAlign=Left
StringStyle=Bold
StringEffect=Shadow
FontEffectColor=0,0,0,20
FontFace=Trebuchet MS
FontSize=12
FontColor=200,200,200,255
AntiAlias=1
Text=%1
[meterDate]
Meter=String
MeasureName=measureDate
X=200
Y=42
W=190
H=16
StringAlign=Right
StringStyle=Bold
StringEffect=Shadow
FontEffectColor=0,0,0,20
FontFace=Trebuchet MS
FontSize=12
FontColor=200,200,200,255
AntiAlias=1
Text=%1; System monitor - Formatage aligné sur Disk et Clock
; ----------------------------------
[Rainmeter]
Update=1000
Background=#@#Background.png
BackgroundMode=3
BackgroundMargins=0,50,0,30
@include=#@#GlobalVariables.inc
ZPos=#Z_STATE#
Group=AllSkins
[Variables]
; Couleurs des jours (R,G,B,A)
color0=255,50,50,205
color1=50,200,50,205
color2=255,165,0,205
color3=255,220,50,205
color4=150,50,200,205
color5=50,130,255,205
color6=255,140,0,205
[Metadata]
Name=System
Author=Custom
Information=Affiche les statistiques système
Version=2.1.0
; ----------------------------------
; MEASURES
; ----------------------------------
[measureCPU]
Measure=CPU
Processor=0
[measureRAM]
Measure=PhysicalMemory
UpdateDivider=20
[measureSWAP]
Measure=SwapMemory
UpdateDivider=20
[measureDayNumber]
Measure=Time
Format=%w
; ----------------------------------
; METERS
; ----------------------------------
[meterTitle]
Meter=String
X=100
Y=8
W=190
H=30
StringAlign=Center
StringCase=Upper
StringStyle=Bold
StringEffect=Shadow
FontEffectColor=0,0,0,120
FontFace=Trebuchet MS
FontSize=14
FontColor=[#color[&measureDayNumber]]
AntiAlias=1
DynamicVariables=1
Text=System
LeftMouseUpAction=[\"taskmgr.exe\"]
ToolTipText=Ouvrir le Gestionnaire des tâches
[meterLabelCPU]
Meter=String
X=10
Y=42
W=190
H=16
StringAlign=Left
StringStyle=Bold
StringEffect=Shadow
FontEffectColor=0,0,0,20
FontFace=Trebuchet MS
FontSize=12
FontColor=200,200,200,255
AntiAlias=1
Text=CPU
[meterValueCPU]
Meter=String
MeasureName=measureCPU
X=200
Y=42
W=190
H=16
StringAlign=Right
StringStyle=Bold
StringEffect=Shadow
FontEffectColor=0,0,0,20
FontFace=Trebuchet MS
FontSize=12
FontColor=200,200,200,255
AntiAlias=1
Text=%1%
[meterBarCPU]
Meter=Shape
X=10
Y=60
W=190
H=8
Shape=Rectangle 0,0,190,8,2 | StrokeWidth 1 | StrokeColor 80,80,80,255 | Fill Color 60,60,60,255
[meterBarCPUFill]
Meter=Bar
MeasureName=measureCPU
X=11
Y=61
W=188
H=6
BarColor=[#color[&measureDayNumber]]
BarOrientation=HORIZONTAL
DynamicVariables=1
[meterLabelRAM]
Meter=String
X=10
Y=72
W=190
H=16
StringAlign=Left
StringStyle=Bold
StringEffect=Shadow
FontEffectColor=0,0,0,20
FontFace=Trebuchet MS
FontSize=12
FontColor=200,200,200,255
AntiAlias=1
Text=RAM
[meterValueRAM]
Meter=String
MeasureName=measureRAM
X=200
Y=72
W=190
H=16
StringAlign=Right
StringStyle=Bold
StringEffect=Shadow
FontEffectColor=0,0,0,20
FontFace=Trebuchet MS
FontSize=12
FontColor=200,200,200,255
AntiAlias=1
Text=%1%
Percentual=1
[meterBarRAM]
Meter=Shape
X=10
Y=90
W=190
H=8
Shape=Rectangle 0,0,190,8,2 | StrokeWidth 1 | StrokeColor 80,80,80,255 | Fill Color 60,60,60,255
[meterBarRAMFill]
Meter=Bar
MeasureName=measureRAM
X=11
Y=91
W=188
H=6
BarColor=[#color[&measureDayNumber]]
BarOrientation=HORIZONTAL
DynamicVariables=1
[meterLabelSWAP]
Meter=String
X=10
Y=102
W=190
H=16
StringAlign=Left
StringStyle=Bold
StringEffect=Shadow
FontEffectColor=0,0,0,20
FontFace=Trebuchet MS
FontSize=12
FontColor=200,200,200,255
AntiAlias=1
Text=SWAP
[meterValueSWAP]
Meter=String
MeasureName=measureSWAP
X=200
Y=102
W=190
H=16
StringAlign=Right
StringStyle=Bold
StringEffect=Shadow
FontEffectColor=0,0,0,20
FontFace=Trebuchet MS
FontSize=12
FontColor=200,200,200,255
AntiAlias=1
Text=%1%
Percentual=1
[meterBarSWAP]
Meter=Shape
X=10
Y=120
W=190
H=8
Shape=Rectangle 0,0,190,8,2 | StrokeWidth 1 | StrokeColor 80,80,80,255 | Fill Color 60,60,60,255
[meterBarSWAPFill]
Meter=Bar
MeasureName=measureSWAP
X=11
Y=121
W=188
H=6
BarColor=[#color[&measureDayNumber]]
BarOrientation=HORIZONTAL
DynamicVariables=1

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-410-R410-Bouton-fonctionne-près-dans-Disk]]
- ⬇️ Next: [[Card-412-R412-Vois-plusieurs-problèmes-Voici-correctio]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]

## 🏷️ Topics

- #power-bi
- #receipts
