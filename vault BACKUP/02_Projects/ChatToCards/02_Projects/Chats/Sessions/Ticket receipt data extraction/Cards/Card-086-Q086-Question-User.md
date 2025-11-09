---
created: 2025-11-05T20:29:25.152702
updated: 2025-11-05T20:29:25.152702
type: chat-card
chat_message_id: 
chat_message_number: 121
role: user
session: [[MOC-Session-Ticket receipt data extraction]]
tags: [expense, receipt, compta, chat-card, powerbi]
---

# Q086-Question-User

← [[Card-085]] | [[MOC-Session-Ticket receipt data extraction|↑ Session]] | [[Card-087]] →

---

markdown---
type: budget
mois: "Octobre 2025"
annee: 2025
budget_prevu: 800.00
tags:
  - compta/budget
  - budget/2025/10

# 💰 Budget Octobre 2025

> [!summary] Vue d'ensemble
> - **Budget prévu** : 800,00 €
> - **Dépensé** : `= sum(this.depenses)` €
> - **Restant** : `= this.budget_prevu - sum(this.depenses)` €
> - **Progression** : `= round((sum(this.depenses) / this.budget_prevu) * 100, 1)`%

## 📊 Indicateurs clés
```dataviewjs
const tickets = dv.pages('"10-COMPTA/Tickets"')
    .where(t => t.date >= "2025-10-01" && t.date <= "2025-10-31");

const total = tickets.array()
    .reduce((sum, t) => sum + (t.montant_total || 0), 0);

const budget = 800;
const restant = budget - total;
const taux = (total / budget * 100).toFixed(1);

// Barre de progression
const progression = "█".repeat(Math.floor(taux/5)) + "░".repeat(20 - Math.floor(taux/5));

dv.paragraph(`**Dépensé** : ${total.toFixed(2)} € / ${budget} €`);
dv.paragraph(`[${progression}] ${taux}%`);
dv.paragraph(``);

// Statut
if (taux < 50) {
    dv.paragraph(`🟢 **Excellent !** Il reste ${restant.toFixed(2)}€`);
} else if (taux < 80) {
    dv.paragraph(`🟡 **Attention** : ${restant.toFixed(2)}€ restants`);
} else if (taux < 100) {
    dv.paragraph(`🟠 **Vigilance** : Seulement ${restant.toFixed(2)}€ restants`);
} else {
    dv.paragraph(`🔴 **ALERTE** : Dépassement de ${Math.abs(restant).toFixed(2)}€`);
}
```

## 📅 Tous les tickets du mois
```dataview
TABLE WITHOUT ID
  file.link as "Date",
  enseigne as "Enseigne",
  montant_total as "Montant",
  length(articles) as "Articles"
FROM "10-COMPTA/Tickets"
WHERE date >= date("2025-10-01") AND date <= date("2025-10-31")
SORT date DESC
```

## 📈 Répartition par catégorie
```dataview
TABLE WITHOUT ID
  categorie as "Catégorie",
  sum(rows.montant) as "Total",
  round((sum(rows.montant) / 800) * 100, 1) + "%" as "% Budget"
FROM "10-COMPTA/Tickets"
WHERE date >= date("2025-10-01") AND date <= date("2025-10-31")
FLATTEN categories as categorie
GROUP BY categorie
SORT sum(rows.montant) DESC
```

### Graphique
```chart
type: pie
labels: [Alimentaire, Non-Alimentaire, Carburant, Restauration]
series:
  - title: Dépenses
    data: [348.50, 192.20, 48.64, 12.50]
width: 80%
labelColors: true
```

## 🏪 Répartition par enseigne
```dataview
TABLE WITHOUT ID
  enseigne as "Enseigne",
  count(rows) as "Nb Tickets",
  sum(rows.montant_total) as "Total €"
FROM "10-COMPTA/Tickets"
WHERE date >= date("2025-10-01") AND date <= date("2025-10-31")
GROUP BY enseigne
SORT sum(rows.montant_total) DESC
```

## 📊 Analyse hebdomadaire

| Semaine | Dépenses | vs Objectif | Statut |
|---------|----------|-------------|--------|
| S40 (1-7 Oct) | 178,42 € | 200 € | 🟢 OK |
| S41 (8-14 Oct) | 315,89 € | 200 € | 🔴 Dépassement |
| S42 (15-21 Oct) | 0,00 € | 200 € | ⚪ En cours |
| S43 (22-28 Oct) | 0,00 € | 200 € | - |
| S44 (29-31 Oct) | 0,00 € | - | - |

## 💡 Insights & Observations

### ✅ Ce qui a bien fonctionné
- [ ] Bonnes promos chez Carrefour (-5,27€)
- [ ] Pas de dépenses impulsives (hors Switch 2...)

### ⚠️ Points d'attention
- [ ] **Gros achat** : Console Switch 2 (459€) - à lisser sur plusieurs mois ?
- [ ] Achats Action (192€) - vérifier nécessité
- [ ] Fréquence courses trop élevée (7 tickets en 2 semaines)

### 🎯 Actions pour la suite
- [ ] Planifier courses hebdomadaires (vs quotidiennes)
- [ ] Comparer systématiquement Leclerc vs Carrefour
- [ ] Éviter courses après 19h (achats impulsifs)

## 🔮 Prévisions fin de mois
```dataviewjs
const depenseActuelle = 601.93;
const jourActuel = 14;
const joursRestants = 31 - jourActuel;
const moyenneJour = depenseActuelle / jourActuel;
const previsionFinMois = depenseActuelle + (moyenneJour * joursRestants);

dv.paragraph(`**Dépense moyenne par jour** : ${moyenneJour.toFixed(2)}€`);
dv.paragraph(`**Prévision fin de mois** : ${previsionFinMois.toFixed(2)}€`);

if (previsionFinMois > 800) {
    dv.paragraph(`🔴 **ALERTE** : Dépassement prévu de ${(previsionFinMois - 800).toFixed(2)}€`);
} else {
    dv.paragraph(`🟢 Dans les clous ! Marge : ${(800 - previsionFinMois).toFixed(2)}€`);
}
```

## 📎 Liens Dashboard

- 📊 [[Dashboard Compta 2025]] : `\\NAS\Compta\2025\Dashboards\Dashboard_Compta_2025.xlsx`
- 📈 Graphiques détaillés : `\\NAS\Compta\2025\10-Octobre\Analyse_Oct_2025.pbix`

## 🔗 Navigation

← [[Budget Septembre 2025]] | [[Budget Novembre 2025]] →

[[Budget Annuel 2025]] | [[Comparatif Mensuel 2025]]


**Créé** : 2025-10-01 | **Dernière MAJ** : {{date:YYYY-MM-DD}}

---

**Card 86/106** | Message #121 | Role: user