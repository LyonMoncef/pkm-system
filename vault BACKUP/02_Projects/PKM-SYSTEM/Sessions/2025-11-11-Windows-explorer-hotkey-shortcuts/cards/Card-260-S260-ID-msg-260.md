---
type: chat-card
parent_export: '[[Export]]'
order: 260
role: user
created: '2025-11-11T00:47:15.337017Z'
tags:
- chat-card
- power-bi
- receipts
attachments_count: 0
---

# 👤 Message 260 - User

**ID:** msg-260

## 💬 Content


**ID:** msg-260

En gardant le même thème police etc que ce skin, tu vas m'afficher une liste de raccourcis à se rappeler dans un widget ; Disk monitor avec couleur par jour et jauge améliorée
; ----------------------------------
[Rainmeter]
Update=1000
Background=#@#Background.png
BackgroundMode=3
BackgroundMargins=0,50,0,30
@include=#@#GlobalVariables.inc
ZPos=[&Z_STATE]
[Variables]
; Couleurs des jours pour le texte
color0=255,50,50,205
color1=50,200,50,205
color2=255,165,0,205
color3=255,220,50,205
color4=150,50,200,205
color5=50,130,255,205
color6=255,140,0,205
; Couleurs de la jauge selon le pourcentage
colorBarLow=50,200,50,255 ; Vert si < 60%
colorBarMedium=255,165,0,255 ; Orange si 60-85%
colorBarHigh=255,50,50,255 ; Rouge si > 85%
; Configuration du disque
disk1=C:
[Metadata]
Name=Disk
Author=Custom
Information=Affiche l'espace disque avec jauge colorée
Version=2.1.0
; ----------------------------------
; MEASURES
; ----------------------------------
[measureTotalDisk1]
Measure=FreeDiskSpace
Drive=#disk1#
Total=1
UpdateDivider=120
[measureUsedDisk1]
Measure=FreeDiskSpace
Drive=#disk1#
InvertMeasure=1
UpdateDivider=120
[measureFreeDiskValue]
Measure=FreeDiskSpace
Drive=#disk1#
UpdateDivider=120
[measureTotalDiskValue]
Measure=FreeDiskSpace
Drive=#disk1#
Total=1
UpdateDivider=120
[measurePercentUsed]
Measure=Calc
Formula=( ( [measureTotalDiskValue] - [measureFreeDiskValue] ) / [measureTotalDiskValue] ) * 100
DynamicVariables=1
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
Text=Disque #disk1#
[meterValueDisk1]
Meter=String
MeasureName=measureFreeDiskValue
X=100
Y=42
W=190
H=16
StringAlign=Center
StringStyle=Bold
StringEffect=Shadow
FontEffectColor=0,0,0,20
FontFace=Trebuchet MS
FontSize=12
FontColor=200,200,200,255
AntiAlias=1
DynamicVariables=1
Text=%1B disponibles
NumOfDecimals=1
AutoScale=1
LeftMouseUpAction=[\"#disk1#\\\"]
ToolTipText=Cliquez pour ouvrir le disque
; Fond de la barre
[meterBarBackground]
Meter=Shape
X=10
Y=70
W=190
H=24
Shape=Rectangle 0,0,190,24,3 | StrokeWidth 1 | StrokeColor 80,80,80,255 | Fill Color 60,60,60,255
DynamicVariables=1
; Barre de progression avec couleur dynamique
[meterBarDisk1]
Meter=Shape
X=11
Y=71
DynamicVariables=1
Shape=Rectangle 0,0,([measurePercentUsed]*1.88),22,3 | Fill Color [#color[&measureDayNumber]] | StrokeWidth 1 | StrokeColor 80,80,80,255
; Texte du pourcentage sur la barre
[meterBarPercentText]
Meter=String
MeasureName=measurePercentUsed
X=100
Y=73
W=190
H=22
StringAlign=Center
StringStyle=Bold
FontFace=Trebuchet MS
FontSize=10
FontColor=255,255,255,255
AntiAlias=1
Text=%1%
NumOfDecimals=0
[MeterToggleDotBg]
Meter=Shape
X=5
Y=5
W=15
H=15
Shape=Circle 7.5,7.5,7.5 | Fill Color 150,150,150,80 ; fond gris clair semi-transparent
DynamicVariables=1
[MeterStatusColor]
Meter=Shape
X=5
Y=5
W=15
H=15
Shape=Circle 7.5,7.5,6 | Fill Color ([&Z_STATE]=0 ? 100,100,100,200 : 50,255,50,200)
DynamicVariables=1
[MeterClickAction]
Meter=String
X=5
Y=5
W=15
H=15
SolidColor=0,0,0,1 ; zone invisible mais cliquable
LeftMouseUpAction=[!SetVariable Z_STATE ([&Z_STATE]=0 ? 2 : 0)]
 [!SetOption \"Disk\" \"ZPos\" [&Z_STATE]]
 [!UpdateMeter *][!Redraw]
DynamicVariables=1
[MeterTooltip]
Meter=String
X=5
Y=5
W=15
H=15
SolidColor=0,0,0,1
ToolTipText=[&Z_STATE]=0 ? \"Affichage normal\" : \"Passage au 1er plan\"
DynamicVariables=1pour les raccourcis suivants
Touche de raccourci pour basculer vers le zoom : Ctrl
Dessiner sans touche de raccourci pour le zoom : Ctrl Alt
Dessiner sans touche de raccourci pour le zoom : Ctrl Alt
Raccourci d'activation
Extracteur de texte : Win+Shift+T mais propose moi un raccourci plus pratique
Activer rogner et verrouiller : Win+CTRL+Shift+T
Activer Color Picker : Win+Shift+C
Activer la règle d'écran : Win+Shift+M
Activer Toujours visible : Win+Ctrl+T
Activer des Espaces de travail : Win+Ctrl+%

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-259-R259-Gardant-même-thème-police-skin]]
- ⬇️ Next: [[Card-261-R261-Widget-Raccourcis-ClavierCode-Widget-Rac]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]

## 🏷️ Topics

- #power-bi
- #receipts
