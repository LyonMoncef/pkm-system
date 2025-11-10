---
type: chat-card
parent_export: '[[Export]]'
order: 1544
role: assistant
created: '2025-11-10T21:46:25.825266Z'
tags:
- chat-card
- obsidian
- receipts
- code
attachments_count: 0
---

# 🤖 Message 1544 - Assistant

**ID:** msg-1544

## 💬 Content


**ID:** msg-1544

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
  status as \"Status\"
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
  category as \"Type\"
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
  category as \"Catégorie\",
  status as \"Status\"
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
  category as \"Catégorie\",
  length(rows) as \"Total\",
  rows.file.link as \"Items\"
FROM \"02_Projects/PKM-SYSTEM/BackLog/Items\"
WHERE status != \"done\"
GROUP BY category
SORT length(rows) DESC
```

---

## 📈 STATS GLOBALES

**Total Items:**
```dataview
TABLE WITHOUT ID length(rows) as \"Count\"
FROM \"02_Projects/PKM-SYSTEM/BackLog/Items\"
```

**Par Status:**
```dataview
TABLE WITHOUT ID
  status as \"Status\",
  length(rows) as \"Count\"
FROM \"02_Projects/PKM-SYSTEM/BackLog/Items\"
GROUP BY status
```

---

## 🔗 Liens

- [[TODO]] - Tâches courantes
- [[Next Action Choice]] - Décisions en cours

---

**Dernière mise à jour:** 2025-11-02T12:05:00

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-1543-R1543-Bashcd-system-nvim-vault-SYSTEM]]
- ⬇️ Next: [[Card-1545-R1545-Bashnvim-vault-Templates-BacklogItem]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #obsidian
- #receipts
- #code
