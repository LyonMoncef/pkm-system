---
type: chat-card
parent_export: '[[Export]]'
order: 1782
role: assistant
created: '2025-11-10T21:46:28.623809Z'
tags:
- chat-card
- python
- obsidian
- code
- git
- automation
attachments_count: 0
---

# 🤖 Message 1782 - Assistant

**ID:** msg-1782

## 💬 Content


**ID:** msg-1782

🎯 ROADMAP CONTEXT BUILDER SYSTEM
⏱️ TOGGL CHECK - Timer actif ?

📝 CRÉER LA CARTE ROADMAP
bashcd ~/pkm-system
nvim vault/02_Projects/PKM-SYSTEM/BackLog/Items/Context\\ Builder\\ System.md
Contenu:
yaml---
created: 2025-11-02T17:00:00
updated: 2025-11-02T17:00:00
type: backlog-item
category: feature
priority: high
status: todo
tags: [feature, automation, context, tooling, python, workflow]
estimated_time: \"6-8h\"
estimated_time_minutes: 420
actual_time: \"\"
blocked_by: []
dependencies:
 - python3
 - pyyaml
 - pathlib
related:
 - \"[[CONTEXT]]\"
 - \"[[TAG_REGISTRY]]\"
 - \"[[MOC - Backlog]]\"
---

# Context Builder System

> **Système 2-temps pour contexte ciblé par session**

---

## 🎯 Description

Script Python qui génère contexte markdown ciblé pour sessions Claude basé sur type de tâche.

**Problème résolu:**
- Context exhaustif = surcharge cognitive
- Context minimal = omissions
- Pas d'anticipation possible

**Solution:**
Approche 2-temps où Claude demande ressources nécessaires, script compile contexte ciblé.

---

## 📋 Roadmap - TODO List

### Phase 1: MVP Script (3-4h)

**Tâches:**
- [ ] [[Context Builder - Setup Project]] - 30min
- [ ] [[Context Builder - Core Parser]] - 1h30
- [ ] [[Context Builder - Tag Extractor]] - 45min
- [ ] [[Context Builder - Structure Tree]] - 45min
- [ ] [[Context Builder - Output Generator]] - 30min

**Livrable:** Script basique fonctionnel

---

### Phase 2: Features Avancées (2-3h)

**Tâches:**
- [ ] [[Context Builder - Example Extractor]] - 1h
- [ ] [[Context Builder - Template Inclusion]] - 45min
- [ ] [[Context Builder - Convention Lookup]] - 45min

**Livrable:** Script complet avec toutes features

---

### Phase 3: Polish & Docs (1h)

**Tâches:**
- [ ] [[Context Builder - CLI Polish]] - 30min
- [ ] [[Context Builder - Documentation]] - 30min

**Livrable:** Script production-ready + docs

---

## ⏱️ Timeline

**Total estimé:** 6-8h
```dataview
TABLE WITHOUT ID
  file.link as \"Tâche\",
  estimated_time as \"Temps\",
  status as \"Status\"
FROM \"02_Projects/PKM-SYSTEM/BackLog/Items\"
WHERE contains(file.name, \"Context Builder\")
  AND file.name != \"Context Builder System\"
```

---

## 🔧 Architecture Technique

### Composants

**1. Parser**
- Lit TAG_REGISTRY.md
- Parse YAML frontmatter
- Extract metadata fichiers

**2. Extractors**
- Tags (depuis TAG_REGISTRY)
- Structure (tree generation)
- Examples (frontmatter + content)
- Templates (full content)
- Conventions (lookup table)

**3. Generator**
- Compile markdown
- Formatting
- Output file

---

## 📊 Usage Prévu

### Exemple: Créer Shortcuts

**Input:**
```bash
python context-builder.py \\
  --tags shortcuts,layer-2 \\
  --structure Shortcuts \\
  --examples \"Shortcuts/Layer-1/*.md\" \\
  --templates ShortcutCard
```

