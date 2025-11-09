---
created: 2025-11-05T20:29:25.113896
updated: 2025-11-05T20:29:25.113896
type: chat-card
chat_message_id: 
chat_message_number: 118
role: user
session: [[MOC-Session-Ticket receipt data extraction]]
tags: [expense, receipt, compta, chat-card, powerbi]
---

# Q083-Question-User

← [[Card-082]] | [[MOC-Session-Ticket receipt data extraction|↑ Session]] | [[Card-084]] →

---

markdown---
type: ticket
date: {{date:YYYY-MM-DD}}
heure: "{{time:HH:mm}}"
enseigne: "[[]]"
magasin: ""
montant_total: 0.00
tags:
  - compta/ticket
  - compta/{{date:YYYY}}/{{date:MM}}
  - enseigne/
aliases: []

# 🧾 Ticket - {{title}}

> [!info] Métadonnées
> - **Date** : `= this.date` à `= this.heure`
> - **Enseigne** : `= this.enseigne`
> - **Magasin** : `= this.magasin`
> - **Montant** : `= this.montant_total` €
> - **Fichiers** : [[#Liens vers NAS]]

## 📊 Vue d'ensemble

| Indicateur | Valeur |
|------------|--------|
| Nombre d'articles | X |
| Panier moyen | XX,XX € |
| Remises | -X,XX € |
| Mode paiement | CB |

## 🛒 Articles achetés
```dataview
TABLE WITHOUT ID
  article as "Article",
  quantite as "Qté",
  prix_unitaire as "PU",
  prix_total as "Total"
FROM "10-COMPTA/Produits"
WHERE contains(tickets, this.file.name)
SORT prix_total DESC
```

### Détail par catégorie

#### 🍎 Alimentaire
- [ ] [[Gazpacho Alvalle]] - 2x - 13,78 €
- [ ] [[Yaourt Grec Citron]] - 1x - 2,89 € ~~5,78€~~ *(PROMO)*
- [ ] [[Baguette Tradition]] - 2x - 2,40 €

#### 🏠 Non Alimentaire  
- [ ] [[Console Nintendo Switch 2]] - 1x - 459,00 €

#### ⛽ Carburant
- [ ] [[Diesel]] - 10,04L - 17,13 €

## 💰 Analyse financière

### Répartition par catégorie
```dataviewjs
// Code pour générer un graphique en barres
const data = [
    {categorie: "Alimentaire", montant: 43.71},
    {categorie: "Beauté/Hygiène", montant: 17.06},
    {categorie: "Non Alimentaire", montant: 19.99}
];

// Affichage simple
dv.table(["Catégorie", "Montant"], 
    data.map(d => [d.categorie, d.montant + " €"])
);
```

### 💡 Insights

> [!success] Points positifs
> - Bonne affaire sur le yaourt grec (-50%)
> - Panier équilibré alimentaire/non-alimentaire

> [!warning] Points d'attention
> - Achat impulsif ? Console Switch 2 (459€)
> - Vérifier si meilleur prix ailleurs

## 🔗 Liens

### Contexte
- **Budget mensuel** : [[Budget Octobre 2025]]
- **Analyse** : [[Analyse Mensuelle Oct 2025]]
- **Enseigne** : [[E.Leclerc]]
- **Comparatif** : [[Comparatif Prix E.Leclerc vs Carrefour]]

### Produits similaires précédemment achetés
```dataview
LIST
FROM "10-COMPTA/Tickets"
WHERE file.name != this.file.name
AND contains(articles, "Gazpacho")
SORT date DESC
LIMIT 5
```

## 📎 Liens vers NAS

> [!abstract] Fichiers stockés
> - 📄 PDF Ticket : `\\NAS\Compta\2025\10-Octobre\2025-10-07_Leclerc_Vienne.pdf`
> - 📊 CSV Data : `\\NAS\Compta\2025\10-Octobre\2025-10-07_Leclerc_Vienne.csv`
> - 🖼️ Photo : `\\NAS\Compta\2025\10-Octobre\2025-10-07_Leclerc_Vienne.jpg`
```button
name Ouvrir PDF sur NAS
type command
action Shell commands: Open PDF
```
```button
name Ouvrir Dashboard Excel
type command
action Shell commands: Open Dashboard
```

## 📅 Timeline
```timeline
+ 2025-10-07 20:00
+ Achat E.Leclerc Vienne
+ 161,29 €
+ 41 articles
```

## 🏷️ Tags additionnels

#depense/alimentaire #depense/high-tech #enseigne/leclerc #promo/octobre


**Créé le** : {{date:YYYY-MM-DD}} | **Modifié le** : {{date:YYYY-MM-DD}}

---

**Card 83/106** | Message #118 | Role: user