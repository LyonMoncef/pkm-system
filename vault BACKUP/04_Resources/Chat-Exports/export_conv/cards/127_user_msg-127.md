---
type: chat-card
parent_export: '[[🚀 POWER BI / EXCEL POWER PIVOT - Architecture de rêve pour tes tickets
  de caisse !]]'
order: 127
role: user
created: '2025-11-09T20:20:59.253315Z'
tags:
- chat-card
- obsidian
- finance
- code
attachments_count: 0
---

# 👤 Message 127 - User

**ID:** msg-127

## 💬 Content

\n\n**ID:** msg-127\n\ndataviewjsconst tickets = dv.pages('\"10-COMPTA/Tickets\"');\n\n// Créer matrice\nconst matrice = {};\ntickets.forEach(t => {\n    const enseigne = t.enseigne;\n    (t.categories || []).forEach(cat => {\n        if (!matrice[enseigne]) matrice[enseigne] = {};\n        matrice[enseigne][cat] = (matrice[enseigne][cat] || 0) + (t.montant_total || 0);\n    });\n});\n\n// Afficher\nconst categories = [...new Set(tickets.flatMap(t => t.categories || []))];\nconst header = [\"Enseigne\", ...categories];\nconst rows = Object.entries(matrice).map(([enseigne, cats]) => {\n    return [enseigne, ...categories.map(c => (cats[c] || 0).toFixed(2) + \"€\")];\n});\n\ndv.table(header, rows);\n\n---\n\n

## 🔗 Navigation

- ⬆️ Previous: [[126_user_msg-126]]
- ⬇️ Next: [[128_user_msg-128]]
- 📊 MOC: [[_MOC_export_conv]]

## 🏷️ Topics

- #obsidian
- #finance
- #code
