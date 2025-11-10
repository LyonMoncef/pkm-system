---
type: chat-card
parent_export: '[[🚀 POWER BI / EXCEL POWER PIVOT - Architecture de rêve pour tes tickets
  de caisse !]]'
order: 115
role: user
created: '2025-11-09T20:20:59.057627Z'
tags:
- chat-card
- excel
- obsidian
- finance
- data-analysis
- receipts
- code
attachments_count: 0
---

# 👤 Message 115 - User

**ID:** msg-115

## 💬 Content

\n\n**ID:** msg-115\n\nmarkdown---\ntype: budget\nmois: \"Octobre 2025\"\nannee: 2025\nbudget_prevu: 800.00\ntags:\n  - compta/budget\n  - budget/2025/10\n---\n\n# 💰 Budget Octobre 2025\n\n> [!summary] Vue d'ensemble\n> - **Budget prévu** : 800,00 €\n> - **Dépensé** : `= sum(this.depenses)` €\n> - **Restant** : `= this.budget_prevu - sum(this.depenses)` €\n> - **Progression** : `= round((sum(this.depenses) / this.budget_prevu) * 100, 1)`%\n\n## 📊 Indicateurs clés\n```dataviewjs\nconst tickets = dv.pages('\"10-COMPTA/Tickets\"')\n    .where(t => t.date >= \"2025-10-01\" && t.date <= \"2025-10-31\");\n\nconst total = tickets.array()\n    .reduce((sum, t) => sum + (t.montant_total || 0), 0);\n\nconst budget = 800;\nconst restant = budget - total;\nconst taux = (total / budget * 100).toFixed(1);\n\n// Barre de progression\nconst progression = \"█\".repeat(Math.floor(taux/5)) + \"░\".repeat(20 - Math.floor(taux/5));\n\ndv.paragraph(`**Dépensé** : ${total.toFixed(2)} € / ${budget} €`);\ndv.paragraph(`[${progression}] ${taux}%`);\ndv.paragraph(``);\n\n// Statut\nif (taux < 50) {\n    dv.paragraph(`🟢 **Excellent !** Il reste ${restant.toFixed(2)}€`);\n} else if (taux < 80) {\n    dv.paragraph(`🟡 **Attention** : ${restant.toFixed(2)}€ restants`);\n} else if (taux < 100) {\n    dv.paragraph(`🟠 **Vigilance** : Seulement ${restant.toFixed(2)}€ restants`);\n} else {\n    dv.paragraph(`🔴 **ALERTE** : Dépassement de ${Math.abs(restant).toFixed(2)}€`);\n}\n```\n\n## 📅 Tous les tickets du mois\n```dataview\nTABLE WITHOUT ID\n  file.link as \"Date\",\n  enseigne as \"Enseigne\",\n  montant_total as \"Montant\",\n  length(articles) as \"Articles\"\nFROM \"10-COMPTA/Tickets\"\nWHERE date >= date(\"2025-10-01\") AND date <= date(\"2025-10-31\")\nSORT date DESC\n```\n\n## 📈 Répartition par catégorie\n```dataview\nTABLE WITHOUT ID\n  categorie as \"Catégorie\",\n  sum(rows.montant) as \"Total\",\n  round((sum(rows.montant) / 800) * 100, 1) + \"%\" as \"% Budget\"\nFROM \"10-COMPTA/Tickets\"\nWHERE date >= date(\"2025-10-01\") AND date <= date(\"2025-10-31\")\nFLATTEN categories as categorie\nGROUP BY categorie\nSORT sum(rows.montant) DESC\n```\n\n### Graphique\n```chart\ntype: pie\nlabels: [Alimentaire, Non-Alimentaire, Carburant, Restauration]\nseries:\n  - title: Dépenses\n    data: [348.50, 192.20, 48.64, 12.50]\nwidth: 80%\nlabelColors: true\n```\n\n## 🏪 Répartition par enseigne\n```dataview\nTABLE WITHOUT ID\n  enseigne as \"Enseigne\",\n  count(rows) as \"Nb Tickets\",\n  sum(rows.montant_total) as \"Total €\"\nFROM \"10-COMPTA/Tickets\"\nWHERE date >= date(\"2025-10-01\") AND date <= date(\"2025-10-31\")\nGROUP BY enseigne\nSORT sum(rows.montant_total) DESC\n```\n\n## 📊 Analyse hebdomadaire\n\n| Semaine | Dépenses | vs Objectif | Statut |\n|---------|----------|-------------|--------|\n| S40 (1-7 Oct) | 178,42 € | 200 € | 🟢 OK |\n| S41 (8-14 Oct) | 315,89 € | 200 € | 🔴 Dépassement |\n| S42 (15-21 Oct) | 0,00 € | 200 € | ⚪ En cours |\n| S43 (22-28 Oct) | 0,00 € | 200 € | - |\n| S44 (29-31 Oct) | 0,00 € | - | - |\n\n## 💡 Insights & Observations\n\n### ✅ Ce qui a bien fonctionné\n- [ ] Bonnes promos chez Carrefour (-5,27€)\n- [ ] Pas de dépenses impulsives (hors Switch 2...)\n\n### ⚠️ Points d'attention\n- [ ] **Gros achat** : Console Switch 2 (459€) - à lisser sur plusieurs mois ?\n- [ ] Achats Action (192€) - vérifier nécessité\n- [ ] Fréquence courses trop élevée (7 tickets en 2 semaines)\n\n### 🎯 Actions pour la suite\n- [ ] Planifier courses hebdomadaires (vs quotidiennes)\n- [ ] Comparer systématiquement Leclerc vs Carrefour\n- [ ] Éviter courses après 19h (achats impulsifs)\n\n## 🔮 Prévisions fin de mois\n```dataviewjs\nconst depenseActuelle = 601.93;\nconst jourActuel = 14;\nconst joursRestants = 31 - jourActuel;\nconst moyenneJour = depenseActuelle / jourActuel;\nconst previsionFinMois = depenseActuelle + (moyenneJour * joursRestants);\n\ndv.paragraph(`**Dépense moyenne par jour** : ${moyenneJour.toFixed(2)}€`);\ndv.paragraph(`**Prévision fin de mois** : ${previsionFinMois.toFixed(2)}€`);\n\nif (previsionFinMois > 800) {\n    dv.paragraph(`🔴 **ALERTE** : Dépassement prévu de ${(previsionFinMois - 800).toFixed(2)}€`);\n} else {\n    dv.paragraph(`🟢 Dans les clous ! Marge : ${(800 - previsionFinMois).toFixed(2)}€`);\n}\n```\n\n## 📎 Liens Dashboard\n\n- 📊 [[Dashboard Compta 2025]] : `\\\\NAS\\Compta\\2025\\Dashboards\\Dashboard_Compta_2025.xlsx`\n- 📈 Graphiques détaillés : `\\\\NAS\\Compta\\2025\\10-Octobre\\Analyse_Oct_2025.pbix`\n\n## 🔗 Navigation\n\n← [[Budget Septembre 2025]] | [[Budget Novembre 2025]] →\n\n[[Budget Annuel 2025]] | [[Comparatif Mensuel 2025]]\n\n---\n\n**Créé** : 2025-10-01 | **Dernière MAJ** : {{date:YYYY-MM-DD}}\n\n---\n\n

## 🔗 Navigation

- ⬆️ Previous: [[114_user_msg-114]]
- ⬇️ Next: [[116_user_msg-116]]
- 📊 MOC: [[_MOC_export_conv]]

## 🏷️ Topics

- #excel
- #obsidian
- #finance
- #data-analysis
- #receipts
- #code
