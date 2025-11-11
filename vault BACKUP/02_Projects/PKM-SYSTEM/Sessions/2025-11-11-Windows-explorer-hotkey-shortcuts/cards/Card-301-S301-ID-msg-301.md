---
type: chat-card
parent_export: '[[Export]]'
order: 301
role: user
created: '2025-11-11T00:47:15.759707Z'
tags:
- chat-card
- power-bi
attachments_count: 0
---

# 👤 Message 301 - User

**ID:** msg-301

## 💬 Content


**ID:** msg-301

j'essaie juste d'afficher le titre mais je vois 0 widget ; Widget Raccourcis Clavier PowerToys
; ----------------------------------
[Rainmeter]
Update=1000
Background=#@#Background.png
BackgroundMode=3
BackgroundMargins=0,50,0,30
@include=#@#GlobalVariables.inc
ZPos=[&Z_STATE]
; Définir la taille du widget
SkinWidth=270
SkinHeight=320
[Variables]
; Couleurs des jours
color0=255,50,50,205
color1=50,200,50,205
color2=255,165,0,205
color3=255,220,50,205
color4=150,50,200,205
color5=50,130,255,205
color6=255,140,0,205
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
X=100
Y=8
W=250
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
Text=Raccourcis Clavier
; Ligne séparatrice
[meterSeparator]
Meter=Shape
X=10
Y=42
W=240
H=2
Shape=Rectangle 0,0,240,1 | Fill Color [#color[&measureDayNumber]]
DynamicVariables=1

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-300-R300-Essaie-juste-afficher-titre-mais]]
- ⬇️ Next: [[Card-302-R302-Problème-vient-probablement-include-Back]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]

## 🏷️ Topics

- #power-bi
