---
type: chat-card
parent_export: '[[Export]]'
order: 209
role: assistant
created: '2025-11-11T00:41:53.383732Z'
tags:
- chat-card
- excel
- python
- obsidian
- finance
- receipts
- code
attachments_count: 0
---

# 🤖 Message 209 - Assistant

**ID:** msg-209

## 💬 Content


**ID:** msg-209

markdown---
cssclass: dashboard
---

# 🏠 Dashboard Compta Personnel

> [!quote] Citation du jour
> \"Un budget, c'est dire à ton argent où aller au lieu de te demander où il est allé.\" - Dave Ramsey

## 🎯 Vue d'ensemble

### 📊 Indicateurs Mois en Cours
```dataviewjs
const maintenant = new Date();
const annee = maintenant.getFullYear();
const mois = String(maintenant.getMonth() + 1).padStart(2, '0');
const premierJour = `${annee}-${mois}-01`;
const dernierJour = new Date(annee, maintenant.getMonth() + 1, 0);
const dernierJourStr = `${annee}-${mois}-${String(dernierJour.getDate()).padStart(2, '0')}`;

const tickets = dv.pages('\"10-COMPTA/Tickets\"')
    .where(t => t.date >= premierJour && t.date <= dernierJourStr);

const total = tickets.array().reduce((sum, t) => sum + (t.montant_total || 0), 0);
const budget = 800;
const restant = budget - total;
const nbTickets = tickets.length;
const panierMoyen = nbTickets > 0 ? total / nbTickets : 0;

// Affichage sous forme de cards
dv.header(3, \"💰 Budget\");
dv.paragraph(`**${total.toFixed(2)} €** / ${budget} €`);
const pct = Math.round((total/budget)*100);
const bars = \"█\".repeat(Math.floor(pct/5)) + \"░\".repeat(20-Math.floor(pct/5));
dv.paragraph(`[${bars}] ${pct}%`);

dv.header(3, \"🎫 Tickets\");
dv.paragraph(`**${nbTickets}** tickets ce mois`);
dv.paragraph(`Panier moyen : **${panierMoyen.toFixed(2)} €**`);

dv.header(3, \"📈 Tendance\");
if (pct < 50) dv.paragraph(\"🟢 Excellent\");
else if (pct < 80) dv.paragraph(\"🟡 Vigilance\");
else if (pct < 100) dv.paragraph(\"🟠 Attention\");
else dv.paragraph(\"🔴 Dépassement\");
```

---

## 📥 À Traiter (Inbox)
```dataview
TABLE WITHOUT ID
  file.link as \"Ticket\",
  date as \"Date\",
  montant_total as \"Montant\"
FROM \"00-INBOX\"
WHERE contains(tags, \"compta/a-traiter\")
SORT date DESC
```

---

## 🕐 Activité Récente

### Derniers tickets (7 jours)
```dataview
TABLE WITHOUT ID
  file.link as \"Date\",
  enseigne as \"Enseigne\",
  montant_total as \"Montant\",
  choice(contains(tags, \"promo\"), \"🏷️\", \"\") as \"Promo\"
FROM \"10-COMPTA/Tickets\"
WHERE date >= date(today) - dur(7 days)
SORT date DESC
LIMIT 10
```

---

## 🏆 Top 5 du Mois

### 🏪 Enseignes
```dataview
TABLE WITHOUT ID
  enseigne as \"Enseigne\",
  count(rows) as \"Tickets\",
  sum(rows.montant_total) as \"Total\"
FROM \"10-COMPTA/Tickets\"
WHERE date >= date(today) - dur(30 days)
GROUP BY enseigne
SORT sum(rows.montant_total) DESC
LIMIT 5
```

### 🛒 Produits
```dataview
TABLE WITHOUT ID
  produit as \"Produit\",
  count(rows) as \"Achats\",
  sum(rows.montant) as \"Total\"
FROM \"10-COMPTA/Tickets\"
WHERE date >= date(today) - dur(30 days)
FLATTEN articles as produit
GROUP BY produit
SORT count(rows) DESC
LIMIT 5
```

---

## 📊 Analyses & Rapports

### 📅 Budgets
```dataview
LIST
FROM \"10-COMPTA/Budgets\"
WHERE type = \"budget\"
SORT file.name DESC
LIMIT 6
```

### 📈 Analyses Mensuelles
```dataview
LIST
FROM \"10-COMPTA/Analyses\"
SORT file.name DESC
LIMIT 3
```

---

## 🔗 Liens Rapides

### 📂 Navigation
- [[Budget Mensuel Courant]]
- [[Liste Courses Récurrentes]]
- [[Comparatif Enseignes]]
- [[Objectifs Financiers 2025]]

### 🛠️ Actions
```button
name 📥 Importer Nouveaux Tickets
type command
action Shell commands: Import Tickets
color blue
```
```button
name 📊 Ouvrir Dashboard Excel
type command
action Shell commands: Open Dashboard
color green
```
```button
name 🔄 Sync NAS
type command
action Shell commands: Sync NAS
color default
```

---

## 📅 Calendar View
```calendar
from: \"10-COMPTA/Tickets\"
```

---

## 📌 Notes Épinglées

- [[Guide Optimisation Courses]]
- [[Stratégie Promos et Fidélité]]
- [[Liste Produits Bio Favoris]]

---

## 🎯 Objectifs du Mois

- [ ] Rester sous 800€ budget courses
- [ ] Tester 2 nouvelles enseignes
- [ ] Comparer 10 produits récurrents
- [ ] Mettre à jour Dashboard Excel
- [ ] Backup mensuel sur NAS

---

**Dernière mise à jour** : `= date(today)` | **Vault size** : `= length(app.vault.getMarkdownFiles())` notes

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-208-R208-Yaml-compta-ticket-enseigne-produit]]
- ⬇️ Next: [[Card-210-R210-DataviewTABLE-WITHOUT-file-link-Produit]]
- 📊 MOC: [[_MOC_Ticket receipt data extraction]]

## 🏷️ Topics

- #excel
- #python
- #obsidian
- #finance
- #receipts
- #code
