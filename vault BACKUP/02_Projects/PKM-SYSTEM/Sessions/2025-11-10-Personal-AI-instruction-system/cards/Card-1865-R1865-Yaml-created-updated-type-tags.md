---
type: chat-card
parent_export: '[[Export]]'
order: 1865
role: assistant
created: '2025-11-10T21:46:29.682479Z'
tags:
- chat-card
- obsidian
- code
- git
attachments_count: 0
---

# 🤖 Message 1865 - Assistant

**ID:** msg-1865

## 💬 Content


**ID:** msg-1865

yaml---
created: 2025-11-02T17:30:00
updated: 2025-11-02T17:30:00
type: moc
tags: [moc, sessions, history]
---

# 🗺️ MOC - Sessions PKM System

> **Index de toutes les sessions de travail**

---

## 📊 Sessions
```dataview
TABLE WITHOUT ID
  file.link as \"Session\",
  session_date as \"Date\",
  duration_total as \"Durée\",
  commits_count as \"Commits\",
  status as \"Status\"
FROM \"02_Projects/PKM-SYSTEM/Sessions\"
WHERE type = \"session-moc\"
SORT session_date DESC
```

---

## 📈 Stats Globales

**Total sessions:**
```dataview
TABLE WITHOUT ID
  \"Sessions\" as Métrique,
  length(rows) as Valeur
FROM \"02_Projects/PKM-SYSTEM/Sessions\"
WHERE type = \"session-moc\"
```

**Commits totaux:**
```dataview
TABLE WITHOUT ID
  \"Commits\" as Métrique,
  sum(rows.commits_count) as Valeur
FROM \"02_Projects/PKM-SYSTEM/Sessions\"
WHERE type = \"session-moc\"
```

**Temps total:**
```dataview
TABLE WITHOUT ID
  \"Minutes\" as Métrique,
  sum(rows.toggl_total_minutes) as Valeur
FROM \"02_Projects/PKM-SYSTEM/Sessions\"
WHERE type = \"session-moc\"
```

---

## 🔗 Liens

- [[TODO]] - Master TODO
- [[MOC - Backlog]] - Backlog items

---

**Dernière mise à jour:** 2025-11-02T17:30:00

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-1864-R1864-Bashnvim-vault-SYSTEM-Sessions-Sessions]]
- ⬇️ Next: [[Card-1866-R1866-Bashcd-system-vault-SYSTEM-Sessions]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #obsidian
- #code
- #git
