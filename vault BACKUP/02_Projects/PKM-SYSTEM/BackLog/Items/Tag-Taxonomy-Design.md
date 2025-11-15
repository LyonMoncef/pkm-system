---
created: 2025-11-14T22:15:00+01:00
updated: 2025-11-14T22:15:00+01:00
type: backlog-item
tags: [backlog-item, taxonomy, architecture, tagging, metadata]
status: todo
priority: high
estimated_time: "3-4h"
category: architecture
project: compta-system
phase: phase-1
related_to: 
  - "[[Transaction-Categorization-Manual]]"
  - "[[Database-Schema-Extension-Metadata]]"
  - "[[Obsidian-Finance-Note-Templates]]"
---

# 🏗️ Tag Taxonomy Design - Finance System

> **Concevoir une taxonomy de tags extensible pour supporter nutrition, recettes, stocks, objectifs**

---

## 📋 Description

Concevoir l'architecture complète de tags/métadonnées qui supportera :
- Catégorisation hiérarchique
- Métadonnées nutritionnelles
- Liens recettes & repas
- Gestion stocks
- Objectifs santé
- Traçabilité temporelle

### Vision Exemple : Raclette
````yaml
article: "RACLETTE CARACTERE 420G"
prix: 3.99

# Hiérarchie Catégories
categories:
  main: Alimentation
  sub: Frais > Fromage
  product: Raclette
  type: Produit laitier

# Tags Simples
tags:
  - fromage
  - raclette
  - produit-laitier
  - frais
  - leclerc

# Temporalité
temporal:
  date_achat: 2025-10-07
  date_consommation: 2025-10-12
  dlc: 2025-10-20
  jours_conservation: 13

# Nutrition (pour 100g)
nutrition:
  calories: 350
  proteines: 23g
  lipides: 28g
  glucides: 1g
  calcium: 600mg
  score_nutri: C

# Stock & Quantité
inventory:
  poids_total: 420g
  prix_100g: 0.95
  location: frigo > bac_legumes
  quantite_restante: 210g
  pourcentage_utilise: 50

# Liens Contexte
links:
  recettes: 
    - "[[Raclette Party]]"
    - "[[Croque Monsieur Raclette]]"
  repas:
    - "[[2025-10-12 Diner Raclette]]"
  contexte:
    - "[[Soirée Amis Octobre]]"

# Métriques Repas
meal_metrics:
  convives: 4
  cout_personne: 1.00
  proteines_apportees: 96g
  calories_apportees: 1470kcal

# Objectifs
goals:
  budget_fromage_mois: 15.00  # 3.99/15 = 26% utilisé
  proteines_jour: 120g  # +23g vers objectif
  calcium_jour: 1000mg  # +600mg vers objectif
````

**Cette structure doit supporter TOUT ÇA ! 🎯**

---

## 🎯 Objectif

Créer architecture de données permettant :
- ✅ Catégorisation hiérarchique multi-niveaux
- ✅ Métadonnées riches (nutrition, temps, stock)
- ✅ Liens bi-directionnels (article ↔ recette ↔ repas)
- ✅ Tracking objectifs (budget, nutrition, santé)
- ✅ Évolutif et maintenable

---

## 🏗️ Architecture Proposée

### Niveau 1 : Tables Database
````sql
-- Table principale : articles_detail (existante, à étendre)
CREATE TABLE articles_detail (
    id INTEGER PRIMARY KEY,
    transaction_id INTEGER,
    date DATE,
    merchant TEXT,
    article TEXT,
    prix_total DECIMAL(10,2),
    
    -- Catégorisation
    category_main TEXT,
    category_sub TEXT,
    product_type TEXT,
    tags TEXT[],  -- Array
    
    -- Nutrition (nullable pour non-food)
    calories_100g DECIMAL(6,2),
    proteines_100g DECIMAL(5,2),
    lipides_100g DECIMAL(5,2),
    glucides_100g DECIMAL(5,2),
    fibres_100g DECIMAL(5,2),
    score_nutri TEXT,
    
    -- Quantité & Stock
    poids_g DECIMAL(8,2),
    quantite DECIMAL(8,2),
    unite TEXT,
    location TEXT,  -- frigo, placard, etc.
    
    -- Temporalité
    date_consommation DATE,
    dlc DATE,
    
    -- Liens (JSON ou foreign keys)
    recette_ids INTEGER[],
    repas_ids INTEGER[],
    contexte_ids INTEGER[]
);

-- Table : recettes
CREATE TABLE recettes (
    id INTEGER PRIMARY KEY,
    nom TEXT,
    ingredients TEXT[],  -- Array article_ids
    instructions TEXT,
    portions INTEGER,
    temps_preparation_min INTEGER,
    cout_total DECIMAL(10,2),
    calories_portion DECIMAL(8,2),
    created_at TIMESTAMP
);

