---
type: chat-card
parent_export: '[[🚀 POWER BI / EXCEL POWER PIVOT - Architecture de rêve pour tes tickets
  de caisse !]]'
order: 114
role: user
created: '2025-11-09T20:20:59.048539Z'
tags:
- chat-card
- obsidian
- finance
- receipts
- code
attachments_count: 0
---

# 👤 Message 114 - User

**ID:** msg-114

## 💬 Content

\n\n**ID:** msg-114\n\nmarkdown---\ntype: produit\nnom: \"Gazpacho Alvalle\"\nmarque: \"Alvalle\"\ncategorie: \"[[Alimentaire]]\"\nsous_categorie: \"Soupes froides\"\nprix_moyen: 6.89\ntags:\n  - compta/produit\n  - alimentaire/soupe\n  - marque/alvalle\n---\n\n# 🥫 Gazpacho Alvalle\n\n> [!info] Fiche Produit\n> - **Marque** : Alvalle\n> - **Catégorie** : [[Alimentaire]] > Soupes froides\n> - **Prix moyen** : 6,89 € (2x bouteilles)\n> - **Contenance** : 2x 1L\n> - **Prix au litre** : 3,45 €\n\n## 📊 Historique d'achats\n```dataview\nTABLE WITHOUT ID\n  file.link as \"Date\",\n  enseigne as \"Enseigne\",\n  prix_unitaire as \"Prix payé\",\n  (prix_unitaire - 6.89) as \"Δ vs Moy\"\nFROM \"10-COMPTA/Tickets\"\nWHERE contains(articles, \"Gazpacho Alvalle\")\nSORT date DESC\n```\n\n### Graphique d'évolution des prix\n```dataviewjs\nconst achats = dv.pages('\"10-COMPTA/Tickets\"')\n    .where(t => t.articles && t.articles.includes(\"Gazpacho Alvalle\"))\n    .sort(t => t.date);\n\n// Affichage simple\ndv.paragraph(`Acheté ${achats.length} fois`);\ndv.paragraph(`Prix min : ${Math.min(...achats.map(a => a.prix_unitaire))}€`);\ndv.paragraph(`Prix max : ${Math.max(...achats.map(a => a.prix_unitaire))}€`);\n```\n\n## 💰 Analyse de prix\n\n| Enseigne | Prix constaté | Fréquence |\n|----------|---------------|-----------|\n| E.Leclerc | 6,89 € | ⭐⭐⭐ |\n| Carrefour Market | 6,89 € | ⭐⭐⭐ |\n| Auchan | 7,49 € | ⭐ |\n\n> [!tip] Recommandation\n> Meilleur rapport qualité/prix chez **E.Leclerc** et **Carrefour Market**\n> \n> Guetter les promos : souvent -20% en été\n\n## 🔄 Fréquence d'achat\n\n- **Dernière fois** : [[2025-10-14 Carrefour Market]]\n- **Avant** : [[2025-10-07 E.Leclerc Vienne]]\n- **Fréquence moyenne** : Tous les ~7 jours\n- **Statut stock** : 🟢 En stock (estimé 3 jours restants)\n\n> [!warning] Alerte stock\n> Prévoir réachat dans **3 jours** (estimation basée sur consommation)\n\n## 🛒 Produits fréquemment achetés avec\n```dataview\nLIST\nFROM \"10-COMPTA/Produits\"\nWHERE file.name != this.file.name\nAND any(tickets, (t) => contains(t.articles, \"Gazpacho Alvalle\"))\nSORT affinite DESC\nLIMIT 5\n```\n\nAffinités détectées :\n- [[Baguette Tradition]] (78% des fois)\n- [[Yaourt Grec]] (65% des fois)\n- [[Tomates séchées]] (54% des fois)\n\n## 📝 Notes & Avis\n\n### Mon avis\n⭐⭐⭐⭐⭐ (5/5)\n\n**Points forts** :\n- Goût authentique\n- Pratique (portion 1L)\n- Bon rapport qualité/prix\n\n**Points faibles** :\n- Un peu salé parfois\n\n### Alternatives testées\n- [[Gazpacho Carrefour Bio]] : Moins bon, plus cher\n- [[Gazpacho Alvalle Concombre]] : Intéressant, à retester\n\n## 🔗 Liens\n\n- [[Liste Produits Essentiels]]\n- [[Recettes avec Gazpacho]]\n- [[Budget Alimentaire Mensuel]]\n\n## 📎 Ressources\n\n- 🌐 Fiche produit : [Alvalle.fr](https://www.alvalle.fr)\n- 📄 Valeurs nutritionnelles : `\\\\NAS\\Compta\\Produits\\Gazpacho_Alvalle_Nutrition.pdf`\n\n---\n\n**Acheté** : `= length(filter(...))` fois | **Dépense totale** : XX,XX €\n\n---\n\n

## 🔗 Navigation

- ⬆️ Previous: [[113_user_msg-113]]
- ⬇️ Next: [[115_user_msg-115]]
- 📊 MOC: [[_MOC_export_conv]]

## 🏷️ Topics

- #obsidian
- #finance
- #receipts
- #code
