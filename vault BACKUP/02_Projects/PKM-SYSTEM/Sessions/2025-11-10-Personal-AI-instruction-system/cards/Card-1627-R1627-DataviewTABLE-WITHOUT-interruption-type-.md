---
type: chat-card
parent_export: '[[Export]]'
order: 1627
role: assistant
created: '2025-11-10T21:46:26.778140Z'
tags:
- chat-card
- obsidian
attachments_count: 0
---

# 🤖 Message 1627 - Assistant

**ID:** msg-1627

## 💬 Content


**ID:** msg-1627

dataviewTABLE WITHOUT ID
 interruption.type as \"Type\",
 sum(interruption.minutes) + \"min\" as \"Total\"
FROM \"02_Projects/PKM-SYSTEM/Toggl\"
FLATTEN interruptions as interruption
WHERE status = \"done\"
GROUP BY interruption.type
SORT sum(interruption.minutes) DESC

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-1626-R1626-DataviewTABLE-WITHOUT-round-average-rows]]
- ⬇️ Next: [[Card-1628-R1628-Bashcd-system-nvim-vault-SYSTEM]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #obsidian