-- Table : repas
CREATE TABLE repas (
    id INTEGER PRIMARY KEY,
    date DATE,
    type TEXT,  -- petit-dej, dejeuner, diner, snack
    recette_id INTEGER,
    convives INTEGER,
    cout_total DECIMAL(10,2),
    cout_personne DECIMAL(10,2),
    calories_total DECIMAL(8,2),
    notes TEXT,
    obsidian_note_path TEXT
);

-- Table : objectifs
CREATE TABLE objectifs (
    id INTEGER PRIMARY KEY,
    type TEXT,  -- budget, nutrition, sante
    category TEXT,  -- fromage, proteines, etc.
    periode TEXT,  -- jour, semaine, mois
    valeur_cible DECIMAL(10,2),
    unite TEXT,
    start_date DATE,
    end_date DATE
);

-- Table : stock_current
CREATE TABLE stock_current (
    article_base TEXT PRIMARY KEY,  -- "Raclette"
    quantite_totale DECIMAL(8,2),
    unite TEXT,
    location TEXT,
    derniere_maj TIMESTAMP,
    dlc_proche DATE
);
````

---

### Niveau 2 : Structure Obsidian
````
vault/
└── 03_Finance/
    ├── Transactions/
    │   └── 2025-10/
    │       └── 2025-10-07-Daily.md
    │
    ├── Articles/
    │   ├── Alimentation/
    │   │   ├── Fromage/
    │   │   │   └── Raclette-Caractere.md
    │   │   ├── Viande/
    │   │   └── Fruits-Legumes/
    │   ├── Transport/
    │   └── Loisirs/
    │
    ├── Recettes/
    │   ├── Raclette-Party.md
    │   ├── Croque-Monsieur-Raclette.md
    │   └── _MOC_Recettes.md
    │
    ├── Repas/
    │   ├── 2025-10/
    │   │   ├── 2025-10-12-Diner-Raclette.md
    │   │   └── 2025-10-13-Dejeuner.md
    │   └── _MOC_Repas.md
    │
    ├── Stock/
    │   ├── Frigo.md
    │   ├── Placard-Epicerie.md
    │   ├── Congelateur.md
    │   └── _Dashboard-Stock.md
    │
    ├── Objectifs/
    │   ├── Budget-Mensuel-2025-10.md
    │   ├── Nutrition-Quotidien.md
    │   └── _MOC_Objectifs.md
    │
    └── Dashboards/
        ├── Dashboard-Nutrition.md
        ├── Dashboard-Budget-Categories.md
        └── Dashboard-Meal-Planning.md
````

---

### Niveau 3 : Tags Hiérarchiques

**Registry complet dans :** `vault/06_Meta/TAG_REGISTRY_FINANCE.md`
````yaml
# CATEGORIES PRINCIPALES
finance/alimentation:
  description: Achats alimentaires
  sous-categories:
    - alimentation/frais
    - alimentation/epicerie
    - alimentation/surgeles
    - alimentation/boissons
    - alimentation/restauration

alimentation/frais:
  sous-categories:
    - frais/fromage
    - frais/viande
    - frais/poisson
    - frais/fruits-legumes
    - frais/produits-laitiers

frais/fromage:
  types:
    - fromage/raclette
    - fromage/emmental
    - fromage/chevre
    - fromage/bleu

# NUTRITION
nutrition/macro:
  - proteines
  - lipides
  - glucides
  - fibres

nutrition/micro:
  - calcium
  - fer
  - vitamine-a
  - vitamine-c

# TEMPORALITE
temporal/cycle:
  - achat
  - stockage
  - consommation
  - perime

# LOCATION
stock/location:
  - frigo
  - placard
  - congelateur
  - cave

# MEAL CONTEXT
meal/type:
  - petit-dejeuner
  - dejeuner
  - diner
  - snack
  - aperitif

meal/occasion:
  - quotidien
  - weekend
  - fete
  - invites
````

---

## 📦 Implémentation

### Phase 1 : Design & Validation (1h)

- [ ] Finaliser schéma DB
- [ ] Valider structure Obsidian
- [ ] Créer TAG_REGISTRY_FINANCE.md
- [ ] Review avec user stories

### Phase 2 : Database Migration (1h)

- [ ] Script SQL migration
- [ ] Ajouter colonnes articles_detail
- [ ] Créer tables recettes, repas, objectifs, stock
- [ ] Tester intégrité

### Phase 3 : Obsidian Templates (1h)

- [ ] Template Article individuel
- [ ] Template Recette
- [ ] Template Repas quotidien
- [ ] Template Objectif

### Phase 4 : Documentation (1h)

- [ ] Guide utilisation tags
- [ ] Exemples concrets
- [ ] Dataview queries exemples
- [ ] Power BI integration guide

---

## 💡 Exemples Concrets

