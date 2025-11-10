---
type: chat-card
parent_export: '[[Export]]'
order: 1625
role: assistant
created: '2025-11-10T21:46:26.754614Z'
tags:
- chat-card
- obsidian
attachments_count: 0
---

# 🤖 Message 1625 - Assistant

**ID:** msg-1625

## 💬 Content


**ID:** msg-1625

dataviewTABLE WITHOUT ID
 file.link as \"Tâche\",
 estimated_time as \"Est.\",
 actual_time as \"Réel\",
 flow_mode + \"%\" as \"Flow\",
 productive_time as \"Prod.\",
 round(efficiency_ratio, 1) as \"Eff.\"
FROM \"02_Projects/PKM-SYSTEM/Toggl\"
WHERE type = \"toggl-task\" AND status = \"done\"
SORT completed_at DESC
LIMIT 10

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-1624-R1624-Yaml-Temps-Productivité-temps-productif]]
- ⬇️ Next: [[Card-1626-R1626-DataviewTABLE-WITHOUT-round-average-rows]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #obsidian
