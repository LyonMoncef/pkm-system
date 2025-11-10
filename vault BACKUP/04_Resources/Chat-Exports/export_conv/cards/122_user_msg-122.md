---
type: chat-card
parent_export: '[[🚀 POWER BI / EXCEL POWER PIVOT - Architecture de rêve pour tes tickets
  de caisse !]]'
order: 122
role: user
created: '2025-11-09T20:20:59.171886Z'
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

# 👤 Message 122 - User

**ID:** msg-122

## 💬 Content

\n\n**ID:** msg-122\n\nmarkdown---\ncssclass: dashboard\n---\n\n# 🏠 Dashboard Compta Personnel\n\n> [!quote] Citation du jour\n> \"Un budget, c'est dire à ton argent où aller au lieu de te demander où il est allé.\" - Dave Ramsey\n\n## 🎯 Vue d'ensemble\n\n### 📊 Indicateurs Mois en Cours\n```dataviewjs\nconst maintenant = new Date();\nconst annee = maintenant.getFullYear();\nconst mois = String(maintenant.getMonth() + 1).padStart(2, '0');\nconst premierJour = `${annee}-${mois}-01`;\nconst dernierJour = new Date(annee, maintenant.getMonth() + 1, 0);\nconst dernierJourStr = `${annee}-${mois}-${String(dernierJour.getDate()).padStart(2, '0')}`;\n\nconst tickets = dv.pages('\"10-COMPTA/Tickets\"')\n    .where(t => t.date >= premierJour && t.date <= dernierJourStr);\n\nconst total = tickets.array().reduce((sum, t) => sum + (t.montant_total || 0), 0);\nconst budget = 800;\nconst restant = budget - total;\nconst nbTickets = tickets.length;\nconst panierMoyen = nbTickets > 0 ? total / nbTickets : 0;\n\n// Affichage sous forme de cards\ndv.header(3, \"💰 Budget\");\ndv.paragraph(`**${total.toFixed(2)} €** / ${budget} €`);\nconst pct = Math.round((total/budget)*100);\nconst bars = \"█\".repeat(Math.floor(pct/5)) + \"░\".repeat(20-Math.floor(pct/5));\ndv.paragraph(`[${bars}] ${pct}%`);\n\ndv.header(3, \"🎫 Tickets\");\ndv.paragraph(`**${nbTickets}** tickets ce mois`);\ndv.paragraph(`Panier moyen : **${panierMoyen.toFixed(2)} €**`);\n\ndv.header(3, \"📈 Tendance\");\nif (pct < 50) dv.paragraph(\"🟢 Excellent\");\nelse if (pct < 80) dv.paragraph(\"🟡 Vigilance\");\nelse if (pct < 100) dv.paragraph(\"🟠 Attention\");\nelse dv.paragraph(\"🔴 Dépassement\");\n```\n\n---\n\n## 📥 À Traiter (Inbox)\n```dataview\nTABLE WITHOUT ID\n  file.link as \"Ticket\",\n  date as \"Date\",\n  montant_total as \"Montant\"\nFROM \"00-INBOX\"\nWHERE contains(tags, \"compta/a-traiter\")\nSORT date DESC\n```\n\n---\n\n## 🕐 Activité Récente\n\n### Derniers tickets (7 jours)\n```dataview\nTABLE WITHOUT ID\n  file.link as \"Date\",\n  enseigne as \"Enseigne\",\n  montant_total as \"Montant\",\n  choice(contains(tags, \"promo\"), \"🏷️\", \"\") as \"Promo\"\nFROM \"10-COMPTA/Tickets\"\nWHERE date >= date(today) - dur(7 days)\nSORT date DESC\nLIMIT 10\n```\n\n---\n\n## 🏆 Top 5 du Mois\n\n### 🏪 Enseignes\n```dataview\nTABLE WITHOUT ID\n  enseigne as \"Enseigne\",\n  count(rows) as \"Tickets\",\n  sum(rows.montant_total) as \"Total\"\nFROM \"10-COMPTA/Tickets\"\nWHERE date >= date(today) - dur(30 days)\nGROUP BY enseigne\nSORT sum(rows.montant_total) DESC\nLIMIT 5\n```\n\n### 🛒 Produits\n```dataview\nTABLE WITHOUT ID\n  produit as \"Produit\",\n  count(rows) as \"Achats\",\n  sum(rows.montant) as \"Total\"\nFROM \"10-COMPTA/Tickets\"\nWHERE date >= date(today) - dur(30 days)\nFLATTEN articles as produit\nGROUP BY produit\nSORT count(rows) DESC\nLIMIT 5\n```\n\n---\n\n## 📊 Analyses & Rapports\n\n### 📅 Budgets\n```dataview\nLIST\nFROM \"10-COMPTA/Budgets\"\nWHERE type = \"budget\"\nSORT file.name DESC\nLIMIT 6\n```\n\n### 📈 Analyses Mensuelles\n```dataview\nLIST\nFROM \"10-COMPTA/Analyses\"\nSORT file.name DESC\nLIMIT 3\n```\n\n---\n\n## 🔗 Liens Rapides\n\n### 📂 Navigation\n- [[Budget Mensuel Courant]]\n- [[Liste Courses Récurrentes]]\n- [[Comparatif Enseignes]]\n- [[Objectifs Financiers 2025]]\n\n### 🛠️ Actions\n```button\nname 📥 Importer Nouveaux Tickets\ntype command\naction Shell commands: Import Tickets\ncolor blue\n```\n```button\nname 📊 Ouvrir Dashboard Excel\ntype command\naction Shell commands: Open Dashboard\ncolor green\n```\n```button\nname 🔄 Sync NAS\ntype command\naction Shell commands: Sync NAS\ncolor default\n```\n\n---\n\n## 📅 Calendar View\n```calendar\nfrom: \"10-COMPTA/Tickets\"\n```\n\n---\n\n## 📌 Notes Épinglées\n\n- [[Guide Optimisation Courses]]\n- [[Stratégie Promos et Fidélité]]\n- [[Liste Produits Bio Favoris]]\n\n---\n\n## 🎯 Objectifs du Mois\n\n- [ ] Rester sous 800€ budget courses\n- [ ] Tester 2 nouvelles enseignes\n- [ ] Comparer 10 produits récurrents\n- [ ] Mettre à jour Dashboard Excel\n- [ ] Backup mensuel sur NAS\n\n---\n\n**Dernière mise à jour** : `= date(today)` | **Vault size** : `= length(app.vault.getMarkdownFiles())` notes\n\n---\n\n

## 🔗 Navigation

- ⬆️ Previous: [[121_user_msg-121]]
- ⬇️ Next: [[123_user_msg-123]]
- 📊 MOC: [[_MOC_export_conv]]

## 🏷️ Topics

- #excel
- #python
- #obsidian
- #finance
- #receipts
- #code
