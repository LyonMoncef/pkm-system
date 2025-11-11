---
type: chat-card
parent_export: '[[Export]]'
order: 134
role: assistant
created: '2025-11-11T00:47:13.983400Z'
tags:
- chat-card
- code
attachments_count: 0
---

# 🤖 Message 134 - Assistant

**ID:** msg-134

## 💬 Content


**ID:** msg-134

L'utilisateur veut que le focus soit sur la liste des fichiers/dossiers après avoir navigué vers un dossier, pas sur la barre d'adresse. Actuellement, le code envoie !d (Alt+D) pour mettre le focus sur la barre d'adresse, puis envoie le chemin et Enter. Mais après ça, le focus reste dans la barre d'adresse.
Pour mettre le focus sur la liste des fichiers, il faut envoyer une touche supplémentaire après l'Enter. Plusieurs options:

Tab pour passer au volet suivant
F6 pour naviguer entre les panneaux
Escape pour sortir de la barre d'adresse et revenir à la liste
Ou simplement envoyer une touche de direction ou un clic

La solution la plus simple serait probablement d'ajouter un Send(\"{Escape}\") ou Send(\"{Tab}\") après l'Enter, ou mieux encore, envoyer juste un focus sur la liste des fichiers.
Laisse-moi proposer une solution qui fonctionne bien.

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-133-R133-Utilisateur-veut-focus-soit-liste]]
- ⬇️ Next: [[Card-135-R135-Utilisateur-veut-focus-soit-liste]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]

## 🏷️ Topics

- #code
