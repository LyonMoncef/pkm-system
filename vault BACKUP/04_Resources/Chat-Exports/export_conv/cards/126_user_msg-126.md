---
type: chat-card
parent_export: '[[🚀 POWER BI / EXCEL POWER PIVOT - Architecture de rêve pour tes tickets
  de caisse !]]'
order: 126
role: user
created: '2025-11-09T20:20:59.242679Z'
tags:
- chat-card
- obsidian
attachments_count: 0
---

# 👤 Message 126 - User

**ID:** msg-126

## 💬 Content

\n\n**ID:** msg-126\n\ndataviewTABLE WITHOUT ID\n  file.link as \"Produit\",\n  derniere_achat as \"Dernier achat\",\n  frequence_moyenne as \"Fréq. (jours)\",\n  choice(\n    (date(today) - derniere_achat).days > frequence_moyenne * 1.2,\n    \"🔴 URGENT\",\n    choice(\n      (date(today) - derniere_achat).days > frequence_moyenne * 0.8,\n      \"🟡 Bientôt\",\n      \"🟢 OK\"\n    )\n  ) as \"Statut\"\nFROM \"10-COMPTA/Produits\"\nWHERE essentiels = true\nSORT (date(today) - derniere_achat).days DESC\n\n---\n\n

## 🔗 Navigation

- ⬆️ Previous: [[125_user_msg-125]]
- ⬇️ Next: [[127_user_msg-127]]
- 📊 MOC: [[_MOC_export_conv]]

## 🏷️ Topics

- #obsidian
