---
type: chat-card
parent_export: '[[Export]]'
order: 1571
role: assistant
created: '2025-11-10T21:46:26.139034Z'
tags:
- chat-card
- obsidian
- receipts
- code
- git
attachments_count: 0
---

# 🤖 Message 1571 - Assistant

**ID:** msg-1571

## 💬 Content


**ID:** msg-1571

Progressé vers l'étape suivante de documentation.L'utilisateur a confirmé qu'il a fait le commit #9. On passe maintenant à l'étape 6 - création des templates et documentation du process de snapshot.🎯 ÉTAPE 6 - TEMPLATES & DOCS (10min)
📝 TEMPLATE 1 - SNAPSHOT META
bashcd ~/pkm-system
nvim vault/04_Resources/Templates/SnapshotMeta.md
Contenu:
markdown---
snapshot_date: {{date:YYYY-MM-DD}}T{{time:HH:mm:ss}}
archived_at: {{date:YYYY-MM-DD}}T{{time:HH:mm:ss}}
type: snapshot-index
version: \"X.Y\"
snapshot_of: \"[[Living Document Name]]\"
snapshot_full: \"[[YYYY-MM-DDTHH-mm-ss - Title vX.Y [FULL]]]\"
reason: \"\"
tags: [snapshot, meta, timeline]
---

# 📸 Snapshot vX.Y - [Titre]

> **Index Snapshot** - Métadonnées seulement

## 📊 Informations

**Version:** X.Y
**Date snapshot:** {{date:YYYY-MM-DD}}T{{time:HH:mm:ss}}
**Archivé le:** {{date:YYYY-MM-DD}}T{{time:HH:mm:ss}}
**Raison:** [Pourquoi ce snapshot]

## 📋 Changements Clés

**Avant (vX.Y):**
- [État avant]

**Après (vX.Y+1):**
- [État après]

## 🔗 Navigation

**Living Document:** [[Living Doc]]
**Snapshot Complet:** [[Snapshot Full]]
**Version Suivante:** vX.Y+1

---

## 🎯 Décision/Résultat

[Si applicable - décision prise, résultat obtenu]

---

## 📝 Notes

[Notes additionnelles]

---

**Créé:** {{date:YYYY-MM-DD}}
**Session:** [Session source]

📝 TEMPLATE 2 - SNAPSHOT FULL (Instructions)
bashnvim vault/04_Resources/Templates/SnapshotFull-Instructions.md
Contenu:
markdown# 📸 Instructions - Snapshot Full

> **Pour créer un snapshot Full, copier la note living et modifier le frontmatter**

## Process

### 1. Copier note living
```bash
cd vault/06_Meta/Decisions/Snapshots
cp \"../[Note].md\" \"Full/YYYY-MM-DDTHH-mm-ss - [Note] vX.Y [FULL].md\"
```

### 2. Modifier le frontmatter

**Remplacer par:**
```yaml
---
created: [DATE ORIGINALE - NE PAS CHANGER]
updated: [DATE ORIGINALE - NE PAS CHANGER]
type: decision-point-archived
version: \"X.Y\"
archived_from: \"[[Living Document]]\"
tags: [decision, choice-point, archived, snapshot-full]
status: archived
---
```

**Changements:**
- ✅ `type:` → `decision-point-archived`
- ✅ `version:` → Version du snapshot (string)
- ✅ Ajouter `archived_from:`
- ✅ Ajouter `snapshot-full` dans tags
- ✅ `status:` → `archived`
- ❌ **NE PAS modifier** `created:` et `updated:` (garder dates originales)

### 3. Ajouter footer

**À la fin du fichier:**
```markdown

---

**📸 Note:** Ceci est un snapshot archivé figé à la version X.Y.
**Living Document:** [[Living Doc Name]]
**Snapshot Metadata:** [[YYYY-MM-DDTHH-mm-ss - Title vX.Y]]
**Archivé le:** {{date:YYYY-MM-DD}}T{{time:HH:mm:ss}}
```

---

## ⚠️ Points Attention

- Les dates `created:` et `updated:` doivent rester celles de la version originale
- Seul le footer indique la date d'archivage
- Le snapshot Full est **immuable** - ne plus modifier après création

📝 DOC 3 - SNAPSHOT PROCESS
bashnvim vault/04_Resources/Templates/SNAPSHOT_PROCESS.md
Contenu:
markdown# 📸 PROCESS - Créer un Snapshot

> **Guide complet pour créer un snapshot de décision/document**

---

## ❓ Quand créer un snapshot ?

### ✅ OUI - Snapshot si:

- ✅ Changement majeur de structure
- ✅ Pivot décisionnel important
- ✅ Refonte complète du contenu
- ✅ Avant archivage définitif
- ✅ Passage version majeure (1.0 → 2.0)

### ❌ NON - Pas de snapshot si:

- ❌ Typo fix
- ❌ Ajout mineur (1-2 lignes)
- ❌ Update timestamp
- ❌ Reformulation mineure
- ❌ Correction orthographe

**Fréquence recommandée:** ~1 snapshot par version majeure

---

## 🔧 Process Étape par Étape

