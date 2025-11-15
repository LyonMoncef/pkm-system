---
created: 2025-11-14T22:50:00+01:00
updated: 2025-11-14T22:50:00+01:00
type: backlog-item
tags: [backlog-item, nutrition, data, api, health]
status: todo
priority: medium
estimated_time: "3-4h"
category: feature
project: compta-system
phase: phase-2
related_to: 
  - "[[Database-Schema-Extension-Metadata]]"
  - "[[Tag-Taxonomy-Design]]"
---

# 💪 Nutrition Data Integration

> **Enrichir articles alimentaires avec données nutritionnelles (calories, macros, micros)**

---

## 📋 Description

Actuellement : Pas de données nutrition
Target : Chaque article alimentaire enrichi avec profil nutritionnel complet

### Sources Données Possibles

1. **Open Food Facts API** (gratuit, FR)
2. **USDA FoodData Central** (gratuit, US)
3. **Base CIQUAL ANSES** (FR officiel)
4. **Manuel** (fallback)

---

## 🎯 Objectif

Enrichir articles avec :
- ✅ Calories / 100g
- ✅ Macros (protéines, lipides, glucides, fibres)
- ✅ Micros (calcium, fer, vitamines clés)
- ✅ Score Nutri (A-E)
- ✅ Allergènes
- ✅ Labels (bio, AOP, etc.)

---

## 📦 Implémentation

### Phase 1 : API Integration (2h)

**Script : `scripts/enrich_nutrition.py`**
```python
import requests
import duckdb

def get_nutrition_openfoodfacts(barcode=None, product_name=None):
    """Query Open Food Facts API."""
    if barcode:
        url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
    else:
        url = f"https://world.openfoodfacts.org/cgi/search.pl?search_terms={product_name}&json=1"
    
    response = requests.get(url)
    data = response.json()
    
    if data.get('status') == 1:
        product = data['product']
        return {
            'calories': product.get('nutriments', {}).get('energy-kcal_100g'),
            'proteines': product.get('nutriments', {}).get('proteins_100g'),
            'lipides': product.get('nutriments', {}).get('fat_100g'),
            'glucides': product.get('nutriments', {}).get('carbohydrates_100g'),
            'score_nutri': product.get('nutrition_grade_fr'),
            # ... plus de champs
        }
    return None
```

### Phase 2 : Enrichment Pipeline (1h)

1. Liste articles sans nutrition
2. Query API pour chaque
3. Update database
4. Manual fallback si API fail

### Phase 3 : Validation (1h)

- Vérifier cohérence données
- Compléter manuellement si besoin
- Export Power BI avec nutrition

---

## 🧪 Critères d'Acceptation

- [ ] 80%+ articles avec nutrition
- [ ] API integration working
- [ ] Fallback manuel documenté
- [ ] Dashboard nutrition créé

---

## 📅 Timeline

**Total : 3-4h**

---

**Priorité :** Medium  
**Dépend de :** Database schema  
**Next :** Inventory management