**Output:** `context-session.md`
```markdown
# 🎯 SESSION CONTEXT

## 🚨 Reminders
[Toggl + Commits]

## 🏷️ Tags
shortcuts, layer-2, pkm-system, hotkey

## 📁 Structure: Shortcuts/
[Tree view]

## 📚 Examples
[2-3 Layer 1 cards]

## 📋 Template: ShortcutCard
[Full template]
```

---

## 📋 Critères Acceptation

### Phase 1 (MVP)
- [ ] Script executable
- [ ] Flag --tags fonctionnel
- [ ] Flag --structure fonctionnel
- [ ] Output markdown valide
- [ ] Reminders toujours inclus

### Phase 2 (Features)
- [ ] Flag --examples fonctionnel
- [ ] Flag --templates fonctionnel
- [ ] Flag --conventions fonctionnel
- [ ] Limit examples à 3
- [ ] Parse frontmatter correct

### Phase 3 (Polish)
- [ ] Help text complet
- [ ] Error handling
- [ ] Documentation README
- [ ] Examples usage

---

## 🔗 Ressources

**Libs Python:**
- `pathlib` - File manipulation
- `pyyaml` - YAML parsing
- `argparse` - CLI
- `fnmatch` - Pattern matching

**Fichiers sources:**
- [[TAG_REGISTRY]] - Tags database
- [[CONTEXT]] - Full context reference
- `vault/**/*.md` - Notes to parse

**Liens:**
- [[MOC - Backlog]]
- [[TODO]]

---

## 📝 Notes

**Alternative court-terme:**
Jusqu'à script prêt, utiliser approche manuelle:
1. Claude liste ressources nécessaires
2. User compile manuellement
3. Upload context ciblé

**Workflow futur:**
1. User: \"Mission: [X]\"
2. Claude: `python context-builder.py [params]`
3. User: Execute + upload
4. Claude: Ready avec context ciblé

---

## 🎯 Next Steps Immédiat

**Si go maintenant:**
1. Créer cartes tâches individuelles (5 x Phase 1)
2. Lancer Toggl \"Context Builder MVP\"
3. Dev script Phase 1 (3-4h)

**Si plus tard:**
1. Backlog item créé ✅
2. Utiliser approche manuelle
3. Planifier session dev script

---

**Créé:** 2025-11-02T17:00:00
**Catégorie:** Feature - Tooling
**Priority:** High (améliore workflow sessions)
**Estimation:** 6-8h total

📋 CARTES TÂCHES INDIVIDUELLES
On crée aussi les sous-tâches ?
Liste Tâches à Créer
Phase 1:

Context Builder - Setup Project.md (30min)
Context Builder - Core Parser.md (1h30)
Context Builder - Tag Extractor.md (45min)
Context Builder - Structure Tree.md (45min)
Context Builder - Output Generator.md (30min)

Phase 2:
6. Context Builder - Example Extractor.md (1h)
7. Context Builder - Template Inclusion.md (45min)
8. Context Builder - Convention Lookup.md (45min)
Phase 3:
9. Context Builder - CLI Polish.md (30min)
10. Context Builder - Documentation.md (30min)

🎯 OPTIONS MAINTENANT
A. Créer roadmap + commit (5min)
B. Créer roadmap + 10 sous-tâches + commit (15min)
C. Créer roadmap + commencer Phase 1 maintenant (3-4h)

⏱️ TEMPS SESSION ACTUELLE
On a déjà fait:

Context discussion
CONTEXT.md créé
Toggl MOC refacto
2 commits

Timer Toggl actuel: [Combien ?]
Options:

Finir session maintenant (commit roadmap + stop Toggl + carte session)
Continuer Phase 1 (dev script MVP maintenant)


🤔 TA DÉCISION ?
A. Créer juste roadmap, commit, finir session
B. Créer roadmap + 10 sous-tâches, commit, finir session
C. Créer roadmap + lancer dev script maintenant (longue session)
Et ton temps Toggl actuel ? 🔴

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-1781-R1781-Utilisateur-veut-continue-fournisse-esti]]
- ⬇️ Next: [[Card-1783-R1783-Bashcd-system-nvim-vault-SYSTEM]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #python
- #obsidian
- #code
- #git
- #automation