### Étape 1: Copier note living → Full/
```bash
cd vault/06_Meta/Decisions/Snapshots
cp \"../[Note].md\" \"Full/YYYY-MM-DDTHH-mm-ss - [Note] vX.Y [FULL].md\"
```

**Convention nommage:**
- Format: `YYYY-MM-DDTHH-mm-ss - [Titre Note] vX.Y [FULL].md`
- Exemple: `2025-11-02T21-45-00 - Next Action Choice v1.0 [FULL].md`

---

### Étape 2: Modifier metadata dans Full

**Ouvrir le fichier Full copié:**
```bash
nvim \"Full/YYYY-MM-DDTHH-mm-ss - [Note] vX.Y [FULL].md\"
```

**Modifier frontmatter:**
```yaml
---
created: [NE PAS CHANGER - garder date originale]
updated: [NE PAS CHANGER - garder date originale]
type: decision-point-archived
version: \"X.Y\"
archived_from: \"[[Living Document]]\"
tags: [decision, choice-point, archived, snapshot-full]
status: archived
---
```

**Ajouter footer à la fin:**
```markdown

---

**📸 Note:** Ceci est un snapshot archivé figé à la version X.Y.
**Living Document:** [[Living Doc Name]]
**Snapshot Metadata:** [[YYYY-MM-DDTHH-mm-ss - Title vX.Y]]
**Archivé le:** YYYY-MM-DDTHH-mm-ss
```

---

### Étape 3: Créer Meta/

**Utiliser template:**
```bash
# Dans Obsidian: utiliser template SnapshotMeta.md
# Ou créer manuellement dans Meta/
```

**Fichier:** `Meta/YYYY-MM-DDTHH-mm-ss - [Note] vX.Y.md`

**Remplir:**
- Version
- Raison du snapshot
- Changements clés (avant/après)
- Liens vers Living et Full

---

### Étape 4: Update living document

**Modifier la note living:**
```yaml
snapshots:
  - \"[[YYYY-MM-DDTHH-mm-ss - Note vX.Y]]\"
```

**Dans changelog:**
```markdown
### vX.Y+1 - DATE

**Changements:**
[...]

**Snapshot vX.Y:** [[YYYY-MM-DDTHH-mm-ss - Note vX.Y]]
```

---

### Étape 5: Commit
```bash
cd ~/pkm-system

git add vault/06_Meta/Decisions/
git commit -m \"feat: create snapshot vX.Y for [Note]

- Snapshot Meta created
- Snapshot Full archived
- Living document updated with reference\"

git push
```

---

## 🎯 Checklist Complète

**Avant de committer:**

- [ ] Full: Copie exacte de la note living
- [ ] Full: Frontmatter modifié (type: archived, version, etc.)
- [ ] Full: Footer ajouté
- [ ] Meta: Créé avec template SnapshotMeta
- [ ] Meta: Tous les champs remplis
- [ ] Living: Référence snapshot dans frontmatter
- [ ] Living: Référence snapshot dans changelog
- [ ] Navigation: Testé Living → Meta → Full → Living
- [ ] Nommage: Conforme convention (ISO timestamp + version)

---

## 📊 Structure Finale
```
Decisions/
├── [Note].md                                    ← Living (vX.Y+1)
│
├── Options/
│   └── ...
│
└── Snapshots/
    ├── Meta/
    │   └── YYYY-MM-DDTHH-mm-ss - Note vX.Y.md  ← Index
    └── Full/
        └── YYYY-MM-DDTHH-mm-ss - Note vX.Y [FULL].md ← Complet
```

---

## 🔗 Ressources

- [[SnapshotMeta]] - Template Meta
- [[SnapshotFull-Instructions]] - Instructions Full
- [[Next Action Choice]] - Exemple snapshot v1.0

---

**Dernière mise à jour:** 2025-11-02
**Auteur:** Session migration snapshots

⚠️ COMMIT #10 - TEMPLATES & DOCS
bashcd ~/pkm-system

# Ajouter les 3 fichiers
git add vault/04_Resources/Templates/

# Vérifier
git status

# Commit
git commit -m \"docs: add snapshot templates and complete process guide

Templates:
- SnapshotMeta.md - Lightweight metadata template
- SnapshotFull-Instructions.md - How to create Full snapshot
- SNAPSHOT_PROCESS.md - Complete step-by-step guide

Documentation:
- When to snapshot (do/don't)
- Naming conventions
- 5-step process
- Checklist before commit
- Examples and resources\"

git push

✅ CHECKLIST ÉTAPE 6

 SnapshotMeta.md créé
 SnapshotFull-Instructions.md créé
 SNAPSHOT_PROCESS.md créé
 Commit #10 poussé


⏱️ ÉTAPE 7 FINALE - TOGGL STOP + CARTE (5min)
Une fois commit #10 fait:

Stop timer Toggl
Créer carte tâche Toggl
Commit carte
DONE ! 🎉

Dis-moi quand commit #10 est poussé ! 🚀

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-1570-R1570-Progressé-vers-étape-suivante-documentat]]
- ⬇️ Next: [[Card-1572-R1572-Progressé-vers-étape-suivante-documentat]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #obsidian
- #receipts
- #code
- #git
