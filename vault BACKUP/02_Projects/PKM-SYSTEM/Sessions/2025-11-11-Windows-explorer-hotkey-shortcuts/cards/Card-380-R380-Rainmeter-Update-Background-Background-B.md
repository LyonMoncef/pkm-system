---
type: chat-card
parent_export: '[[Export]]'
order: 380
role: assistant
created: '2025-11-11T00:47:16.644250Z'
tags:
- chat-card
- receipts
attachments_count: 0
---

# 🤖 Message 380 - Assistant

**ID:** msg-380

## 💬 Content


**ID:** msg-380

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

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-379-R379-Variables-fontName-Trebuchet-textSize-ti]]
- ⬇️ Next: [[Card-381-R381-Rainmeter-ZPos-MeterToggleClick-LeftMous]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]

## 🏷️ Topics

- #receipts
