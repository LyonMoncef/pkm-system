---
type: chat-card
parent_export: '[[Export]]'
order: 288
role: assistant
created: '2025-11-11T00:47:15.615985Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 288 - Assistant

**ID:** msg-288

## 💬 Content


**ID:** msg-288

J'ai ajouté SkinWidth=270 et SkinHeight=320 dans la section [Rainmeter].
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

Dis-moi ce que tu vois ! 🔍

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-287-R287-Widget-Raccourcis-Clavier-PowerToys-Rain]]
- ⬇️ Next: [[Card-289-R289-IniWindowX-WindowY]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]
