---
type: chat-card
parent_export: '[[Export]]'
order: 99
role: assistant
created: '2025-11-11T00:47:13.571042Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 99 - Assistant

**ID:** msg-99

## 💬 Content


**ID:** msg-99

L'utilisateur a un problème avec des raccourcis AutoHotkey. Il veut créer des séquences de touches du type \"Win+E puis une lettre\" pour ouvrir l'Explorateur Windows dans des dossiers spécifiques.
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

Je vais lui proposer plusieurs approches en français.

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-098-R098-Utilisateur-problème-avec-raccourcis-Aut]]
- ⬇️ Next: [[Card-100-R100-Comprends-problème-Voici-plusieurs-solut]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]
