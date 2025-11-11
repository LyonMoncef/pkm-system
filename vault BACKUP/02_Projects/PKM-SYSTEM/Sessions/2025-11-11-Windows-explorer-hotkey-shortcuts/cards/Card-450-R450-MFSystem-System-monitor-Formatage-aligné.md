---
type: chat-card
parent_export: '[[Export]]'
order: 450
role: assistant
created: '2025-11-11T00:47:17.494891Z'
tags:
- chat-card
- power-bi
- receipts
attachments_count: 0
---

# 🤖 Message 450 - Assistant

**ID:** msg-450

## 💬 Content


**ID:** msg-450

MFSystem :
; System monitor - Formatage aligné sur Disk et Clock
; ----------------------------------
[Rainmeter]
Update=1000
Background=#@#Background.png
BackgroundMode=3
BackgroundMargins=0,50,0,30
@include=#@#GlobalVariables.inc
AlwaysOnTop=#ALWAYS_ON_TOP#
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
DynamicVariables=1Network : et pareil pour le dernier, Le bouton toggle affiche un demi cercle tronqué de 10x21 pixels
bleu turquoise
Il fonctionne pour les 2 skins mais ne bouge pas et ne change pas de couleurFais au plus simple pour avoir juste un indicateur visuel le plus simple possibleAfficher plus

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-449-R449-NETWORK-version-modernisée-Rainmeter-Upd]]
- ⬇️ Next: [[Card-451-R451-MFSystem-System-monitor-Formatage-aligné]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]

## 🏷️ Topics

- #power-bi
- #receipts
