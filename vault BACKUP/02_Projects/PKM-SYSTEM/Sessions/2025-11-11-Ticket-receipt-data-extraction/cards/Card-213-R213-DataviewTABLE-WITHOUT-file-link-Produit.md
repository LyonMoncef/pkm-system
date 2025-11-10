---
type: chat-card
parent_export: '[[Export]]'
order: 213
role: assistant
created: '2025-11-11T00:41:53.421968Z'
tags:
- chat-card
- obsidian
attachments_count: 0
---

# 🤖 Message 213 - Assistant

**ID:** msg-213

## 💬 Content


**ID:** msg-213

dataviewTABLE WITHOUT ID
 file.link as \"Produit\",
 derniere_achat as \"Dernier achat\",
 frequence_moyenne as \"Fréq. (jours)\",
 choice(
 (date(today) - derniere_achat).days > frequence_moyenne * 1.2,
 \"🔴 URGENT\",
 choice(
 (date(today) - derniere_achat).days > frequence_moyenne * 0.8,
 \"🟡 Bientôt\",
 \"🟢 OK\"
 )
 ) as \"Statut\"
FROM \"10-COMPTA/Produits\"
WHERE essentiels = true
SORT (date(today) - derniere_achat).days DESC

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-212-R212-Dataviewjsconst-tickets-pages-COMPTA-Tic]]
- ⬇️ Next: [[Card-214-R214-Dataviewjsconst-tickets-pages-COMPTA-Tic]]
- 📊 MOC: [[_MOC_Ticket receipt data extraction]]

## 🏷️ Topics

- #obsidian
