---
type: chat-card
parent_export: '[[Export]]'
order: 1586
role: assistant
created: '2025-11-10T21:46:26.302954Z'
tags:
- chat-card
- obsidian
- receipts
- code
- git
attachments_count: 0
---

# 🤖 Message 1586 - Assistant

**ID:** msg-1586

## 💬 Content


**ID:** msg-1586

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

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-1585-R1585-Bashnvim-vault-Templates]]
- ⬇️ Next: [[Card-1587-R1587-Bashcd-system-Ajouter-fichiers-vault]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #obsidian
- #receipts
- #code
- #git
