---
type: chat-card
parent_export: '[[Export]]'
order: 1371
role: assistant
created: '2025-11-10T21:46:23.947858Z'
tags:
- chat-card
- obsidian
- code
- git
attachments_count: 0
---

# 🤖 Message 1371 - Assistant

**ID:** msg-1371

## 💬 Content


**ID:** msg-1371

markdown# 📸 PROCESS - Créer un Snapshot

## Quand créer un snapshot ?

✅ Changement majeur de structure
✅ Pivot décisionnel important
✅ Refonte complète du contenu
✅ Avant archivage définitif

❌ Typo fix
❌ Ajout mineur
❌ Update timestamp

---

## Process étape par étape

### 1. Copier note living → Full/
```bash
cd vault/06_Meta/Decisions/Snapshots
cp \"../[Note].md\" \"Full/YYYY-MM-DDTHH-mm-ss - [Note] vX.Y [FULL].md\"
```

### 2. Modifier metadata dans Full
```yaml
type: decision-point-archived
status: archived
archived_from: \"[[Living]]\"
```

### 3. Créer Meta/

Utiliser template `SnapshotMeta.md`

### 4. Update living document
```yaml
snapshots:
  - \"[[YYYY-MM-DDTHH-mm-ss - Note vX.Y]]\"
```

### 5. Commit
```bash
git add vault/06_Meta/Decisions/
git commit -m \"feat: create snapshot vX.Y for [Note]\"
git push
```

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-1370-R1370-Yaml-date-YYYY-time-date]]
- ⬇️ Next: [[Card-1372-R1372-Bashgit-vault-Templates-commit-docs]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #obsidian
- #code
- #git
