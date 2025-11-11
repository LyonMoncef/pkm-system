---
type: chat-card
parent_export: '[[Export]]'
order: 226
role: assistant
created: '2025-11-11T00:21:45.891177Z'
tags:
- chat-card
- power-bi
- python
- receipts
- automation
attachments_count: 0
---

# 🤖 Message 226 - Assistant

**ID:** msg-226

## 💬 Content


**ID:** msg-226

MFok problème résolu, cette version fonctionne parfaitement; Skin de monitoring pour NAS
; ----------------------------------
[Rainmeter]
Update=1000
Background=#@#Background.png
BackgroundMode=3
BackgroundMargins=0,34,0,20
[Metadata]
Name=NAS Monitor
Author=Custom
Information=Affiche les informations du NAS
License=Creative Commons BY-NC-SA 3.0
Version=1.0.0
[Variables]
fontName=Trebuchet MS
textSize=10
colorBar=235,170,0,255
colorText=255,255,255,205
colorOnline=50,200,50,205
colorOffline=255,50,50,205
; Adresse IP de votre NAS
NAS_IP=192.168.1.141
; Lettre du lecteur réseau mappé (exemple: Z:)
; Pour mapper un lecteur : Explorateur > Cet ordinateur > Mapper un lecteur réseau
NAS_Drive=Z:
; ----------------------------------
; MEASURES
; ----------------------------------
[measurePingNAS]
; Vérifie si le NAS est accessible via ping
Measure=Plugin
Plugin=PowershellRM
ScriptFile=#@#Scripts\\PingNAS.ps1
; Ce script sera créé automatiquement
UpdateRate=5
[measureNASDiskTotal]
; Espace total du NAS (nécessite un lecteur mappé)
Measure=FreeDiskSpace
Drive=#NAS_Drive#
Total=1
UpdateDivider=120
IgnoreRemovable=0
[measureNASDiskUsed]
; Espace utilisé du NAS
Measure=FreeDiskSpace
Drive=#NAS_Drive#
InvertMeasure=1
UpdateDivider=120
IgnoreRemovable=0
[measureNASPercent]
; Pourcentage d'utilisation
Measure=Calc
Formula=(measureNASDiskUsed / measureNASDiskTotal) * 100
; ----------------------------------
; STYLES
; ----------------------------------
[styleTitle]
StringAlign=Center
StringCase=Upper
StringStyle=Bold
StringEffect=Shadow
FontEffectColor=0,0,0,50
FontColor=#colorText#
FontFace=#fontName#
FontSize=14
AntiAlias=1
ClipString=1
[styleLeftText]
StringAlign=Left
StringCase=None
StringStyle=Bold
StringEffect=Shadow
FontEffectColor=0,0,0,20
FontColor=#colorText#
FontFace=#fontName#
FontSize=#textSize#
AntiAlias=1
ClipString=1
[styleRightText]
StringAlign=Right
StringCase=None
StringStyle=Bold
StringEffect=Shadow
FontEffectColor=0,0,0,20
FontColor=#colorText#
FontFace=#fontName#
FontSize=#textSize#
AntiAlias=1
ClipString=1
DynamicVariables=1
[styleCenterText]
StringAlign=Center
StringCase=None
StringStyle=Bold
StringEffect=Shadow
FontEffectColor=0,0,0,20
FontColor=#colorText#
FontFace=#fontName#
FontSize=11
AntiAlias=1
ClipString=1
DynamicVariables=1
[styleBar]
BarColor=#colorBar#
BarOrientation=HORIZONTAL
SolidColor=255,255,255,15
[styleSeperator]
SolidColor=255,255,255,15
; ----------------------------------
; METERS
; ----------------------------------
[meterTitle]
Meter=String
MeterStyle=styleTitle
X=100
Y=12
W=190
H=18
Text=NAS Monitor
[meterIPLabel]
Meter=String
MeterStyle=styleLeftText
X=10
Y=40
W=190
H=16
Text=Adresse IP
[meterIPValue]
Meter=String
MeterStyle=styleRightText
X=200
Y=0r
W=190
H=16
Text=#NAS_IP#
LeftMouseUpAction=[\"\\\\#NAS_IP#\"]
[meterSeperator]
Meter=Image
MeterStyle=styleSeperator
X=10
Y=58
W=190
H=1
[meterDiskLabel]
Meter=String
MeterStyle=styleCenterText
X=100
Y=66
W=190
H=16
Text=Espace Disque (#NAS_Drive#)
[meterNASDiskValue]
Meter=String
MeterStyle=styleCenterText
MeasureName=measureNASDiskUsed
MeasureName2=measureNASDiskTotal
X=100
Y=84
W=190
H=16
Text=%1B / %2B
NumOfDecimals=1
AutoScale=1
LeftMouseUpAction=[\"#NAS_Drive#\\\"]
IfCondition=measureNASDiskTotal = 0
IfTrueAction=[!SetOption meterNASDiskValue Text \"Lecteur non mappé\"]
[meterNASPercent]
Meter=String
MeterStyle=styleCenterText
MeasureName=measureNASPercent
X=100
Y=102
W=190
H=16
Text=%1% utilisé
NumOfDecimals=1
IfCondition=measureNASDiskTotal = 0
IfTrueAction=[!SetOption meterNASPercent Text \"\"]
[meterNASBar]
Meter=Bar
MeterStyle=styleBar
MeasureName=measureNASDiskUsed
X=10
Y=122
W=190
H=2Quels sont les autres infos que je peux rajouter ?Afficher plus

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-225-R225-MFok-problème-résolu-cette-version]]
- ⬇️ Next: [[Card-227-R227-Problème-résolu-cette-version-fonctionne]]
- 📊 MOC: [[_MOC_Rainmeter skin localization]]

## 🏷️ Topics

- #power-bi
- #python
- #receipts
- #automation
