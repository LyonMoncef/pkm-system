---
type: chat-card
parent_export: '[[Export]]'
order: 300
role: assistant
created: '2025-11-10T22:55:58.803975Z'
tags:
- chat-card
- git
attachments_count: 0
---

# 🤖 Message 300 - Assistant

**ID:** msg-300

## 💬 Content


**ID:** msg-300

PAS DE PANIQUE ! 🚨
Voici comment supprimer le dernier commit :

🔄 SUPPRIMER LE DERNIER COMMIT
Option 1 : Garder les modifications (Recommandé)
bash# Annule le commit mais garde les fichiers modifiés
git reset --soft HEAD~1
Résultat :

Le commit disparaît
Tes fichiers restent modifiés (staged)
Tu peux refaire un commit propre


Option 2 : Tout annuler (Attention !)
bash# Annule le commit ET supprime les modifications
git reset --hard HEAD~1
⚠️ DANGER : Tes modifications sont PERDUES !

Option 3 : Modifier le dernier commit
bash# Si tu veux juste changer le message ou ajouter des fichiers
git commit --amend

# Ou avec un nouveau message direct
git commit --amend -m \"Nouveau message de commit\"

🤔 Qu'est-ce qui s'est passé ?
Dis-moi :

Tu as déjà push sur GitHub ?
Ou c'est juste un commit local ?

Si c'est local : Option 1 suffit !
Si tu as déjà push : On fait ça :
bash# Annule localement
git reset --soft HEAD~1

# Force push (écrase l'historique distant)
git push origin main --force

C'est quoi le problème exactement ?

Message de commit à corriger ?
Fichiers oubliés ?
Fichiers à ne pas commit ?

Dis-moi et je te guide ! 💪Réessayer

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-299-Q299-On-supprime-le-dernier-commit-déjà]]
- ⬇️ Next: [[Card-301-R301-PANIQUE-Voici-comment-supprimer-dernier]]
- 📊 MOC: [[_MOC_Personal productivity widget design]]

## 🏷️ Topics

- #git
