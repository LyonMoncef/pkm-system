---
created: 2025-11-05T20:29:25.127886
updated: 2025-11-05T20:29:25.127886
type: chat-card
chat_message_id: 
chat_message_number: 119
role: user
session: [[MOC-Session-Ticket receipt data extraction]]
tags: [expense, receipt, compta, chat-card, powerbi]
---

# Q084-Question-Format-Donnees

← [[Card-083]] | [[MOC-Session-Ticket receipt data extraction|↑ Session]] | [[Card-085]] →

---

markdown---
type: enseigne
nom: "E.Leclerc"
categorie: "Hypermarché"
tags:
  - compta/enseigne
  - lieu/vienne
logo: "🛒"

# 🛒 E.Leclerc

> [!info] Informations
> - **Type** : Hypermarché
> - **Secteur** : Grande distribution
> - **Programme fidélité** : Carte E.Leclerc
> - **Site web** : [e.leclerc](https://www.e.leclerc/)

## 📍 Magasins fréquentés

### E.Leclerc Viennedis
- **Adresse** : Chemin des Lones, 38200 Vienne
- **Téléphone** : 04.74.31.97.05
- **Distance** : 8,5 km de chez moi
- **Horaires** : Lun-Sam 8h30-20h, Dim 9h-12h30
- **Carte** : [Voir sur Maps](https://maps.google.com/?q=45.5236,4.8748)

### E.Leclerc Station 24/24
- **Type** : Station-service
- **Adresse** : ZAC Le Croissant Fertile, 38200 Vienne

## 📊 Statistiques
```dataview
TABLE WITHOUT ID
  file.name as "Date",
  montant_total as "Montant",
  length(articles) as "Nb Articles"
FROM "10-COMPTA/Tickets"
WHERE enseigne = "E.Leclerc"
SORT date DESC
```

### Vue agrégée
```dataviewjs
// Calculer stats
const tickets = dv.pages('"10-COMPTA/Tickets"')
    .where(t => t.enseigne === "E.Leclerc");

const total = tickets
    .map(t => t.montant_total)
    .reduce((a,b) => a+b, 0);

const nbTickets = tickets.length;
const panierMoyen = total / nbTickets;

dv.table(["Indicateur", "Valeur"], [
    ["Nombre de tickets", nbTickets],
    ["Dépense totale", total.toFixed(2) + " €"],
    ["Panier moyen", panierMoyen.toFixed(2) + " €"],
    ["Dernière visite", tickets.sort(t => t.date, 'desc')[0].date]
]);
```

## 📈 Évolution dans le temps
```dataview
CALENDAR date
FROM "10-COMPTA/Tickets"
WHERE enseigne = "E.Leclerc"
```

## 🏆 Top Produits achetés
```dataview
TABLE WITHOUT ID
  produit as "Produit",
  count(rows) as "Fréquence",
  sum(rows.prix_total) as "Total dépensé"
FROM "10-COMPTA/Tickets"
WHERE enseigne = "E.Leclerc"
FLATTEN articles as produit
GROUP BY produit
SORT count(rows) DESC
LIMIT 10
```

## 💡 Insights & Patterns

### Meilleurs jours pour les promos
- **Mardi** : Souvent promos sur les produits frais
- **Jeudi** : Opérations spéciales high-tech

### Stratégie d'achat optimale
- [ ] Privilégier les marques MDD (Marque De Distributeur)
- [ ] Acheter en lot les non-périssables
- [ ] Comparer avec [[Carrefour Market]] pour les promos

## 🔗 Liens connexes

- [[Comparatif Enseignes]]
- [[Budget Courses Mensuelles]]
- [[Liste Produits Récurrents]]

## 📎 Ressources externes

- 📊 Dashboard Excel : `\\NAS\Compta\2025\Analyses\Dashboard_Leclerc.xlsx`
- 📁 Catalogue promos : `\\NAS\Compta\Prospectus\Leclerc\`


**Tickets liés** : `= length(filter(file.lists, (l) => contains(l.enseigne, "E.Leclerc")))` tickets

---

**Card 84/106** | Message #119 | Role: user