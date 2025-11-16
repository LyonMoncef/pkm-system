---
created: 2025-11-15T00:30:00+01:00
updated: 2025-11-15T00:30:00+01:00
type: backlog-item
tags: [backlog-item, architecture, taxonomy, multi-dimensional, pkm]
status: future
priority: high
estimated_time: "9-10h"
category: architecture
project: compta-system
phase: phase-4
related_to: 
  - "[[Tag-Taxonomy-Design]]"
  - "[[Database-Schema-Extension-Metadata]]"
---

# 🏗️ Multi-Dimensional Taxonomy System

> **Système de classification multi-dimensionnelle inspiré PKM - Navigation graphe vs arbre**

---

## 📋 Vision

Remplacer hiérarchie unique 2-niveaux par système permettant classification selon PLUSIEURS axes simultanés.

### Philosophie PKM

**Actuellement :** Arbre hiérarchique (1 chemin)
```
Alimentation > Frais > Fromage
```

**Futur :** Graphe multi-dimensionnel (N chemins)
```
MÊME article "Raclette 420g" vu sous PLUSIEURS angles :

[Budget]        : Alimentation > Frais > Fromage
[Nutrition]     : Protéines > Animales > Produits laitiers
[Impact]        : Carbone élevé > Local > AOP
[Temporalité]   : Hebdomadaire > Saisonnier > Hiver
[Émotionnel]    : Plaisir > Social > Convivial
[EU Taxonomy]   : Sustainable > Circular Economy
```

**→ Navigation multi-axiale comme Obsidian Graph View ! 🎯**

---

## 🎯 Objectifs

### Classification Flexible
- ✅ Multiples taxonomies actives simultanément
- ✅ Même article dans plusieurs classifications
- ✅ Navigation par n'importe quel axe

### Analyses Riches
- ✅ Croisements : "Plaisir" ET "Carbone élevé"
- ✅ Patterns : Corrélation budget vs nutrition
- ✅ Insights : Optimisation coût/santé/impact

### Extensibilité
- ✅ Ajouter taxonomies sans casser existantes
- ✅ User peut créer taxonomies custom
- ✅ Import taxonomies standards (EU, UNSPSC, etc.)

---

## 🏗️ Architecture Proposée

### Structure Database
```sql
-- Taxonomies disponibles
CREATE TABLE taxonomies (
    taxonomy_id INTEGER PRIMARY KEY,
    taxonomy_key TEXT UNIQUE,
    display_name TEXT,
    icon TEXT,
    description TEXT,
    is_active BOOLEAN,
    is_default BOOLEAN,
    source TEXT,  -- 'user', 'standard', 'imported'
    version TEXT,
    created_at TIMESTAMP
);

-- Catégories par taxonomy (N-levels)
CREATE TABLE taxonomy_categories (
    category_id INTEGER PRIMARY KEY,
    taxonomy_id INTEGER REFERENCES taxonomies(taxonomy_id),
    category_key TEXT,
    parent_id INTEGER,  -- Self-reference pour N-levels
    display_name TEXT,
    level INTEGER,
    path TEXT,  -- Full path for queries
    metadata JSONB,  -- Custom fields per taxonomy
    icon TEXT,
    color TEXT
);

-- Many-to-Many : Articles ↔ Catégories
CREATE TABLE article_classifications (
    article_id INTEGER REFERENCES articles_detail(id),
    category_id INTEGER REFERENCES taxonomy_categories(category_id),
    taxonomy_id INTEGER REFERENCES taxonomies(taxonomy_id),
    confidence DECIMAL(3,2),  -- 0.0-1.0
    source TEXT,  -- 'manual', 'auto', 'ai', 'imported'
    created_at TIMESTAMP,
    created_by TEXT,
    PRIMARY KEY (article_id, category_id)
);
```

---

## 📦 Taxonomies Standard Prévues

### 1. Budget Personnel (actuelle)
```yaml
budget:
  Alimentation, Transport, Loisirs, Logement...
```

### 2. Nutrition
```yaml
nutrition:
  Macros: Protéines > Animales > Produits laitiers
  Micros: Calcium > Source élevée
  Score: Nutri-Score A-E
```

### 3. Impact Environnemental
```yaml
impact:
  Carbone: Élevé/Moyen/Faible
  Provenance: Local (<100km) / National / Import
  Labels: Bio, AOP, Label Rouge
```

### 4. Temporalité
```yaml
temporalite:
  Fréquence: Quotidien/Hebdo/Mensuel/Ponctuel
  Saison: Printemps/Été/Automne/Hiver
  Occasion: Quotidien/Weekend/Fête
```

### 5. Émotionnel
```yaml
emotional:
  Intention: Nécessité / Plaisir / Social
  Ressenti: Essentiel / Utile / Superflu / Regret
  Contexte: Solo / Famille / Amis
```

### 6. EU Finance Taxonomy
```yaml
eu_finance:
  Climate Mitigation
  Circular Economy
  Sustainable Water
  Pollution Prevention
  Biodiversity
```

### 7. UNSPSC (optionnel)
```yaml
unspsc:
  United Nations Standard Products and Services Code
  Classification internationale marchandises
```

---

## 🎨 Web UI - Navigation Multi-Axiale

### Switcher de Vue
```
┌────────────────────────────────────────┐
│ Vue : [💰 Budget ▼]                    │
│                                        │
│ Taxonomies actives :                   │
│ ☑ 💰 Budget Personnel                 │
│ ☑ 🇪🇺 EU Finance Taxonomy             │
│ ☑ 💪 Nutrition                        │
│ ☐ 🌱 Impact (désactivée)              │
│ ☐ 📅 Temporalité (désactivée)         │
│ ☐ ❤️ Émotionnel (désactivée)          │
│                                        │
│ [+ Créer Taxonomy Custom]              │
└────────────────────────────────────────┘
```

