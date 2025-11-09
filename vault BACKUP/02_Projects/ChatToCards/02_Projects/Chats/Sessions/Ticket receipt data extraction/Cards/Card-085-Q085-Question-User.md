---
created: 2025-11-05T20:29:25.142263
updated: 2025-11-05T20:29:25.142263
type: chat-card
chat_message_id: 
chat_message_number: 120
role: user
session: [[MOC-Session-Ticket receipt data extraction]]
tags: [compta, expense, chat-card, receipt]
---

# Q085-Question-User

← [[Card-084]] | [[MOC-Session-Ticket receipt data extraction|↑ Session]] | [[Card-086]] →

---

markdown---
type: produit
nom: "Gazpacho Alvalle"
marque: "Alvalle"
categorie: "[[Alimentaire]]"
sous_categorie: "Soupes froides"
prix_moyen: 6.89
tags:
  - compta/produit
  - alimentaire/soupe
  - marque/alvalle

# 🥫 Gazpacho Alvalle

> [!info] Fiche Produit
> - **Marque** : Alvalle
> - **Catégorie** : [[Alimentaire]] > Soupes froides
> - **Prix moyen** : 6,89 € (2x bouteilles)
> - **Contenance** : 2x 1L
> - **Prix au litre** : 3,45 €

## 📊 Historique d'achats
```dataview
TABLE WITHOUT ID
  file.link as "Date",
  enseigne as "Enseigne",
  prix_unitaire as "Prix payé",
  (prix_unitaire - 6.89) as "Δ vs Moy"
FROM "10-COMPTA/Tickets"
WHERE contains(articles, "Gazpacho Alvalle")
SORT date DESC
```

### Graphique d'évolution des prix
```dataviewjs
const achats = dv.pages('"10-COMPTA/Tickets"')
    .where(t => t.articles && t.articles.includes("Gazpacho Alvalle"))
    .sort(t => t.date);

// Affichage simple
dv.paragraph(`Acheté ${achats.length} fois`);
dv.paragraph(`Prix min : ${Math.min(...achats.map(a => a.prix_unitaire))}€`);
dv.paragraph(`Prix max : ${Math.max(...achats.map(a => a.prix_unitaire))}€`);
```

## 💰 Analyse de prix

| Enseigne | Prix constaté | Fréquence |
|----------|---------------|-----------|
| E.Leclerc | 6,89 € | ⭐⭐⭐ |
| Carrefour Market | 6,89 € | ⭐⭐⭐ |
| Auchan | 7,49 € | ⭐ |

> [!tip] Recommandation
> Meilleur rapport qualité/prix chez **E.Leclerc** et **Carrefour Market**
> 
> Guetter les promos : souvent -20% en été

## 🔄 Fréquence d'achat

- **Dernière fois** : [[2025-10-14 Carrefour Market]]
- **Avant** : [[2025-10-07 E.Leclerc Vienne]]
- **Fréquence moyenne** : Tous les ~7 jours
- **Statut stock** : 🟢 En stock (estimé 3 jours restants)

> [!warning] Alerte stock
> Prévoir réachat dans **3 jours** (estimation basée sur consommation)

## 🛒 Produits fréquemment achetés avec
```dataview
LIST
FROM "10-COMPTA/Produits"
WHERE file.name != this.file.name
AND any(tickets, (t) => contains(t.articles, "Gazpacho Alvalle"))
SORT affinite DESC
LIMIT 5
```

Affinités détectées :
- [[Baguette Tradition]] (78% des fois)
- [[Yaourt Grec]] (65% des fois)
- [[Tomates séchées]] (54% des fois)

## 📝 Notes & Avis

### Mon avis
⭐⭐⭐⭐⭐ (5/5)

**Points forts** :
- Goût authentique
- Pratique (portion 1L)
- Bon rapport qualité/prix

**Points faibles** :
- Un peu salé parfois

### Alternatives testées
- [[Gazpacho Carrefour Bio]] : Moins bon, plus cher
- [[Gazpacho Alvalle Concombre]] : Intéressant, à retester

## 🔗 Liens

- [[Liste Produits Essentiels]]
- [[Recettes avec Gazpacho]]
- [[Budget Alimentaire Mensuel]]

## 📎 Ressources

- 🌐 Fiche produit : [Alvalle.fr](https://www.alvalle.fr)
- 📄 Valeurs nutritionnelles : `\\NAS\Compta\Produits\Gazpacho_Alvalle_Nutrition.pdf`


**Acheté** : `= length(filter(...))` fois | **Dépense totale** : XX,XX €

---

**Card 85/106** | Message #120 | Role: user