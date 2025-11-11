---
type: chat-card
parent_export: '[[Export]]'
order: 597
role: assistant
created: '2025-11-11T00:21:49.148840Z'
tags:
- chat-card
- receipts
attachments_count: 0
---

# 🤖 Message 597 - Assistant

**ID:** msg-597

## 💬 Content


**ID:** msg-597

Le problème vient probablement du fait que les mesures s'exécutent après l'affichage initial. Ajoutons un UpdateDivider=-1 pour forcer l'exécution immédiate :ColorByDay.inc - Mesures de couleurCode ∙ Version 2 [measureDayNumber]
; Retourne le numéro du jour (0=Dimanche, 1=Lundi, etc.)
Measure=Time
Format=%w
UpdateDivider=-1

[measureDayColor]
; Change automatiquement la variable colorDynamic selon le jour
Measure=Calc
Formula=measureDayNumber
UpdateDividerAttendez, UpdateDivider=-1 n'existe pas. Le vrai problème c'est que les actions IfTrueAction s'exécutent après le premier rendu.
Voici la vraie solution - initialiser colorDynamic avec la bonne couleur dès le départ :Clock.ini - Version Test SimplifiéeCode ∙ Version 4 ; Clock avec couleur par jour
; ----------------------------------

[Rainmeter]
Update=1000
Background=#@#Background.png
BackgroundMode=3
BackgroundMargins=0,34,0,20
OnRefreshAction=[!UpdateMeasure measureDayNumber][!UpdateMeasure measureDayColor][!UJ'ai ajouté OnRefreshAction dans la section [Rainmeter] qui force les mesures à se mettre à jour immédiatement au chargement du skin.
Mais franchement, je pense qu'on se complique la vie. Voici une solution beaucoup plus simple qui fonctionne à coup sûr :Clock.ini - Version Simple qui MarcheCode ; Clock avec couleur par jour - VERSION SIMPLE
; ----------------------------------

[Rainmeter]
Update=1000
Background=#@#Background.png
BackgroundMode=3
BackgroundMargins=0,34,0,20

[Variables]
; Couleurs des jours
colorSunday=255,50,50,205
colorMoCette version utilise des formules conditionnelles inline dans FontColor - ça fonctionne immédiatement sans attendre de mise à jour !
La syntaxe [&measureDayNumber:] lit la valeur directement et applique la bonne couleur.
Testez cette version, elle devrait afficher la couleur correcte dès le chargement ! 🎨
Quelle version voulez-vous utiliser ? Celle avec OnRefreshAction ou celle avec les formules inline ?

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-596-R596-Problème-vient-probablement-fait-mesures]]
- ⬇️ Next: [[Card-598-R598-Problème-vient-probablement-fait-mesures]]
- 📊 MOC: [[_MOC_Rainmeter skin localization]]

## 🏷️ Topics

- #receipts
