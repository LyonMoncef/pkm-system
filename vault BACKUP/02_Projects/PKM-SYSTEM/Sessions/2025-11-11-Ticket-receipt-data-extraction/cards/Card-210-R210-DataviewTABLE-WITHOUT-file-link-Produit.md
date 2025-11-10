---
type: chat-card
parent_export: '[[Export]]'
order: 210
role: assistant
created: '2025-11-11T00:41:53.392031Z'
tags:
- chat-card
- obsidian
attachments_count: 0
---

# 🤖 Message 210 - Assistant

**ID:** msg-210

## 💬 Content


**ID:** msg-210

dataviewTABLE WITHOUT ID
 file.link as \"Produit\",
 derniere_achat as \"Dernier achat\",
 round((date(today) - derniere_achat).days, 0) as \"Jours écoulés\"
FROM \"10-COMPTA/Produits\"
WHERE derniere_achat < date(today) - dur(30 days)
SORT derniere_achat ASC

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-209-R209-Markdown-cssclass-dashboard-Dashboard-Co]]
- ⬇️ Next: [[Card-211-R211-DataviewTABLE-WITHOUT-date-Date-enseigne]]
- 📊 MOC: [[_MOC_Ticket receipt data extraction]]

## 🏷️ Topics

- #obsidian
