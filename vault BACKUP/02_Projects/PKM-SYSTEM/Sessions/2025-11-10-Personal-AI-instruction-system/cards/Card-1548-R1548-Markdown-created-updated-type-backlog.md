---
type: chat-card
parent_export: '[[Export]]'
order: 1548
role: assistant
created: '2025-11-10T21:46:25.867114Z'
tags:
- chat-card
- python
- obsidian
- code
- git
- automation
attachments_count: 0
---

# 🤖 Message 1548 - Assistant

**ID:** msg-1548

## 💬 Content


**ID:** msg-1548

markdown---
created: 2025-11-02T11:45:00
updated: 2025-11-02T12:10:00
type: backlog-item
category: technical-debt
priority: medium
status: todo
tags: [privacy, security, toggl, gitignore]
estimated_time: \"1-2h\"
estimated_time_minutes: 90
related:
 - \"[[TODO]]\"
 - \"[[TAG_REGISTRY]]\"
---

# Privacy Toggl Review

## 🎯 Description

Review et améliorer privacy des tâches Toggl versionnées dans Git.

## 📋 Contexte

**Problème:**
Actuellement, toutes les tâches Toggl sont versionnées (potentiellement publiques si repo public).

**Données sensibles potentielles:**
- Temps précis de travail
- Patterns de travail personnels
- Timestamps détaillés
- Descriptions de tâches

**Use Case:**
Avant partage public du repo, filtrer/anonymiser données personnelles.

**Inspiration:**
Session 2025-11-02 - Discussion .gitignore exceptions

## 🔧 Solutions Possibles

### Option A: Filtrage Sélectif .gitignore
**Description:** Versionner structure mais pas contenu
**Code:**
```gitignore
!vault/02_Projects/PKM-SYSTEM/Toggl/
vault/02_Projects/PKM-SYSTEM/Toggl/**
!vault/02_Projects/PKM-SYSTEM/Toggl/README.md
```
**Avantages:**
- Simple
- Garde structure

**Inconvénients:**
- Perd traçabilité tâches

**Temps estimé:** 15min

### Option B: Script Anonymisation
**Description:** Script qui sanitize avant commit
**Avantages:**
- Garde structure ET traçabilité
- Contrôle granulaire

**Inconvénients:**
- Dev script + maintenance

**Temps estimé:** 2-3h

### Option C: Split Repo
**Description:** Repo public (code) + repo privé (notes)
**Temps estimé:** 30min setup

## 📊 Critères Acceptation

- [ ] Aucune donnée temporelle sensible exposée
- [ ] Structure Toggl préservée
- [ ] Documentation claire de ce qui est versionnée

## 🔗 Ressources

**Liens:**
- [Git Filter-Branch docs](https://git-scm.com)
- [[Backlog]]

---

## 📝 Notes

**Décision:** À prendre avant premier partage public du repo.
Pour l'instant, repo privé donc OK.

---

**Créé:** 2025-11-02
**Session:** Migration snapshots discussion

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-1547-R1547-Bashnvim-vault-SYSTEM-BackLog-Items]]
- ⬇️ Next: [[Card-1549-R1549-Bashnvim-vault-SYSTEM-BackLog-Items]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #python
- #obsidian
- #code
- #git
- #automation
