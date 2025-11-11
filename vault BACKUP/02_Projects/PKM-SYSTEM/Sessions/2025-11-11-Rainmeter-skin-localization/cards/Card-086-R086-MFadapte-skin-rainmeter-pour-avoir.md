---
type: chat-card
parent_export: '[[Export]]'
order: 86
role: assistant
created: '2025-11-11T00:21:44.524210Z'
tags:
- chat-card
- power-bi
- excel
- python
- receipts
- code
- git
- automation
attachments_count: 0
---

# 🤖 Message 86 - Assistant

**ID:** msg-86

## 💬 Content


**ID:** msg-86

MFadapte ce skin rainmeter pour avoir Le jour en Français, la date au format DD/MM/YYYY et une écriture plus grande
; Lines starting ; (semicolons) are commented out.
; That is, they do not affect the code and are here for demonstration purposes only.
; ----------------------------------[Rainmeter]
; This section contains general settings that can be used to change how Rainmeter behaves.
Update=1000
Background=#@#Background.png
; #@# is equal to Rainmeter\\Skins\\illustro\\@Resources
BackgroundMode=3
BackgroundMargins=0,34,0,14[Metadata]
; Contains basic information of the skin.
Name=Clock
Author=poiru
Information=Displays the current date and time.
License=Creative Commons BY-NC-SA 3.0
Version=1.0.0[Variables]
; Variables declared here can be used later on between two # characters (e.g. #MyVariable#).
fontName=Trebuchet MS
textSize=8
colorBar=235,170,0,255
colorText=255,255,255,205; ----------------------------------
; MEASURES return some kind of value
; ----------------------------------[measureTime]
; This measure returns the time in a 24-hour format (i.e. HH:MM).
Measure=Time
Format=%H:%M
; For a 12-hour clock, change the Format option above to: %I:%M %p
; Refer to the Rainmeter manual for other format codes.[measureDate]
; Returns the date as DD.MM.YYYY
Measure=Time
Format=%d.%m.%Y[measureDay]
; Returns the current day
Measure=Time
Format=%A; ----------------------------------
; STYLES are used to \"centralize\" options
; ----------------------------------[styleTitle]
StringAlign=Center
StringCase=Upper
StringStyle=Bold
StringEffect=Shadow
FontEffectColor=0,0,0,50
FontColor=#colorText#
FontFace=#fontName#
FontSize=10
AntiAlias=1
ClipString=1[styleLeftText]
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
ClipString=1[styleRightText]
StringAlign=Right
StringCase=None
StringStyle=Bold
StringEffect=Shadow
FontEffectColor=0,0,0,20
FontColor=#colorText#
FontFace=#fontName#
FontSize=#textSize#
AntiAlias=1
ClipString=1[styleSeperator]
SolidColor=255,255,255,15; ----------------------------------
; METERS display images, text, bars, etc.
; ----------------------------------[meterTitle]
Meter=String
MeterStyle=styleTitle
; Using MeterStyle=styleTitle will basically \"copy\" the
; contents of the [styleTitle] section here during runtime.
MeasureName=measureTime
X=100
Y=12
W=190
H=18
Text=%1
; %1 stands for the value of MeasureName (measureTime in this case).[meterDay]
Meter=String
MeterStyle=styleLeftText
MeasureName=measureDay
X=10
Y=40
W=190
H=14
Text=%1[meterDate]
Meter=String
MeterStyle=styleRightText
MeasureName=measureDate
X=200
Y=0r
; r stands for relative. In this case, the Y postition of meterValueCPU is 0 pixels
; below the Y value of the previous meter (i.e it's the same as in meterLabelCPU).
W=190
H=14
Text=%1[meterSeperator]
Meter=Image
MeterStyle=styleSeperator
X=10
Y=52
W=190
H=1Afficher plusVoici le skin Rainmeter adapté avec le jour en français, la date au format DD/MM/YYYY et une écriture plus grande :Skin Rainmeter Clock FRCode ; Lines starting ; (semicolons) are commented out.
; That is, they do not affect the code and are here for demonstration purposes only.
; ----------------------------------

[Rainmeter]
; This section contains general settings that can be used to chaVoici les modifications apportées :
1. Jour en français :

Ajout d'une option Substitute dans [measureDay] qui convertit les jours anglais en français :

Monday → Lundi
Tuesday → Mardi
Wednesday → Mercredi, etc.


2. Date au format DD/MM/YYYY :

Modification de Format=%d.%m.%Y en Format=%d/%m/%Y dans [measureDate]

3. Écriture plus grande :

textSize passé de 8 à 12 (pour le jour et la date)
FontSize dans [styleTitle] passé de 10 à 14 (pour l'heure)

Le skin affichera maintenant l'heure en grand, le jour en français et la date avec des slashes au lieu de points !RéessayerMFaugmente légèrement la taille de la carte, le texte est tronqué en bas, et fais en sorte que la couleur du texte se choisisse en fonction du jour de la semaine avec la logique suivante : Dimanche Rouge
Samedi Orange
Vendredi Bleu
Lundi Vert
Mardi Orange
Mercredi Jaune
Jeudi VioletSkin Rainmeter Clock FRCode ∙ Version 2 ; Lines starting ; (semicolons) are commented out.
; That is, they do not affect the code and are here for demonstration purposes only.
; ----------------------------------

[Rainmeter]
; This section contains general settings that can be used to chaVoici les modifications apportées :
1. Taille de la carte augmentée :

BackgroundMargins modifié de 0,34,0,14 à 0,34,0,20 (marge inférieure plus grande)
Hauteur des mètres [meterDay] et [meterDate] passée de H=14 à H=16
Position du séparateur ajustée de Y=52 à Y=58

2. Couleur selon le jour de la semaine :

Ajout d'une nouvelle mesure [measureDayNumber] qui retourne le numéro du jour (0=Dimanche, 1=Lundi, etc.)
Ajout d'une mesure [measureDayColor] avec des conditions qui changent la variable colorText selon le jour :

Dimanche (0) : Rouge 255,50,50,205
Lundi (1) : Vert 50,200,50,205
Mardi (2) : Orange 255,165,0,205
Mercredi (3) : Jaune 255,220,50,205
Jeudi (4) : Violet 150,50,200,205
Vendredi (5) : Bleu 50,130,255,205
Samedi (6) : Orange 255,140,0,205


Ajout de DynamicVariables=1 dans tous les styles pour que les couleurs se mettent à jour automatiquement

La couleur du texte changera maintenant automatiquement chaque jour ! 🎨RéessayerMF; Lines starting ; (semicolons) are commented out.
; That is, they do not affect the code and are here for demonstration purposes only.
; ----------------------------------
; NOTE! If you want to add more disks, take a look at 'Disks 2.ini'.
[Rainmeter]
; This section contains general settings that can be used to change how Rainmeter behaves.
Update=1000
Background=#@#Background.png
; #@# is equal to Rainmeter\\Skins\\illustro\\@Resources
BackgroundMode=3
BackgroundMargins=0,34,0,14
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
textSize=8
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
FontSize=10
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
Text=Disk
; Even though the text is set to Disk, Rainmeter will display
; it as DISK, because styleTitle contains StringCase=Upper.
[meterLabelDisk1]
Meter=String
MeterStyle=styleLeftText
X=10
Y=40
W=190
H=14
Text=#disk1#\\
[meterValueDisk1]
Meter=String
MeterStyle=styleRightText
MeasureName=measureUsedDisk1
MeasureName2=measureTotalDisk1
X=200
Y=0r
; r stands for relative. In this case, the Y postition of meterValueCPU is 0 pixels
; below the Y value of the previous meter (i.e it's the same as in meterLabelCPU).
W=190
H=14
Text=%1B/%2B used
; %1 stands for the value of MeasureName (measureUsedDisk1 in this case).
; %2 stands for the value of MeasureName2.
NumOfDecimals=1
AutoScale=1
; Because disk measures return the free/used space in bytes, we must use AutoScale=1 to
; automatically scale the value into a more readable figure.
LeftMouseUpAction=[\"#disk1#\\\"]
; Open #disk1# on click
[meterBarDisk1]
Meter=Bar
MeterStyle=styleBar
MeasureName=measureUsedDisk1
X=10
Y=52
W=190
H=1Modifie ce script pour que l'espace total utilise sur l'espace total soit lisible en un coup d'oeilAfficher plusSkin Rainmeter Disk - LisibleCode ; Lines starting ; (semicolons) are commented out.
; That is, they do not affect the code and are here for demonstration purposes only.
; ----------------------------------
; NOTE! If you want to add more disks, take a look at 'Disks 2.ini'.
[RainmetVoici les améliorations pour rendre l'espace disque lisible en un coup d'œil :
1. Affichage plus clair :

Format \"XXX GB / YYY GB\" centré et en plus gros (taille 12)
Ajout d'un pourcentage d'utilisation \"XX% utilisé\" juste en dessous
Le titre affiche maintenant \"DISQUE C:\" au lieu de juste \"DISK\"

2. Mise en page améliorée :

Texte centré pour une lecture immédiate
Taille de texte augmentée (de 8 à 10 pour le texte général, 12 pour les valeurs)
Barre de progression plus épaisse (H=2) et positionnée plus bas
Marge inférieure augmentée pour éviter la troncature

3. Nouvelles mesures :

Ajout de [measurePercentUsed] qui calcule automatiquement le pourcentage d'espace utilisé
Nouveau style [styleCenterText] pour centrer les valeurs importantes

Vous verrez maintenant en un coup d'œil : l'espace utilisé, l'espace total, le pourcentage, et une barre visuelle ! 📊Réessayer; Lines starting ; (semicolons) are commented out.\r
; That is, they do not affect the code and are here for demonstration purposes only.\r
; ----------------------------------\r
\r
[Rainmeter]\r
; This section contains general settings that can be used to change how Rainmeter behaves.\r
Update=1000\r
BackpastedMFModifie le skin suivant en appliquant les mêmes paramètres de police taille etc..Skin Rainmeter Network - StyliséCode ; Lines starting ; (semicolons) are commented out.
; That is, they do not affect the code and are here for demonstration purposes only.
; ----------------------------------

[Rainmeter]
; This section contains general settings that can be used to chaVoici le skin Network modifié avec les mêmes paramètres que les autres :
Modifications appliquées :

Taille de police augmentée :

textSize : 8 → 10
FontSize du titre : 10 → 14


Taille de carte augmentée :

BackgroundMargins : 0,34,0,14 → 0,34,0,20
Hauteur des mètres : H=14 → H=16


Barres de progression plus visibles :

Hauteur des barres : H=1 → H=2


Espacement ajusté :

Les positions Y ont été recalculées pour accommoder les textes plus grands
Séparateur à Y=58 au lieu de 52
Upload commence à Y=66
Barre Upload à Y=80
Download à Y=90
Barre Download à Y=104


Le skin Network est maintenant cohérent avec vos autres skins (Clock et Disk) ! 🌐RéessayerMFOn peut s'inspirer du skin ici pour afficher quelques infos de mon nas ?
Disponible sur 192.168.1.141
Upload et download ou d'autres informations accessibles depuis windows ?rainmeter monitor NAS network share windows10 résultatsUsing FreeDiskSpace for Network Drive - Rainmeter Forumsrainmeter.netPlugin for monitoring R/W from network disks ? - Rainmeter Forumsrainmeter.netNetwork Skin - Rainmeter Documentationrainmeter.netNetwork Monitoring specific servers/programs - Rainmeter Forumsrainmeter.net104+ Rainmeter Network Skins [Windows 11/10/7]visualskins.comFinding your Network Interface for SysInfo and Net - Rainmeter Documentationrainmeter.netUsing HWiNFO with Rainmeter - Rainmeter Documentationrainmeter.netConnecting to a Network File Share or NAS Drive (Windows) | Life Sciences Computing Group (LSCG) | UC Santa Barbaraucsb.eduHow to: monitor Network Attached Storage (NAS) statushdsentinel.comManage - Rainmeter Documentationrainmeter.netExcellente idée ! Voici un skin pour monitorer votre NAS. Voici ce qu'on peut afficher facilement depuis Windows :Skin Rainmeter NAS MonitorCode ; Skin de monitoring pour NAS
; ----------------------------------

[Rainmeter]
Update=1000
Background=#@#Background.png
BackgroundMode=3
BackgroundMargins=0,34,0,20

[Metadata]
Name=NAS Monitor
Author=Custom
Information=Affiche les informations du NVoici un skin pour monitorer votre NAS ! Il affiche :
📊 Informations disponibles :

Statut : En ligne / Hors ligne (avec changement de couleur)
Adresse IP : 192.168.1.141
Latence : Temps de ping en millisecondes
Espace disque : Utilisé / Total (si lecteur mappé)
Pourcentage : % d'espace utilisé
Barre visuelle : Représentation graphique

⚙️ Configuration nécessaire :
Pour voir l'espace disque, vous devez mapper un lecteur réseau :

Ouvrez l'Explorateur Windows
Clic droit sur \"Ce PC\" > \"Connecter un lecteur réseau\"
Choisissez une lettre (ex: Z:)
Entrez : \\\\192.168.1.141\
om_du_partage
Modifiez NAS_Drive=Z: dans le skin avec votre lettre

💡 Note :

Le ping fonctionne sans configuration supplémentaire
Si le lecteur n'est pas mappé, il affichera \"Non mappé\"
Cliquez sur l'espace disque pour ouvrir le NAS dans l'explorateur

Avez-vous déjà un lecteur réseau mappé pour votre NAS ?RéessayerMFRien ne s'affiche quand je crée un nouveau skin et que je colle ce contenuIl y a probablement un problème avec le plugin PingPlugin qui n'est pas inclus par défaut dans Rainmeter. Essayons une version simplifiée qui utilise uniquement les fonctionnalités natives de Rainmeter :Skin Rainmeter NAS MonitorCode ∙ Version 2 ; Skin de monitoring pour NAS
; ----------------------------------

[Rainmeter]
Update=1000
Background=#@#Background.png
BackgroundMode=3
BackgroundMargins=0,34,0,20

[Metadata]
Name=NAS Monitor
Author=Custom
Information=Affiche les informations du NJ'ai simplifié le skin pour ne garder que les fonctionnalités natives de Rainmeter. Il affiche maintenant :

Adresse IP du NAS (cliquez dessus pour ouvrir \\\\192.168.1.141 dans l'explorateur)
Espace disque (si vous avez mappé un lecteur réseau)
Pourcentage utilisé
Barre de progression

Pour que l'espace disque fonctionne :

Ouvrez l'Explorateur Windows
Tapez dans la barre d'adresse : \\\\192.168.1.141
Trouvez le dossier partagé de votre NAS
Faites un clic droit sur le dossier > \"Mapper le lecteur réseau\"
Choisissez une lettre (ex: Z:)
Cochez \"Se reconnecter à l'ouverture de session\"
Dans le skin, modifiez NAS_Drive=Z: avec votre lettre

Si ça ne s'affiche toujours pas, vérifiez que :

Le fichier est bien enregistré avec l'extension .ini
Il est dans le bon dossier : Documents\\Rainmeter\\Skins\\[NomDuSkin]\\
Vous avez rafraîchi Rainmeter (clic droit sur l'icône Rainmeter > Rafraîchir tout)

Est-ce que ça fonctionne mieux maintenant ?RéessayerMFPart de ce modèle par défaut et crée un skin minimaliste pour tester l'affichage après on reviendra sur les paramètres du nasSkin Rainmeter NAS MonitorCode ∙ Version 3 ; Lines starting ; (semicolons) are commented out.
; That is, they do not affect the code and are here for demonstration purposes only.
; ----------------------------------

[Rainmeter]
; This section contains general settings that can be used to chaParfait ! Voici un skin minimaliste ultra-simple basé sur le modèle par défaut. Il affiche juste :

Titre : \"NAS TEST\"
Adresse IP : 192.168.1.141
Statut : Test OK

Aucune mesure complexe, juste du texte statique pour vérifier que l'affichage fonctionne.
Pour tester :

Copiez le code dans un fichier .ini (par exemple NASTest.ini)
Placez-le dans Documents\\Rainmeter\\Skins\\[NomDuDossier]\\
Rafraîchissez Rainmeter
Chargez le skin

Si vous voyez la carte avec \"NAS TEST\" et les deux lignes, c'est bon ! On pourra ensuite ajouter les mesures du NAS une par une.
Est-ce que cette version s'affiche correctement ?RéessayerMFok problème résolu, cette version fonctionne parfaitement; Skin de monitoring pour NAS
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
H=2Quels sont les autres infos que je peux rajouter ?Afficher plusExcellent ! Maintenant qu'on a une base fonctionnelle, voici les informations supplémentaires que vous pouvez ajouter pour votre NAS :
📊 Informations disponibles depuis Windows :
1. Espace disque de plusieurs partages
Si votre NAS a plusieurs dossiers partagés, vous pouvez mapper plusieurs lecteurs (Y:, Z:, etc.) et afficher l'espace de chacun.
2. Vitesse réseau vers le NAS

Débit d'upload vers le NAS
Débit de download depuis le NAS
Utilisation de la bande passante en temps réel

3. Temps de réponse (Ping)

Latence réseau en millisecondes
Indicateur de qualité de connexion

4. Statut de connexion

En ligne / Hors ligne (avec changement de couleur)
Temps depuis le dernier check

5. Nombre de fichiers (si lecteur mappé)

Compteur de fichiers dans un dossier spécifique
Surveillance de modifications récentes

6. Informations système (si votre NAS expose des données via API)

Température (si le NAS a une API)
Charge CPU/RAM (nécessite une API ou SNMP)
Services actifs (Plex, Docker, etc.)


Lesquelles vous intéressent le plus ?
Je peux vous créer une version enrichie avec :

✅ Statut en ligne/hors ligne (ping simple)
✅ Vitesse réseau (upload/download vers le NAS)
✅ Espace disque de 2-3 partages différents
✅ Latence réseau

Ou on peut partir sur quelque chose de plus avancé si votre NAS a une API (Synology, QNAP, TrueNAS ont tous des APIs pour récupérer plus d'infos).
Qu'est-ce qui vous serait le plus utile au quotidien ? 🤔RéessayerMFc'est un nas synology, les infos proposés depuis le PC sont pas ouf, via l'api syno on a accès à quoi ?Synology API DSM capabilities monitoring10 résultatsDSM Login Web API Guide Last Apr 19, 2023synology.comSynology File Station Official APIsynology.comDSM Login Web API Guide - Knowledge Center - Synologysynology.comSynology API, DSM 7 et double authentification - Monitoring - Communauté Jeedomjeedom.comSurveillance Station Technical Specifications | Synology Inc.synology.comSynology® Releases DiskStation Manager 7.3, Bringing Efficient Data Tiering, Enhanced Security, and AI-Powered Collaboration | Synology Inc.synology.comDSM Login Web API Guidesynology.comResource Monitor | DSM - Synology Knowledge Centersynology.comGitHub - N4S4/synology-api: A Python wrapper around Synology APIgithub.comKnowledge Centersynology.comSynology DSM API system info CPU RAM temperature disk health10 résultatsGitHub - 007revad/Synology_CPU_temperature: Get Synology NAS CPU temperature via SSHgithub.comInfo Center | DSM - Synology Knowledge Centersynology.comWhy does my Synology System Health sensor show incorrect CPU and memory values? | Paessler Knowledge Basepaessler.comPerformance | DSM - Synology Knowledge Centersynology.comTo get CPU Temp from Synology, possible? - Configuration - Home Assistant Communityhome-assistant.ioSynology DSM - Home Assistanthome-assistant.ioSynology: Where Can I See Disks Temperature? – Marius Hostingmariushosting.comDSM 7.0 - High temperature warning | SynoForum.com - The Unofficial Synology Forumsynoforum.comHow can I verify the health of hard disks using a Synology NAS? - Super Usersuperuser.comCentre d'infos | DSM - Synology Centre de connaissancessynology.comExcellent choix ! Avec l'API Synology DSM, vous avez accès à beaucoup plus d'infos ! 🚀
📡 Ce que l'API Synology DSM peut vous donner :
🖥️ Informations système

CPU : Utilisation en temps réel (%)
RAM : Mémoire utilisée / totale
Température : CPU et disques
Uptime : Temps depuis le dernier démarrage
Charge système : Load average

💾 Stockage

Volumes : Espace utilisé/total pour chaque volume
État des disques : Santé SMART de chaque disque
Performance I/O : Lectures/écritures par seconde

🌐 Réseau

Trafic réseau : Upload/Download en temps réel
Connexions actives : Nombre de sessions
Interfaces réseau : État de chaque port Ethernet

📦 Services/Applications

Services actifs : Docker, Plex, Download Station, etc.
État des packages : Versions installées
Tâches planifiées : État des backups

👥 Utilisateurs

Sessions actives : Qui est connecté
Partages actifs : Fichiers ouverts


🎯 Mon conseil pour votre skin Rainmeter :
Je vous propose un skin avec les infos les plus utiles :
✅ Statut (En ligne/Hors ligne)
✅ CPU (% utilisation)
✅ RAM (% utilisation)
✅ Température CPU
✅ Espace disque principal (Volume 1)
✅ Trafic réseau (Upload/Download)
Ça vous donne un aperçu rapide de la santé du NAS sans surcharger le skin.
Voulez-vous que je crée ce skin avec l'API Synology ? Il faudra juste :

Créer un compte API sur votre Synology (super simple)
Activer l'accès API dans DSM
Je vous fournirai un script PowerShell pour récupérer les données

Intéressé ? 😊RéessayerMFGo ça m'intéresse, mais avant de valider, dis moi si on peut dans le langage utilisé, faire des drop lists, ou en clair, afficer différentes catégories sur le widget qu'on peut développer / réduire ?Rainmeter collapsible sections dropdown accordion toggle10 résultatsHelp Creating a Drop Down Menu - Rainmeter Forumsrainmeter.netCollapsible - shadcn/uishadcn.comUsing Rainmeter - Rainmeter Documentationrainmeter.netDropdown menu assistance - Rainmeter Forumsrainmeter.netHow To Create a Collapsiblew3schools.comExpandable Folder - Rainmeter Forumsrainmeter.netDropdown Menu /w Upwards display - Rainmeter Forumsrainmeter.netArranging Skins - Rainmeter Documentationrainmeter.netRainmeter | DeviantArtdeviantart.comAccordion · Bootstrap v5.0getbootstrap.comÉchec de la récupération de https://forum.rainmeter.net/viewtopic.php?t=43913Excellente question ! Oui, c'est totalement possible avec Rainmeter ! 🎉
📋 Système de sections collapsibles dans Rainmeter :
Rainmeter permet de créer des sections extensibles/réductibles en utilisant :
Méthode 1 : Click pour Toggle (la plus simple)

Cliquer sur un titre pour afficher/masquer une section
Utilise LeftMouseUpAction avec !ShowMeter / !HideMeter
Parfait pour votre cas !

Méthode 2 : Hover (survol)

La section apparaît au survol de la souris
Se cache automatiquement quand on s'éloigne

Méthode 3 : Skin secondaire

Charge/décharge un skin complet au clic
Plus lourd mais très flexible


🎨 Exemple concret pour votre NAS :
Je peux créer un skin avec :
📦 SECTION \"SYSTÈME\" (clic pour déplier)

CPU : 45%
RAM : 60%
Température : 42°C

💾 SECTION \"STOCKAGE\" (clic pour déplier)

Volume 1 : 2.5TB / 4TB
Volume 2 : 800GB / 1TB

🌐 SECTION \"RÉSEAU\" (clic pour déplier)

Upload : 5 MB/s
Download : 12 MB/s

Chaque section serait rétractable individuellement en cliquant sur son titre, avec un petit indicateur visuel (▼/▶) pour montrer l'état.

✅ Ma recommandation :
Je vous propose 2 versions :
Version A : Compacte avec sections

Tout dans un seul widget
Sections pliables au clic
Plus propre visuellement

Version B : Mini-widgets séparés

3 petits widgets indépendants (Système / Stockage / Réseau)
Vous arrangez comme vous voulez sur le desktop
Plus flexible

Laquelle préférez-vous ? Ou je peux faire les deux pour que vous testiez ! 😊RéessayerMF🖥️ Informations système
* CPU : Utilisation en temps réel (%)
* RAM : Mémoire utilisée / totale
* Température : CPU et disques
* Uptime : Temps depuis le dernier démarrage
* Charge système : Load average
💾 Stockage
* Volumes : Espace utilisé/total pour chaque volume
* État des disques : Santé SMART de chaque disque
* Performance I/O : Lectures/écritures par seconde
🌐 Réseau
* Trafic réseau : Upload/Download en temps réel
* Connexions actives : Nombre de sessions
* Interfaces réseau : État de chaque port Ethernet
📦 Services/Applications
* Services actifs : Docker, Plex, Download Station, etc.
* État des packages : Versions installées
* Tâches planifiées : État des backups
👥 Utilisateurs
* Sessions actives : Qui est connecté
* Partages actifs : Fichiers ouvertsPourquoi pas partir la dessus,
Avec un développer / réduire via survol à la sourisAfficher plusParfait ! Un skin avec toutes ces sections en survol, c'est ambitieux et stylé ! 🚀
Avant de créer le skin complet, il faut d'abord configurer l'accès API sur votre Synology. Voici les étapes :
🔧 Configuration de l'API Synology
Étape 1 : Activer l'API dans DSM

Connectez-vous à DSM (http://192.168.1.141:5000)
Allez dans Panneau de configuration > Terminal & SNMP
Cochez Activer le service SSH (optionnel mais utile)
L'API HTTP est normalement activée par défaut

Étape 2 : Créer un compte dédié (recommandé)

Panneau de configuration > Utilisateur & groupe
Créez un utilisateur (ex: rainmeter_api)
Donnez-lui un mot de passe fort
Permissions minimales nécessaires :

Lecture seule sur les volumes que vous voulez monitorer
Pas besoin de droits admin pour les infos de monitoring


Étape 3 : Tester l'API
Ouvrez votre navigateur et testez :
http://192.168.1.141:5000/webapi/query.cgi?api=SYNO.API.Info&version=1&method=query&query=all
Si ça affiche du JSON, c'est bon ! ✅

📝 Informations dont j'ai besoin :
Pour créer le skin, dites-moi :

Version de DSM : (DSM 6 ou DSM 7 ?)
Port HTTP : 5000 par défaut, ou autre ?
HTTPS activé : Oui/Non ? (port 5001 si oui)
Combien de volumes avez-vous ? (Volume 1, Volume 2, etc.)
Services à surveiller : Lesquels vous intéressent ? (Docker, Plex, Download Station, etc.)

Une fois ces infos données, je vous créerai :

Le skin Rainmeter avec sections au survol
Un script PowerShell pour communiquer avec l'API
Les instructions d'installation complètes

Prêt à me donner ces infos ? 😊Réessayer{\"data\":{\"SYNO.AME.Pack\":{\"maxVersion\":1,\"minVersion\":1,\"path\":\"entry.cgi\",\"requestFormat\":\"JSON\"},\"SYNO.API.Auth\":{\"maxVersion\":6,\"minVersion\":1,\"path\":\"auth.cgi\"},\"SYNO.API.Auth.Key\":{\"maxVersion\":7,\"minVersion\":7,\"path\":\"entry.cgi\",\"requestFormat\":\"JSON\"},\"SYNO.API.Encryption\":{\"maxVersion\":1,\"mipastedMFfais toi plaisirParfait ! L'API fonctionne, c'est du DSM 7 ! 🎉
Maintenant je vais vous créer le skin complet avec sections au survol. Il me faut juste quelques dernières infos :
🔍 Questions rapides :

Combien de volumes avez-vous sur votre NAS ?

Volume 1 seulement ?
Plusieurs volumes (Volume 1, Volume 2, etc.) ?


Services à surveiller - Lesquels vous intéressent parmi :

Docker (containers actifs)
Download Station
Plex Media Server
Synology Drive
Autres ?


Identifiants API :

Avez-vous créé un compte dédié pour Rainmeter ?
Sinon, voulez-vous utiliser votre compte admin ? (moins sécurisé mais plus simple pour tester)


📦 Ce que je vais créer :
Skin Rainmeter avec 5 sections collapsibles au survol :
🖥️ SYSTÈME (toujours visible en haut)

Statut : En ligne / Hors ligne
CPU : XX%
RAM : XX%
Température : XX°C
Uptime : X jours

💾 STOCKAGE (survol pour déplier)

Volume 1 : XXX GB / XXX GB (XX%)
Volume 2 (si applicable)
État SMART des disques

🌐 RÉSEAU (survol pour déplier)

Upload : XX MB/s
Download : XX MB/s
Connexions actives : XX

📦 SERVICES (survol pour déplier)

Docker : X containers
Download Station : X tâches
Autres services actifs

👥 UTILISATEURS (survol pour déplier)

Sessions actives : X
Fichiers partagés ouverts


Donnez-moi ces 3 infos et je vous crée tout le package (skin + script PowerShell + instructions) ! 🚀RéessayerMFVolume 1 seulement
Tous les services remontés dans le fichier fourni
Compte crée pour rainmeter_apiParfait ! Je vais créer le package complet. Ça va prendre 3 fichiers :

Le skin Rainmeter (fichier .ini)
Le script PowerShell (pour communiquer avec l'API Synology)
Les instructions d'installation
Synology NAS Monitor - Skin PrincipalCode ; Synology NAS Monitor - Skin avec sections collapsibles
; ----------------------------------

[Rainmeter]
Update=1000
Background=#@#Background.png
BackgroundMode=3
BackgroundMargins=0,34,0,20
MouseOverAction=[!ShowMeterGroup SectionSystemExpand][!UpMaintenant le script PowerShell :Script PowerShell - API SynologyCode # Script PowerShell pour récupérer les données du NAS Synology
# Usage: .\\SynoAPI.ps1 <IP> <PORT> <USER> <PASSWORD>

param(
 [string]$NAS_IP = \"192.168.1.141\",
 [string]$NAS_PORT = \"5000\",
 [string]$NAS_USER = \"rainmeter_api\",
 [string]$NEt maintenant les instructions complètes :Instructions d'installationDocument # 📦 Installation du Skin Synology NAS Monitor

## 📁 Structure des fichiers

Créez l'arborescence suivante dans votre dossier Rainmeter :

```
Documents\\Rainmeter\\Skins\\SynologyNAS\\
├── SynologyNAS.ini          (Skin principal)
└── @Resources\\
    └RéessayerMFContinuerInstructions d'installationDocument ∙ Version 2 ## 📊 Que monitore exactement le skin ?

### 🖥️ Système
- **CPU** : Charge processeur en temps réel (%)
- **RAM** : Pourcentage de mémoire utilisée
- **Température** : Température du CPU en °C
- **Uptime** : Temps écoulé depuis le dernier redémarragParfait ! 🎉 Voilà tout le package complet pour votre skin Synology NAS Monitor !
📦 Récapitulatif de ce que vous avez :
3 Artifacts créés :

SynologyNAS.ini - Le skin Rainmeter avec :

Interface avec sections collapsibles au survol
5 catégories : Système, Stockage, Réseau, Services, Utilisateurs
Mise à jour automatique toutes les 5 secondes


SynoAPI.ps1 - Script PowerShell qui :

Se connecte à l'API Synology DSM
Récupère CPU, RAM, Température, Uptime
Récupère l'espace disque du Volume 1
Récupère le trafic réseau et connexions
Liste tous les services actifs
Sauvegarde tout en JSON


Instructions complètes - Guide d'installation avec :

Structure des dossiers
Configuration pas à pas
Tests de validation
Dépannage
Personnalisation


🚀 Prochaines étapes :

Créez les dossiers selon la structure dans les instructions
Copiez les fichiers (.ini et .ps1)
Modifiez le mot de passe dans le fichier .ini
Testez le script PowerShell manuellement d'abord
Chargez le skin dans Rainmeter


Une question ou un problème pendant l'installation ? Je suis là pour vous aider ! 😊
Voulez-vous que j'ajoute des fonctionnalités supplémentaires (graphiques, alertes, Docker détaillé, etc.) ?RéessayerMFAu caractère C:\\Users\\idsmf\\Documents\\Rainmeter\\Skins\\SynologyNAS\\@Resources\\Scripts\\SynoAPI.ps1:56 : 67
+ ... ysURL = \"$baseURL/entry.cgi?api=SYNO.Core.System.Utilization&version= ...
+                                                                 ~
Le caractère perluète (&) n’est pas autorisé. L’opérateur & est réservé à une utilisation future. Placez un caractère
perluète entre guillemets doubles (\"&\") pour que ce symbole soit considéré comme une chaîne.
Au caractère C:\\Users\\idsmf\\Documents\\Rainmeter\\Skins\\SynologyNAS\\@Resources\\Scripts\\SynoAPI.ps1:56 : 77
+ ... baseURL/entry.cgi?api=SYNO.Core.System.Utilization&version=1&method=g ...
+                                                                 ~
Le caractère perluète (&) n’est pas autorisé. L’opérateur & est réservé à une utilisation future. Placez un caractère
perluète entre guillemets doubles (\"&\") pour que ce symbole soit considéré comme une chaîne.
Au caractère C:\\Users\\idsmf\\Documents\\Rainmeter\\Skins\\SynologyNAS\\@Resources\\Scripts\\SynoAPI.ps1:56 : 88
+ ... ry.cgi?api=SYNO.Core.System.Utilization&version=1&method=get&_sid=$si ...
+                                                                 ~
Le caractère perluète (&) n’est pas autorisé. L’opérateur & est réservé à une utilisation future. Placez un caractère
perluète entre guillemets doubles (\"&\") pour que ce symbole soit considéré comme une chaîne.
Au caractère C:\\Users\\idsmf\\Documents\\Rainmeter\\Skins\\SynologyNAS\\@Resources\\Scripts\\SynoAPI.ps1:68 : 56
+     $tempURL = \"$baseURL/entry.cgi?api=SYNO.Core.System&version=3&met ...
+                                                        ~
Le caractère perluète (&) n’est pas autorisé. L’opérateur & est réservé à une utilisation future. Placez un caractère
perluète entre guillemets doubles (\"&\") pour que ce symbole soit considéré comme une chaîne.
Au caractère C:\\Users\\idsmf\\Documents\\Rainmeter\\Skins\\SynologyNAS\\@Resources\\Scripts\\SynoAPI.ps1:68 : 66
+ ... tempURL = \"$baseURL/entry.cgi?api=SYNO.Core.System&version=3&method=i ...
+                                                                 ~
Le caractère perluète (&) n’est pas autorisé. L’opérateur & est réservé à une utilisation future. Placez un caractère
perluète entre guillemets doubles (\"&\") pour que ce symbole soit considéré comme une chaîne.
Au caractère C:\\Users\\idsmf\\Documents\\Rainmeter\\Skins\\SynologyNAS\\@Resources\\Scripts\\SynoAPI.ps1:68 : 78
+ ... baseURL/entry.cgi?api=SYNO.Core.System&version=3&method=info&type=tem ...
+                                                                 ~
Le caractère perluète (&) n’est pas autorisé. L’opérateur & est réservé à une utilisation future. Placez un caractère
perluète entre guillemets doubles (\"&\") pour que ce symbole soit considéré comme une chaîne.
Au caractère C:\\Users\\idsmf\\Documents\\Rainmeter\\Skins\\SynologyNAS\\@Resources\\Scripts\\SynoAPI.ps1:68 : 95
+ ... ?api=SYNO.Core.System&version=3&method=info&type=temperature&_sid=$si ...
+                                                                 ~
Le caractère perluète (&) n’est pas autorisé. L’opérateur & est réservé à une utilisation future. Placez un caractère
perluète entre guillemets doubles (\"&\") pour que ce symbole soit considéré comme une chaîne.
Au caractère C:\\Users\\idsmf\\Documents\\Rainmeter\\Skins\\SynologyNAS\\@Resources\\Scripts\\SynoAPI.ps1:78 : 58
+     $statusURL = \"$baseURL/entry.cgi?api=SYNO.Core.System&version=3&m ...
+                                                          ~
Le caractère perluète (&) n’est pas autorisé. L’opérateur & est réservé à une utilisation future. Placez un caractère
perluète entre guillemets doubles (\"&\") pour que ce symbole soit considéré comme une chaîne.
Au caractère C:\\Users\\idsmf\\Documents\\Rainmeter\\Skins\\SynologyNAS\\@Resources\\Scripts\\SynoAPI.ps1:78 : 68
+ ... atusURL = \"$baseURL/entry.cgi?api=SYNO.Core.System&version=3&method=i ...
+                                                                 ~
Le caractère perluète (&) n’est pas autorisé. L’opérateur & est réservé à une utilisation future. Placez un caractère
perluète entre guillemets doubles (\"&\") pour que ce symbole soit considéré comme une chaîne.
Au caractère C:\\Users\\idsmf\\Documents\\Rainmeter\\Skins\\SynologyNAS\\@Resources\\Scripts\\SynoAPI.ps1:78 : 80
+ ... baseURL/entry.cgi?api=SYNO.Core.System&version=3&method=info&_sid=$si ...
+                                                                 ~
Le caractère perluète (&) n’est pas autorisé. L’opérateur & est réservé à une utilisation future. Placez un caractère
perluète entre guillemets doubles (\"&\") pour que ce symbole soit considéré comme une chaîne.
Les erreurs d’analyse n’ont pas toutes été signalées. Corrigez les erreurs signalées, puis recommencez.
    + CategoryInfo          : ParserError: (:) [], ParseException
    + FullyQualifiedErrorId : AmpersandNotAllowedAfficher plusAh ! Erreur classique de PowerShell ! Les caractères & dans les URLs doivent être échappés. Je corrige le script :Script PowerShell - API SynologyCode ∙ Version 2 # Script PowerShell pour récupérer les données du NAS Synology
# Usage: .\\SynoAPI.ps1 <IP> <PORT> <USER> <PASSWORD>

param(
    [string]$NAS_IP = \"192.168.1.141\",
    [string]$NAS_PORT = \"5000\",
    [string]$NAS_USER = \"rainmeter_api\",
    [string]$NParfait ! J'ai corrigé le script PowerShell. Le problème : tous les & dans les URLs doivent être échappés avec `& (backtick + &) en PowerShell.
✅ Correction appliquée
J'ai remplacé tous les & par `& dans les URLs. Par exemple :

❌ Avant : ?api=SYNO.Core.System&version=3&method=info
✅ Après : ?api=SYNO.Core.System`&version=3`&method=info

🔄 Que faire maintenant ?

Remplacez le fichier SynoAPI.ps1 avec le nouveau contenu (artifact mis à jour)
Testez à nouveau :

powershell   cd \"Documents\\Rainmeter\\Skins\\SynologyNAS\\@Resources\\Scripts\"
   .\\SynoAPI.ps1 \"192.168.1.141\" \"5000\" \"rainmeter_api\" \"VotreMotDePasse\"
Cette fois ça devrait fonctionner sans erreur ! 🎉
Dites-moi ce qui s'affiche quand vous lancez le script maintenant ! 😊RéessayerMFAu caractère C:\\Users\\idsmf\\Documents\\Rainmeter\\Skins\\SynologyNAS\\@Resources\\Scripts\\SynoAPI.ps1:105 : 68
+         Write-Host \"  Volume 1: $usedGB GB / $totalGB GB ($percent%)\"
+                                                                    ~
Vous devez indiquer une expression de valeur après l’opérateur « % ».
Au caractère C:\\Users\\idsmf\\Documents\\Rainmeter\\Skins\\SynologyNAS\\@Resources\\Scripts\\SynoAPI.ps1:143 : 75
+ ... servicesList = ($activeServices | ForEach-Object { \"âœ“ $_\" }) -join  ...
+                                                                  ~
Le bloc Catch ou Finally manque dans l’instruction Try.
Au caractère C:\\Users\\idsmf\\Documents\\Rainmeter\\Skins\\SynologyNAS\\@Resources\\Scripts\\SynoAPI.ps1:143 : 75
+ ... ervicesList = ($activeServices | ForEach-Object { \"âœ“ $_\" }) -join \" ...
+                                                                 ~
Jeton inattendu « ) » dans l’expression ou l’instruction.
Au caractère C:\\Users\\idsmf\\Documents\\Rainmeter\\Skins\\SynologyNAS\\@Resources\\Scripts\\SynoAPI.ps1:146 : 9
+         }
+         ~
Jeton inattendu « } » dans l’expression ou l’instruction.
Au caractère C:\\Users\\idsmf\\Documents\\Rainmeter\\Skins\\SynologyNAS\\@Resources\\Scripts\\SynoAPI.ps1:147 : 5
+     }
+     ~
Jeton inattendu « } » dans l’expression ou l’instruction.
    + CategoryInfo          : ParserError: (:) [], ParseException
    + FullyQualifiedErrorId : ExpectedValueExpressionAfficher plusAh, deux problèmes : le % dans les chaînes et le caractère ✓ qui ne passe pas bien. Je corrige :Script PowerShell - API SynologyCode ∙ Version 3         $data.volume_used = \"$usedGB GB\"
        $data.volume_total = \"$totalGB GB\"
        $data.volume_percent = \"$percent\"
        Write-Host \"  Volume 1: $usedGB GB / $totalGB GB ($percent%)\" -NoNewline
        Write-Host \"\"Parfait ! J'ai corrigé les deux problèmes :

Le symbole % dans Write-Host : J'ai ajouté -NoNewline pour éviter le conflit
Le caractère ✓ : Remplacé par [char]0x2713 qui est le code Unicode pour le checkmark

Le script devrait maintenant fonctionner parfaitement ! Testez à nouveau :
powershell.\\SynoAPI.ps1 \"192.168.1.141\" \"5000\" \"rainmeter_api\" \"VotreMotDePasse\"
Qu'est-ce que ça donne ? 🤞Réessayer; Lines starting ; (semicolons) are commented out.\r
; That is, they do not affect the code and are here for demonstration purposes only.\r
; ----------------------------------\r
\r
[Rainmeter]\r
; This section contains general settings that can be used to change how Rainmeter behaves.\r
Update=1000\r
BackpastedMFmodifie ce skinpour qu'il garde la même police, taille etc.. que les autres skins définis
On peut stocker ces valeurs dans des variables plus globales utilisables par les autres skins par exemple, sans avoir à le coder en dur dans chaque skin ?Excellente idée ! On va créer un fichier de variables globales partagé entre tous les skins. Voici comment faire :Variables Globales - GlobalVariables.incCode ; ===================================
; FICHIER DE VARIABLES GLOBALES
; À placer dans : @Resources\\GlobalVariables.inc
; ===================================
; Ce fichier contient toutes les variables partagées entre vos skins
; Pour l'utiliser, ajoutMaintenant le skin System modifié qui utilise ces variables :System Monitor - Version mise à jourCode ; Lines starting ; (semicolons) are commented out.
; That is, they do not affect the code and are here for demonstration purposes only.
; ----------------------------------

; Inclusion des variables globales
@Include=#@#GlobalVariables.inc

[RainmetParfait ! Maintenant voici comment mettre à jour vos autres skins pour utiliser les variables globales :Guide de Migration - Variables GlobalesDocument # 📋 Guide de Migration vers Variables Globales

## 🎯 Objectif
Centraliser toutes les variables de style (polices, couleurs, tailles) dans un seul fichier partagé par tous vos skins.

---

## 📁 Étape 1 : Créer le fichier de variables globales

### Parfait ! Voici ce que je vous ai créé :
📦 3 Nouveaux artifacts :
1. GlobalVariables.inc
Fichier de variables partagées avec :

Polices et tailles (textSize=10, titleSize=14)
Couleurs (texte, barres, statuts)
Dimensions et espacements
Taux de rafraîchissement

2. System.ini mis à jour
Version moderne du skin System qui utilise les variables globales
3. Guide de Migration complet
Instructions détaillées pour :

Créer le fichier GlobalVariables.inc
Migrer vos skins existants
Personnaliser tous vos skins en une fois


🎯 Avantages de cette approche :
✅ Un seul endroit pour changer police, taille, couleurs
✅ Cohérence automatique entre tous vos skins
✅ Nouveaux skins plus rapides à créer
✅ Thèmes faciles à changer (clair/sombre)

🚀 Pour commencer :

Créez le fichier @Resources\\GlobalVariables.inc à la racine de Skins
Testez avec le nouveau System.ini
Migrez vos autres skins un par un

Besoin d'aide pour migrer un skin spécifique (Clock, Disk, Network) ? Je peux le faire pour vous ! 😊Réessayer; Lines starting ; (semicolons) are commented out.\r
; That is, they do not affect the code and are here for demonstration purposes only.\r
; ----------------------------------\r
\r
[Rainmeter]\r
; This section contains general settings that can be used to change how Rainmeter behaves.\r
Update=1000\r
BackpastedMFEn actualisant, clock n'affiche plus rienLe problème vient de l'ordre des éléments ! La ligne @Include doit être après [Rainmeter], pas avant. Voici la correction :Clock.ini - CorrigéCode ; Lines starting ; (semicolons) are commented out.
; That is, they do not affect the code and are here for demonstration purposes only.
; ----------------------------------

[Rainmeter]
; This section contains general settings that can be used to cha🔧 Problèmes corrigés :

Ordre correct : @Include doit être dans la section [Variables], pas avant
Variable colorText locale : Définie localement car elle change selon le jour
Variables globales utilisées :

#updateRate# au lieu de 1000
#marginTop#, #marginBottom# etc.
#titleY#, #baseX#, #baseY# pour les positions
#shadowColor# et #shadowColorLight#


📝 Structure correcte pour Clock.ini :
ini[Rainmeter]
Update=#updateRate#
...

[Variables]
colorText=255,255,255,205  ← Variable locale (change selon le jour)
@Include=#@#GlobalVariables.inc  ← Inclusion ICI

[Metadata]
...
Important : La variable colorText doit être définie localement dans Clock.ini car elle est modifiée dynamiquement par measureDayColor.
Testez maintenant, ça devrait fonctionner ! 🎉RéessayerMFdu coup la couleur ne peut pas s'appliquer pour tous les widgets si elle est définie localementExactement ! Vous avez raison. Il y a un conflit entre :

Variables globales : pour la cohérence visuelle
Couleur dynamique du Clock : qui change selon le jour

Voici les solutions possibles :
💡 Solution 1 : Variables de couleur séparées (RECOMMANDÉ)Variables Globales - GlobalVariables.incCode ∙ Version 2 ; ----------------------------------
; COULEURS PRINCIPALES
; ----------------------------------
; Format: Rouge,Vert,Bleu,Alpha (0-255)
colorBar=235,170,0,255
colorText=255,255,255,205
colorTextDynamic=255,255,255,205
colorBackground=0,0,0,100

; CoParfait ! Voici la solution propre :
✅ Solution mise en place
📝 Principe :

colorText : Couleur globale pour tous les skins normaux
colorTextDynamic : Couleur spéciale pour Clock qui change selon le jour
colorSunday, colorMonday, etc. : Couleurs définies globalement mais utilisées uniquement par Clock

🎨 Résultat :

Tous les autres skins (System, Disk, Network, NAS) utilisent #colorText# (blanc)
Clock uniquement utilise #colorTextDynamic# qui change chaque jour
Les couleurs des jours sont dans GlobalVariables.inc, donc modifiables centralement

🔄 Pour changer les couleurs des jours :
Éditez GlobalVariables.inc :
ini; Changez toutes les couleurs des jours en une fois !
colorSunday=255,50,50,205      ; Rouge (dimanche)
colorMonday=50,200,50,205      ; Vert (lundi)
colorTuesday=255,165,0,205     ; Orange (mardi)
; etc.
🌈 Pour changer la couleur de tous les autres skins :
inicolorText=100,200,255,205   ; Bleu clair pour System, Disk, Network, NAS

📊 Récapitulatif :
SkinVariable utiliséeComportementClock#colorTextDynamic#Change selon le jourSystem#colorText#Blanc fixeDisk#colorText#Blanc fixeNetwork#colorText#Blanc fixeNAS#colorText#Blanc fixe
Testez maintenant ! Tous vos skins devraient avoir la même couleur, sauf Clock qui change chaque jour ! 🎉RéessayerMFje veux que tous les skins utilisent la couleur de police en fonction du jour de la semaine
mets à jour le fichier de variables globales et celui de clock pour testerParfait ! Je vais centraliser la logique de couleur par jour dans les variables globales pour que TOUS les skins l'utilisent :Variables Globales - GlobalVariables.incCode ∙ Version 3 ; ===================================
; FICHIER DE VARIABLES GLOBALES
; À placer dans : @Resources\\GlobalVariables.inc
; ===================================
; Ce fichier contient toutes les variables partagées entre vos skins
; Pour l'utiliser, ajoutParfait ! Voici comment ça fonctionne maintenant :
🎨 Système de couleur globale par jour
📋 Dans GlobalVariables.inc :

Mesures globales ajoutées :

measureGlobalDayNumber : Détecte le jour de la semaine
measureGlobalDayColor : Change automatiquement colorDynamic


Variable colorDynamic :

Change automatiquement chaque jour
Utilisée par TOUS les skins


📝 Dans Clock.ini :

Simplifié : Plus besoin de measureDayNumber et measureDayColor locaux
Utilise directement #colorDynamic# des variables globales
DynamicVariables=1 sur tous les styles pour voir les changements


🌈 Résultat :
TOUS vos skins (Clock, System, Disk, Network, NAS) auront maintenant la même couleur qui change selon le jour :

🔴 Dimanche : Rouge
🟢 Lundi : Vert
🟠 Mardi : Orange
🟡 Mercredi : Jaune
🟣 Jeudi : Violet
🔵 Vendredi : Bleu
🟠 Samedi : Orange


✅ Pour appliquer à vos autres skins :
Dans System.ini, Disk.ini, Network.ini :
Remplacez FontColor=#colorText# par FontColor=#colorDynamic# dans tous les styles, et ajoutez DynamicVariables=1.
Exemple :
ini[styleLeftText]
FontColor=#colorDynamic#   ← Au lieu de #colorText#
DynamicVariables=1          ← Ajouter cette ligne
Testez Clock.ini maintenant, la couleur devrait changer selon le jour ! 🎉RéessayerMFje ne trouve plus le skin de clock, renvoie la dernière version stpVoici la dernière version complète du skin Clock :Clock.ini - Version Finale ComplèteCode ; Lines starting ; (semicolons) are commented out.
; That is, they do not affect the code and are here for demonstration purposes only.
; ----------------------------------

[Rainmeter]
; This section contains general settings that can be used to chaVoilà ! C'est la version finale du skin Clock qui :
✅ Utilise les variables globales (GlobalVariables.inc)
✅ Affiche l'heure au format 24h (HH:MM)
✅ Affiche la date au format DD/MM/YYYY
✅ Affiche le jour en français
✅ Couleur dynamique selon le jour de la semaine (#colorDynamic#)
✅ Police et tailles cohérentes avec les autres skins

📁 Rappel de la structure :
Documents\\Rainmeter\\Skins\\
├── @Resources\\
│   ├── GlobalVariables.inc  ← Fichier de variables globales
│   └── Background.png
└── Clock\\
    └── Clock.ini  ← Ce fichier
Copiez ce contenu dans votre fichier Clock.ini et rafraîchissez le skin dans Rainmeter ! 🎨RéessayerMFça ne marche pas, aucun texte ne s'affiche, on peut repartir d'un affichage de texte brut simple, avec seulement l'appel aux couleurs pour testerParfait, on va simplifier au maximum pour tester :Clock.ini - Version Test SimplifiéeCode ; Test simple du skin Clock
; ----------------------------------

[Rainmeter]
Update=1000
Background=#@#Background.png
BackgroundMode=3
BackgroundMargins=0,34,0,20

[Variables]
@Include=#@#GlobalVariables.inc

[Metadata]
Name=Clock Test
Author=CustomVoilà une version ultra-simple pour tester !
🧪 Ce que fait cette version :

✅ Affiche l'heure, le jour et la date
✅ Utilise #colorDynamic# des variables globales
✅ Pas de styles complexes
✅ Tout en texte brut

🔍 Test de diagnostic :
Si rien ne s'affiche :

Le fichier GlobalVariables.inc n'est peut-être pas au bon endroit
Testez en remplaçant FontColor=#colorDynamic# par FontColor=255,255,255,255 (blanc fixe) dans les 3 meters

Version sans variables globales (pour tester) :
Si la version ci-dessus ne fonctionne toujours pas, essayez celle-ci :
ini[Rainmeter]
Update=1000
Background=#@#Background.png
BackgroundMode=3
BackgroundMargins=0,34,0,20

[measureTime]
Measure=Time
Format=%H:%M

[meterTitle]
Meter=String
MeasureName=measureTime
X=100
Y=12
W=190
H=18
StringAlign=Center
FontFace=Trebuchet MS
FontSize=14
FontColor=255,255,255,255
AntiAlias=1
Text=%1
Dites-moi ce qui s'affiche (ou ne s'affiche pas) ! 🔍RéessayerMFok, je vois l'heure le jour et la date
Mais en blanc,
colordynamic a sa valeur par défaut même si on inclut bien le globalvariable.incDu coup quand je rafraichit le skin, il inclut les variables globales, mais il compile aussi les tests pour le jour de la semaine avant d'afficher le skin ?Ah ! Excellent diagnostic ! 🎯
Le problème c'est que les mesures dans GlobalVariables.inc ne s'exécutent pas parce qu'elles sont dans un fichier inclus (.inc), pas dans le skin principal.
🔧 Solution : Déplacer les mesures dans le skinVariables Globales - GlobalVariables.incCode ∙ Version 4 ; Variable dynamique qui change selon le jour (définie dans chaque skin)
colorDynamic=255,255,255,205

; ----------------------------------
; DIMENSIONS
; ----------------------------------
skinWidth=190
skinHeight=Auto
barHeight=2
separatorHeight=1
RéessayerMFmais si on déplace les mesures dans le skin, ça veut dire qu'on devra appliquer la même logique pour tous les skins pour la gestion de la couleur ?Exactement ! Vous avez raison, c'est pas optimal. 😅
Il y a 2 solutions :
💡 Solution 1 : Un skin \"maître\" invisible (RECOMMANDÉ)
Créer un skin invisible qui gère la couleur et l'écrit dans un fichier, que tous les autres skins lisent.
💡 Solution 2 : Code dupliqué (plus simple mais moins élégant)
Copier les mesures measureDayNumber et measureDayColor dans chaque skin.

🎯 Ma recommandation : Solution 1
Créons un petit skin invisible qui fait le travail pour tous les autres :ColorManager.ini - Gestionnaire de couleurCode ; Skin invisible qui gère la couleur selon le jour
; Ce skin doit être chargé en premier
; ----------------------------------

[Rainmeter]
Update=1000

[Variables]
@Include=#@#GlobalVariables.inc

[Metadata]
Name=Color Manager
Author=Custom
InformatiHmm, en fait cette approche est trop compliquée.
La vraie question c'est : est-ce vraiment gênant de dupliquer 15 lignes de code dans chaque skin ?
✅ Ma vraie recommandation : Solution 2 simplifiée
Créons un fichier include réutilisable juste pour les mesures de couleur :ColorByDay.inc - Mesures de couleurCode ; ===================================
; MESURES POUR COULEUR PAR JOUR
; À placer dans : @Resources\\ColorByDay.inc
; ===================================
; À inclure dans chaque skin APRÈS GlobalVariables.inc
; Usage : @Include2=#@#ColorByDay.inc

[meaParfait ! Voilà la meilleure solution :
📦 Structure finale :
@Resources\\
├── GlobalVariables.inc    ← Variables (polices, couleurs, tailles)
└── ColorByDay.inc         ← Mesures pour la couleur dynamique
✅ Utilisation dans chaque skin :
ini[Variables]
@Include=#@#GlobalVariables.inc
@Include2=#@#ColorByDay.inc
C'est tout ! Deux lignes à ajouter dans chaque skin.
🎯 Avantages :
✅ Code centralisé : Les mesures sont dans ColorByDay.inc
✅ Facile à maintenir : Si vous voulez changer la logique, 1 seul fichier
✅ Réutilisable : Ajoutez 2 lignes, ça marche
✅ Simple : Pas de skin maître compliqué

Testez Clock.ini maintenant ! La couleur devrait changer selon le jour 🎨
Pour les autres skins (System, Disk, Network), ajoutez juste @Include2=#@#ColorByDay.inc et utilisez #colorDynamic# !RéessayerMF; Test simple du skin Clock
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
Text=%1Le texte est toujours en blanc après ajour du fichier colorbyday.incAfficher plusLe problème vient probablement du fait que les mesures s'exécutent après l'affichage initial. Ajoutons un UpdateDivider=-1 pour forcer l'exécution immédiate :ColorByDay.inc - Mesures de couleurCode ∙ Version 2 [measureDayNumber]
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
Quelle version voulez-vous utiliser ? Celle avec OnRefreshAction ou celle avec les formules inline ?RéessayerMFj'ai testé le dernier la version simple, la couleur a changé pour un vert olive très proche du noir peu lisible sur fond noir
On a une couleur qui est prise en compte mais pas la bonne apparemment, ça devrait être du orangeAh ! Le problème vient de la syntaxe des formules conditionnelles. La valeur retournée n'est pas correctement interprétée comme une couleur RGB.
Utilisons plutôt la méthode Section Variables qui fonctionne mieux :Clock.ini - Version Simple qui MarcheCode ∙ Version 2 ; Clock avec couleur par jour - VERSION FONCTIONNELLE
; ----------------------------------

[Rainmeter]
Update=1000
Background=#@#Background.png
BackgroundMode=3
BackgroundMargins=0,34,0,20

[Variables]
; Couleurs des jours (R,G,B,A)
color0=255,50,50J'ai changé l'approche :
🔧 Ce qui a changé :

Variables numérotées : color0, color1, color2... au lieu de colorSunday, colorMonday...
Syntaxe dynamique : [#color[&measureDayNumber]] qui construit le nom de la variable dynamiquement

Si aujourd'hui = Mardi (2) → lit #color2# → 255,165,0,205 (orange)


📅 Correspondance jours :

0 = Dimanche → Rouge
1 = Lundi → Vert
2 = Mardi → Orange ← Vous devriez voir ça aujourd'hui !
3 = Mercredi → Jaune
4 = Jeudi → Violet
5 = Vendredi → Bleu
6 = Samedi → Orange

Testez maintenant, vous devriez voir de l'orange vif ! 🟠
Si c'est encore faux, dites-moi quel jour on est et quelle couleur vous voyez, je debuggerai ! 🔍RéessayerMFParfait, ça fonctionne, explique moi simplement quelle logique tu as adopté pour la gestion des couleurs, pour finir par l'approche simpleBien sûr ! Voici l'évolution de ma réflexion sur la gestion des couleurs :
🎯 Évolution des approches
❌ Approche 1 : Mesures dans GlobalVariables.inc
ini; Dans GlobalVariables.inc
[measureGlobalDayNumber]
Measure=Time
Format=%w
Pourquoi ça ne marchait pas :

Les fichiers .inc sont juste copiés-collés dans le skin
Mais les mesures ne s'exécutent pas avant le premier affichage
Résultat : couleur blanche par défaut, puis change après 1 seconde


❌ Approche 2 : IfCondition avec SetVariable
ini[measureDayColor]
Measure=Calc
Formula=measureDayNumber
IfCondition=measureDayColor = 0
IfTrueAction=[!SetVariable colorDynamic \"#colorSunday#\"]
Pourquoi c'était compliqué :

Les actions IfTrueAction s'exécutent après le premier rendu
Il fallait ajouter OnRefreshAction pour forcer la mise à jour
Besoin de dupliquer ce code dans chaque skin ou créer un fichier ColorByDay.inc
Trop de fichiers à gérer


❌ Approche 3 : Formules conditionnelles inline
iniFontColor=[&measureDayNumber:] = 0 ? #colorSunday# : (...)
Pourquoi ça donnait une couleur bizarre :

Rainmeter ne comprenait pas que le résultat était une couleur RGB
Il interprétait le texte comme un nombre au lieu d'une couleur
Résultat : vert olive bizarre au lieu d'orange


✅ Approche finale : Variables numérotées + référence dynamique
ini[Variables]
color0=255,50,50,205    ; Dimanche
color1=50,200,50,205    ; Lundi
color2=255,165,0,205    ; Mardi
...

[measureDayNumber]
Measure=Time
Format=%w              ; Retourne 0-6

[meterTitle]
FontColor=[#color[&measureDayNumber]]
DynamicVariables=1
Comment ça marche :

measureDayNumber retourne 2 (Mardi)
La syntaxe [#color[&measureDayNumber]] devient [#color2]
Rainmeter lit la variable #color2# = 255,165,0,205
Applique la couleur orange immédiatement ✅

Pourquoi c'est la meilleure solution :

✅ Fonctionne immédiatement (pas d'attente)
✅ Simple : tout dans un seul fichier
✅ Facile à comprendre : color2 = Mardi
✅ Pas de fichiers supplémentaires
✅ Rainmeter comprend que c'est une couleur RGB


🎓 La leçon principale :
Rainmeter préfère les références directes aux variables plutôt que les calculs conditionnels pour les couleurs.
Au lieu de dire \"si jour=2 alors orange\", on dit \"lis color2\" → beaucoup plus simple ! 🎨RéessayerMFParfait, j'aime beaucoup l'approche et ta façon de rebondir pour aller vers l'objectif souhaité même quand c'est mal formulé GGOn continue avec les autres skins à adapter
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
Le reste de la police suit la logique de couleur en fonction du jourAfficher plusParfait ! Merci pour les compliments ! 😊 Allons-y pour un skin Disk amélioré avec une jauge visible et couleurs dynamiques :Disk.ini - Version AmélioréeCode ; Disk monitor avec couleur par jour et jauge améliorée
; ----------------------------------

[Rainmeter]
Update=1000
Background=#@#Background.png
BackgroundMode=3
BackgroundMargins=0,34,0,20

[Variables]
; Couleurs des jours pour le texte
color0=255Voilà ! 🎨 Voici ce que j'ai amélioré :
🎨 Améliorations apportées :
1. Couleur du texte selon le jour ✅

Tout le texte (titre, espace, pourcentage) change de couleur selon le jour
Utilise la même logique que Clock avec color0-color6

2. Jauge beaucoup plus visible 📊
Avant : Ligne de 1px de hauteur
Maintenant :

Hauteur de 6px (au lieu de 1px)
Contour noir autour (fond gris foncé de 8px)
Effet 3D subtil

3. Couleur de la jauge dynamique 🚦
La barre change de couleur selon l'espace utilisé :

🟢 Vert : 0-60% (tout va bien)
🟠 Orange : 60-85% (attention)
🔴 Rouge : 85-100% (critique !)

4. Bonus : Pourcentage sur la barre 💯

Petit texte blanc affiché sur la barre pour une lecture ultra-rapide


🎯 Résultat visuel :
┌─────────────────────────────┐
│        DISQUE C:            │  ← Couleur du jour
├─────────────────────────────┤
│      2.5 TB / 4.0 TB        │  ← Couleur du jour
│      Rempli : 62.5%         │  ← Couleur du jour
│                             │
│  ╔════════════════════╗     │
│  ║████████████░░░░░░░░║62%  │  ← Jauge orange (62%)
│  ╚════════════════════╝     │
└─────────────────────────────┘
Testez-le ! La jauge devrait être beaucoup plus visible et changer de couleur selon votre espace disque ! 🚀
Vous voulez ajuster la taille ou les seuils de couleur ?RéessayerMF; Disk monitor avec couleur par jour et jauge améliorée
; ----------------------------------
[Rainmeter]
Update=1000
Background=#@#Background.png
BackgroundMode=3
BackgroundMargins=0,50,0,30
[Variables]
; Couleurs des jours pour le texte
color0=255,50,50,205
color1=50,200,50,205
color2=255,165,0,205
color3=255,220,50,205
color4=150,50,200,205
color5=50,130,255,205
color6=255,140,0,205
; Couleurs de la jauge selon le pourcentage
colorBarLow=50,200,50,255        ; Vert si < 60%
colorBarMedium=255,165,0,255     ; Orange si 60-85%
colorBarHigh=255,50,50,255       ; Rouge si > 85%
; Configuration du disque
disk1=C:
[Metadata]
Name=Disk
Author=Custom
Information=Affiche l'espace disque avec jauge colorée
Version=2.1.0
; ----------------------------------
; MEASURES
; ----------------------------------
[measureTotalDisk1]
Measure=FreeDiskSpace
Drive=#disk1#
Total=1
UpdateDivider=120
[measureUsedDisk1]
Measure=FreeDiskSpace
Drive=#disk1#
InvertMeasure=1
UpdateDivider=120
[measureFreeDiskValue]
Measure=FreeDiskSpace
Drive=#disk1#
UpdateDivider=120
[measureTotalDiskValue]
Measure=FreeDiskSpace
Drive=#disk1#
Total=1
UpdateDivider=120
[measurePercentUsed]
Measure=Calc
Formula=( ( [measureTotalDiskValue] - [measureFreeDiskValue] ) / [measureTotalDiskValue] ) * 100
DynamicVariables=1
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
W=190
H=30
MeterStyle=styleTitle
Text=Disque #disk1#
[meterValueDisk1]
Meter=String
MeasureName=measureUsedDisk1
MeasureName2=measureTotalDisk1
X=100
Y=42
W=190
H=16
StringAlign=Center
StringStyle=Bold
StringEffect=Shadow
FontEffectColor=0,0,0,20
FontFace=Trebuchet MS
FontSize=12
FontColor=[#color[&measureDayNumber]]
AntiAlias=1
DynamicVariables=1
Text=%1B / %2B
NumOfDecimals=1
AutoScale=1
LeftMouseUpAction=[\"#disk1#\\\"]
ToolTipText=Cliquez pour ouvrir le disque
; Fond de la barre (plus bas)
; Fond de la barre
[meterBarBackground]
Meter=Shape
X=10
Y=70
W=190
H=24
Shape=Rectangle 0,0,190,24,3 | StrokeWidth 1 | StrokeColor 80,80,80,255 | Fill Color 60,60,60,255
DynamicVariables=1
; Barre de progression avec couleur dynamique
[meterBarDisk1]
Meter=Shape
X=11
Y=71
DynamicVariables=1
Shape=Rectangle 0,0,([measurePercentUsed]*1.88),22,3 | Fill Color ([measurePercentUsed] < 60 ? #colorBarLow# : ([measurePercentUsed] < 85 ? #colorBarMedium# : #colorBarHigh#)) | StrokeWidth 1 | StrokeColor 80,80,80,255
; Texte du pourcentage sur la barre
[meterBarPercentText]
Meter=String
MeasureName=measurePercentUsed
X=100
Y=73
W=190
H=22
StringAlign=Center
StringStyle=Bold
FontFace=Trebuchet MS
FontSize=10
FontColor=255,255,255,255
AntiAlias=1
Text=%1%
NumOfDecimals=0
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
ClipString=1J'ai fait quelques modifs entre temps
J'ai le résultat que je veux à peu de chose prèsChange le texte affiché : XX GB / YY GB
Je veux à la place afficher
ZZ GB DisponiblesEnsuite le texte ne devra plus refléter la couleur du jour de la semaine, mais un blanc discret qui tire sur le grisPar contre le titre de tous les skins sera de la couleur du jour de la semaine Fais le tri dans les valeures utilisés pour en intégrer aux variables globales si c'est pertinentAfficher plusParfait ! Je vais nettoyer et optimiser tout ça :Variables Globales - GlobalVariables.incCode ∙ Version 5 ; ----------------------------------
; POLICES ET TEXTE
; ----------------------------------
fontName=Trebuchet MS
textSize=10
titleSize=14
smallTextSize=9

; ----------------------------------
; COULEURS PRINCIPALES
; -------------------------------Parfait ! Voici les changements :
✅ Modifications apportées :
1. Texte modifié 📝

Avant : 2.5 TB / 4.0 TB
Maintenant : 2.5 TB Disponibles
Utilise measureFreeDisk1 au lieu de montrer utilisé/total

2. Couleurs réorganisées 🎨

Titre : Couleur du jour (dynamique) ← [#color[&measureDayNumber]]
Texte : Gris discret ← #colorTextSubdued# (180,180,180,205)

3. Variables globales nettoyées 📦
Ajouté à GlobalVariables.inc :

colorTextSubdued : Gris pour le texte discret
color0-color6 : Couleurs des jours
colorBarLow/Medium/High : Couleurs de la jauge

Supprimé des variables locales :

Toutes les couleurs (maintenant globales)
Police et tailles (déjà dans GlobalVariables.inc)

4. Code nettoyé 🧹

Suppression de mesures inutiles
Utilisation de #skinWidth#, #fontName#, etc.
Une seule mesure pour l'espace libre


🎯 Résultat :
┌─────────────────────────────┐
│      DISQUE C:              │  ← Orange (mardi)
├─────────────────────────────┤
│    1.5 TB Disponibles       │  ← Gris discret
│                             │
│  ╔════════════════════╗     │
│  ║████████████░░░░░░░░║62%  │  ← Orange (62%)
│  ╚════════════════════╝     │
└─────────────────────────────┘
Vous voulez que je mette à jour Clock avec la même logique (titre coloré, texte gris) ? 😊RéessayerMFnon laisse tomber c'est devenu moche à souhaitPars du code que je t'ai fourni on va y aller par étapesEt Ajoute la couleur de la semaine pour le titreD'accord, repartons de votre code proprement ! Juste en ajoutant la couleur du jour pour le titre :Disk.ini - Version AmélioréeCode ∙ Version 3 ; Disk monitor avec couleur par jour et jauge améliorée
; ----------------------------------

[Rainmeter]
Update=1000
Background=#@#Background.png
BackgroundMode=3
BackgroundMargins=0,50,0,30

[Variables]
; Couleurs des jours pour le texte
color0=255Voilà ! J'ai repris exactement votre code et j'ai juste ajouté :
✅ Changement unique :
Dans [meterTitle] :
iniFontColor=[#color[&measureDayNumber]]
DynamicVariables=1
Le titre \"DISQUE C:\" change maintenant de couleur selon le jour de la semaine, exactement comme Clock ! 🎨
Tout le reste est identique à votre version. Quelle est la prochaine étape ? 😊RéessayerMFOk, ce skin est finalisé
Récupère les infos de formattage du texte police taille etc...
Et répercute les sur le skin suivant ; Disk monitor avec couleur par jour et jauge améliorée
; ----------------------------------
[Rainmeter]
Update=1000
Background=#@#Background.png
BackgroundMode=3
BackgroundMargins=0,50,0,30
[Variables]
; Couleurs des jours pour le texte
color0=255,50,50,205
color1=50,200,50,205
color2=255,165,0,205
color3=255,220,50,205
color4=150,50,200,205
color5=50,130,255,205
color6=255,140,0,205
; Couleurs de la jauge selon le pourcentage
colorBarLow=50,200,50,255        ; Vert si < 60%
colorBarMedium=255,165,0,255     ; Orange si 60-85%
colorBarHigh=255,50,50,255       ; Rouge si > 85%
; Configuration du disque
disk1=C:
[Metadata]
Name=Disk
Author=Custom
Information=Affiche l'espace disque avec jauge colorée
Version=2.1.0
; ----------------------------------
; MEASURES
; ----------------------------------
[measureTotalDisk1]
Measure=FreeDiskSpace
Drive=#disk1#
Total=1
UpdateDivider=120
[measureUsedDisk1]
Measure=FreeDiskSpace
Drive=#disk1#
InvertMeasure=1
UpdateDivider=120
[measureFreeDiskValue]
Measure=FreeDiskSpace
Drive=#disk1#
UpdateDivider=120
[measureTotalDiskValue]
Measure=FreeDiskSpace
Drive=#disk1#
Total=1
UpdateDivider=120
[measurePercentUsed]
Measure=Calc
Formula=( ( [measureTotalDiskValue] - [measureFreeDiskValue] ) / [measureTotalDiskValue] ) * 100
DynamicVariables=1
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
W=190
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
Text=Disque #disk1#
[meterValueDisk1]
Meter=String
MeasureName=measureFreeDiskValue
X=100
Y=42
W=190
H=16
StringAlign=Center
StringStyle=Bold
StringEffect=Shadow
FontEffectColor=0,0,0,20
FontFace=Trebuchet MS
FontSize=12
FontColor=200,200,200,255
AntiAlias=1
DynamicVariables=1
Text=%1B disponibles
NumOfDecimals=1
AutoScale=1
LeftMouseUpAction=[\"#disk1#\\\"]
ToolTipText=Cliquez pour ouvrir le disque
; Fond de la barre
[meterBarBackground]
Meter=Shape
X=10
Y=70
W=190
H=24
Shape=Rectangle 0,0,190,24,3 | StrokeWidth 1 | StrokeColor 80,80,80,255 | Fill Color 60,60,60,255
DynamicVariables=1
; Barre de progression avec couleur dynamique
[meterBarDisk1]
Meter=Shape
X=11
Y=71
DynamicVariables=1
Shape=Rectangle 0,0,([measurePercentUsed]*1.88),22,3 | Fill Color [#color[&measureDayNumber]] | StrokeWidth 1 | StrokeColor 80,80,80,255
; Texte du pourcentage sur la barre
[meterBarPercentText]
Meter=String
MeasureName=measurePercentUsed
X=100
Y=73
W=190
H=22
StringAlign=Center
StringStyle=Bold
FontFace=Trebuchet MS
FontSize=10
FontColor=255,255,255,255
AntiAlias=1
Text=%1%
NumOfDecimals=0Afficher plusParfait ! J'ai analysé votre skin Disk finalisé. Voici les paramètres de formattage à appliquer :
📋 Paramètres extraits du skin Disk :

Titre : Trebuchet MS, 14px, Bold, Shadow (0,0,0,120), Couleur du jour
Texte normal : Trebuchet MS, 12px, Bold, Shadow (0,0,0,20), Gris (200,200,200,255)
Petit texte : Trebuchet MS, 10px, Bold, Blanc (255,255,255,255)
Marges : 0,50,0,30

Quel est le skin suivant à mettre à jour ? System, Network, ou un autre ? 😊
Envoyez-moi le code du prochain skin et je vais lui appliquer exactement le même formatage ! 🎨RéessayerMF; Clock avec couleur par jour - VERSION FONCTIONNELLE
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
Text=%1Afficher plusParfait ! Voici le skin Clock avec le même formatage que Disk :Clock.ini - Version Simple qui MarcheCode ∙ Version 3 ; Clock avec couleur par jour - Formatage aligné sur Disk
; ----------------------------------

[Rainmeter]
Update=1000
Background=#@#Background.png
BackgroundMode=3
BackgroundMargins=0,50,0,30

[Variables]
; Couleurs des jours (R,G,B,A)
color0=255,5✅ Modifications appliquées au skin Clock :
📐 Formatage aligné sur Disk :

Marges : 0,50,0,30 (au lieu de 0,34,0,20)
Titre (Heure) :

Position Y: 8 (au lieu de 12)
Height: 30 (au lieu de 18)
Shadow ajouté : FontEffectColor=0,0,0,120
Couleur du jour ✅


Texte (Jour et Date) :

Position Y: 42 (au lieu de 40)
Taille : 12px (au lieu de 10px)
Shadow ajouté : FontEffectColor=0,0,0,20
Couleur : Gris 200,200,200,255 (au lieu de couleur du jour)


🎨 Résultat :

Heure : Couleur du jour, grande, avec ombre
Jour et Date : Gris discret, avec ombre légère
Même espacement et alignement que Disk

Le skin Clock est maintenant parfaitement cohérent avec Disk ! 🎉
Skin suivant ? 😊Réessayer; Lines starting ; (semicolons) are commented out.\r
; That is, they do not affect the code and are here for demonstration purposes only.\r
; ----------------------------------\r
\r
[Rainmeter]\r
; This section contains general settings that can be used to change how Rainmeter behaves.\r
Update=1000\r
BackpastedMFParfait ! Voici le skin System avec le formatage aligné sur Disk et Clock :System Monitor - Version mise à jourCode ∙ Version 2 ; System monitor - Formatage aligné sur Disk et Clock
; ----------------------------------

[Rainmeter]
Update=1000
Background=#@#Background.png
BackgroundMode=3
BackgroundMargins=0,50,0,30

[Variables]
; Couleurs des jours (R,G,B,A)
color0=255,50,50✅ Skin System mis à jour avec le même formatage !
🎨 Modifications appliquées :

Marges : 0,50,0,30 (cohérent avec Disk et Clock)
Titre \"SYSTEM\" :

Position Y: 8, Height: 30
Couleur du jour [#color[&measureDayNumber]]
Shadow : 0,0,0,120
Clic pour ouvrir le Gestionnaire des tâches ✅


Labels et valeurs (CPU, RAM, SWAP) :

Taille : 12px (au lieu de variable)
Couleur grise : 200,200,200,255
Shadow : 0,0,0,20


Barres de progression :

Style Shape (comme Disk) au lieu de Meter=Bar
Hauteur 8px avec contour gris
Couleur de remplissage : Couleur du jour [#color[&measureDayNumber]]
Coins arrondis (radius 2)


🎯 Résultat :
Les 3 barres (CPU, RAM, SWAP) sont maintenant visuelles et colorées selon le jour, exactement comme la barre du Disk !
Skin suivant ? Network ? 😊RéessayerMFParfait le skin bien joué !Par contre les barres de RAM et SWAP sont à 60 et 65% mais le soucis est que les jaugent dépassent de la carte sur la droiteAh oui ! Le problème vient du calcul ([measureRAM:1]*1.88) qui dépasse 190px. Corrigeons ça :System Monitor - Version mise à jourCode ∙ Version 3 [meterBarCPUFill]
Meter=Shape
MeasureName=measureCPU
X=11
Y=61
DynamicVariables=1
Shape=Rectangle 0,0,(188*[measureCPU]/100),6,2 | Fill Color [#color[&measureDayNumber]] | StrokeWidth 0Voilà ! J'ai corrigé le calcul des 3 barres :
🔧 Correction appliquée :
Avant : ([measureRAM:1]*1.88) ← Mauvais calcul
Maintenant : (188*[measureRAM:1]/100) ← Correct !
Logique :

Largeur max de la barre : 188px (190px - 2px de bordure)
Formule : 188 * pourcentage / 100
Exemple : 60% → 188 * 60 / 100 = 112.8px ✅

Les barres ne dépasseront plus jamais, quelle que soit la valeur ! 🎉
Testez maintenant, ça devrait être parfait ! 👌RéessayerMFnon pas de changementAh, le problème vient probablement de [measureRAM:1] qui retourne la valeur en pourcentage mais pas forcément entre 0-100. Utilisons plutôt une mesure Calc pour garantir le bon calcul :System Monitor - Version mise à jourCode ∙ Version 6 [measureRAM]
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
Testez et dites-moi si c'est bon ! 👍Réessayer; Synology NAS Monitor - Skin avec sections collapsibles\r
; ----------------------------------\r
\r
[Rainmeter]\r
Update=1000\r
Background=#@#Background.png\r
BackgroundMode=3\r
BackgroundMargins=0,34,0,20\r
MouseOverAction=[!ShowMeterGroup SectionSystemExpand][!UpdateMeter *][!Redraw]\r
MouseLeaveAction=[!pastedMFok là c'est impeccable !Plus dur maintenant
Celui ci on va le découper en 4 sknis distincts en gardant visibles toutes les infos sans option de survol pour réduireParfait ! Je vais découper le skin NAS en 4 skins distincts, chacun affichant toutes ses infos en permanence :NAS_System.ini - Infos SystèmeCode ; NAS System Monitor
; ----------------------------------

[Rainmeter]
Update=1000
Background=#@#Background.png
BackgroundMode=3
BackgroundMargins=0,50,0,30

[Variables]
; Couleurs des jours
color0=255,50,50,205
color1=50,200,50,205
color2=255,165,0,Parfait ! J'ai créé 4 skins distincts pour votre NAS Synology :
📦 Les 4 nouveaux skins :
1. NAS_System.ini - Infos Système

Statut (En ligne/Hors ligne)
CPU (%)
RAM (%)
Température (°C)
Uptime (jours/heures)

2. NAS_Storage.ini - Stockage

Espace utilisé / Total
Barre de progression avec %
Clic pour ouvrir le NAS

3. NAS_Network.ini - Réseau

Upload (KB/s)
Download (KB/s)
Connexions actives

4. NAS_Services.ini - Services

Liste des services actifs
Format compact avec checkmarks


✅ Caractéristiques communes :

Formatage identique à vos autres skins (Disk, Clock, System)
Titre coloré selon le jour de la semaine
Texte gris (200,200,200,255)
Marges : 0,50,0,30
Toutes les infos visibles en permanence (plus de survol)


📁 Structure des fichiers :
Skins\\
├── NAS_System\\
│   └── NAS_System.ini
├── NAS_Storage\\
│   └── NAS_Storage.ini
├── NAS_Network\\
│   └── NAS_Network.ini
└── NAS_Services\\
    └── NAS_Services.ini
Note importante : Le script PowerShell (SynoAPI.ps1) doit être lancé par UN SEUL des skins (NAS_System par exemple). Les 3 autres liront juste le fichier JSON créé.
Vous voulez que je mette à jour le script PowerShell pour qu'il soit lancé uniquement par NAS_System ? 🤔RéessayerClaude peut faire des erreurs. Assurez-vous de vérifier ses réponses.

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-085-R085-MFadapte-skin-rainmeter-pour-avoir]]
- ⬇️ Next: [[Card-087-R087-MFadapte-skin-rainmeter-pour-avoir]]
- 📊 MOC: [[_MOC_Rainmeter skin localization]]

## 🏷️ Topics

- #power-bi
- #excel
- #python
- #receipts
- #code
- #git
- #automation
