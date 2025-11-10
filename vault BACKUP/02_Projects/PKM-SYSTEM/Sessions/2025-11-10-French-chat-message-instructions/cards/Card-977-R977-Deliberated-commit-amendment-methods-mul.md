---
type: chat-card
parent_export: '[[Export]]'
order: 977
role: assistant
created: '2025-11-10T21:12:18.609652Z'
tags:
- chat-card
- code
- git
attachments_count: 0
---

# 🤖 Message 977 - Assistant

**ID:** msg-977

## 💬 Content


**ID:** msg-977

Deliberated git commit amendment methods for multiline messages.L'utilisateur a fait un commit mais n'a pris que la première ligne du message de commit au lieu du message complet multilignes que j'avais proposé. Il veut modifier le message du commit.
Pour modifier le dernier commit (qui n'a pas encore été pushé ou même s'il a été pushé sur une branche perso), on utilise:
bashgit commit --amend
Ça va ouvrir l'éditeur (vim/nano) pour modifier le message. Ou on peut faire:
bashgit commit --amend -m \"nouveau message\"
Mais comme le message que je veux est multilignes, je vais lui donner la commande avec l'éditeur ou la syntaxe multilignes.
En fait, le plus simple est d'utiliser git commit --amend qui ouvrira l'éditeur configuré (probablement vim ou nano), ou alors d'utiliser la syntaxe avec des sauts de ligne.
Je vais lui donner les deux options.

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-976-R976-Deliberated-commit-amendment-methods-mul]]
- ⬇️ Next: [[Card-978-R978-Deliberated-commit-amendment-methods-mul]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #code
- #git
