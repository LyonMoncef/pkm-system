---
type: chat-card
parent_export: '[[Export]]'
order: 1584
role: assistant
created: '2025-11-10T21:46:26.282699Z'
tags:
- chat-card
- obsidian
- code
attachments_count: 0
---

# 🤖 Message 1584 - Assistant

**ID:** msg-1584

## 💬 Content


**ID:** msg-1584

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

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-1583-R1583-Bashnvim-vault-Templates-SnapshotFull-In]]
- ⬇️ Next: [[Card-1585-R1585-Bashnvim-vault-Templates]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #obsidian
- #code