### Note Article : `Raclette-Caractere.md`
````markdown
---
type: article-food
article_id: 47
category_main: Alimentation
category_sub: Frais > Fromage
product: Raclette
tags: [fromage, raclette, produit-laitier, frais, leclerc]
date_achat: 2025-10-07
prix: 3.99
poids: 420g
prix_100g: 0.95
location: frigo/bac-legumes
nutrition:
  calories: 350
  proteines: 23
  lipides: 28
  score: C
---

# 🧀 Raclette Caractère 420g

## 📊 Informations Achat

**Acheté le :** [[2025-10-07-Daily]]  
**Enseigne :** E.Leclerc  
**Prix :** 3.99€ (0.95€/100g)  
**Transaction :** [[Transaction #47]]

## 📦 Stock

**Location actuelle :** Frigo > Bac légumes  
**Quantité restante :** 210g (50%)  
**DLC :** 2025-10-20 (6 jours restants) ⚠️

## 🍽️ Utilisation

**Consommé le :** [[2025-10-12-Diner-Raclette]]  
**Recettes utilisées :**
- [[Raclette Party]] (210g utilisés)

**Reste à utiliser :** 210g

**Suggestions recettes :**
```dataview
LIST
FROM "03_Finance/Recettes"
WHERE contains(ingredients, "raclette")
AND file != this.file
```

## 💪 Nutrition

**Pour 100g :**
- Calories : 350 kcal
- Protéines : 23g
- Lipides : 28g
- Glucides : 1g
- Calcium : 600mg

**Score Nutri :** C

**Contribution repas :**
- Protéines : +96g (pour 420g total)
- Calcium : +2520mg

## 🎯 Impact Objectifs
```dataview
TABLE
  objectif.budget AS "Budget Fromage",
  (3.99 / objectif.budget * 100) AS "% Utilisé"
FROM "03_Finance/Objectifs"
WHERE type = "budget" AND category = "fromage"
```

## 🔗 Liens

**Catégorie :** [[Fromage]]  
**Type :** [[Produit Laitier]]  
**Enseigne :** [[E.Leclerc]]  
**Contexte :** [[Soirée Amis Octobre]]
````

---

### Note Recette : `Raclette-Party.md`
````markdown
---
type: recette
recette_id: 12
tags: [recette, fromage, hiver, convivial, facile]
portions: 4
temps_prep: 15min
temps_cuisson: 30min
cout_total: 28.50
calories_portion: 650
---

# 🧀 Raclette Party

> Soirée conviviale fromage fondu - 4 personnes

## 🛒 Ingrédients

**Fromages (base 4 personnes) :**
- [ ] [[Raclette-Caractere]] : 420g (3.99€) ✅ En stock
- [ ] [[Emmental-Rape]] : 200g (2.50€) ⚠️ À acheter

**Charcuterie :**
- [ ] [[Jambon-Blanc]] : 200g (3.20€)
- [ ] [[Rosette]] : 150g (4.50€)

**Accompagnements :**
- [ ] [[Pommes-Terre]] : 1.5kg (2.80€) ✅ En stock
- [ ] [[Cornichons]] : 1 bocal (2.50€)
- [ ] [[Oignons-Pickles]] : 1 bocal (2.00€)

**Total coût :** 28.50€ (7.12€/personne)

## 📝 Préparation

1. Laver et cuire pommes de terre (20min vapeur)
2. Découper charcuterie
3. Préchauffer appareil raclette
4. Disposer fromages, charcuterie, accompagnements

## 💪 Nutrition (par personne)

- Calories : ~650 kcal
- Protéines : 45g
- Lipides : 38g
- Glucides : 35g

## 🍽️ Repas Réalisés
```dataview
LIST date
FROM "03_Finance/Repas"
WHERE contains(recette, "Raclette Party")
SORT date DESC
```

## 💰 Historique Coûts
```dataview
TABLE
  date,
  convives,
  cout_total,
  cout_personne
FROM "03_Finance/Repas"
WHERE contains(recette, "Raclette Party")
```

## 🎯 Optimisations

**Alternatives moins chères :**
- Raclette marque distributeur : -1.50€
- Remplacer rosette par jambon : -2.00€

**Économie potentielle :** 3.50€ (-12%)
````

---

## 🔗 Références

**Dependencies :**
- [[Transaction-Categorization-Manual]]
- [[Database-Schema-Extension-Metadata]]
- [[Nutrition-Data-Integration]]

**Outputs :**
- TAG_REGISTRY_FINANCE.md
- Database schema SQL
- Obsidian templates
- Migration scripts

---

## 📅 Timeline

**Total : 3-4h**

| Phase | Durée | Status |
|-------|-------|--------|
| Design & validation | 1h | ⬜ Todo |
| DB migration | 1h | ⬜ Todo |
| Obsidian templates | 1h | ⬜ Todo |
| Documentation | 1h | ⬜ Todo |

---

**Priorité :** High (architecture fondamentale)  
**Bloquant :** Catégorisation manuelle  
**Next :** Database schema extension