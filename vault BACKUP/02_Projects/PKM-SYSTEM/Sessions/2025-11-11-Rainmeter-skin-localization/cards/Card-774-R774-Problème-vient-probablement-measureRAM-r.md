---
type: chat-card
parent_export: '[[Export]]'
order: 774
role: assistant
created: '2025-11-11T00:21:51.005370Z'
tags:
- chat-card
- power-bi
attachments_count: 0
---

# 🤖 Message 774 - Assistant

**ID:** msg-774

## 💬 Content


**ID:** msg-774

Ah, le problème vient probablement de [measureRAM:1] qui retourne la valeur en pourcentage mais pas forcément entre 0-100. Utilisons plutôt une mesure Calc pour garantir le bon calcul :System Monitor - Version mise à jourCode ∙ Version 6 [measureRAM]
Measure=PhysicalMemory
UpdateDivider=20

[measureRAMPercent]
Measure=Calc
Formula=(measureRAM / 4294967296) * 100
DynamicVariables=1

[measureSWAP]
Measure=SwapMemory
UpdateDivider=20

[measureSWAPPercent]
Measure=Calc
Formula=(measureSWAttendez, c'est trop compliqué. Le vrai problème c'est que Percentual=1 dans le Text n'affecte pas la mesure elle-même. Utilisons la solution la plus simple :System Monitor - Version mise à jourCode ∙ Version 7 ; System monitor - Formatage aligné sur Disk et Clock
; ----------------------------------

[Rainmeter]
Update=1000
Background=#@#Background.png
BackgroundMode=3
BackgroundMargins=0,50,0,30

[Variables]
; Couleurs des jours (R,G,B,A)
color0=255,50,50Voilà ! J'ai remplacé les Meter=Shape par des Meter=Bar classiques pour les barres de remplissage.
🔧 Changement :
Au lieu de calculer manuellement la largeur avec Shape, j'utilise maintenant le type Bar natif de Rainmeter qui :

✅ Gère automatiquement les pourcentages (0-100%)
✅ Ne dépassera jamais la largeur définie (W=188)
✅ Fonctionne directement avec measureRAM et measureSWAP

Les barres devraient maintenant rester parfaitement dans les limites ! 🎯
Testez et dites-moi si c'est bon ! 👍Réessayer

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-773-S773-ID-msg-773]]
- ⬇️ Next: [[Card-775-R775-Problème-vient-probablement-measureRAM-r]]
- 📊 MOC: [[_MOC_Rainmeter skin localization]]

## 🏷️ Topics

- #power-bi
