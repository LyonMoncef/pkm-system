---
type: chat-card
parent_export: '[[Export]]'
order: 498
role: assistant
created: '2025-11-11T00:21:48.303630Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 498 - Assistant

**ID:** msg-498

## 💬 Content


**ID:** msg-498

Parfait ! Je vais centraliser la logique de couleur par jour dans les variables globales pour que TOUS les skins l'utilisent :Variables Globales - GlobalVariables.incCode ∙ Version 3 ; ===================================
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
FontColor=#colorDynamic# ← Au lieu de #colorText#
DynamicVariables=1 ← Ajouter cette ligne
Testez Clock.ini maintenant, la couleur devrait changer selon le jour ! 🎉Réessayer

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-497-S497-ID-msg-497]]
- ⬇️ Next: [[Card-499-R499-Parfait-vais-centraliser-logique-couleur]]
- 📊 MOC: [[_MOC_Rainmeter skin localization]]
