---
created: 2025-11-14T22:30:00+01:00
updated: 2025-11-14T22:30:00+01:00
type: backlog-item
tags: [backlog-item, database, architecture, schema, duckdb]
status: todo
priority: high
estimated_time: "2-3h"
category: architecture
project: compta-system
phase: phase-2
related_to: 
  - "[[Tag-Taxonomy-Design]]"
  - "[[Transaction-Categorization-Manual]]"
  - "[[Nutrition-Data-Integration]]"
---

# 🗄️ Database Schema Extension - Metadata Support

> **Étendre le schéma DuckDB pour supporter métadonnées nutrition, stocks, recettes, objectifs**

---

## 📋 Description

Schéma actuel : Simple (date, merchant, amount, article)
Target : Schéma riche supportant nutrition, stocks, recettes, liens contextuels

### Current State
```sql
-- Table actuelle
transactions (id, date, merchant, amount, category, raw_data)
articles_detail (id, transaction_id, article, prix_total, quantite)
```

### Target State
```sql
-- Tables étendues + nouvelles tables
articles_detail (+ nutrition, stock, temporal, tags)
recettes (ingredients, instructions, nutrition)
repas (date, recette, convives, cout)
stock_current (article, quantite, location, dlc)
objectifs (type, category, cible, periode)
article_nutrition (article_id, calories, proteines, etc)
article_links (article_id, recette_id, repas_id)
```

---

## 🎯 Objectif

Créer structure database supportant :
- ✅ Métadonnées nutritionnelles complètes
- ✅ Tracking stock temps réel
- ✅ Liens article ↔ recette ↔ repas
- ✅ Objectifs budget/nutrition/santé
- ✅ Requêtes analytics avancées

---

## 📦 Implémentation

### Phase 1 : Extend articles_detail (1h)
```sql
-- Migration script
ALTER TABLE articles_detail ADD COLUMN category_main TEXT;
ALTER TABLE articles_detail ADD COLUMN category_sub TEXT;
ALTER TABLE articles_detail ADD COLUMN product_type TEXT;
ALTER TABLE articles_detail ADD COLUMN tags TEXT[];

-- Nutrition
ALTER TABLE articles_detail ADD COLUMN poids_g DECIMAL(8,2);
ALTER TABLE articles_detail ADD COLUMN location TEXT;
ALTER TABLE articles_detail ADD COLUMN date_consommation DATE;
ALTER TABLE articles_detail ADD COLUMN dlc DATE;

-- Links (arrays of IDs)
ALTER TABLE articles_detail ADD COLUMN recette_ids INTEGER[];
ALTER TABLE articles_detail ADD COLUMN repas_ids INTEGER[];
```

### Phase 2 : Create New Tables (1h)
```sql
-- Nutrition détaillée
CREATE TABLE article_nutrition (
    article_id INTEGER PRIMARY KEY REFERENCES articles_detail(id),
    calories_100g DECIMAL(6,2),
    proteines_100g DECIMAL(5,2),
    lipides_100g DECIMAL(5,2),
    glucides_100g DECIMAL(5,2),
    fibres_100g DECIMAL(5,2),
    calcium_100g DECIMAL(6,2),
    fer_100g DECIMAL(5,2),
    score_nutri TEXT,
    allergens TEXT[]
);

-- Recettes
CREATE TABLE recettes (
    id INTEGER PRIMARY KEY,
    nom TEXT NOT NULL,
    description TEXT,
    portions INTEGER DEFAULT 4,
    temps_prep_min INTEGER,
    temps_cuisson_min INTEGER,
    difficulte TEXT,
    cout_estime DECIMAL(10,2),
    calories_portion DECIMAL(8,2),
    tags TEXT[],
    created_at TIMESTAMP DEFAULT NOW(),
    obsidian_path TEXT
);

-- Ingrédients recette
CREATE TABLE recette_ingredients (
    recette_id INTEGER REFERENCES recettes(id),
    article_base TEXT,  -- "Raclette", "Pommes de terre"
    quantite DECIMAL(8,2),
    unite TEXT,
    PRIMARY KEY (recette_id, article_base)
);

-- Repas
CREATE TABLE repas (
    id INTEGER PRIMARY KEY,
    date DATE NOT NULL,
    type TEXT,  -- petit-dej, dejeuner, diner, snack
    recette_id INTEGER REFERENCES recettes(id),
    convives INTEGER DEFAULT 1,
    cout_total DECIMAL(10,2),
    cout_personne DECIMAL(10,2),
    calories_total DECIMAL(8,2),
    notes TEXT,
    obsidian_path TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Stock actuel
CREATE TABLE stock_current (
    article_base TEXT PRIMARY KEY,
    quantite_totale DECIMAL(8,2),
    unite TEXT,
    location TEXT,  -- frigo, placard, congelateur
    dlc_proche DATE,
    derniere_maj TIMESTAMP DEFAULT NOW()
);

-- Objectifs
CREATE TABLE objectifs (
    id INTEGER PRIMARY KEY,
    type TEXT NOT NULL,  -- budget, nutrition, sante
    category TEXT,
    periode TEXT,  -- jour, semaine, mois, annee
    valeur_cible DECIMAL(10,2),
    unite TEXT,
    start_date DATE,
    end_date DATE,
    actif BOOLEAN DEFAULT true
);

-- Suivi objectifs
CREATE TABLE objectifs_tracking (
    objectif_id INTEGER REFERENCES objectifs(id),
    date DATE,
    valeur_actuelle DECIMAL(10,2),
    pourcentage DECIMAL(5,2),
    PRIMARY KEY (objectif_id, date)
);
```

### Phase 3 : Migration Script (30min)

**Script : `scripts/db_migration_v2.py`**
```python
#!/usr/bin/env python3
"""
Database Migration v1 to v2 - Add metadata support
"""
import duckdb
from pathlib import Path

def migrate():
    conn = duckdb.connect('finance-system/data/finance.duckdb')
    
    # Backup
    conn.execute("EXPORT DATABASE 'finance-system/data/backup_v1'")
    
    # Run migrations
    # ... (execute all ALTER TABLE and CREATE TABLE)
    
    conn.close()
```

---

## 🧪 Critères d'Acceptation

- [ ] Toutes colonnes ajoutées sans erreur
- [ ] Nouvelles tables créées
- [ ] Backup v1 créé
- [ ] Requêtes test passent
- [ ] Documentation schéma à jour

---

## 📅 Timeline

**Total : 2-3h**

| Phase | Durée | Status |
|-------|-------|--------|
| Extend tables | 1h | ⬜ Todo |
| Create tables | 1h | ⬜ Todo |
| Migration script | 30min | ⬜ Todo |
| Testing | 30min | ⬜ Todo |

---

**Priorité :** High (bloque features nutrition/recettes)  
**Dépend de :** Tag Taxonomy Design  
**Next :** Obsidian templates