---
type: chat-card
parent_export: '[[🚀 POWER BI / EXCEL POWER PIVOT - Architecture de rêve pour tes tickets
  de caisse !]]'
order: 125
role: user
created: '2025-11-09T20:20:59.230819Z'
tags:
- chat-card
- obsidian
- finance
- code
attachments_count: 0
---

# 👤 Message 125 - User

**ID:** msg-125

## 💬 Content

\n\n**ID:** msg-125\n\ndataviewjsconst tickets = dv.pages('\"10-COMPTA/Tickets\"')\n    .where(t => t.date >= \"2025-10-01\");\n\n// Compter par jour de la semaine\nconst parJour = {};\ntickets.forEach(t => {\n    const jour = new Date(t.date).getDay();\n    const nomJour = [\"Dim\", \"Lun\", \"Mar\", \"Mer\", \"Jeu\", \"Ven\", \"Sam\"][jour];\n    parJour[nomJour] = (parJour[nomJour] || 0) + 1;\n});\n\n// Afficher\ndv.header(4, \"Fréquence par jour de la semaine\");\nObject.entries(parJour).forEach(([jour, count]) => {\n    const bars = \"█\".repeat(count) + \"░\".repeat(10 - count);\n    dv.paragraph(`${jour}: [${bars}] ${count}`);\n});\n\n---\n\n

## 🔗 Navigation

- ⬆️ Previous: [[124_user_msg-124]]
- ⬇️ Next: [[126_user_msg-126]]
- 📊 MOC: [[_MOC_export_conv]]

## 🏷️ Topics

- #obsidian
- #finance
- #code