### Dashboard Adaptatif

Affichage change selon taxonomy sélectionnée :

**Vue Budget :**
```
🛒 Alimentation : 746€ (75%)
🚗 Transport : 31€ (3%)
```

**Vue EU Finance :**
```
♻️ Circular Economy : 320€ (32%)
🌊 Sustainable Water : 180€ (18%)
⚡ Climate Mitigation : 450€ (45%)
```

**Vue Nutrition :**
```
💪 Protéines : 450€ (120g/j avg)
🔥 Lipides : 320€ (85g/j avg)
🌾 Glucides : 280€ (250g/j avg)
```

---

## 🔄 Auto-Tagging Multi-Taxonomy
```python
def auto_classify_article(article):
    """Tag article dans toutes taxonomies actives."""
    
    classifications = []
    
    # Taxonomy 1: Budget (règles manuelles)
    budget_cat = classify_budget(article)
    classifications.append({
        'taxonomy': 'budget',
        'category': budget_cat,
        'confidence': 1.0,
        'source': 'manual'
    })
    
    # Taxonomy 2: Nutrition (API)
    if is_food_item(article):
        nutrition_cats = classify_nutrition_api(article)
        classifications.extend(nutrition_cats)
    
    # Taxonomy 3: Impact (heuristiques)
    impact_cats = classify_impact(article)
    classifications.extend(impact_cats)
    
    # Taxonomy 4: EU Finance (mapping)
    eu_cats = map_to_eu_taxonomy(article, budget_cat)
    classifications.extend(eu_cats)
    
    return classifications
```

---

## 📊 Power BI - Multi-View Reports

### Dynamic Reports

**Slicer : Choisir Taxonomy**
```
[Taxonomy Selector]
├─ Budget Personnel
├─ EU Finance Taxonomy
├─ Nutrition
└─ Impact

[Visuals adaptent automatiquement]
```

**Requêtes DAX :**
```dax
// Mesure dynamique selon taxonomy
Total By Active Taxonomy = 
CALCULATE(
    SUM(articles[prix_total]),
    FILTER(
        article_classifications,
        article_classifications[taxonomy_id] = SELECTEDVALUE(taxonomies[taxonomy_id])
    )
)
```

---

## 🧪 Validation Concept

### Proof of Concept (Phase C actuelle)

**Tester dual-taxonomy :**
1. Garder système actuel (Budget)
2. Ajouter 2ème taxonomy (EU Finance)
3. Articles taggés dans les 2
4. Web UI switcher entre vues
5. Valider architecture avant migration complète

**Si validé → Migration complète système multi-taxonomy**

---

## 📦 Implémentation

### Phase 1 : Architecture DB (3h)
- [ ] Créer tables taxonomies/categories/classifications
- [ ] Migrer données actuelles vers nouvelle structure
- [ ] Scripts migration/rollback

### Phase 2 : YAML Taxonomy Definitions (2h)
- [ ] Format standard définition taxonomies
- [ ] Import/Export taxonomies
- [ ] Validation schéma

### Phase 3 : Auto-Classification (2h)
- [ ] Règles auto-tag par taxonomy
- [ ] API nutrition integration
- [ ] Heuristiques impact/temporalité

### Phase 4 : Web UI Multi-View (2h)
- [ ] Switcher taxonomies
- [ ] Dashboard adaptatif
- [ ] Gestion taxonomies actives

### Phase 5 : Power BI Integration (1h)
- [ ] Export multi-taxonomy
- [ ] DAX measures dynamiques
- [ ] Templates reports

---

## 🎯 Critères d'Acceptation

- [ ] User peut activer/désactiver taxonomies
- [ ] Article visible sous tous ses axes
- [ ] Navigation fluide entre vues
- [ ] Auto-classification fonctionne
- [ ] Power BI adapte visuels
- [ ] Performance acceptable (<1s switch vue)

---

## 💡 Extensions Futures

### Taxonomies Custom User
```yaml
# User peut créer sa propre taxonomy
my_custom_taxonomy:
  display_name: "Ma Classification Gaming"
  categories:
    jeux_retro:
      display: "Jeux Rétro"
    jeux_next_gen:
      display: "Next Gen"
```

### AI-Assisted Classification
```python
# GPT-4 suggère classifications
classifications = openai.classify(
    article="Console Nintendo Switch",
    taxonomies=['budget', 'emotional', 'lifecycle']
)
```

### Graph Visualization
```javascript
// Obsidian-style graph view
// Nodes = Articles
// Edges = Shared classifications
// Clusters = Taxonomies
```

---

## 🔗 Références

**Conversations :**
- Session Multi-Taxonomy Discussion
- EU Finance Taxonomy Conversation

**Inspiration :**
- Obsidian Graph View
- Faceted Classification (Library Science)
- Semantic Web / RDF

**Standards :**
- EU Taxonomy Regulation
- UNSPSC
- GS1 Product Classification

---

## 📅 Timeline

**Proof of Concept :** Session actuelle (3h)  
**Full Implementation :** Future session (9-10h)

**Priority :** High (transformational feature)  
**Status :** Future (after PoC validation)

---

**Créé :** 2025-11-15  
**Philosophie :** "Un graphe, pas un arbre"  
**Impact :** Transformational - change paradigm classification
