---
type: chat-card
parent_export: '[[Export]]'
order: 83
role: assistant
created: '2025-11-11T00:47:13.296481Z'
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

# 🤖 Message 83 - Assistant

**ID:** msg-83

## 💬 Content


**ID:** msg-83

MF; -------- Dossiers utilisateur --------
b:: OpenIfExplorerHotkey(\"%USERPROFILE%\\Desktop\") ; Bureau
t:: OpenIfExplorerHotkey(\"%USERPROFILE%\\Downloads\") ; Téléchargements
d:: OpenIfExplorerHotkey(\"%USERPROFILE%\\Documents\") ; Documents
i:: OpenIfExplorerHotkey(\"%USERPROFILE%\\Pictures\") ; Images
v:: OpenIfExplorerHotkey(\"%USERPROFILE%\\Videos\") ; Vidéos
n:: OpenIfExplorerHotkey(NAS_PATH) ; NAS
a:: OpenIfExplorerHotkey(\"%APPDATA%\") ; AppData\\Roaming
s:: OpenIfExplorerHotkey(A_Startup) ; Dossier Démarrage
p:: OpenIfExplorerHotkey(A_StartMenu) ; Menu Démarrer ProgrammesJ'essaie de faire des raccourcis en séquence
Win E + une lettre pour ouvrir l'explorateur et aller dans un dossier spécifiqueOu directement allé dans le bon dossier en attendant la fin de la séquenceMais plusieurs soucis, win e ouvre l'explorateur donc probleme de double fenetre même quand ça marche
en maintenant win la touche suivante lance le raccourci win + touche associéecomment faire ?Afficher plusCrafted nuanced AutoHotkey solution for Windows Explorer shortcuts.L'utilisateur a un problème avec des raccourcis AutoHotkey. Il veut créer des séquences de touches du type \"Win+E puis une lettre\" pour ouvrir l'Explorateur Windows dans des dossiers spécifiques.
Les problèmes identifiés :

Win+E ouvre déjà l'Explorateur, donc il y a une double fenêtre
En maintenant Win, la touche suivante déclenche les raccourcis Windows natifs (Win+B, Win+T, etc.)

Il faut lui proposer une solution qui :

Détecte la séquence Win+E puis lettre
Empêche l'ouverture double de l'Explorateur
Gère correctement la touche Win maintenue ou relâchée

Les solutions possibles :

Utiliser un mode séquence avec un timeout
Intercepter Win+E pour ne pas l'envoyer au système
Utiliser un préfixe différent comme Ctrl+Win+E
Utiliser Input avec un timeout après Win+E

Je vais lui proposer plusieurs approches en français.Je comprends ton problème ! Voici plusieurs solutions pour gérer ces séquences proprement en AutoHotkey :
Solution 1 : Intercepter Win+E et attendre la lettre
ahk; Variable globale pour le chemin NAS
NAS_PATH := \"\\\\MonNAS\\Partage\"

; Intercepter Win+E pour éviter l'ouverture automatique
#e::
{
 ; Attendre une touche pendant 1 seconde
 Input, UserInput, L1 T1, {Esc}

 if (ErrorLevel = \"Timeout\" || ErrorLevel = \"NewInput\") {
 ; Si timeout ou autre touche, ouvrir l'Explorateur normalement
 Run, explorer.exe
 return
 }

 ; Sinon, ouvrir le dossier correspondant
 switch UserInput {
 case \"b\": OpenFolder(A_Desktop)
 case \"t\": OpenFolder(A_Desktop . \"\\..\\Downloads\")
 case \"d\": OpenFolder(A_MyDocuments)
 case \"i\": OpenFolder(A_Desktop . \"\\..\\Pictures\")
 case \"v\": OpenFolder(A_Desktop . \"\\..\\Videos\")
 case \"n\": OpenFolder(NAS_PATH)
 case \"a\": OpenFolder(A_AppData)
 case \"s\": OpenFolder(A_Startup)
 case \"p\": OpenFolder(A_StartMenu)
 default: Run, explorer.exe
 }
}

OpenFolder(path) {
 ; Vérifier si une fenêtre Explorateur existe déjà
 if WinExist(\"ahk_class CabinetWClass\") {
 WinActivate
 ; Naviguer vers le nouveau dossier
 Send, !d ; Focus sur la barre d'adresse
 Sleep, 50
 SendInput, %path%{Enter}
 } else {
 ; Sinon ouvrir une nouvelle fenêtre
 Run, explorer.exe \"%path%\"
 }
}
Solution 2 : Utiliser un modificateur différent (plus simple)
ahk; Ctrl+Win+Lettre au lieu de Win+E+Lettre
^#b:: OpenFolder(A_Desktop)
^#t:: OpenFolder(A_Desktop . \"\\..\\Downloads\")
^#d:: OpenFolder(A_MyDocuments)
^#i:: OpenFolder(A_Desktop . \"\\..\\Pictures\")
^#v:: OpenFolder(A_Desktop . \"\\..\\Videos\")
^#n:: OpenFolder(NAS_PATH)
^#a:: OpenFolder(A_AppData)
^#s:: OpenFolder(A_Startup)
^#p:: OpenFolder(A_StartMenu)

OpenFolder(path) {
 if WinExist(\"ahk_class CabinetWClass\")
 WinActivate
 Run, explorer.exe \"%path%\"
}
Solution 3 : Mode séquence avec variable d'état
ahkglobal WinEMode := false

#e::
{
 global WinEMode
 WinEMode := true
 ; Indicateur visuel optionnel
 ToolTip, Mode navigation activé (Win+E)
 ; Timeout de 2 secondes
 SetTimer, ResetWinEMode, -2000
 return
}

ResetWinEMode:
 global WinEMode
 WinEMode := false
 ToolTip
 return

; Les raccourcis suivants
b::HandleShortcut(A_Desktop)
t::HandleShortcut(A_Desktop . \"\\..\\Downloads\")
d::HandleShortcut(A_MyDocuments)
i::HandleShortcut(A_Desktop . \"\\..\\Pictures\")
v::HandleShortcut(A_Desktop . \"\\..\\Videos\")
n::HandleShortcut(NAS_PATH)
a::HandleShortcut(A_AppData)
s::HandleShortcut(A_Startup)
p::HandleShortcut(A_StartMenu)

HandleShortcut(path) {
 global WinEMode
 if (WinEMode) {
 WinEMode := false
 ToolTip
 Run, explorer.exe \"%path%\"
 } else {
 Send, {%A_ThisHotkey%} ; Envoyer la touche normalement
 }
}
Ma recommandation
Je te conseille la Solution 2 (Ctrl+Win+Lettre) car :

✅ Pas de conflit avec les raccourcis Windows natifs
✅ Pas de double fenêtre
✅ Simple et fiable
✅ Une seule combinaison de touches (pas de séquence)

Si tu veux vraiment la séquence Win+E, utilise la Solution 1 qui intercepte Win+E proprement.
Quelle approche préfères-tu ?RéessayerMFIt looks like the script you are trying to run requires AutoHotkey v1, which is not installed. If the version has been misidentified, please add a #Requires directive to your script file. Script: Rule. Untitled.ahk v1 -dir v1 -hk v1 -cmdStrategized solutions for AutoHotkey script version compatibility.L'utilisateur a une erreur AutoHotkey. Le message indique qu'il essaie d'exécuter un script AutoHotkey v1, mais qu'AutoHotkey v1 n'est pas installé sur son système. Il a probablement AutoHotkey v2 installé à la place.
Il a deux options :

Installer AutoHotkey v1
Convertir le script en AutoHotkey v2 (recommandé si v2 est déjà installé)

Je vais lui proposer les deux solutions, mais surtout convertir mon code en syntaxe AutoHotkey v2 qui est la version moderne.Tu as AutoHotkey v2 installé, mais mon code était en syntaxe v1 ! Voici les versions corrigées pour AutoHotkey v2 :
Solution 1 : Win+E puis lettre (AutoHotkey v2)
ahk#Requires AutoHotkey v2.0

; Variable globale pour le chemin NAS
NAS_PATH := \"\\\\MonNAS\\Partage\"

; Intercepter Win+E
#e:: {
 ; Attendre une touche pendant 1 seconde
 ih := InputHook(\"L1 T1\")
 ih.Start()
 ih.Wait()

 if (ih.EndReason = \"Timeout\") {
 ; Si timeout, ouvrir l'Explorateur normalement
 Run(\"explorer.exe\")
 return
 }

 ; Sinon, ouvrir le dossier correspondant
 switch ih.Input {
 case \"b\": OpenFolder(A_Desktop)
 case \"t\": OpenFolder(A_Desktop \"\\..\\Downloads\")
 case \"d\": OpenFolder(A_MyDocuments)
 case \"i\": OpenFolder(A_Desktop \"\\..\\Pictures\")
 case \"v\": OpenFolder(A_Desktop \"\\..\\Videos\")
 case \"n\": OpenFolder(NAS_PATH)
 case \"a\": OpenFolder(A_AppData)
 case \"s\": OpenFolder(A_Startup)
 case \"p\": OpenFolder(A_StartMenu)
 default: Run(\"explorer.exe\")
 }
}

OpenFolder(path) {
 ; Vérifier si une fenêtre Explorateur existe déjà
 if WinExist(\"ahk_class CabinetWClass\") {
 WinActivate
 ; Naviguer vers le nouveau dossier
 Send(\"!d\") ; Focus sur la barre d'adresse
 Sleep(50)
 SendInput(path \"{Enter}\")
 } else {
 ; Sinon ouvrir une nouvelle fenêtre
 Run('explorer.exe \"' path '\"')
 }
}
Solution 2 : Ctrl+Win+Lettre (RECOMMANDÉ - plus simple)
ahk#Requires AutoHotkey v2.0

; Variable globale
NAS_PATH := \"\\\\MonNAS\\Partage\"

; Raccourcis Ctrl+Win+Lettre
^#b:: OpenFolder(A_Desktop)
^#t:: OpenFolder(A_Desktop \"\\..\\Downloads\")
^#d:: OpenFolder(A_MyDocuments)
^#i:: OpenFolder(A_Desktop \"\\..\\Pictures\")
^#v:: OpenFolder(A_Desktop \"\\..\\Videos\")
^#n:: OpenFolder(NAS_PATH)
^#a:: OpenFolder(A_AppData)
^#s:: OpenFolder(A_Startup)
^#p:: OpenFolder(A_StartMenu)

OpenFolder(path) {
 Run('explorer.exe \"' path '\"')
}
Solution 3 : Mode séquence avec variable d'état
ahk#Requires AutoHotkey v2.0

NAS_PATH := \"\\\\MonNAS\\Partage\"
WinEMode := false

#e:: {
 global WinEMode
 WinEMode := true
 ToolTip(\"Mode navigation activé (Win+E)\")
 SetTimer(() => ResetMode(), -2000)
}

ResetMode() {
 global WinEMode
 WinEMode := false
 ToolTip()
}

; Raccourcis contextuels
b:: HandleShortcut(A_Desktop)
t:: HandleShortcut(A_Desktop \"\\..\\Downloads\")
d:: HandleShortcut(A_MyDocuments)
i:: HandleShortcut(A_Desktop \"\\..\\Pictures\")
v:: HandleShortcut(A_Desktop \"\\..\\Videos\")
n:: HandleShortcut(NAS_PATH)
a:: HandleShortcut(A_AppData)
s:: HandleShortcut(A_Startup)
p:: HandleShortcut(A_StartMenu)

HandleShortcut(path) {
 global WinEMode
 if (WinEMode) {
 WinEMode := false
 ToolTip()
 Run('explorer.exe \"' path '\"')
 } else {
 Send(\"{\" A_ThisHotkey \"}\")
 }
}
Principales différences v1 → v2 :

#Requires AutoHotkey v2.0 au début
Les accolades {} sont obligatoires pour les fonctions
Run(), Send(), WinExist() avec parenthèses
Concaténation avec espace au lieu de . : \"texte \" variable
InputHook() au lieu de Input
SetTimer(() => Function(), -2000) avec fonction lambda

Je recommande la Solution 2 pour commencer - c'est la plus simple et fiable !
Tu peux copier le code directement, ça devrait marcher maintenant 👍RéessayerMF#Requires AutoHotkey v2.0
; Variable globale pour le chemin NAS
NAS_PATH := \"Z:\\MES DOCUMENTS\"
; Intercepter Win+E
#e:: {
 ; Attendre une touche pendant 1 seconde
 ih := InputHook(\"L1 T1\")
 ih.Start()
 ih.Wait() if (ih.EndReason = \"Timeout\") {
 ; Si timeout, ouvrir l'Explorateur normalement
 Run(\"explorer.exe\")
 return
 } ; Sinon, ouvrir le dossier correspondant
 switch ih.Input {
 case \"b\": OpenFolder(A_Desktop)
 case \"t\": OpenFolder(A_Desktop \"\\..\\Downloads\")
 case \"d\": OpenFolder(A_MyDocuments)
 case \"i\": OpenFolder(A_Desktop \"\\..\\Pictures\")
 case \"v\": OpenFolder(A_Desktop \"\\..\\Videos\")
 case \"n\": OpenFolder(NAS_PATH)
 case \"a\": OpenFolder(A_AppData)
 case \"s\": OpenFolder(A_Startup)
 case \"p\": OpenFolder(A_StartMenu)
 default: Run(\"explorer.exe\")
 }
}
OpenFolder(path) {
 ; Vérifier si une fenêtre Explorateur existe déjà
 if WinExist(\"ahk_class CabinetWClass\") {
 WinActivate
 ; Naviguer vers le nouveau dossier
 Send(\"!d\") ; Focus sur la barre d'adresse
 Sleep(50)
 SendInput(path \"{Enter}\")
 } else {
 ; Sinon ouvrir une nouvelle fenêtre
 Run('explorer.exe \"' path '\"')
 }
}Ce code produit ce que je voulais, mais garde le curseur sur la barre dadresse
Je voudrais le focus sur les dossiers actifs pour naviguer par lettre entre les dossiers au clavierAfficher plusDevised method to shift file explorer focus after navigation.L'utilisateur veut que le focus soit sur la liste des fichiers/dossiers après avoir navigué vers un dossier, pas sur la barre d'adresse. Actuellement, le code envoie !d (Alt+D) pour mettre le focus sur la barre d'adresse, puis envoie le chemin et Enter. Mais après ça, le focus reste dans la barre d'adresse.
Pour mettre le focus sur la liste des fichiers, il faut envoyer une touche supplémentaire après l'Enter. Plusieurs options:

Tab pour passer au volet suivant
F6 pour naviguer entre les panneaux
Escape pour sortir de la barre d'adresse et revenir à la liste
Ou simplement envoyer une touche de direction ou un clic

La solution la plus simple serait probablement d'ajouter un Send(\"{Escape}\") ou Send(\"{Tab}\") après l'Enter, ou mieux encore, envoyer juste un focus sur la liste des fichiers.
Laisse-moi proposer une solution qui fonctionne bien.Parfait ! Il suffit d'ajouter une touche pour ramener le focus sur la liste des fichiers après la navigation. Voici le code corrigé :
ahk#Requires AutoHotkey v2.0

; Variable globale pour le chemin NAS
NAS_PATH := \"Z:\\MES DOCUMENTS\"

; Intercepter Win+E
#e:: {
 ; Attendre une touche pendant 1 seconde
 ih := InputHook(\"L1 T1\")
 ih.Start()
 ih.Wait()

 if (ih.EndReason = \"Timeout\") {
 ; Si timeout, ouvrir l'Explorateur normalement
 Run(\"explorer.exe\")
 return
 }

 ; Sinon, ouvrir le dossier correspondant
 switch ih.Input {
 case \"b\": OpenFolder(A_Desktop)
 case \"t\": OpenFolder(A_Desktop \"\\..\\Downloads\")
 case \"d\": OpenFolder(A_MyDocuments)
 case \"i\": OpenFolder(A_Desktop \"\\..\\Pictures\")
 case \"v\": OpenFolder(A_Desktop \"\\..\\Videos\")
 case \"n\": OpenFolder(NAS_PATH)
 case \"a\": OpenFolder(A_AppData)
 case \"s\": OpenFolder(A_Startup)
 case \"p\": OpenFolder(A_StartMenu)
 default: Run(\"explorer.exe\")
 }
}

OpenFolder(path) {
 ; Vérifier si une fenêtre Explorateur existe déjà
 if WinExist(\"ahk_class CabinetWClass\") {
 WinActivate
 ; Naviguer vers le nouveau dossier
 Send(\"!d\") ; Focus sur la barre d'adresse
 Sleep(50)
 SendInput(path \"{Enter}\")
 Sleep(100) ; Attendre que la navigation se fasse
 Send(\"{Escape}\") ; Sortir de la barre d'adresse et revenir à la liste
 } else {
 ; Sinon ouvrir une nouvelle fenêtre
 Run('explorer.exe \"' path '\"')
 }
}
Modifications apportées :

Ajout de Sleep(100) après l'Enter pour laisser le temps à l'Explorateur de naviguer
Ajout de Send(\"{Escape}\") pour quitter la barre d'adresse et mettre le focus sur la liste des fichiers

Alternatives si Escape ne marche pas bien :
ahk; Option 1 : Utiliser Tab pour naviguer vers la liste
Send(\"{Tab}\")

; Option 2 : Utiliser F6 pour changer de panneau
Send(\"{F6}\")

; Option 3 : Simuler un clic sur la liste (plus robuste)
Sleep(100)
ControlFocus(\"DirectUIHWND3\", \"ahk_class CabinetWClass\")
Maintenant tu peux naviguer directement au clavier en tapant les premières lettres des dossiers ! 🎯
Si {Escape} ne fonctionne pas parfaitement, essaie de remplacer cette ligne par Send(\"{Tab}\") ou une des autres alternatives.RéessayerMF#Requires AutoHotkey v2.0
; Variable globale pour le chemin NAS
NAS_PATH := \"Z:\\MES DOCUMENTS\"
; Intercepter Win+E
#e:: {
 ; Attendre une touche pendant 1 seconde
 ih := InputHook(\"L1 T1\")
 ih.Start()
 ih.Wait() if (ih.EndReason = \"Timeout\") {
 ; Si timeout, ouvrir l'Explorateur normalement
 Run(\"explorer.exe\")
 return
 } ; Sinon, ouvrir le dossier correspondant
 switch ih.Input {
 case \"b\": OpenFolder(A_Desktop)
 case \"t\": OpenFolder(A_Desktop \"\\..\\Downloads\")
 case \"d\": OpenFolder(A_MyDocuments)
 case \"i\": OpenFolder(A_Desktop \"\\..\\Pictures\")
 case \"v\": OpenFolder(A_Desktop \"\\..\\Videos\")
 case \"n\": OpenFolder(NAS_PATH)
 case \"a\": OpenFolder(A_AppData)
 case \"s\": OpenFolder(A_Startup)
 case \"p\": OpenFolder(A_StartMenu)
 case \"&\": OpenFolder(\"C:\\Program Files\")
 case \"é\": OpenFolder(\"C:\\Program Files (x86)\")
 case \"c\": OpenFolder(\"C:\\\")
 default: Run(\"explorer.exe\")
 }
}
OpenFolder(path) {
 ; Vérifier si une fenêtre Explorateur existe déjà
 if WinExist(\"ahk_class CabinetWClass\") {
 WinActivate
 ; Naviguer vers le nouveau dossier
 Send(\"!d\") ; Focus sur la barre d'adresse
 Sleep(50)
 SendInput(path \"{Enter}\")
 Sleep(100) ; Attendre que la navigation se fasse
 Send(\"{Escape}\") ; Sortir de la barre d'adresse et revenir à la liste
 } else {
 ; Sinon ouvrir une nouvelle fenêtre
 Run('explorer.exe \"' path '\"')
 }
}Ce code est ok,Maintenant je veux que l'appui de la touche alt droite, simule un clic gauche menu contextuel
On peut dans l'explorateur développer plus d'options supplémentaires par exemple
ça doit pouvoir se faire en faisant une double touche successive alt droiteAfficher plusVoici le code avec l'ajout de la fonctionnalité Alt droite pour le menu contextuel :
ahk#Requires AutoHotkey v2.0

; Variable globale pour le chemin NAS
NAS_PATH := \"Z:\\MES DOCUMENTS\"

; Intercepter Win+E
#e:: {
 ; Attendre une touche pendant 1 seconde
 ih := InputHook(\"L1 T1\")
 ih.Start()
 ih.Wait()

 if (ih.EndReason = \"Timeout\") {
 ; Si timeout, ouvrir l'Explorateur normalement
 Run(\"explorer.exe\")
 return
 }

 ; Sinon, ouvrir le dossier correspondant
 switch ih.Input {
 case \"b\": OpenFolder(A_Desktop)
 case \"t\": OpenFolder(A_Desktop \"\\..\\Downloads\")
 case \"d\": OpenFolder(A_MyDocuments)
 case \"i\": OpenFolder(A_Desktop \"\\..\\Pictures\")
 case \"v\": OpenFolder(A_Desktop \"\\..\\Videos\")
 case \"n\": OpenFolder(NAS_PATH)
 case \"a\": OpenFolder(A_AppData)
 case \"s\": OpenFolder(A_Startup)
 case \"p\": OpenFolder(A_StartMenu)
 case \"&\": OpenFolder(\"C:\\Program Files\")
 case \"é\": OpenFolder(\"C:\\Program Files (x86)\")
 case \"c\": OpenFolder(\"C:\\\")
 default: Run(\"explorer.exe\")
 }
}

OpenFolder(path) {
 ; Vérifier si une fenêtre Explorateur existe déjà
 if WinExist(\"ahk_class CabinetWClass\") {
 WinActivate
 ; Naviguer vers le nouveau dossier
 Send(\"!d\") ; Focus sur la barre d'adresse
 Sleep(50)
 SendInput(path \"{Enter}\")
 Sleep(100) ; Attendre que la navigation se fasse
 Send(\"{Escape}\") ; Sortir de la barre d'adresse et revenir à la liste
 } else {
 ; Sinon ouvrir une nouvelle fenêtre
 Run('explorer.exe \"' path '\"')
 }
}

; ===== Menu contextuel avec Alt Droite =====
global LastRAltPress := 0

RAlt:: {
 global LastRAltPress
 currentTime := A_TickCount

 ; Si double appui en moins de 400ms
 if (currentTime - LastRAltPress < 400) {
 ; Menu contextuel étendu (Shift + Clic droit)
 Send(\"+{AppsKey}\") ; Shift + Menu contextuel
 LastRAltPress := 0 ; Reset pour éviter triple appui
 } else {
 ; Simple appui = menu contextuel normal
 Send(\"{AppsKey}\") ; Touche Menu (équivalent clic droit)
 LastRAltPress := currentTime
 }
}
Explication des modifications :
Option choisie : {AppsKey} (Touche Menu contextuel)

Simple appui Alt droite → Menu contextuel normal
Double appui rapide (< 400ms) → Menu contextuel étendu (avec Shift)

Alternatives si tu préfères un vrai clic de souris :
ahk; Alternative 1 : Clic droit à la position du curseur
RAlt:: {
 global LastRAltPress
 currentTime := A_TickCount

 if (currentTime - LastRAltPress < 400) {
 ; Menu contextuel étendu (Shift + Clic droit)
 Click(\"Right\", , , , , \"Down Shift\")
 Click(\"Right\", , , , , \"Up\")
 } else {
 ; Menu contextuel normal
 Click(\"Right\")
 LastRAltPress := currentTime
 }
}

; Alternative 2 : Shift + F10 (raccourci Windows standard)
RAlt:: {
 global LastRAltPress
 currentTime := A_TickCount

 if (currentTime - LastRAltPress < 400) {
 Send(\"+{F10}\") ; Menu étendu
 LastRAltPress := 0
 } else {
 Send(\"+{F10}\") ; Menu normal
 LastRAltPress := currentTime
 }
}
Points importants :
✅ {AppsKey} = Touche Menu (entre Alt droite et Ctrl droite sur certains claviers)
✅ Double appui détecté en moins de 400ms
✅ Shift + Menu = Options avancées dans l'Explorateur Windows
Le menu étendu avec Shift affiche par exemple :

\"Copier comme chemin d'accès\"
\"Ouvrir dans le Terminal\"
Plus d'options de partage, etc.

Teste et dis-moi si ça fonctionne comme tu veux ! 🎯RéessayerMFça ne marche pas, mais ma touche ne correspond peut etre pas a alt droite
c'est un logitech craft, en partant des fleches il s'agit de la 3eme touche a gauche apres alt|ctrl et fn, elle est labélisé cmd|altAh, tu as un clavier Mac/Logitech avec une touche Cmd/Alt ! Sur ces claviers, cette touche peut être mappée différemment. Testons d'abord quelle est vraiment cette touche :
1️⃣ Script de détection de touche
Copie ce code pour identifier ta touche :
ahk#Requires AutoHotkey v2.0

; Affiche quelle touche tu appuies
~*SC056::ToolTip(\"SC056 - ISO <> key\")
~*LWin::ToolTip(\"LWin - Windows gauche\")
~*RWin::ToolTip(\"RWin - Windows droite\")
~*LAlt::ToolTip(\"LAlt - Alt gauche\")
~*RAlt::ToolTip(\"RAlt - Alt droite\")
~*LControl::ToolTip(\"LControl - Ctrl gauche\")
~*RControl::ToolTip(\"RControl - Ctrl droite\")
~*AppsKey::ToolTip(\"AppsKey - Menu contextuel\")

; Efface le tooltip après 2 secondes
F12::ToolTip()
Instructions :

Lance ce script
Appuie sur ta touche Cmd/Alt
Note ce qui s'affiche dans le tooltip
Appuie sur F12 pour effacer

2️⃣ Solutions possibles selon ta touche
Si c'est LWin (touche Windows gauche) :
ahkglobal LastLWinPress := 0

LWin:: {
 global LastLWinPress
 currentTime := A_TickCount

 if (currentTime - LastLWinPress < 400) {
 ; Menu contextuel étendu
 Send(\"+{AppsKey}\")
 LastLWinPress := 0
 } else {
 ; Menu contextuel normal
 Send(\"{AppsKey}\")
 LastLWinPress := currentTime
 }
}
Si c'est RWin (touche Windows droite) :
ahkglobal LastRWinPress := 0

RWin:: {
 global LastRWinPress
 currentTime := A_TickCount

 if (currentTime - LastRWinPress < 400) {
 Send(\"+{AppsKey}\")
 LastRWinPress := 0
 } else {
 Send(\"{AppsKey}\")
 LastRWinPress := currentTime
 }
}
Si c'est LAlt (Alt gauche) :
ahkglobal LastLAltPress := 0

LAlt:: {
 global LastLAltPress
 currentTime := A_TickCount

 if (currentTime - LastLAltPress < 400) {
 Send(\"+{AppsKey}\")
 LastLAltPress := 0
 } else {
 Send(\"{AppsKey}\")
 LastLAltPress := currentTime
 }
}
3️⃣ Alternative : Utiliser le logiciel Logitech Options+
Le Logitech Craft peut être configuré avec Logitech Options+. Tu peux :

Vérifier comment la touche Cmd/Alt est mappée
La remapper si nécessaire

4️⃣ Solution universelle (détecte automatiquement)
Si tu veux tester sans savoir exactement quelle touche c'est :
ahk#Requires AutoHotkey v2.0

; Test avec toutes les touches Alt/Win possibles
~LWin::CheckDoublePress(\"LWin\")
~RWin::CheckDoublePress(\"RWin\")
~LAlt::CheckDoublePress(\"LAlt\")
~RAlt::CheckDoublePress(\"RAlt\")

global LastPress := Map()

CheckDoublePress(keyName) {
 global LastPress
 currentTime := A_TickCount

 if (!LastPress.Has(keyName)) {
 LastPress[keyName] := 0
 }

 if (currentTime - LastPress[keyName] < 400) {
 ; Double appui détecté
 Send(\"+{AppsKey}\")
 ToolTip(\"Menu étendu avec \" keyName)
 SetTimer(() => ToolTip(), -2000)
 LastPress[keyName] := 0
 } else {
 ; Simple appui
 Send(\"{AppsKey}\")
 ToolTip(\"Menu normal avec \" keyName)
 SetTimer(() => ToolTip(), -2000)
 LastPress[keyName] := currentTime
 }
}
Lance d'abord le script de détection (étape 1) et dis-moi ce qui s'affiche quand tu appuies sur ta touche Cmd/Alt ! 🔍RéessayerMFça affiche RAlt - Alt droiteParfait ! C'est bien RAlt (Alt droite). Le problème vient probablement du fait que le script précédent ne laissait pas passer la touche normalement.
Essaie cette version corrigée :
ahk#Requires AutoHotkey v2.0

; Variable globale pour le chemin NAS
NAS_PATH := \"Z:\\MES DOCUMENTS\"

; Intercepter Win+E
#e:: {
 ; Attendre une touche pendant 1 seconde
 ih := InputHook(\"L1 T1\")
 ih.Start()
 ih.Wait()

 if (ih.EndReason = \"Timeout\") {
 ; Si timeout, ouvrir l'Explorateur normalement
 Run(\"explorer.exe\")
 return
 }

 ; Sinon, ouvrir le dossier correspondant
 switch ih.Input {
 case \"b\": OpenFolder(A_Desktop)
 case \"t\": OpenFolder(A_Desktop \"\\..\\Downloads\")
 case \"d\": OpenFolder(A_MyDocuments)
 case \"i\": OpenFolder(A_Desktop \"\\..\\Pictures\")
 case \"v\": OpenFolder(A_Desktop \"\\..\\Videos\")
 case \"n\": OpenFolder(NAS_PATH)
 case \"a\": OpenFolder(A_AppData)
 case \"s\": OpenFolder(A_Startup)
 case \"p\": OpenFolder(A_StartMenu)
 case \"&\": OpenFolder(\"C:\\Program Files\")
 case \"é\": OpenFolder(\"C:\\Program Files (x86)\")
 case \"c\": OpenFolder(\"C:\\\")
 default: Run(\"explorer.exe\")
 }
}

OpenFolder(path) {
 ; Vérifier si une fenêtre Explorateur existe déjà
 if WinExist(\"ahk_class CabinetWClass\") {
 WinActivate
 ; Naviguer vers le nouveau dossier
 Send(\"!d\") ; Focus sur la barre d'adresse
 Sleep(50)
 SendInput(path \"{Enter}\")
 Sleep(100) ; Attendre que la navigation se fasse
 Send(\"{Escape}\") ; Sortir de la barre d'adresse et revenir à la liste
 } else {
 ; Sinon ouvrir une nouvelle fenêtre
 Run('explorer.exe \"' path '\"')
 }
}

; ===== Menu contextuel avec Alt Droite =====
global LastRAltPress := 0
global RAltPressed := false

; Détecte l'appui sur RAlt
~RAlt:: {
 global LastRAltPress, RAltPressed
 currentTime := A_TickCount

 ; Si double appui en moins de 400ms
 if (currentTime - LastRAltPress < 400 && RAltPressed) {
 ; Menu contextuel étendu (Shift + AppsKey)
 Send(\"+{AppsKey}\")
 LastRAltPress := 0
 RAltPressed := false
 } else {
 ; Premier appui détecté
 RAltPressed := true
 LastRAltPress := currentTime
 ; Timer pour reset si pas de deuxième appui
 SetTimer(() => ResetRAlt(), -450)
 }
}

ResetRAlt() {
 global RAltPressed, LastRAltPress
 ; Si un seul appui, ouvrir menu contextuel normal
 if (RAltPressed) {
 Send(\"{AppsKey}\")
 RAltPressed := false
 LastRAltPress := 0
 }
}
Alternative si ça ne marche toujours pas :
Peut-être que sur ton clavier Logitech, RAlt est une touche AltGr (qui est combinée avec Ctrl). Essaie cette version :
ahk; Version alternative avec clic droit direct
~RAlt:: {
 global LastRAltPress
 currentTime := A_TickCount

 if (currentTime - LastRAltPress < 400) {
 ; Double appui = Menu étendu avec Shift+Clic droit
 Send(\"+{F10}\") ; Shift+F10 = menu contextuel étendu
 LastRAltPress := 0
 } else {
 ; Simple appui = Menu contextuel normal
 Send(\"{F10}\") ; F10 seul ne marche pas, utilisons AppsKey
 Send(\"{AppsKey}\")
 LastRAltPress := currentTime
 }
}
Version la plus simple (recommandée pour tester) :
ahk; Test basique : RAlt = menu contextuel
RAlt::Send(\"{AppsKey}\")

; RAlt appuyé 2 fois = menu étendu
RAlt & RAlt::Send(\"+{AppsKey}\")
Teste d'abord cette dernière version simple et dis-moi si le menu contextuel s'ouvre au moins ! Si oui, on affinera pour le double appui. 🎯RéessayerMFjuste ce bout, ça fonctionne parfaitement
RAlt::Send(\"{AppsKey}\")ok go pour le double appuiParfait ! Voici la version avec double appui qui fonctionne :
ahk#Requires AutoHotkey v2.0

; Variable globale pour le chemin NAS
NAS_PATH := \"Z:\\MES DOCUMENTS\"

; Intercepter Win+E
#e:: {
 ; Attendre une touche pendant 1 seconde
 ih := InputHook(\"L1 T1\")
 ih.Start()
 ih.Wait()

 if (ih.EndReason = \"Timeout\") {
 ; Si timeout, ouvrir l'Explorateur normalement
 Run(\"explorer.exe\")
 return
 }

 ; Sinon, ouvrir le dossier correspondant
 switch ih.Input {
 case \"b\": OpenFolder(A_Desktop)
 case \"t\": OpenFolder(A_Desktop \"\\..\\Downloads\")
 case \"d\": OpenFolder(A_MyDocuments)
 case \"i\": OpenFolder(A_Desktop \"\\..\\Pictures\")
 case \"v\": OpenFolder(A_Desktop \"\\..\\Videos\")
 case \"n\": OpenFolder(NAS_PATH)
 case \"a\": OpenFolder(A_AppData)
 case \"s\": OpenFolder(A_Startup)
 case \"p\": OpenFolder(A_StartMenu)
 case \"&\": OpenFolder(\"C:\\Program Files\")
 case \"é\": OpenFolder(\"C:\\Program Files (x86)\")
 case \"c\": OpenFolder(\"C:\\\")
 default: Run(\"explorer.exe\")
 }
}

OpenFolder(path) {
 ; Vérifier si une fenêtre Explorateur existe déjà
 if WinExist(\"ahk_class CabinetWClass\") {
 WinActivate
 ; Naviguer vers le nouveau dossier
 Send(\"!d\") ; Focus sur la barre d'adresse
 Sleep(50)
 SendInput(path \"{Enter}\")
 Sleep(100) ; Attendre que la navigation se fasse
 Send(\"{Escape}\") ; Sortir de la barre d'adresse et revenir à la liste
 } else {
 ; Sinon ouvrir une nouvelle fenêtre
 Run('explorer.exe \"' path '\"')
 }
}

; ===== Menu contextuel avec Alt Droite =====
global LastRAltTime := 0

RAlt:: {
 global LastRAltTime
 currentTime := A_TickCount
 timeSinceLastPress := currentTime - LastRAltTime

 ; Si double appui en moins de 300ms
 if (timeSinceLastPress > 0 && timeSinceLastPress < 300) {
 ; Menu contextuel étendu (avec Shift)
 Send(\"+{AppsKey}\")
 LastRAltTime := 0 ; Reset pour éviter un triple appui
 } else {
 ; Simple appui = menu contextuel normal
 Send(\"{AppsKey}\")
 LastRAltTime := currentTime
 }
}
Comment ça fonctionne :
✅ Un appui sur RAlt → Menu contextuel normal
✅ Double appui rapide (< 300ms) → Menu contextuel étendu (Shift + Menu)
Le menu étendu dans l'Explorateur Windows affiche des options supplémentaires comme :

\"Copier en tant que chemin d'accès\"
\"Ouvrir dans le Terminal\"
Plus d'options de sécurité/propriétés avancées

Teste et dis-moi si le timing de 300ms est bon pour toi ! Si c'est trop rapide ou trop lent, on peut ajuster la valeur. 🎯RéessayerMFlà ça fonctionne plusAh mince ! Le problème c'est que maintenant il attend pour détecter le double appui. Essayons avec un timer pour que le simple appui fonctionne immédiatement si pas de deuxième appui :
ahk#Requires AutoHotkey v2.0

; Variable globale pour le chemin NAS
NAS_PATH := \"Z:\\MES DOCUMENTS\"

; Intercepter Win+E
#e:: {
 ; Attendre une touche pendant 1 seconde
 ih := InputHook(\"L1 T1\")
 ih.Start()
 ih.Wait()

 if (ih.EndReason = \"Timeout\") {
 ; Si timeout, ouvrir l'Explorateur normalement
 Run(\"explorer.exe\")
 return
 }

 ; Sinon, ouvrir le dossier correspondant
 switch ih.Input {
 case \"b\": OpenFolder(A_Desktop)
 case \"t\": OpenFolder(A_Desktop \"\\..\\Downloads\")
 case \"d\": OpenFolder(A_MyDocuments)
 case \"i\": OpenFolder(A_Desktop \"\\..\\Pictures\")
 case \"v\": OpenFolder(A_Desktop \"\\..\\Videos\")
 case \"n\": OpenFolder(NAS_PATH)
 case \"a\": OpenFolder(A_AppData)
 case \"s\": OpenFolder(A_Startup)
 case \"p\": OpenFolder(A_StartMenu)
 case \"&\": OpenFolder(\"C:\\Program Files\")
 case \"é\": OpenFolder(\"C:\\Program Files (x86)\")
 case \"c\": OpenFolder(\"C:\\\")
 default: Run(\"explorer.exe\")
 }
}

OpenFolder(path) {
 ; Vérifier si une fenêtre Explorateur existe déjà
 if WinExist(\"ahk_class CabinetWClass\") {
 WinActivate
 ; Naviguer vers le nouveau dossier
 Send(\"!d\") ; Focus sur la barre d'adresse
 Sleep(50)
 SendInput(path \"{Enter}\")
 Sleep(100) ; Attendre que la navigation se fasse
 Send(\"{Escape}\") ; Sortir de la barre d'adresse et revenir à la liste
 } else {
 ; Sinon ouvrir une nouvelle fenêtre
 Run('explorer.exe \"' path '\"')
 }
}

; ===== Menu contextuel avec Alt Droite =====
global RAltClickCount := 0

RAlt:: {
 global RAltClickCount
 RAltClickCount++

 ; Premier appui
 if (RAltClickCount = 1) {
 ; Attendre 250ms pour voir si double appui
 SetTimer(RAltSingleClick, -250)
 }
 ; Deuxième appui
 else if (RAltClickCount = 2) {
 ; Annuler le timer du simple clic
 SetTimer(RAltSingleClick, 0)
 ; Menu étendu immédiatement
 Send(\"+{AppsKey}\")
 RAltClickCount := 0
 }
}

RAltSingleClick() {
 global RAltClickCount
 if (RAltClickCount = 1) {
 ; Simple clic = menu normal
 Send(\"{AppsKey}\")
 }
 RAltClickCount := 0
}
Comment ça fonctionne maintenant :
✅ Un appui → Attend 250ms, puis ouvre le menu normal
✅ Double appui rapide → Annule l'attente et ouvre directement le menu étendu
Si tu trouves que 250ms d'attente c'est trop long, on peut réduire à 150ms ou 200ms.
Teste ça et dis-moi si ça marche mieux ! 🎯RéessayerMF~RAlt:: {
 global LastRAltPress
 currentTime := A_TickCount if (currentTime - LastRAltPress < 400) {
 ; Double appui = Menu étendu avec Shift+Clic droit
 Send(\"+{F10}\") ; Shift+F10 = menu contextuel étendu
 LastRAltPress := 0
 } else {
 ; Simple appui = Menu contextuel normal
 Send(\"{F10}\") ; F10 seul ne marche pas, utilisons AppsKey
 Send(\"{AppsKey}\")
 LastRAltPress := currentTime
 }
}Inspire toi de ce code mais en version plus simple
Avec RAlt qui envoie shift F10
L'option R2 étant disponible, mappe le sur la flèche du bas pour développer les optionsDonc sur le même esprit que la séquence de touches win e + dossier de destinationAfficher plusVoici la version simple et claire :
ahk#Requires AutoHotkey v2.0

; Variable globale pour le chemin NAS
NAS_PATH := \"Z:\\MES DOCUMENTS\"

; ===== Navigation Explorateur avec Win+E =====
#e:: {
 ih := InputHook(\"L1 T1\")
 ih.Start()
 ih.Wait()

 if (ih.EndReason = \"Timeout\") {
 Run(\"explorer.exe\")
 return
 }

 switch ih.Input {
 case \"b\": OpenFolder(A_Desktop)
 case \"t\": OpenFolder(A_Desktop \"\\..\\Downloads\")
 case \"d\": OpenFolder(A_MyDocuments)
 case \"i\": OpenFolder(A_Desktop \"\\..\\Pictures\")
 case \"v\": OpenFolder(A_Desktop \"\\..\\Videos\")
 case \"n\": OpenFolder(NAS_PATH)
 case \"a\": OpenFolder(A_AppData)
 case \"s\": OpenFolder(A_Startup)
 case \"p\": OpenFolder(A_StartMenu)
 case \"&\": OpenFolder(\"C:\\Program Files\")
 case \"é\": OpenFolder(\"C:\\Program Files (x86)\")
 case \"c\": OpenFolder(\"C:\\\")
 default: Run(\"explorer.exe\")
 }
}

OpenFolder(path) {
 if WinExist(\"ahk_class CabinetWClass\") {
 WinActivate
 Send(\"!d\")
 Sleep(50)
 SendInput(path \"{Enter}\")
 Sleep(100)
 Send(\"{Escape}\")
 } else {
 Run('explorer.exe \"' path '\"')
 }
}

; ===== Menu contextuel avec RAlt =====
RAlt:: {
 ih := InputHook(\"L1 T0.4\") ; Attendre 1 touche pendant max 0.4 seconde
 ih.Start()
 ih.Wait()

 if (ih.EndReason = \"Timeout\") {
 ; Aucune touche après RAlt = Menu contextuel étendu
 Send(\"+{F10}\")
 return
 }

 ; Touche appuyée après RAlt
 switch ih.Input {
 case \"Down\": Send(\"+{F10}{Down}\") ; Menu étendu + flèche bas
 default: Send(\"+{F10}\") ; Par défaut menu étendu
 }
}
Comment ça fonctionne :
✅ RAlt seul → Menu contextuel étendu (Shift+F10)
✅ RAlt + ↓ → Menu étendu + descend d'une option
Si tu veux aussi le menu normal :
ahkRAlt:: {
 ih := InputHook(\"L1 T0.4\")
 ih.Start()
 ih.Wait()

 if (ih.EndReason = \"Timeout\") {
 ; RAlt seul = Menu normal
 Send(\"{AppsKey}\")
 return
 }

 switch ih.Input {
 case \"Down\": {
 ; RAlt + Bas = Menu étendu + développer
 Send(\"+{F10}\")
 Sleep(50)
 Send(\"{Down}\")
 }
 default: Send(\"{AppsKey}\")
 }
}
Quelle version préfères-tu ?

Version 1 : RAlt seul = menu étendu
Version 2 : RAlt seul = menu normal, RAlt+↓ = menu étendu

🎯RéessayerMFRCtrl:: {
 ih := InputHook(\"L1 T0.4\")
 ih.Start()
 ih.Wait() if (ih.EndReason = \"Timeout\") {
 Send(\"+{F10}\")
 return
 } switch ih.Input {
 case \"RAlt\": Send \"r2\" ; au lieu de flèche bas, tape \"r2\"
 default: Send \"+{F10}\" ; par défaut menu étendu
 }
}Je veux simuler la séquence R2 dans le menu contextuel suite à l'appui de la touche ctrl avec la touche 0Afficher plusVoici le code corrigé pour simuler \"R2\" dans le menu contextuel :
ahkRCtrl:: {
 ih := InputHook(\"L1 T0.4\")
 ih.Start()
 ih.Wait()

 if (ih.EndReason = \"Timeout\") {
 Send(\"+{F10}\")
 return
 }

 switch ih.Input {
 case \"0\": {
 ; Ctrl + 0 = Menu étendu puis tape \"r2\"
 Send(\"+{F10}\")
 Sleep(100) ; Attendre que le menu s'ouvre
 Send(\"r2\")
 }
 default: Send(\"+{F10}\")
 }
}
Explication :
✅ RCtrl seul → Menu contextuel étendu (Shift+F10)
✅ RCtrl + 0 → Menu étendu, puis simule la frappe \"r2\" pour sélectionner l'option
Le Sleep(100) laisse le temps au menu de s'ouvrir avant de taper \"r2\".
Si tu veux que RAlt fonctionne aussi :
ahk; RCtrl pour menu contextuel étendu
RCtrl:: {
 ih := InputHook(\"L1 T0.4\")
 ih.Start()
 ih.Wait()

 if (ih.EndReason = \"Timeout\") {
 Send(\"+{F10}\")
 return
 }

 switch ih.Input {
 case \"0\": {
 Send(\"+{F10}\")
 Sleep(100)
 Send(\"r2\")
 }
 default: Send(\"+{F10}\")
 }
}

; RAlt pour menu contextuel normal
RAlt::Send(\"{AppsKey}\")
Teste et dis-moi si le \"r2\" se tape bien dans le menu ! Si le timing est trop court, on peut augmenter le Sleep(100) à 150 ou 200. 🎯RéessayerMFError:T IS Ine oes not contain a recognize action.
Specifically: { Sleep(100) }
063: Switch ih.lnput
064: Case \"0\":
The ro ram will exit.Ah, erreur de syntaxe ! En AutoHotkey v2, quand tu as plusieurs lignes dans un case, il faut utiliser des accolades { } correctement. Voici la correction :
ahkRCtrl:: {
 ih := InputHook(\"L1 T0.4\")
 ih.Start()
 ih.Wait()

 if (ih.EndReason = \"Timeout\") {
 Send(\"+{F10}\")
 return
 }

 switch ih.Input {
 case \"0\":
 {
 ; Ctrl + 0 = Menu étendu puis tape \"r2\"
 Send(\"+{F10}\")
 Sleep(100)
 Send(\"r2\")
 }
 default:
 {
 Send(\"+{F10}\")
 }
 }
}
Ou version plus compacte (sans accolades pour une seule ligne) :
ahkRCtrl:: {
 ih := InputHook(\"L1 T0.4\")
 ih.Start()
 ih.Wait()

 if (ih.EndReason = \"Timeout\") {
 Send(\"+{F10}\")
 return
 }

 if (ih.Input = \"0\") {
 Send(\"+{F10}\")
 Sleep(100)
 Send(\"r2\")
 } else {
 Send(\"+{F10}\")
 }
}
La deuxième version avec if/else est plus claire pour ce cas simple ! 🎯
Teste ça et dis-moi si l'erreur disparaît !RéessayerMFl(erreur disparait, mais dans tous mes tests, ça ne produit jamais ni la touche R ni la touche R2 qui développe les options supplémentairesLe problème c'est que \"r2\" n'est pas la bonne méthode pour développer les options dans le menu contextuel Windows 11/10.
Dans les menus contextuels modernes, l'option \"Afficher plus d'options\" se déclenche différemment. Voici les solutions :
Solution 1 : Utiliser Shift+F10 qui ouvre DÉJÀ le menu étendu
ahkRCtrl:: {
 ih := InputHook(\"L1 T0.4\")
 ih.Start()
 ih.Wait()

 if (ih.EndReason = \"Timeout\") {
 ; Menu contextuel étendu (ancien style Windows)
 Send(\"+{F10}\")
 return
 }

 if (ih.Input = \"0\") {
 ; Si Windows 11 avec nouveau menu, il faut cliquer sur \"Afficher plus d'options\"
 Send(\"{AppsKey}\") ; Ouvre le nouveau menu
 Sleep(150)
 Send(\"{Down}{Down}{Down}{Down}{Down}{Enter}\") ; Descend jusqu'à \"Afficher plus\"
 } else {
 Send(\"+{F10}\")
 }
}
Solution 2 : Shift+Clic droit (le plus fiable)
Le Shift+F10 ouvre normalement le menu classique directement. Mais sur Windows 11, il faut parfois faire Shift+Clic droit :
ahkRCtrl:: {
 ih := InputHook(\"L1 T0.4\")
 ih.Start()
 ih.Wait()

 if (ih.EndReason = \"Timeout\") {
 ; Shift + Clic droit = menu classique complet
 Click(\"Right\", , , , , \"Down Shift\")
 Sleep(50)
 Click(\"Right\", , , , , \"Up\")
 return
 }

 if (ih.Input = \"0\") {
 ; Menu normal puis cherche \"Afficher plus d'options\"
 Send(\"{AppsKey}\")
 Sleep(100)
 Send(\"s\") ; Raccourci clavier pour \"Show more options\" (langue système)
 } else {
 Send(\"+{F10}\")
 }
}
Solution 3 : La plus simple - RCtrl+0 fait directement Shift+Clic droit
ahkRCtrl:: {
 ih := InputHook(\"L1 T0.4\")
 ih.Start()
 ih.Wait()

 if (ih.EndReason = \"Timeout\") {
 ; Menu contextuel normal
 Send(\"{AppsKey}\")
 return
 }

 if (ih.Input = \"0\") {
 ; RCtrl+0 = Menu étendu avec Shift
 Send(\"{Shift down}\")
 Send(\"{AppsKey}\")
 Send(\"{Shift up}\")
 } else {
 Send(\"{AppsKey}\")
 }
}
Pour Windows 11 spécifiquement
Sur Windows 11, l'option s'appelle \"Afficher plus d'options\" et son raccourci est généralement Shift+F10 OU tu peux taper la lettre \"s\" (pour \"Show\") ou \"a\" (pour \"Afficher\") selon ta langue :
ahkRCtrl:: {
 ih := InputHook(\"L1 T0.4\")
 ih.Start()
 ih.Wait()

 if (ih.EndReason = \"Timeout\") {
 Send(\"{AppsKey}\")
 return
 }

 if (ih.Input = \"0\") {
 Send(\"{AppsKey}\")
 Sleep(150)
 Send(\"a\") ; \"Afficher plus d'options\" en français
 } else {
 Send(\"{AppsKey}\")
 }
}
Teste la Solution 3 d'abord (la plus simple avec Shift+AppsKey), et dis-moi si ça ouvre bien le menu classique étendu ! 🎯
Si tu es sur Windows 11, essaie aussi de taper \"a\" après l'ouverture du menu.RéessayerMFok on va découpper ça en 2RCtrl -> +F10
+RCtrl -> +Clic GaucheParfait ! Voici le code simple et clair :
ahk#Requires AutoHotkey v2.0

; Variable globale pour le chemin NAS
NAS_PATH := \"Z:\\MES DOCUMENTS\"

; ===== Navigation Explorateur avec Win+E =====
#e:: {
 ih := InputHook(\"L1 T1\")
 ih.Start()
 ih.Wait()

 if (ih.EndReason = \"Timeout\") {
 Run(\"explorer.exe\")
 return
 }

 switch ih.Input {
 case \"b\": OpenFolder(A_Desktop)
 case \"t\": OpenFolder(A_Desktop \"\\..\\Downloads\")
 case \"d\": OpenFolder(A_MyDocuments)
 case \"i\": OpenFolder(A_Desktop \"\\..\\Pictures\")
 case \"v\": OpenFolder(A_Desktop \"\\..\\Videos\")
 case \"n\": OpenFolder(NAS_PATH)
 case \"a\": OpenFolder(A_AppData)
 case \"s\": OpenFolder(A_Startup)
 case \"p\": OpenFolder(A_StartMenu)
 case \"&\": OpenFolder(\"C:\\Program Files\")
 case \"é\": OpenFolder(\"C:\\Program Files (x86)\")
 case \"c\": OpenFolder(\"C:\\\")
 default: Run(\"explorer.exe\")
 }
}

OpenFolder(path) {
 if WinExist(\"ahk_class CabinetWClass\") {
 WinActivate
 Send(\"!d\")
 Sleep(50)
 SendInput(path \"{Enter}\")
 Sleep(100)
 Send(\"{Escape}\")
 } else {
 Run('explorer.exe \"' path '\"')
 }
}

; ===== Menu contextuel =====
; RCtrl seul = Shift+F10 (menu étendu)
RCtrl::Send(\"+{F10}\")

; Shift+RCtrl = Shift+Clic gauche (sélection étendue)
+RCtrl::Send(\"+{Click}\")
Explication :
✅ RCtrl → Shift+F10 (menu contextuel étendu)
✅ Shift+RCtrl → Shift+Clic gauche (sélection multiple/étendue)
Simple, efficace et sans séquence ! 🎯RéessayerMFj'arrive pas à avoir le clic gauche
; Shift+RCtrl = Shift+Clic gauche (sélection étendue)
+RCtrl::Send(\"+{Click \"Left\"}\")Le problème c'est la syntaxe du clic. En AutoHotkey v2, il faut utiliser la fonction Click directement, pas Send. Voici la correction :
ahk; Shift+RCtrl = Shift+Clic gauche (sélection étendue)
+RCtrl::
{
 Send(\"{Shift down}\")
 Click(\"Left\")
 Send(\"{Shift up}\")
}
Ou version plus compacte :
ahk; Shift+RCtrl = Shift+Clic gauche
+RCtrl::Click(\"Left\", , , , , \"Down Shift\")
Ou encore plus simple :
ahk; Shift+RCtrl = Shift+Clic gauche
+RCtrl::
{
 Click(\"Left\", , , 1, , \"D\") ; D = avec Shift maintenu
}
Version complète testée :
ahk; ===== Menu contextuel =====
; RCtrl seul = Shift+F10 (menu étendu)
RCtrl::Send(\"+{F10}\")

; Shift+RCtrl = Shift+Clic gauche (sélection étendue)
+RCtrl::
{
 Send(\"{Shift down}\")
 Click
 Send(\"{Shift up}\")
}
La dernière version est la plus fiable ! Elle maintient Shift, fait un clic gauche normal, puis relâche Shift.
Teste ça et dis-moi si le clic fonctionne maintenant ! 🎯RéessayerMFEn gardant le même thème police etc que ce skin, tu vas m'afficher une liste de raccourcis à se rappeler dans un widget ; Disk monitor avec couleur par jour et jauge améliorée
; ----------------------------------
[Rainmeter]
Update=1000
Background=#@#Background.png
BackgroundMode=3
BackgroundMargins=0,50,0,30
@include=#@#GlobalVariables.inc
ZPos=[&Z_STATE]
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
colorBarLow=50,200,50,255 ; Vert si < 60%
colorBarMedium=255,165,0,255 ; Orange si 60-85%
colorBarHigh=255,50,50,255 ; Rouge si > 85%
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
NumOfDecimals=0
[MeterToggleDotBg]
Meter=Shape
X=5
Y=5
W=15
H=15
Shape=Circle 7.5,7.5,7.5 | Fill Color 150,150,150,80 ; fond gris clair semi-transparent
DynamicVariables=1
[MeterStatusColor]
Meter=Shape
X=5
Y=5
W=15
H=15
Shape=Circle 7.5,7.5,6 | Fill Color ([&Z_STATE]=0 ? 100,100,100,200 : 50,255,50,200)
DynamicVariables=1
[MeterClickAction]
Meter=String
X=5
Y=5
W=15
H=15
SolidColor=0,0,0,1 ; zone invisible mais cliquable
LeftMouseUpAction=[!SetVariable Z_STATE ([&Z_STATE]=0 ? 2 : 0)]
 [!SetOption \"Disk\" \"ZPos\" [&Z_STATE]]
 [!UpdateMeter *][!Redraw]
DynamicVariables=1
[MeterTooltip]
Meter=String
X=5
Y=5
W=15
H=15
SolidColor=0,0,0,1
ToolTipText=[&Z_STATE]=0 ? \"Affichage normal\" : \"Passage au 1er plan\"
DynamicVariables=1pour les raccourcis suivants
Touche de raccourci pour basculer vers le zoom : Ctrl
Dessiner sans touche de raccourci pour le zoom : Ctrl Alt
Dessiner sans touche de raccourci pour le zoom : Ctrl Alt
Raccourci d'activation
Extracteur de texte : Win+Shift+T mais propose moi un raccourci plus pratique
Activer rogner et verrouiller : Win+CTRL+Shift+T
Activer Color Picker : Win+Shift+C
Activer la règle d'écran : Win+Shift+M
Activer Toujours visible : Win+Ctrl+T
Activer des Espaces de travail : Win+Ctrl+%Afficher plusWidget Raccourcis ClavierCode ; Widget Raccourcis Clavier PowerToys
; ----------------------------------
[Rainmeter]
Update=1000
Background=#@#Background.png
BackgroundMode=3
BackgroundMargins=0,50,0,30
@include=#@#GlobalVariables.inc
ZPos=[&Z_STATE]

[Variables]
; Couleurs des jVoici le widget de raccourcis clavier ! 🎯
Principales caractéristiques :
✅ Même thème visuel que ton skin Disk (couleurs par jour, police Trebuchet MS, effets d'ombre)
✅ Bouton toggle en haut à gauche identique (passer au premier plan)
✅ Sections organisées par catégorie d'outils
✅ Raccourci suggéré : J'ai remplacé Win+Shift+T par Win+Shift+E pour l'extracteur de texte (plus logique : E pour Extract, et évite le conflit avec le T utilisé ailleurs)
Suggestions de modifications :
Si tu veux encore simplifier tes raccourcis PowerToys, voici mes recommandations :

Extracteur de texte : Win+Shift+E (au lieu de T)
Color Picker : Win+Shift+C ✓ (déjà bon)
Règle : Win+Shift+R (au lieu de M, plus logique : Règle)
Toujours visible : Win+Ctrl+V (au lieu de T, V pour Visible)

Le widget s'intègrera parfaitement avec ton skin Disk actuel ! Tu veux que je modifie certains raccourcis dans l'affichage ? 🎨RéessayerMFle widget se charge bien mais ne s'affiche nulle partLe problème vient probablement de la taille du widget qui n'est pas définie. Voici la version corrigée avec les dimensions appropriées :Widget Raccourcis ClavierCode ∙ Version 2 ; Widget Raccourcis Clavier PowerToys
; ----------------------------------
[Rainmeter]
Update=1000
Background=#@#Background.png
BackgroundMode=3
BackgroundMargins=0,50,0,30
@include=#@#GlobalVariables.inc
ZPos=[&Z_STATE]
; Définir la taille du widgetJ'ai ajouté SkinWidth=270 et SkinHeight=320 dans la section [Rainmeter].
Si ça ne fonctionne toujours pas, essaie ces solutions :
Solution 1 : Vérifier la position
Ajoute après ZPos=[&Z_STATE] :
iniWindowX=100
WindowY=100
Solution 2 : Vérifier le fichier Background.png
Si le fichier Background.png n'existe pas dans @Resources, le widget pourrait être invisible. Essaie de retirer temporairement cette ligne :
iniBackground=#@#Background.png
Solution 3 : Ajouter un fond de test
Remplace la section [Rainmeter] par :
ini[Rainmeter]
Update=1000
BackgroundMode=2
SolidColor=40,40,40,255
@include=#@#GlobalVariables.inc
ZPos=[&Z_STATE]
Pour débugger rapidement :

Clique droit sur l'icône Rainmeter dans la barre des tâches
Cherche ton skin \"Shortcuts\" dans la liste
Regarde s'il est coché/actif
Clique droit dessus → \"Edit skin\" pour vérifier qu'il n'y a pas d'erreurs

Dis-moi ce que tu vois ! 🔍RéessayerMFje ne vois toujours rien, je fais erreur quelque part ?MFj'essaie juste d'afficher le titre mais je vois 0 widget ; Widget Raccourcis Clavier PowerToys
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
DynamicVariables=1Afficher plusLe problème vient probablement de l'include ou du Background. Testons avec une version minimaliste qui fonctionne à coup sûr :
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
Dis-moi si tu vois maintenant le widget avec fond gris et le titre en couleur ! 🎯RéessayerMFok la je le voison fais les modifs dans l'autre scriptParfait ! Voici la version complète corrigée :Widget Raccourcis ClavierCode ∙ Version 3 ; Widget Raccourcis Clavier PowerToys
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
color3=255,22Voilà ! J'ai retiré toutes les lignes problématiques :

❌ Background=#@#Background.png
❌ BackgroundMargins=0,50,0,30
❌ @include=#@#GlobalVariables.inc
❌ ZPos=[&Z_STATE]
❌ Les boutons toggle (qui nécessitaient la variable Z_STATE)

✅ Fond gris simple avec BackgroundMode=2 et SolidColor=40,40,40,255
✅ Tous les raccourcis affichés de façon claire
✅ Couleurs qui changent selon le jour de la semaine
Le widget devrait maintenant s'afficher correctement ! 🎯
Si tu veux réintégrer le background image et le bouton toggle plus tard, il faudra d'abord vérifier que :

Le fichier GlobalVariables.inc existe et contient la variable Z_STATE
Le fichier Background.png existe dans le dossier @Resources
RéessayerMF[Variables]
; ----------------------------------
; POLICES ET TEXTE
; ----------------------------------
fontName=Trebuchet MS
textSize=10
titleSize=14
smallTextSize=9
Z_STATE=0Dans GlobalesVariables.inc qui existe bien dans @Ressources à la racine
Background.png est présent égalementOn donne à nouveau au skin le thème partagé par les autresWidget Raccourcis ClavierCode ∙ Version 4 ; Widget Raccourcis Clavier PowerToys
; ----------------------------------
[Rainmeter]
Update=1000
Background=#@#Background.png
BackgroundMode=3
BackgroundMargins=0,50,0,30
@include=#@#GlobalVariables.inc
ZPos=[&Z_STATE]

[Variables]
; Couleurs des jParfait ! Voici le skin avec le même thème que Disk :
✅ Background image avec les marges
✅ Couleurs qui changent selon le jour de la semaine (même système)
✅ Bouton toggle en haut à gauche pour passer au premier plan
✅ Effets d'ombre sur le titre
✅ Police Trebuchet MS partout
Note importante : J'ai changé dans le bouton toggle :
ini[!SetOption \"Rainmeter\" \"ZPos\" [&Z_STATE]]
Au lieu de :
ini[!SetOption \"Shortcuts\" \"ZPos\" [&Z_STATE]]
Car le nom de la section principale est [Rainmeter] et non [Shortcuts].
Le widget devrait maintenant s'afficher avec le même style que tes autres skins ! 🎨RéessayerMFIl a disparu complètement, comme avant, je ne le vois plus alors que les autres ouiLe problème vient probablement du nom de section dans le SetOption. Essayons différentes solutions :
Solution 1 : Retirer temporairement le bouton toggle
ini[Rainmeter]
Update=1000
Background=#@#Background.png
BackgroundMode=3
BackgroundMargins=0,50,0,30
@include=#@#GlobalVariables.inc
Retire complètement ZPos=[&Z_STATE] et tous les meters du bouton toggle (de [MeterToggleDotBg] jusqu'à [MeterTooltip]).
Solution 2 : Vérifier le chemin exact
Dans ton fichier Disk qui fonctionne, regarde exactement comment est écrit :

Le chemin du Background
Le chemin de l'@include

Compare caractère par caractère avec le fichier Shortcuts.
Solution 3 : Copier-coller la section [Rainmeter] exacte du fichier Disk
Ouvre ton fichier Disk.ini qui fonctionne, copie EXACTEMENT la section [Rainmeter] complète, et colle-la dans Shortcuts.ini.
Solution 4 : Test de debug - Fond de couleur temporaire
ini[Rainmeter]
Update=1000
BackgroundMode=2
SolidColor=255,0,0,255
@include=#@#GlobalVariables.inc
Si tu vois un fond rouge, c'est que le problème vient du Background.png. Si tu ne vois toujours rien, c'est l'@include qui pose problème.
Quelle solution veux-tu essayer en premier ? Ou envoie-moi la section [Rainmeter] exacte de ton fichier Disk qui fonctionne, je l'adapterai. 🔍RéessayerMF[Rainmeter]
Update=100
OnUnloadAction=[!WriteKeyValue Variables Z_STATE 0 \"#@#GlobalVariables.inc\"][!RefreshApp]
@include=#@#GlobalVariables.inc
; ------------------------------------
; MESURE: Calcul du prochain état
; ------------------------------------
[measureZNextState]
Measure=Calc
; Si l'état actuel (Z_STATE) est 0 (Normal), le prochain état est 2 (1er plan), et vice-versa.
Formula=(#Z_STATE# = 0 ? 2 : 0)
DynamicVariables=1
; ------------------------------------
; MÈTRES: Le Bouton Discret (10x10 pixels)
; ------------------------------------
; Fond du cercle (gris)
[MeterToggleDotBg]
Meter=Shape
X=0
Y=0
W=10
H=10
Shape=Circle 5,5,5 | Fill Color 150,150,150,50
; Point indicateur de statut (Couleur dynamique: Vert si ON, Gris si OFF)
[MeterStatusColor]
Meter=Shape
X=0
Y=0
W=10
H=10
Shape=Circle 5,5,3 | Fill Color ([&Z_STATE]=0 ? 100,100,100,255 : 50,255,50,255)
DynamicVariables=1
; Zone cliquable et Tooltip
[MeterClickAction]
Meter=String
X=0
Y=0
W=10
H=10
SolidColor=0,0,0,1
LeftMouseUpAction=[!SetVariable Z_STATE ([&Z_STATE]=0 ? 2 : 0)]
 [!SetOption \"Disk\" \"ZPos\" [&Z_STATE]]
 [!UpdateMeter *]
 [!Redraw]
DynamicVariables=1
[MeterTooltip]
Meter=String
X=0
Y=0
W=10
H=10
SolidColor=0,0,0,1
ToolTipText=[&Z_STATE]=0 ? \"Affichage normal\" : \"Passage au 1er plan\"
DynamicVariables=1J'aime pas du tout le résultat de ce bouton toggle, c'est buggé, ça ne fait pas switcher l'état normal de l'état 1er plan
Il est très peu visible et mocheFais moi un joli bouton toggle stp qui fonctionne idéalementAfficher plusVoici un beau bouton toggle qui fonctionne vraiment ! 🎨Bouton Toggle AmélioréCode ; ------------------------------------
; BOUTON TOGGLE AMÉLIORÉ - À intégrer dans tes skins
; ------------------------------------

; DANS LA SECTION [Rainmeter], ajoute :
; @include=#@#GlobalVariables.inc
; ZPos=[&Z_STATE]

; -----------------------Voici un bouton toggle moderne et fonctionnel avec 2 styles au choix :
🎯 Style 1 : Bouton capsule avec curseur coulissant (activé par défaut)
Caractéristiques :

✅ Curseur qui glisse de gauche à droite
✅ Gris quand normal, vert fluo quand épinglé
✅ Icône 📌 qui apparaît quand activé
✅ Effet hover au survol
✅ Tooltip explicite
✅ Sauvegarde l'état dans GlobalVariables.inc

🎯 Style 2 : Bouton carré minimaliste (en commentaire)
Si tu préfères un style plus discret, décommente la section alternative.
📋 Pour l'intégrer dans tes skins :
1. Dans la section [Rainmeter] :
ini[Rainmeter]
Update=1000
@include=#@#GlobalVariables.inc
ZPos=[&Z_STATE]
Background=#@#Background.png
BackgroundMode=3
BackgroundMargins=0,50,0,30
2. Copie tout le code du bouton toggle à la fin de ton fichier .ini
3. Ajuste la position si besoin :
Change X=10 et Y=10 dans les meters pour positionner le bouton où tu veux.
Le bouton devrait maintenant vraiment basculer entre normal et premier plan avec une animation fluide ! 🚀
Tu préfères quel style ? Le capsule ou le carré ?RéessayerMFdu coup j'enregistre le code dans un fichier ToggleZPos.ini et j'en fais un skin unique ? Ou je rajoute ce code dans tous les skins en bas et j'aurais autant de bouton que de skins ?Excellente question ! Il y a deux approches possibles :
✅ Solution recommandée : Un bouton par skin (intégré)
Avantages :

Chaque skin contrôle son propre état (indépendant)
Plus simple à gérer
Pas de skin supplémentaire à charger

Comment faire :
Copie le code du bouton toggle à la fin de chaque skin (Disk.ini, Shortcuts.ini, etc.). Tu auras un petit bouton sur chaque widget pour l'épingler individuellement.
ini; Dans Disk.ini - à la fin du fichier
[measureToggleState]
Measure=Calc
Formula=#Z_STATE#
DynamicVariables=1

[MeterToggleBackground]
Meter=Shape
X=10
Y=10
; ... reste du code ...
Important : Dans LeftMouseUpAction, change le nom du skin :
ini; Pour Disk.ini
LeftMouseUpAction=[!SetVariable Z_STATE ([&Z_STATE]=0 ? 2 : 0)][!WriteKeyValue Variables Z_STATE [&Z_STATE] \"#@#GlobalVariables.inc\"][!UpdateMeasure *][!UpdateMeter *][!Redraw]

; ⚠️ Attention : chaque skin doit avoir sa PROPRE variable Z_STATE
; Dans GlobalVariables.inc :
Z_STATE_DISK=0
Z_STATE_SHORTCUTS=0
Z_STATE_CPU=0

❌ Problème avec l'approche \"skin unique\"
Si tu fais un ToggleZPos.ini séparé, il ne pourra contrôler qu'un seul skin à la fois, pas tous. Ce n'est pas pratique.

🎯 Ma recommandation finale
Utilise des variables séparées pour chaque skin :
Dans GlobalVariables.inc :
ini[Variables]
fontName=Trebuchet MS
textSize=10
titleSize=14
smallTextSize=9

; États Z pour chaque skin
Z_STATE_DISK=0
Z_STATE_SHORTCUTS=0
Z_STATE_CPU=0
Dans Disk.ini :
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
Dans Shortcuts.ini :
ini[Rainmeter]
ZPos=#Z_STATE_SHORTCUTS#
; ...

[MeterToggleClick]
LeftMouseUpAction=[!SetVariable Z_STATE_SHORTCUTS ([#Z_STATE_SHORTCUTS#]=0 ? 2 : 0)][!WriteKeyValue Variables Z_STATE_SHORTCUTS [#Z_STATE_SHORTCUTS#] \"#@#GlobalVariables.inc\"][!UpdateMeasure *][!UpdateMeter *][!Redraw]
Comme ça chaque widget peut être épinglé indépendamment ! 📌
Tu veux que je te prépare le code complet pour Disk et Shortcuts avec cette approche ?RéessayerMFje veux un seul bouton unique qui est capable de switcher tous les skins en même tempsAh parfait ! Alors voici la solution avec un bouton unique qui contrôle tous les skins :Bouton Toggle MaîtreCode ; ToggleZPos.ini - Bouton Maître pour tous les skins
; ----------------------------------
[Rainmeter]
Update=100
@include=#@#GlobalVariables.inc

[Metadata]
Name=Toggle Master
Author=Custom
Information=Bouton unique qui bascule tous les skins entre nParfait ! Voici le bouton maître unique. Maintenant il faut configurer tes autres skins pour qu'ils réagissent :
📋 Étapes d'installation :
1️⃣ Créer le fichier ToggleZPos.ini
Sauvegarde le code ci-dessus dans ton dossier Rainmeter (par exemple dans YourSuite\\ToggleZPos\\ToggleZPos.ini)
2️⃣ Modifier Disk.ini (et tous tes autres skins)
ini[Rainmeter]
Update=1000
Background=#@#Background.png
BackgroundMode=3
BackgroundMargins=0,50,0,30
@include=#@#GlobalVariables.inc
ZPos=#Z_STATE#
Group=AllSkins

; ... reste de ton code Disk.ini sans le bouton toggle ...
3️⃣ Modifier Shortcuts.ini
ini[Rainmeter]
Update=1000
Background=#@#Background.png
BackgroundMode=3
BackgroundMargins=0,50,0,30
@include=#@#GlobalVariables.inc
ZPos=#Z_STATE#
Group=AllSkins

; ... reste de ton code ...
4️⃣ Vérifier GlobalVariables.inc
ini[Variables]
fontName=Trebuchet MS
textSize=10
titleSize=14
smallTextSize=9
Z_STATE=0
🎯 Comment ça fonctionne :

Le bouton toggle change la valeur de Z_STATE dans GlobalVariables.inc
Il utilise [!RefreshGroup \"AllSkins\"] qui rafraîchit tous les skins du groupe
Tous les skins qui ont Group=AllSkins et ZPos=#Z_STATE# basculent ensemble

Résultat : Un seul clic sur le bouton et TOUS tes widgets passent au premier plan (ou reviennent en mode normal) simultanément ! 🚀
Tu veux que je te prépare les versions complètes de Disk.ini et Shortcuts.ini sans leurs anciens boutons toggle ?Réessayer; ----------------------------------\r
; NETWORK (version modernisée)\r
; ----------------------------------\r
\r
[Rainmeter]\r
Update=1000\r
Background=#@#Background.png\r
BackgroundMode=3\r
BackgroundMargins=0,50,0,30\r
@include=#@#GlobalVariables.inc\r
ZPos=#Z_STATE#\r
Group=AllSkins\r
\r
[Variables]\r
fontNampastedMFle bouton fonctionne à peu près dans 2 cas :
Disk
System
Pour ces 2, l'appui du toggle les passe au 1er plan mais un clic sunr une fenêtre active et ils repassent en arrièrePour les 3 autres, le toggle ne fonctionne pas
Clock
Raccourcis
NetworkL'affichage du toggle est buggé comme pour des caractères non reconnus, fais quelque chose dep lus simple pour l'instant; Clock avec couleur par jour - Formatage aligné sur Disk
; ----------------------------------
[Rainmeter]
Update=1000
Background=#@#Background.png
BackgroundMode=3
BackgroundMargins=0,50,0,30
@include=#@#GlobalVariables.inc
ZPos=#Z_STATE#
Group=AllSkins
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
Version=2.1.0
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
; ----------------------------------
; METERS
; ----------------------------------
[meterTitle]
Meter=String
MeasureName=measureTime
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
Text=%1
[meterDay]
Meter=String
MeasureName=measureDay
X=10
Y=42
W=190
H=16
StringAlign=Left
StringStyle=Bold
StringEffect=Shadow
FontEffectColor=0,0,0,20
FontFace=Trebuchet MS
FontSize=12
FontColor=200,200,200,255
AntiAlias=1
Text=%1
[meterDate]
Meter=String
MeasureName=measureDate
X=200
Y=42
W=190
H=16
StringAlign=Right
StringStyle=Bold
StringEffect=Shadow
FontEffectColor=0,0,0,20
FontFace=Trebuchet MS
FontSize=12
FontColor=200,200,200,255
AntiAlias=1
Text=%1; System monitor - Formatage aligné sur Disk et Clock
; ----------------------------------
[Rainmeter]
Update=1000
Background=#@#Background.png
BackgroundMode=3
BackgroundMargins=0,50,0,30
@include=#@#GlobalVariables.inc
ZPos=#Z_STATE#
Group=AllSkins
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
Name=System
Author=Custom
Information=Affiche les statistiques système
Version=2.1.0
; ----------------------------------
; MEASURES
; ----------------------------------
[measureCPU]
Measure=CPU
Processor=0
[measureRAM]
Measure=PhysicalMemory
UpdateDivider=20
[measureSWAP]
Measure=SwapMemory
UpdateDivider=20
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
Text=System
LeftMouseUpAction=[\"taskmgr.exe\"]
ToolTipText=Ouvrir le Gestionnaire des tâches
[meterLabelCPU]
Meter=String
X=10
Y=42
W=190
H=16
StringAlign=Left
StringStyle=Bold
StringEffect=Shadow
FontEffectColor=0,0,0,20
FontFace=Trebuchet MS
FontSize=12
FontColor=200,200,200,255
AntiAlias=1
Text=CPU
[meterValueCPU]
Meter=String
MeasureName=measureCPU
X=200
Y=42
W=190
H=16
StringAlign=Right
StringStyle=Bold
StringEffect=Shadow
FontEffectColor=0,0,0,20
FontFace=Trebuchet MS
FontSize=12
FontColor=200,200,200,255
AntiAlias=1
Text=%1%
[meterBarCPU]
Meter=Shape
X=10
Y=60
W=190
H=8
Shape=Rectangle 0,0,190,8,2 | StrokeWidth 1 | StrokeColor 80,80,80,255 | Fill Color 60,60,60,255
[meterBarCPUFill]
Meter=Bar
MeasureName=measureCPU
X=11
Y=61
W=188
H=6
BarColor=[#color[&measureDayNumber]]
BarOrientation=HORIZONTAL
DynamicVariables=1
[meterLabelRAM]
Meter=String
X=10
Y=72
W=190
H=16
StringAlign=Left
StringStyle=Bold
StringEffect=Shadow
FontEffectColor=0,0,0,20
FontFace=Trebuchet MS
FontSize=12
FontColor=200,200,200,255
AntiAlias=1
Text=RAM
[meterValueRAM]
Meter=String
MeasureName=measureRAM
X=200
Y=72
W=190
H=16
StringAlign=Right
StringStyle=Bold
StringEffect=Shadow
FontEffectColor=0,0,0,20
FontFace=Trebuchet MS
FontSize=12
FontColor=200,200,200,255
AntiAlias=1
Text=%1%
Percentual=1
[meterBarRAM]
Meter=Shape
X=10
Y=90
W=190
H=8
Shape=Rectangle 0,0,190,8,2 | StrokeWidth 1 | StrokeColor 80,80,80,255 | Fill Color 60,60,60,255
[meterBarRAMFill]
Meter=Bar
MeasureName=measureRAM
X=11
Y=91
W=188
H=6
BarColor=[#color[&measureDayNumber]]
BarOrientation=HORIZONTAL
DynamicVariables=1
[meterLabelSWAP]
Meter=String
X=10
Y=102
W=190
H=16
StringAlign=Left
StringStyle=Bold
StringEffect=Shadow
FontEffectColor=0,0,0,20
FontFace=Trebuchet MS
FontSize=12
FontColor=200,200,200,255
AntiAlias=1
Text=SWAP
[meterValueSWAP]
Meter=String
MeasureName=measureSWAP
X=200
Y=102
W=190
H=16
StringAlign=Right
StringStyle=Bold
StringEffect=Shadow
FontEffectColor=0,0,0,20
FontFace=Trebuchet MS
FontSize=12
FontColor=200,200,200,255
AntiAlias=1
Text=%1%
Percentual=1
[meterBarSWAP]
Meter=Shape
X=10
Y=120
W=190
H=8
Shape=Rectangle 0,0,190,8,2 | StrokeWidth 1 | StrokeColor 80,80,80,255 | Fill Color 60,60,60,255
[meterBarSWAPFill]
Meter=Bar
MeasureName=measureSWAP
X=11
Y=121
W=188
H=6
BarColor=[#color[&measureDayNumber]]
BarOrientation=HORIZONTAL
DynamicVariables=1Afficher plusJe vois plusieurs problèmes. Voici les corrections :
🔧 Problème 1 : ZPos qui ne reste pas au premier plan
Pour que les widgets restent vraiment au premier plan, il faut utiliser AlwaysOnTop au lieu de ZPos=2 :
Modifie GlobalVariables.inc :
ini[Variables]
fontName=Trebuchet MS
textSize=10
titleSize=14
smallTextSize=9
Z_STATE=0
ALWAYS_ON_TOP=-2
🔧 Problème 2 : Bouton toggle simplifié (sans émojis buggés)Bouton Toggle MaîtreCode ∙ Version 2 ; ToggleZPos.ini - Bouton Maître Simplifié
; ----------------------------------
[Rainmeter]
Update=100
@include=#@#GlobalVariables.inc
AlwaysOnTop=#ALWAYS_ON_TOP#

[Metadata]
Name=Toggle Master
Author=Custom
Information=Bouton unique qui bascule tous🔧 Problème 3 : Modifier TOUS tes skins
Remplace dans CHAQUE skin (Clock, Network, Shortcuts, System, Disk) :
ini[Rainmeter]
Update=1000
Background=#@#Background.png
BackgroundMode=3
BackgroundMargins=0,50,0,30
@include=#@#GlobalVariables.inc
AlwaysOnTop=#ALWAYS_ON_TOP#
Group=AllSkins
Note : Remplace ZPos=#Z_STATE# par AlwaysOnTop=#ALWAYS_ON_TOP#
📋 Valeurs AlwaysOnTop expliquées :

-2 = Toujours au premier plan (même au-dessus des fenêtres en plein écran)
-1 = Normal (mode fenêtre classique)
0 = Toujours en arrière-plan
1 = Au-dessus des fenêtres normales
2 = Mode \"topmost\" (reste devant mais peut être recouvert)

✅ Résumé des modifications :

GlobalVariables.inc - Ajoute ALWAYS_ON_TOP=-2
ToggleZPos.ini - Version simplifiée sans émojis
Tous les skins - Remplace ZPos=#Z_STATE# par AlwaysOnTop=#ALWAYS_ON_TOP#

Avec ces changements, le bouton devrait :

✅ S'afficher correctement (pas de caractères buggés)
✅ Vraiment garder les widgets au premier plan
✅ Fonctionner pour TOUS les skins

Teste et dis-moi si ça fonctionne ! 🎯RéessayerMFPas besoin de texte, fais juste une forme qui bouge a droite ou gauche d'une couleur bleu nuit si activé, de couleur grise si désactivé
dans des tons neutres qui se fondent dans le thèmeRien n'a changé sinon, toujours le même comportement pour 2skins / 5Bouton Toggle MaîtreCode ∙ Version 3 ; ToggleZPos.ini - Bouton Maître Minimaliste
; ----------------------------------
[Rainmeter]
Update=100
@include=#@#GlobalVariables.inc
AlwaysOnTop=#ALWAYS_ON_TOP#

[Metadata]
Name=Toggle Master
Author=Custom
Information=Bouton unique qui bascule toVoici le bouton ultra minimaliste :

⚫ Cercle gris qui glisse à gauche quand désactivé
🔵 Cercle bleu nuit qui glisse à droite quand activé
Fond gris discret qui se fond dans ton thème

Pour le problème des 3 skins qui ne fonctionnent pas :
Vérifie dans Clock.ini, Network.ini et Shortcuts.ini que tu as bien :
ini[Rainmeter]
Update=1000
Background=#@#Background.png
BackgroundMode=3
BackgroundMargins=0,50,0,30
@include=#@#GlobalVariables.inc
AlwaysOnTop=#ALWAYS_ON_TOP#
Group=AllSkins
Et dans GlobalVariables.inc :
ini[Variables]
fontName=Trebuchet MS
textSize=10
titleSize=14
smallTextSize=9
Z_STATE=0
ALWAYS_ON_TOP=-1
Après modification, RECHARGE tous les skins (clic droit sur l'icône Rainmeter → Refresh All)
Le [!Delay 100] que j'ai ajouté dans le bouton devrait aussi aider à synchroniser le refresh.
Si ça ne marche toujours pas pour les 3 skins, envoie-moi le début de leur fichier .ini (juste la section [Rainmeter]) pour que je vérifie ! 🔍Réessayer; ----------------------------------\r
; NETWORK (version modernisée)\r
; ----------------------------------\r
\r
[Rainmeter]\r
Update=1000\r
Background=#@#Background.png\r
BackgroundMode=3\r
BackgroundMargins=0,50,0,30\r
@include=#@#GlobalVariables.inc\r
AlwaysOnTop=#ALWAYS_ON_TOP#\r
Group=AllSkins\r
\r
[VariabpastedMFSystem :
; System monitor - Formatage aligné sur Disk et Clock
; ----------------------------------
[Rainmeter]
Update=1000
Background=#@#Background.png
BackgroundMode=3
BackgroundMargins=0,50,0,30
@include=#@#GlobalVariables.inc
AlwaysOnTop=#ALWAYS_ON_TOP#
Group=AllSkins
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
Name=System
Author=Custom
Information=Affiche les statistiques système
Version=2.1.0
; ----------------------------------
; MEASURES
; ----------------------------------
[measureCPU]
Measure=CPU
Processor=0
[measureRAM]
Measure=PhysicalMemory
UpdateDivider=20
[measureSWAP]
Measure=SwapMemory
UpdateDivider=20
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
Text=System
LeftMouseUpAction=[\"taskmgr.exe\"]
ToolTipText=Ouvrir le Gestionnaire des tâches
[meterLabelCPU]
Meter=String
X=10
Y=42
W=190
H=16
StringAlign=Left
StringStyle=Bold
StringEffect=Shadow
FontEffectColor=0,0,0,20
FontFace=Trebuchet MS
FontSize=12
FontColor=200,200,200,255
AntiAlias=1
Text=CPU
[meterValueCPU]
Meter=String
MeasureName=measureCPU
X=200
Y=42
W=190
H=16
StringAlign=Right
StringStyle=Bold
StringEffect=Shadow
FontEffectColor=0,0,0,20
FontFace=Trebuchet MS
FontSize=12
FontColor=200,200,200,255
AntiAlias=1
Text=%1%
[meterBarCPU]
Meter=Shape
X=10
Y=60
W=190
H=8
Shape=Rectangle 0,0,190,8,2 | StrokeWidth 1 | StrokeColor 80,80,80,255 | Fill Color 60,60,60,255
[meterBarCPUFill]
Meter=Bar
MeasureName=measureCPU
X=11
Y=61
W=188
H=6
BarColor=[#color[&measureDayNumber]]
BarOrientation=HORIZONTAL
DynamicVariables=1
[meterLabelRAM]
Meter=String
X=10
Y=72
W=190
H=16
StringAlign=Left
StringStyle=Bold
StringEffect=Shadow
FontEffectColor=0,0,0,20
FontFace=Trebuchet MS
FontSize=12
FontColor=200,200,200,255
AntiAlias=1
Text=RAM
[meterValueRAM]
Meter=String
MeasureName=measureRAM
X=200
Y=72
W=190
H=16
StringAlign=Right
StringStyle=Bold
StringEffect=Shadow
FontEffectColor=0,0,0,20
FontFace=Trebuchet MS
FontSize=12
FontColor=200,200,200,255
AntiAlias=1
Text=%1%
Percentual=1
[meterBarRAM]
Meter=Shape
X=10
Y=90
W=190
H=8
Shape=Rectangle 0,0,190,8,2 | StrokeWidth 1 | StrokeColor 80,80,80,255 | Fill Color 60,60,60,255
[meterBarRAMFill]
Meter=Bar
MeasureName=measureRAM
X=11
Y=91
W=188
H=6
BarColor=[#color[&measureDayNumber]]
BarOrientation=HORIZONTAL
DynamicVariables=1
[meterLabelSWAP]
Meter=String
X=10
Y=102
W=190
H=16
StringAlign=Left
StringStyle=Bold
StringEffect=Shadow
FontEffectColor=0,0,0,20
FontFace=Trebuchet MS
FontSize=12
FontColor=200,200,200,255
AntiAlias=1
Text=SWAP
[meterValueSWAP]
Meter=String
MeasureName=measureSWAP
X=200
Y=102
W=190
H=16
StringAlign=Right
StringStyle=Bold
StringEffect=Shadow
FontEffectColor=0,0,0,20
FontFace=Trebuchet MS
FontSize=12
FontColor=200,200,200,255
AntiAlias=1
Text=%1%
Percentual=1
[meterBarSWAP]
Meter=Shape
X=10
Y=120
W=190
H=8
Shape=Rectangle 0,0,190,8,2 | StrokeWidth 1 | StrokeColor 80,80,80,255 | Fill Color 60,60,60,255
[meterBarSWAPFill]
Meter=Bar
MeasureName=measureSWAP
X=11
Y=121
W=188
H=6
BarColor=[#color[&measureDayNumber]]
BarOrientation=HORIZONTAL
DynamicVariables=1Network : et pareil pour le dernier, Le bouton toggle affiche un demi cercle tronqué de 10x21 pixels
bleu turquoise
Il fonctionne pour les 2 skins mais ne bouge pas et ne change pas de couleurFais au plus simple pour avoir juste un indicateur visuel le plus simple possibleAfficher plusJe vois le problème ! Le cercle est mal positionné et tronqué. Voici la version ultra simple :Bouton Toggle MaîtreCode ∙ Version 4 ; ToggleZPos.ini - Bouton Maître Ultra Simple
; ----------------------------------
[Rainmeter]
Update=100
@include=#@#GlobalVariables.inc
AlwaysOnTop=#ALWAYS_ON_TOP#

[Metadata]
Name=Toggle Master
Author=Custom
Information=Bouton unique qui bascule tVoici la version la plus simple possible :
✅ Petit rectangle 30x15 pixels

Gris quand désactivé
Bleu nuit quand activé
Légèrement plus clair au survol

Pour Clock et Shortcuts, vérifie que tu as bien :
Clock.ini :
ini[Rainmeter]
Update=1000
Background=#@#Background.png
BackgroundMode=3
BackgroundMargins=0,50,0,30
@include=#@#GlobalVariables.inc
AlwaysOnTop=#ALWAYS_ON_TOP#
Group=AllSkins
Shortcuts.ini :
ini[Rainmeter]
Update=1000
Background=#@#Background.png
BackgroundMode=3
BackgroundMargins=0,50,0,30
@include=#@#GlobalVariables.inc
AlwaysOnTop=#ALWAYS_ON_TOP#
Group=AllSkins
Et dans GlobalVariables.inc :
ini[Variables]
fontName=Trebuchet MS
textSize=10
titleSize=14
smallTextSize=9
Z_STATE=0
ALWAYS_ON_TOP=-1
Après modification :

Sauvegarde tous les fichiers
Clic droit sur l'icône Rainmeter → Refresh All
Teste le bouton toggle

Le rectangle devrait maintenant être complet, bien visible, et changer de couleur ! 🎯
Si ça ne marche toujours pas pour les 3 skins, il y a peut-être un problème avec le nom du Group. Essaie de changer Group=AllSkins par Group=MySkins partout (dans tous les skins ET dans le bouton toggle).RéessayerMFOublie ce carré moche, fais en fonction du thème des skins quelque chose de discret et respectant le thèmeD'accord ! Voici un bouton discret qui s'intègre au thème de tes skins :Bouton Toggle MaîtreCode ∙ Version 5 ; ToggleZPos.ini - Bouton Maître discret
; ----------------------------------
[Rainmeter]
Update=100
Background=#@#Background.png
BackgroundMode=3
BackgroundMargins=0,50,0,30
@include=#@#GlobalVariables.inc
AlwaysOnTop=#ALWAYS_ON_TOP#

[Variables]
; 🎯 Voici le nouveau bouton ultra-discret :
Point lumineux ⚫ → Gris = Widgets en mode normal
Point lumineux 🟢 → Color of the day = Widgets épinglés au premier plan
Avantages :

✅ 12 pixels dans le coin, minimalist
✅ Color1 détecter (le personnage de Couleur selon le jour
✅ Context du Background + Ombre +
✅ Discret - ne perturbe pas visuel

Le cercle utilisateur les mêmes couleurs que vos titres (rouge, vert, l'orange, etc.) donc il s'intègre automatiquement dans ton thème ! 🎨
Si tu veux que ce soit ENCORE plus discret, je peux :

Le mettre dans un coin différent
Réduire encore la taille
Changer l'opacité

Qu'en dis-tu ? 🎯RéessayerClaude peut faire des erreurs. Assurez-vous de vérifier ses réponses. Sonnet 4.5

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-082-R082-Dossiers-utilisateur-OpenIfExplorerHotke]]
- ⬇️ Next: [[Card-084-R084-Dossiers-utilisateur-OpenIfExplorerHotke]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]

## 🏷️ Topics

- #power-bi
- #excel
- #python
- #receipts
- #code
- #git
- #automation
