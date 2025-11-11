---
type: chat-card
parent_export: '[[Export]]'
order: 720
role: assistant
created: '2025-11-11T00:21:50.485426Z'
tags:
- chat-card
- power-bi
attachments_count: 0
---

# 🤖 Message 720 - Assistant

**ID:** msg-720

## 💬 Content


**ID:** msg-720

; Clock avec couleur par jour - VERSION FONCTIONNELLE
; ----------------------------------
[Rainmeter]
Update=1000
Background=#@#Background.png
BackgroundMode=3
BackgroundMargins=0,34,0,20
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
Version=2.0.0
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
[measureColor]
Measure=String
String=[#color[&measureDayNumber]]
DynamicVariables=1
; ----------------------------------
; METERS
; ----------------------------------
[meterTitle]
Meter=String
MeasureName=measureTime
X=100
Y=12
W=190
H=18
StringAlign=Center
StringCase=Upper
StringStyle=Bold
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
Y=40
W=190
H=16
StringAlign=Left
StringStyle=Bold
FontFace=Trebuchet MS
FontSize=10
FontColor=[#color[&measureDayNumber]]
AntiAlias=1
DynamicVariables=1
Text=%1
[meterDate]
Meter=String
MeasureName=measureDate
X=200
Y=40
W=190
H=16
StringAlign=Right
StringStyle=Bold
FontFace=Trebuchet MS
FontSize=10
FontColor=[#color[&measureDayNumber]]
AntiAlias=1
DynamicVariables=1
Text=%1Afficher plus

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-719-R719-Clock-avec-couleur-jour-VERSION]]
- ⬇️ Next: [[Card-721-S721-ID-msg-721]]
- 📊 MOC: [[_MOC_Rainmeter skin localization]]

## 🏷️ Topics

- #power-bi
