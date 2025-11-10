---
type: chat-card
parent_export: '[[Export]]'
order: 216
role: assistant
created: '2025-11-10T21:46:08.527678Z'
tags:
- chat-card
- obsidian
- receipts
- code
attachments_count: 0
---

# 🤖 Message 216 - Assistant

**ID:** msg-216

## 💬 Content


**ID:** msg-216

🎯 OK, ON DÉGROSSIT - PLAN ULTRA SIMPLE
Tu as 100% raison. Fini le rêve, on ship.

✅ OBJECTIF AUJOURD'HUI
Avoir 3 templates utilisables + méthodo claire = TU PEUX COMMENCER À NOTER
Pas de système complexe. Juste de quoi:

Capturer une idée rapidement
La retrouver facilement
La lier à d'autres


📋 LES 3 TEMPLATES ESSENTIELS
TEMPLATE 1: Note Rapide
Pour capturer vite fait
yaml---
created: {{date:YYYY-MM-DD}}
type: fleeting
tags: [inbox]
status: to-process
---

# {{title}}

[ton idée ici]

---
À traiter: classer + lier + enrichir
Usage: Tu notes, tu te poses pas de questions.

TEMPLATE 2: Note Concept
Quand tu développes une idée
yaml---
created: {{date:YYYY-MM-DD}}
type: concept
tags: []
related: []
---

# {{title}}

## Idée principale

[résumé en 2-3 phrases]

## Développement

[détails]

## Liens

- [[Note reliée]]
Usage: Idée = note concept.

TEMPLATE 3: Note Projet
Pour les trucs en cours
yaml---
created: {{date:YYYY-MM-DD}}
type: project
status: active
tags: [project]
---

# {{title}}

## État actuel

- [ ] Tâche 1
- [ ] Tâche 2

## Prochaine action

[quoi faire maintenant]

## Contexte

[[Lien vers discussions]]
```

**Usage:** Projets = note projet.

---

## 🏷️ TAGS MINIMAUX (extensibles plus tard)
```
#inbox → Tout ce qui arrive
#concept → Idées développées
#project → Projets actifs
#resource → Ressources/références
#archive → Trucs finis

# Plus tard tu ajoutes sous-tags genre:
#project/pkm-system
#concept/emotions
etc.
```

**Règle:** Si tu hésites sur le tag = mets `#inbox`

---

## 📁 STRUCTURE VAULT MINIMALE
```
MonVault/
├── 00-INBOX/ → Tout ce qui arrive
├── 01-CONCEPTS/ → Idées développées
├── 02-PROJETS/ → Projets actifs
├── 99-ARCHIVE/ → Trucs terminés
└── _templates/ → Tes 3 templates
Tu crées ça maintenant. 5 dossiers. C'est tout.

🎯 MÉTHODO EN 3 ÉTAPES
1. CAPTURE (tous les jours)

Idée = nouvelle note dans 00-INBOX/
Template \"Note Rapide\"
Tag #inbox
TU TE POSES ZÉRO QUESTION

2. TRAITEMENT (1x par semaine)

Tu ouvres 00-INBOX/
Pour chaque note:

Soit → Développe en Concept (déplace vers 01-CONCEPTS/)
Soit → Rattache à un Projet (déplace vers 02-PROJETS/)
Soit → Archive si plus pertinent


3. LIENS (pendant le traitement)

Quand tu traites une note, crée 2-3 liens [[]] vers autres notes
C'est tout. Pas de graph parfait. Juste des liens basiques.


⚡ ON COMMENCE MAINTENANT
Action immédiate:

Crée les 5 dossiers dans ton vault (2 min)
Crée les 3 templates dans _templates/ (5 min)
Capture ta première note sur ce qu'on vient de décider (2 min)

Je te donne les templates prêts à copier-coller ?
Ou tu veux qu'on ajuste un truc avant ?
Dis-moi \"GO templates\" et je te balance les 3 fichiers prêts à l'emploi. 🚀

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-215-R215-Clairement-mode-trop-trucs-cours]]
- ⬇️ Next: [[Card-217-R217-Yaml-created-date-YYYY-type]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #obsidian
- #receipts
- #code
