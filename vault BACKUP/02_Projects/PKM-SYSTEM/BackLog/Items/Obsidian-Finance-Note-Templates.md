---
created: 2025-11-14T22:40:00+01:00
updated: 2025-11-14T22:40:00+01:00
type: backlog-item
tags: [backlog-item, obsidian, templates, finance, notes]
status: todo
priority: medium
estimated_time: "2-3h"
category: tooling
project: compta-system
phase: phase-2
related_to: 
  - "[[Tag-Taxonomy-Design]]"
  - "[[Database-Schema-Extension-Metadata]]"
---

# 📝 Obsidian Finance Note Templates

> **Créer templates Obsidian pour Articles, Recettes, Repas, Objectifs avec Dataview queries**

---

## 📋 Description

Créer templates réutilisables pour structurer notes finance dans Obsidian.

### Templates Nécessaires

1. **Article Individuel** - Track item acheté
2. **Recette** - Instructions + ingrédients + nutrition
3. **Repas Quotidien** - Journal repas avec coûts
4. **Objectif** - Budget/nutrition goals
5. **Daily Finance** - Note quotidienne transactions
6. **Stock Location** - État frigo/placard

---

## 🎯 Objectif

Templates permettant :
- ✅ Création rapide notes structurées
- ✅ YAML frontmatter cohérent
- ✅ Dataview queries intégrées
- ✅ Liens bi-directionnels automatiques

---

## 📦 Templates à Créer

### Template 1 : Article Food

**Fichier : `vault/04_Resources/Templates/Finance-Article-Food.md`**
```markdown
---
type: article-food
article_id: <% tp.system.prompt("Article ID") %>
category_main: <% tp.system.suggester(["Alimentation", "Transport", "Loisirs"], ["Alimentation", "Transport", "Loisirs"]) %>
category_sub: <% tp.system.prompt("Sous-catégorie") %>
product: <% tp.system.prompt("Nom produit") %>
tags: [<% tp.system.prompt("Tags (comma-separated)") %>]
date_achat: <% tp.date.now("YYYY-MM-DD") %>
prix: <% tp.system.prompt("Prix") %>
merchant: <% tp.system.prompt("Enseigne") %>
---

# 🛒 <% tp.file.title %>

## 📊 Informations Achat

**Acheté le :** [[<% tp.date.now("YYYY-MM-DD") %>-Daily]]  
**Enseigne :** <% merchant %>  
**Prix :** <% prix %>€  
**Poids :** <% tp.system.prompt("Poids (g)") %>g

## 📦 Stock

**Location :** <% tp.system.suggester(["Frigo", "Placard", "Congélateur"], ["frigo", "placard", "congelateur"]) %>  
**Quantité restante :**   
**DLC :** 

## 🍽️ Utilisation

**Consommé le :**  
**Recettes :**

## 💪 Nutrition (pour 100g)

- Calories :  
- Protéines :  
- Lipides :  
- Glucides :  

## 🔗 Liens

**Catégorie :** [[]]  
**Type :** [[]]
```

### Template 2 : Recette

**Fichier : `vault/04_Resources/Templates/Finance-Recette.md`**
```markdown
---
type: recette
recette_id: 
tags: [recette]
portions: 4
temps_prep: 
temps_cuisson: 
cout_total: 
calories_portion: 
created: <% tp.date.now("YYYY-MM-DD") %>
---

# 🍳 <% tp.file.title %>

> <% tp.system.prompt("Description courte") %>

## 🛒 Ingrédients (base <% portions %> personnes)

**Catégorie 1 :**
- [ ] [[]] : Xg (X€)

## 📝 Préparation

1. 
2. 
3. 

## 💪 Nutrition (par personne)

- Calories : ~<% calories_portion %> kcal
- Protéines :  
- Lipides :  
- Glucides :  

## 🍽️ Repas Réalisés

\`\`\`dataview
TABLE date, convives, cout_total, cout_personne
FROM "03_Finance/Repas"
WHERE contains(recette, this.file.name)
SORT date DESC
\`\`\`

## 💰 Coût Total

**Ingrédients :** <% cout_total %>€  
**Coût/personne :** <% cout_total / portions %>€

## 🎯 Notes
```

### Template 3 : Repas Quotidien

**Fichier : `vault/04_Resources/Templates/Finance-Repas.md`**
```markdown
---
type: repas
date: <% tp.date.now("YYYY-MM-DD") %>
type_repas: <% tp.system.suggester(["Petit-déjeuner", "Déjeuner", "Dîner", "Snack"], ["petit-dej", "dejeuner", "diner", "snack"]) %>
recette: 
convives: <% tp.system.prompt("Nombre convives", "1") %>
cout_total: 
tags: [repas]
---

# 🍽️ <% tp.file.title %>

**Date :** <% tp.date.now("YYYY-MM-DD") %>  
**Type :** <% type_repas %>  
**Convives :** <% convives %>

## 🍳 Recette

**Recette utilisée :** [[]]  
**Lien :** 

## 🛒 Ingrédients Utilisés

\`\`\`dataview
TABLE article, quantite, prix_total
FROM "03_Finance/Articles"
WHERE contains(repas_ids, this.file.name)
\`\`\`

## 💰 Coût

**Total :** <% cout_total %>€  
**Par personne :** <% cout_total / convives %>€

## 💪 Nutrition Estimée

- Calories totales :  
- Protéines :  

## 📝 Notes

**Appréciation :**  
**À refaire :** Oui / Non  
**Modifications pour prochaine fois :**
```

### Template 4 : Daily Finance

**Fichier : `vault/04_Resources/Templates/Finance-Daily.md`**
```markdown
---
date: <% tp.date.now("YYYY-MM-DD") %>
type: daily-finance
tags: [finance, daily]
balance_start: 
balance_end: 
spent_today: 
---

# 💰 Finance - <% tp.date.now("YYYY-MM-DD") %>

## 📊 Balance

**Balance début :**  
**Balance fin :**  
**Dépenses :** 

## 💳 Transactions Aujourd'hui

\`\`\`dataview
TABLE merchant, article, amount, category_main
FROM "03_Finance/Articles"
WHERE date = date(<% tp.date.now("YYYY-MM-DD") %>)
SORT amount DESC
\`\`\`

## 💰 Budgets - État

\`\`\`dataview
TABLE category, spent, budget, remaining
FROM "03_Finance/Objectifs"  
WHERE type = "budget" AND periode = "mois"
\`\`\`

## 📅 Échéances Prochaines

| Date | Description | Montant |
|------|-------------|---------|
|      |             |         |

## 🔗 Liens

- [[<% tp.date.now("YYYY-MM-DD", -1) %>-Daily]] ← Hier
- [[<% tp.date.now("YYYY-MM-DD", 1) %>-Daily]] → Demain
```

---

## 🧪 Critères d'Acceptation

- [ ] 6 templates créés
- [ ] YAML frontmatter validé
- [ ] Dataview queries testées
- [ ] Templater snippets fonctionnels
- [ ] Documentation utilisation

---

## 📅 Timeline

**Total : 2-3h**

---

**Priorité :** Medium  
**Dépend de :** Tag Taxonomy  
**Next :** Nutrition integration