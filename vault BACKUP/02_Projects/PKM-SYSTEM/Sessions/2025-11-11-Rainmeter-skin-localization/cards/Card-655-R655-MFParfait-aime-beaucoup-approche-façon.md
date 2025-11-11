---
type: chat-card
parent_export: '[[Export]]'
order: 655
role: assistant
created: '2025-11-11T00:21:49.780853Z'
tags:
- chat-card
- power-bi
- receipts
attachments_count: 0
---

# 🤖 Message 655 - Assistant

**ID:** msg-655

## 💬 Content


**ID:** msg-655

MFParfait, j'aime beaucoup l'approche et ta façon de rebondir pour aller vers l'objectif souhaité même quand c'est mal formulé GGOn continue avec les autres skins à adapter
; Lines starting ; (semicolons) are commented out.
; That is, they do not affect the code and are here for demonstration purposes only.
; ----------------------------------
; NOTE! If you want to add more disks, take a look at 'Disks 2.ini'.
[Rainmeter]
; This section contains general settings that can be used to change how Rainmeter behaves.
Update=1000
Background=#@#Background.png
; #@# is equal to Rainmeter\\Skins\\illustro\\@Resources
BackgroundMode=3
BackgroundMargins=0,34,0,20
[Metadata]
; Contains basic information of the skin.
Name=Disk
Author=poiru
Information=Displays disk usage.
License=Creative Commons BY-NC-SA 3.0
Version=1.0.0
[Variables]
; Variables declared here can be used later on between two # characters (e.g. #MyVariable#).
fontName=Trebuchet MS
textSize=10
colorBar=235,170,0,255
colorText=255,255,255,205
disk1=C:
; ----------------------------------
; MEASURES return some kind of value
; ----------------------------------
[measureTotalDisk1]
; This measure returns the total disk space
Measure=FreeDiskSpace
Drive=#disk1#
Total=1
UpdateDivider=120
[measureUsedDisk1]
; Returns inverted value of free disk space (i.e. used disk space)
Measure=FreeDiskSpace
Drive=#disk1#
InvertMeasure=1
UpdateDivider=120
[measurePercentUsed]
; Calculate percentage used
Measure=Calc
Formula=(measureUsedDisk1 / measureTotalDisk1) * 100
; ----------------------------------
; STYLES are used to \"centralize\" options
; ----------------------------------
[styleTitle]
StringAlign=Center
StringCase=Upper
StringStyle=Bold
StringEffect=Shadow
FontEffectColor=0,0,0,50
FontColor=#colorText#
FontFace=#fontName#
FontSize=11
AntiAlias=1
ClipString=1
[styleLeftText]
StringAlign=Left
; Meters using styleLeftText will be left-aligned.
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
[styleCenterText]
StringAlign=Center
StringCase=None
StringStyle=Bold
StringEffect=Shadow
FontEffectColor=0,0,0,20
FontColor=#colorText#
FontFace=#fontName#
FontSize=12
AntiAlias=1
ClipString=1
[styleBar]
BarColor=#colorBar#
BarOrientation=HORIZONTAL
SolidColor=255,255,255,15
; ----------------------------------
; METERS display images, text, bars, etc.
; ----------------------------------
[meterTitle]
Meter=String
MeterStyle=styleTitle
; Using MeterStyle=styleTitle will basically \"copy\" the
; contents of the [styleTitle] section here during runtime.
X=100
Y=12
W=190
H=18
Text=Disque #disk1#
; Even though the text is set to Disk, Rainmeter will display
; it as DISK, because styleTitle contains StringCase=Upper.
[meterValueDisk1]
Meter=String
MeterStyle=styleCenterText
MeasureName=measureUsedDisk1
MeasureName2=measureTotalDisk1
X=100
Y=40
W=190
H=16
Text=%1B / %2B
; %1 stands for the value of MeasureName (measureUsedDisk1 in this case).
; %2 stands for the value of MeasureName2.
NumOfDecimals=1
AutoScale=1
; Because disk measures return the free/used space in bytes, we must use AutoScale=1 to
; automatically scale the value into a more readable figure.
LeftMouseUpAction=[\"#disk1#\\\"]
; Open #disk1# on click
[meterPercentage]
Meter=String
MeterStyle=styleCenterText
MeasureName=measurePercentUsed
X=100
Y=58
W=190
H=16
Text=Rempli : %1%
NumOfDecimals=1
[meterBarDisk1]
Meter=Bar
MeterStyle=styleBar
MeasureName=measureUsedDisk1
X=10
Y=78
W=190
H=2Possible de rendre la jauge plus lisible ? Plus grosse avec un contour, une couleur en fonction du pourcentage pour la jauge
Le reste de la police suit la logique de couleur en fonction du jourAfficher plus

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-654-R654-Variables-Dimanche-Lundi-Mardi-measureDa]]
- ⬇️ Next: [[Card-656-R656-MFParfait-aime-beaucoup-approche-façon]]
- 📊 MOC: [[_MOC_Rainmeter skin localization]]

## 🏷️ Topics

- #power-bi
- #receipts
