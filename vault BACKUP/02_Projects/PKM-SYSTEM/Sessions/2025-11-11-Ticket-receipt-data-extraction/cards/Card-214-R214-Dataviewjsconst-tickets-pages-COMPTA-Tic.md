---
type: chat-card
parent_export: '[[Export]]'
order: 214
role: assistant
created: '2025-11-11T00:41:53.432244Z'
tags:
- chat-card
- obsidian
- finance
- code
attachments_count: 0
---

# 🤖 Message 214 - Assistant

**ID:** msg-214

## 💬 Content


**ID:** msg-214

dataviewjsconst tickets = dv.pages('\"10-COMPTA/Tickets\"');

// Créer matrice
const matrice = {};
tickets.forEach(t => {
 const enseigne = t.enseigne;
 (t.categories || []).forEach(cat => {
 if (!matrice[enseigne]) matrice[enseigne] = {};
 matrice[enseigne][cat] = (matrice[enseigne][cat] || 0) + (t.montant_total || 0);
 });
});

// Afficher
const categories = [...new Set(tickets.flatMap(t => t.categories || []))];
const header = [\"Enseigne\", ...categories];
const rows = Object.entries(matrice).map(([enseigne, cats]) => {
 return [enseigne, ...categories.map(c => (cats[c] || 0).toFixed(2) + \"€\")];
});

dv.table(header, rows);

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-213-R213-DataviewTABLE-WITHOUT-file-link-Produit]]
- ⬇️ Next: [[Card-215-R215-Dashboard-style-markdown-preview-view]]
- 📊 MOC: [[_MOC_Ticket receipt data extraction]]

## 🏷️ Topics

- #obsidian
- #finance
- #code
