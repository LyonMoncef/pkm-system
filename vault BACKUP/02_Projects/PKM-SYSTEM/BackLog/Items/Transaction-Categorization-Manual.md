---
created: 2025-11-14T22:00:00+01:00
updated: 2025-11-14T22:00:00+01:00
type: backlog-item
tags: [backlog-item, categorization, finance, tagging, manual]
status: todo
priority: high
estimated_time: "2-3h"
category: core-feature
project: compta-system
phase: phase-1
related_to: 
  - "[[finance.duckdb]]"
  - "[[articles_detail]]"
  - "[[Tag-Taxonomy-Design]]"
---

# 🏷️ Transaction Categorization - Manual Phase

> **Catégorisation manuelle des 96 transactions existantes avec taxonomy de base**

---

## 📋 Description

Actuellement : 96 transactions sans catégories structurées.
Objectif : Établir une catégorisation de base manuelle pour permettre analyses.

### Context

**Données actuelles :**
- 96 articles individuels
- Merchants : Leclerc, Action, Carrefour, Total, McDonald's
- Montants : 0.43€ à 459€
- Pas de catégories assignées

**Target :**
- Chaque transaction catégorisée
- Hiérarchie catégories 2-3 niveaux
- Tags assignés manuellement
- Base pour auto-catégorisation future

---

## 🎯 Objectif

Créer système de catégorisation permettant :
- ✅ Analyses par catégorie (Alimentation, Transport, etc.)
- ✅ Sous-catégories détaillées (Fromage, Carburant, etc.)
- ✅ Dashboard Power BI par catégorie
- ✅ Base taxonomy extensible

---

## 🏗️ Taxonomy Proposée (MVP)

### Niveau 1 : Catégories Principales
````
📊 CATEGORIES PRINCIPALES
├── 🛒 Alimentation
├── 🚗 Transport
├── 🏠 Logement
├── 🎮 Loisirs
├── 👕 Habillement
├── 💪 Santé
├── 🎓 Éducation
├── 💰 Finances
└── 🔧 Autres
````

### Niveau 2 : Sous-Catégories (Exemples)
````
🛒 Alimentation
├── Frais
│   ├── Fromage
│   ├── Viande
│   ├── Poisson
│   ├── Fruits & Légumes
│   └── Produits laitiers
├── Épicerie
│   ├── Conserves
│   ├── Pâtes & Riz
│   ├── Sauces & Condiments
│   └── Petit déjeuner
├── Surgelés
├── Boissons
│   ├── Alcool
│   └── Non-alcoolisé
└── Restauration
    ├── Fast-food
    └── Restaurant

🚗 Transport
├── Carburant
│   ├── Diesel
│   └── Essence
├── Entretien
└── Parking

🎮 Loisirs
├── Gaming
│   ├── Consoles
│   └── Jeux
├── Sorties
└── Culture
````

---

## 📦 Implémentation

### Phase 1 : Enrichir Database (1h)

**Ajouter colonnes catégories :**
````sql
-- DuckDB
ALTER TABLE transactions ADD COLUMN category_main TEXT;
ALTER TABLE transactions ADD COLUMN category_sub TEXT;
ALTER TABLE transactions ADD COLUMN tags TEXT[]; -- Array de tags

ALTER TABLE articles_detail ADD COLUMN category_main TEXT;
ALTER TABLE articles_detail ADD COLUMN category_sub TEXT;
ALTER TABLE articles_detail ADD COLUMN product_type TEXT;
ALTER TABLE articles_detail ADD COLUMN tags TEXT[];
````

**Script : `add_category_columns.py`**

---

### Phase 2 : Catégorisation Manuelle (1-2h)

**Méthode :**

1. **Export CSV pour review**
````bash
   python3 scripts/export_for_categorization.py
   # Génère: categories_to_fill.xlsx
````

2. **Remplir manuellement dans Excel**
   - Colonnes : article | merchant | amount | category_main | category_sub
   - 96 lignes à catégoriser

3. **Re-import dans DB**
````bash
   python3 scripts/import_categories.py --file categories_filled.xlsx
````

**Alternative : UI Web simple (optionnel)**
- Flask app locale
- Affiche article par article
- Dropdown catégories
- Save direct dans DB

---

### Phase 3 : Validation & Export (30min)

**Vérifications :**
````sql
-- Transactions sans catégorie
SELECT COUNT(*) FROM transactions WHERE category_main IS NULL;

-- Distribution catégories
SELECT category_main, COUNT(*), SUM(amount) as total
FROM transactions
GROUP BY category_main
ORDER BY total DESC;
````

**Re-export Power BI :**
````bash
python3 scripts/export_for_powerbi.py
# Inclut maintenant les catégories
````

---

## 🧪 Critères d'Acceptation

### Data Quality

- [ ] 100% transactions catégorisées (category_main)
- [ ] 80%+ avec sous-catégorie (category_sub)
- [ ] Pas de catégories incohérentes
- [ ] Taxonomy documentée

### Power BI

- [ ] Nouveau visual : Pie chart par catégorie principale
- [ ] Nouveau visual : Bar chart sous-catégories
- [ ] Filtres catégories fonctionnels
- [ ] Dashboard updated

### Documentation

- [ ] Liste complète taxonomy
- [ ] Guide catégorisation
- [ ] Mapping merchant → catégories communes

---

## 📊 Dashboard Updates Attendus

**Nouveaux visuals Power BI :**

1. **Pie Chart - Catégories Principales**
   - Alimentation vs Transport vs Loisirs
   - Voir répartition budget

2. **Treemap - Hiérarchie Catégories**
   - Niveau 1 : Catégorie principale
   - Niveau 2 : Sous-catégorie
   - Taille : Montant dépensé

3. **Table - Top Articles par Catégorie**
   - Filtrable par catégorie
   - Voir détail dépenses

---

## 💡 Notes

### Règles Catégorisation

**Console Switch 459€ :**
- category_main: `Loisirs`
- category_sub: `Gaming > Consoles`
- tags: `gaming`, `console`, `nintendo`, `switch`

**Raclette 3.99€ :**
- category_main: `Alimentation`
- category_sub: `Frais > Fromage`
- tags: `fromage`, `raclette`, `produit-laitier`

**Diesel 17.13€ :**
- category_main: `Transport`
- category_sub: `Carburant > Diesel`
- tags: `carburant`, `diesel`, `total-energies`

### Évolutions Futures

Cette catégorisation manuelle servira de :
- **Training data** pour ML auto-catégorisation
- **Base** pour taxonomy extensible
- **Reference** pour nutrition tracking
- **Foundation** pour meal planning

---

## 🔗 Références

**Related Items :**
- [[Tag-Taxonomy-Design]] - Design taxonomy complète
- [[Database-Schema-Extension-Metadata]] - Structure DB extensible
- [[Nutrition-Data-Integration]] - Phase suivante nutrition

**Files :**
- `finance-system/data/finance.duckdb`
- `finance-system/exports/powerbi/articles_detail.xlsx`

---

## 📅 Timeline

**Total : 2-3h**

| Phase | Durée | Status |
|-------|-------|--------|
| Add columns DB | 30min | ⬜ Todo |
| Manual categorization | 1-2h | ⬜ Todo |
| Validation & export | 30min | ⬜ Todo |
| Power BI update | 30min | ⬜ Todo |

---

**Créé :** Finance System MVP Session  
**Priorité :** High (bloque analyses avancées)  
**Bloquant :** Non mais fortement recommandé  
**Next :** Tag taxonomy design
