---
type: chat-card
parent_export: '[[🚀 POWER BI / EXCEL POWER PIVOT - Architecture de rêve pour tes tickets
  de caisse !]]'
order: 113
role: user
created: '2025-11-09T20:20:59.039802Z'
tags:
- chat-card
- excel
- obsidian
- finance
- receipts
- code
attachments_count: 0
---

# 👤 Message 113 - User

**ID:** msg-113

## 💬 Content

\n\n**ID:** msg-113\n\nmarkdown---\ntype: enseigne\nnom: \"E.Leclerc\"\ncategorie: \"Hypermarché\"\ntags:\n  - compta/enseigne\n  - lieu/vienne\nlogo: \"🛒\"\n---\n\n# 🛒 E.Leclerc\n\n> [!info] Informations\n> - **Type** : Hypermarché\n> - **Secteur** : Grande distribution\n> - **Programme fidélité** : Carte E.Leclerc\n> - **Site web** : [e.leclerc](https://www.e.leclerc/)\n\n## 📍 Magasins fréquentés\n\n### E.Leclerc Viennedis\n- **Adresse** : Chemin des Lones, 38200 Vienne\n- **Téléphone** : 04.74.31.97.05\n- **Distance** : 8,5 km de chez moi\n- **Horaires** : Lun-Sam 8h30-20h, Dim 9h-12h30\n- **Carte** : [Voir sur Maps](https://maps.google.com/?q=45.5236,4.8748)\n\n### E.Leclerc Station 24/24\n- **Type** : Station-service\n- **Adresse** : ZAC Le Croissant Fertile, 38200 Vienne\n\n## 📊 Statistiques\n```dataview\nTABLE WITHOUT ID\n  file.name as \"Date\",\n  montant_total as \"Montant\",\n  length(articles) as \"Nb Articles\"\nFROM \"10-COMPTA/Tickets\"\nWHERE enseigne = \"E.Leclerc\"\nSORT date DESC\n```\n\n### Vue agrégée\n```dataviewjs\n// Calculer stats\nconst tickets = dv.pages('\"10-COMPTA/Tickets\"')\n    .where(t => t.enseigne === \"E.Leclerc\");\n\nconst total = tickets\n    .map(t => t.montant_total)\n    .reduce((a,b) => a+b, 0);\n\nconst nbTickets = tickets.length;\nconst panierMoyen = total / nbTickets;\n\ndv.table([\"Indicateur\", \"Valeur\"], [\n    [\"Nombre de tickets\", nbTickets],\n    [\"Dépense totale\", total.toFixed(2) + \" €\"],\n    [\"Panier moyen\", panierMoyen.toFixed(2) + \" €\"],\n    [\"Dernière visite\", tickets.sort(t => t.date, 'desc')[0].date]\n]);\n```\n\n## 📈 Évolution dans le temps\n```dataview\nCALENDAR date\nFROM \"10-COMPTA/Tickets\"\nWHERE enseigne = \"E.Leclerc\"\n```\n\n## 🏆 Top Produits achetés\n```dataview\nTABLE WITHOUT ID\n  produit as \"Produit\",\n  count(rows) as \"Fréquence\",\n  sum(rows.prix_total) as \"Total dépensé\"\nFROM \"10-COMPTA/Tickets\"\nWHERE enseigne = \"E.Leclerc\"\nFLATTEN articles as produit\nGROUP BY produit\nSORT count(rows) DESC\nLIMIT 10\n```\n\n## 💡 Insights & Patterns\n\n### Meilleurs jours pour les promos\n- **Mardi** : Souvent promos sur les produits frais\n- **Jeudi** : Opérations spéciales high-tech\n\n### Stratégie d'achat optimale\n- [ ] Privilégier les marques MDD (Marque De Distributeur)\n- [ ] Acheter en lot les non-périssables\n- [ ] Comparer avec [[Carrefour Market]] pour les promos\n\n## 🔗 Liens connexes\n\n- [[Comparatif Enseignes]]\n- [[Budget Courses Mensuelles]]\n- [[Liste Produits Récurrents]]\n\n## 📎 Ressources externes\n\n- 📊 Dashboard Excel : `\\\\NAS\\Compta\\2025\\Analyses\\Dashboard_Leclerc.xlsx`\n- 📁 Catalogue promos : `\\\\NAS\\Compta\\Prospectus\\Leclerc\\`\n\n---\n\n**Tickets liés** : `= length(filter(file.lists, (l) => contains(l.enseigne, \"E.Leclerc\")))` tickets\n\n---\n\n

## 🔗 Navigation

- ⬆️ Previous: [[112_user_msg-112]]
- ⬇️ Next: [[114_user_msg-114]]
- 📊 MOC: [[_MOC_export_conv]]

## 🏷️ Topics

- #excel
- #obsidian
- #finance
- #receipts
- #code
