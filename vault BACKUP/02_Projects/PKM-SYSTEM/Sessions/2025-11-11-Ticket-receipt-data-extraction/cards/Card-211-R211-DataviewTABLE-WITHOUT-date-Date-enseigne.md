---
type: chat-card
parent_export: '[[Export]]'
order: 211
role: assistant
created: '2025-11-11T00:41:53.401844Z'
tags:
- chat-card
- obsidian
- finance
attachments_count: 0
---

# 🤖 Message 211 - Assistant

**ID:** msg-211

## 💬 Content


**ID:** msg-211

dataviewTABLE WITHOUT ID
 date as \"Date\",
 enseigne as \"Enseigne\",
 prix_unitaire as \"Prix\",
 round((prix_unitaire - 6.89) / 6.89 * 100, 1) + \"%\" as \"Δ%\"
FROM \"10-COMPTA/Tickets\"
WHERE contains(articles, \"Gazpacho Alvalle\")
SORT date DESC

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-210-R210-DataviewTABLE-WITHOUT-file-link-Produit]]
- ⬇️ Next: [[Card-212-R212-Dataviewjsconst-tickets-pages-COMPTA-Tic]]
- 📊 MOC: [[_MOC_Ticket receipt data extraction]]

## 🏷️ Topics

- #obsidian
- #finance
