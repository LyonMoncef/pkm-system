---
type: chat-card
parent_export: '[[Export]]'
order: 1522
role: assistant
created: '2025-11-10T21:46:25.588053Z'
tags:
- chat-card
- obsidian
- receipts
- code
attachments_count: 0
---

# 🤖 Message 1522 - Assistant

**ID:** msg-1522

## 💬 Content


**ID:** msg-1522

markdown---
created: 2025-11-02T12:05:00
updated: 2025-11-02T12:05:00
type: moc
tags: [moc, backlog, pkm-system]
---

# 🎯 MOC - Backlog PKM System

> **Collection d'idées, bugs et améliorations futures**

---

## 🔴 URGENT
```dataview
TABLE WITHOUT ID
  file.link as \"Item\",
  priority as \"⚠️\",
  estimated_time as \"Temps\",
  tags as \"Tags\"
FROM \"02_Projects/PKM-SYSTEM/BackLog/Items\"
WHERE priority = \"urgent\" AND status != \"done\"
SORT created ASC
```

---

## 🟠 HIGH PRIORITY
```dataview
TABLE WITHOUT ID
  file.link as \"Item\",
  estimated_time as \"Temps\",
  status as \"Status\",
  tags as \"Tags\"
FROM \"02_Projects/PKM-SYSTEM/BackLog/Items\"
WHERE priority = \"high\" AND status != \"done\"
SORT created ASC
```

---

## 🟡 MEDIUM PRIORITY
```dataview
TABLE WITHOUT ID
  file.link as \"Item\",
  estimated_time as \"Temps\",
  category as \"Catégorie\"
FROM \"02_Projects/PKM-SYSTEM/BackLog/Items\"
WHERE priority = \"medium\" AND status != \"done\"
SORT created ASC
```

---

## 🟢 LOW PRIORITY / IDEAS
```dataview
TABLE WITHOUT ID
  file.link as \"Item\",
  category as \"Catégorie\",
  created as \"Ajouté\"
FROM \"02_Projects/PKM-SYSTEM/BackLog/Items\"
WHERE priority = \"low\" AND status != \"done\"
SORT created DESC
```

---

## ✅ DONE (10 derniers)
```dataview
TABLE WITHOUT ID
  file.link as \"Item\",
  completed_at as \"Complété\",
  choice(actual_time, actual_time, estimated_time) as \"Temps\"
FROM \"02_Projects/PKM-SYSTEM/BackLog/Items\"
WHERE status = \"done\"
SORT completed_at DESC
LIMIT 10
```

---

## 📊 PAR CATÉGORIE
```dataview
TABLE WITHOUT ID
  rows.file.link as \"Items\",
  length(rows) as \"Total\"
FROM \"02_Projects/PKM-SYSTEM/BackLog/Items\"
WHERE status != \"done\"
GROUP BY category
SORT length(rows) DESC
```

---

## 🏷️ PAR TAG
```dataview
TABLE WITHOUT ID
  rows.file.link as \"Items\",
  length(rows) as \"Count\"
FROM \"02_Projects/PKM-SYSTEM/BackLog/Items\"
FLATTEN file.tags as tag
WHERE status != \"done\"
GROUP BY tag
SORT length(rows) DESC
```

---

## 📈 STATS
```dataview
TABLE WITHOUT ID
  \"Total Items\" as \"Métrique\",
  length(rows) as \"Valeur\"
FROM \"02_Projects/PKM-SYSTEM/BackLog/Items\"

UNION

TABLE WITHOUT ID
  \"À Faire\" as \"Métrique\",
  length(rows) as \"Valeur\"
FROM \"02_Projects/PKM-SYSTEM/BackLog/Items\"
WHERE status = \"todo\"

UNION

TABLE WITHOUT ID
  \"En Cours\" as \"Métrique\",
  length(rows) as \"Valeur\"
FROM \"02_Projects/PKM-SYSTEM/BackLog/Items\"
WHERE status = \"in-progress\"

UNION

TABLE WITHOUT ID
  \"Complétés\" as \"Métrique\",
  length(rows) as \"Valeur\"
FROM \"02_Projects/PKM-SYSTEM/BackLog/Items\"
WHERE status = \"done\"
```

---

## 🔗 Liens

- [[TODO]] - Tâches courantes
- [[Next Action Choice]] - Décisions en cours

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-1521-R1521-BackLog-Backlog-Living-document-Snapshot]]
- ⬇️ Next: [[Card-1523-R1523-Yaml-created-date-YYYY-time]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #obsidian
- #receipts
- #code
