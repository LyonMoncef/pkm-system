---
type: chat-card
parent_export: '[[Export]]'
order: 212
role: assistant
created: '2025-11-11T00:41:53.412902Z'
tags:
- chat-card
- obsidian
- finance
- code
attachments_count: 0
---

# 🤖 Message 212 - Assistant

**ID:** msg-212

## 💬 Content


**ID:** msg-212

dataviewjsconst tickets = dv.pages('\"10-COMPTA/Tickets\"')
 .where(t => t.date >= \"2025-10-01\");

// Compter par jour de la semaine
const parJour = {};
tickets.forEach(t => {
 const jour = new Date(t.date).getDay();
 const nomJour = [\"Dim\", \"Lun\", \"Mar\", \"Mer\", \"Jeu\", \"Ven\", \"Sam\"][jour];
 parJour[nomJour] = (parJour[nomJour] || 0) + 1;
});

// Afficher
dv.header(4, \"Fréquence par jour de la semaine\");
Object.entries(parJour).forEach(([jour, count]) => {
 const bars = \"█\".repeat(count) + \"░\".repeat(10 - count);
 dv.paragraph(`${jour}: [${bars}] ${count}`);
});

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-211-R211-DataviewTABLE-WITHOUT-date-Date-enseigne]]
- ⬇️ Next: [[Card-213-R213-DataviewTABLE-WITHOUT-file-link-Produit]]
- 📊 MOC: [[_MOC_Ticket receipt data extraction]]

## 🏷️ Topics

- #obsidian
- #finance
- #code
