# Finance System - Category Taxonomy

## 📋 Vue d'ensemble

Ce système gère les catégories de dépenses de manière centralisée.

### Fichiers

- **categories.yaml** : Source of truth, définition complète taxonomy
- **migration_rules.yaml** : Règles pour renommer/migrer catégories
- **README.md** : Cette documentation

## 🔧 Utilisation

### Modifier une Catégorie

1. Éditer `categories.yaml`
2. Changer `display_name` ou ajouter sous-catégorie
3. Run sync: `python3 scripts/taxonomy_sync.py`
4. Export Power BI: `python3 scripts/export_with_categories.py`

### Renommer une Catégorie

1. Éditer `migration_rules.yaml`
2. Ajouter mapping ancien → nouveau
3. Run migration: `python3 scripts/taxonomy_migrate.py`

### Ajouter une Nouvelle Catégorie
```yaml
nouvelle_categorie:
  display_name: "Ma Catégorie"
  icon: "🎯"
  description: "Description"
  ordre: 10
  
  subcategories:
    sous_cat_1:
      display: "Sous > Cat 1"
      keywords: [mot1, mot2]
```

Puis run `taxonomy_sync.py`

## 📊 Structure
```
categorie_principale (key)
├── display_name: Nom affiché
├── icon: Emoji
├── description: Description
├── color: Code couleur hex
├── ordre: Ordre affichage
└── subcategories:
    └── sous_categorie (key)
        ├── display: Nom complet
        └── keywords: Mots-clés auto-detect
```

## 🎯 Règles

- **category_key** : IMMUABLE (snake_case)
- **display_name** : Modifiable à volonté
- Toujours run sync après modification
- Backup DB avant migration

## 📝 Exemples

### Renommer "Loisirs" → "Divertissement"
```yaml
# categories.yaml
loisirs:  # ← key reste inchangé
  display_name: "Divertissement"  # ← nom affiché changé
```

### Fusionner Catégories
```yaml
# migration_rules.yaml
merge_rules:
  - source: ["Gaming", "Jeux Vidéo"]
    target: "loisirs.gaming_jeux"
```
