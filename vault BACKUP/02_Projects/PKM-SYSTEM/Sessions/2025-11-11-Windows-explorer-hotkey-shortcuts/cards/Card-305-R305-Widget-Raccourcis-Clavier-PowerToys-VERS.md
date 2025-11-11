---
type: chat-card
parent_export: '[[Export]]'
order: 305
role: assistant
created: '2025-11-11T00:47:15.811353Z'
tags:
- chat-card
- power-bi
attachments_count: 0
---

# 🤖 Message 305 - Assistant

**ID:** msg-305

## 💬 Content


**ID:** msg-305

ini; Widget Raccourcis Clavier PowerToys - VERSION TEST
; ----------------------------------
[Rainmeter]
Update=1000
BackgroundMode=2
SolidColor=40,40,40,255

[Variables]
; Couleurs des jours
color0=255,50,50,255
color1=50,200,50,255
color2=255,165,0,255
color3=255,220,50,255
color4=150,50,200,255
color5=50,130,255,255
color6=255,140,0,255

[Metadata]
Name=Shortcuts
Author=Custom
Information=Liste des raccourcis clavier PowerToys
Version=1.0.0

; ----------------------------------
; MEASURES
; ----------------------------------
[measureDayNumber]
Measure=Time
Format=%w

; ----------------------------------
; METERS
; ----------------------------------
[meterTitle]
Meter=String
X=135
Y=15
W=250
H=30
StringAlign=Center
StringCase=Upper
StringStyle=Bold
FontFace=Trebuchet MS
FontSize=14
FontColor=[#color[&measureDayNumber]]
AntiAlias=1
DynamicVariables=1
Text=RACCOURCIS CLAVIER

; Ligne séparatrice
[meterSeparator]
Meter=Shape
X=10
Y=50
W=250
H=2
Shape=Rectangle 0,0,250,1 | Fill Color [#color[&measureDayNumber]]
DynamicVariables=1

; --- PowerToys Zoom ---
[meterZoomTitle]
Meter=String
X=15
Y=65
StringStyle=Bold
FontFace=Trebuchet MS
FontSize=11
FontColor=[#color[&measureDayNumber]]
AntiAlias=1
DynamicVariables=1
Text=PowerToys Zoom

[meterZoom1]
Meter=String
X=20
Y=85
FontFace=Trebuchet MS
FontSize=9
FontColor=200,200,200,255
AntiAlias=1
Text=Activer zoom : Ctrl

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-304-R304-Problème-vient-probablement-include-Back]]
- ⬇️ Next: [[Card-306-R306-MFok-voison-fais-modifs-dans]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]

## 🏷️ Topics

- #power-bi
