---
type: chat-card
parent_export: '[[Export]]'
order: 1255
role: assistant
created: '2025-11-10T21:46:22.662291Z'
tags:
- chat-card
- obsidian
- code
attachments_count: 0
---

# 🤖 Message 1255 - Assistant

**ID:** msg-1255

## 💬 Content


**ID:** msg-1255

markdown---

## 📊 VUES DÉCISIONS

### 🎯 Options Pending - Quick View
```dataview
TABLE WITHOUT ID
  file.link as \"Option\",
  choice(priority = \"urgent\", \"🔴\",
    choice(priority = \"high\", \"🟠\", \"🟡\")) as \"\",
  priority as \"Priorité\",
  estimated_time as \"Temps\",
  decision_point.file.link as \"Décision\"
FROM \"06_Meta/Decisions/Options\"
WHERE status != \"completed\"
SORT
  choice(priority = \"urgent\", 1,
    choice(priority = \"high\", 2, 3)) ASC,
  file.name ASC
```

---

### ✅ Options Complétées - Historique
```dataview
TABLE WITHOUT ID
  file.link as \"Option\",
  \"✅\" as \"\",
  completed_at as \"Date\",
  decision_point.file.link as \"Décision\"
FROM \"06_Meta/Decisions/Options\"
WHERE status = \"completed\"
SORT completed_at DESC
LIMIT 10
```

---

### 📈 Stats Globales Décisions
```dataview
TABLE WITHOUT ID
  rows.decision_point.file.link as \"Point de Décision\",
  length(rows) as \"Total Options\",
  length(filter(rows, (r) => r.status = \"completed\")) as \"✅ Done\",
  length(filter(rows, (r) => r.status != \"completed\")) as \"⏳ Pending\"
FROM \"06_Meta/Decisions/Options\"
GROUP BY decision_point
SORT length(filter(rows, (r) => r.status != \"completed\")) DESC
```

---

### 🔥 Urgent & High Priority
```dataview
TABLE WITHOUT ID
  file.link as \"Option\",
  choice(priority = \"urgent\", \"🔴\", \"🟠\") as \"\",
  estimated_time as \"Temps\",
  decision_point.file.link as \"Décision\"
FROM \"06_Meta/Decisions/Options\"
WHERE (priority = \"urgent\" OR priority = \"high\")
  AND status != \"completed\"
SORT
  choice(priority = \"urgent\", 1, 2) ASC,
  file.name ASC
```

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-1254-R1254-Markdown-created-updated-type-decision]]
- ⬇️ Next: [[Card-1256-R1256-Yaml-created-updated-type-choice]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #obsidian
- #code
