---
type: chat-card
parent_export: '[[Export]]'
order: 593
role: assistant
created: '2025-11-11T00:21:49.103869Z'
tags:
- chat-card
- power-bi
attachments_count: 0
---

# 🤖 Message 593 - Assistant

**ID:** msg-593

## 💬 Content


**ID:** msg-593

MF; Test simple du skin Clock
; ----------------------------------
[Rainmeter]
Update=1000
Background=#@#Background.png
BackgroundMode=3
BackgroundMargins=0,34,0,20
[Variables]
@Include=#@#GlobalVariables.inc
@Include2=#@#ColorByDay.inc
[Metadata]
Name=Clock Test
Author=Custom
Information=Test simple
Version=1.0.0
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
FontColor=#colorDynamic#
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
FontColor=#colorDynamic#
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
FontColor=#colorDynamic#
AntiAlias=1
DynamicVariables=1
Text=%1Le texte est toujours en blanc après ajour du fichier colorbyday.incAfficher plus

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-592-R592-Test-simple-skin-Clock-Rainmeter]]
- ⬇️ Next: [[Card-594-R594-Test-simple-skin-Clock-Rainmeter]]
- 📊 MOC: [[_MOC_Rainmeter skin localization]]

## 🏷️ Topics

- #power-bi
