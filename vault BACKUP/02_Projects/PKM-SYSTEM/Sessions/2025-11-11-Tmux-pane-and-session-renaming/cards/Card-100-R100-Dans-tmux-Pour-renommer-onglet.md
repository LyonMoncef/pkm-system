---
type: chat-card
parent_export: '[[Export]]'
order: 100
role: assistant
created: '2025-11-11T01:09:02.781887Z'
tags:
- chat-card
- code
attachments_count: 0
---

# 🤖 Message 100 - Assistant

**ID:** msg-100

## 💬 Content


**ID:** msg-100

Dans tmux :
Pour renommer l'onglet/window actuel : prefix + , (virgule)
Pour le pane : tmux ne permet pas nativement de renommer les panes individuels. Les panes n'ont que des numéros (index), pas de noms.
Si tu veux vraiment identifier tes panes, tu as quelques options :

Utiliser prefix + q pour afficher brièvement les numéros des panes
Définir un titre pour le terminal dans le pane avec : printf '\\033]2;%s\\033\\\\' 'Mon titre'
Utiliser select-pane -T \"titre\" et afficher ce titre dans ta statusbar (nécessite configuration)

Récap :

Session : prefix + $
Window/onglet : prefix + ,
Pane : pas de renommage natif

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-099-R099-Utilisateur-demande-comment-renommer-dan]]
- ⬇️ Next: [[Card-101-R101-Claude-peut-faire-erreurs-Assurez]]
- 📊 MOC: [[_MOC_Tmux pane and session renaming]]

## 🏷️ Topics

- #code
