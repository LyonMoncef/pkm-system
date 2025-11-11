---
type: chat-card
parent_export: '[[Export]]'
order: 303
role: assistant
created: '2025-11-11T00:47:15.791240Z'
tags:
- chat-card
- power-bi
attachments_count: 0
---

# 🤖 Message 303 - Assistant

**ID:** msg-303

## 💬 Content


**ID:** msg-303

Le problème vient probablement de l'include ou du Background. Testons avec une version minimaliste qui fonctionne à coup sûr :
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
Sauvegarde ce fichier et recharge le skin.
Si tu vois maintenant quelque chose, c'est que le problème venait de :

@include=#@#GlobalVariables.inc (fichier manquant ou erreur)
Background=#@#Background.png (fichier manquant)
ZPos=[&Z_STATE] (variable non définie)

Une fois que cette version test fonctionne, on pourra rajouter progressivement les autres éléments.
Dis-moi si tu vois maintenant le widget avec fond gris et le titre en couleur ! 🎯

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-302-R302-Problème-vient-probablement-include-Back]]
- ⬇️ Next: [[Card-304-R304-Problème-vient-probablement-include-Back]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]

## 🏷️ Topics

- #power-bi
