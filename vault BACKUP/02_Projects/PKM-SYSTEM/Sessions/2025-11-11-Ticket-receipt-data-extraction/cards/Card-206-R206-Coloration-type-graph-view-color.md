---
type: chat-card
parent_export: '[[Export]]'
order: 206
role: assistant
created: '2025-11-11T00:41:53.356898Z'
tags:
- chat-card
- finance
- code
attachments_count: 0
---

# 🤖 Message 206 - Assistant

**ID:** msg-206

## 💬 Content


**ID:** msg-206

css/* Coloration des nœuds par type */
.graph-view.color-fill-tag[data-tag-name=\"compta/ticket\"] {
 color: #3b82f6; /* Bleu pour tickets */
}

.graph-view.color-fill-tag[data-tag-name=\"compta/enseigne\"] {
 color: #10b981; /* Vert pour enseignes */
}

.graph-view.color-fill-tag[data-tag-name=\"compta/produit\"] {
 color: #f59e0b; /* Orange pour produits */
}

.graph-view.color-fill-tag[data-tag-name=\"compta/budget\"] {
 color: #ef4444; /* Rouge pour budgets */
}

/* Taille des nœuds selon importance */
.graph-view.color-fill-tag[data-tag-name=\"compta/ticket\"] {
 r: 4;
}

.graph-view.color-fill-tag[data-tag-name=\"compta/enseigne\"] {
 r: 8;
}

/* Liens plus épais entre tickets et enseignes */
.graph-view .link[data-link-tags*=\"enseigne\"] {
 stroke-width: 2;
 stroke: #10b981;
}
```

### **Filtres Graph View recommandés**
```
# Vue Tickets du mois
path:\"10-COMPTA/Tickets\"
tag:#compta/2025/10

# Vue Enseignes + Leurs tickets
tag:#compta/enseigne OR tag:#compta/ticket

# Vue Produits les plus achetés
tag:#compta/produit
outgoing-link-count:>5

# Vue Budget Overview
path:\"10-COMPTA/Budgets\" OR tag:#compta/budget

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-205-R205-Json-shell-command-start-Compta]]
- ⬇️ Next: [[Card-207-R207-Javascript-Template-Capture-Rapide-Ticke]]
- 📊 MOC: [[_MOC_Ticket receipt data extraction]]

## 🏷️ Topics

- #finance
- #code
