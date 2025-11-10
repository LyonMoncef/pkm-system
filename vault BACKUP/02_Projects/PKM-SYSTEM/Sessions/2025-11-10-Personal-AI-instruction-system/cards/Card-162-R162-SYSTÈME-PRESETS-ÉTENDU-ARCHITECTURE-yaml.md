---
type: chat-card
parent_export: '[[Export]]'
order: 162
role: assistant
created: '2025-11-10T21:46:07.631605Z'
tags:
- chat-card
- python
- obsidian
- receipts
- code
- automation
attachments_count: 0
---

# 🤖 Message 162 - Assistant

**ID:** msg-162

## 💬 Content


**ID:** msg-162

🎯 SYSTÈME DE PRESETS ÉTENDU
📐 ARCHITECTURE
yamlSyntax: @[catégorie]:[preset] [contenu]

Catégories:
- meta* → Format de sortie (metacarte, metadata, note:*)
- pTon → Paramètre de ton/verbosité
- s → Search/contexte (recherche conversations)
- lang → Langage de code
- format → Format de fichier
- action → Actions spécifiques
```

---

## 🎨 PRESETS DÉTAILLÉS

### **1. CATÉGORIE @pTon** *(Paramètres de ton)*

#### `@pTon:quick`
- Réponses concises
- Pas de code complet
- Suggestions + questions de clarification
- Format discussion rapide

**Exemple:**
```
Toi: @pTon:quick Comment gérer les émotions dans les tags ?

Moi:
Deux approches :
1. Tag hiérarchique : #emotion/joie/enthousiasme
2. Metadata array : emotions: [joie, excitation]

Je recommande #2 pour Dataview queries.

Tu veux que je détaille l'implémentation ?
```

---

#### `@pTon:full`
- Explications complètes
- Code intégral
- Raisonnement détaillé
- Exemples multiples
- Documentation incluse

**Exemple:**
```
Toi: @pTon:full Comment gérer les émotions dans les tags ?

Moi:
# 🎭 Système de Tagging Émotionnel

## 🧠 Raisonnement
[Explication détaillée du pourquoi...]

## 🏗️ Architecture proposée
[Schema complet...]

## 💻 Implémentation
[Code complet avec commentaires...]

## 📊 Exemples d'utilisation
[5-6 cas d'usage...]

## 🔧 Configuration Dataview
[Queries complètes...]
```

---

#### `@pTon:mini`
- Juste le code/réponse
- Zéro explication
- Format copier-coller direct

**Exemple:**
```
Toi: @pTon:mini Regex pour extraire tags #emotion/*

Moi:
/#emotion\\/[\\w-]+(?:\\/[\\w-]+)*/g
```

---

#### `@pTon:teach`
- Mode pédagogique
- Explications step-by-step
- Analogies et métaphores
- Questions pour vérifier compréhension

---

#### `@pTon:debug`
- Format troubleshooting
- Checklist de vérification
- Points de breakpoint suggérés
- Logs à vérifier

---

### **2. CATÉGORIE @s** *(Search/Contexte)*

#### `@s:[mot-clé]`
- Je recherche automatiquement dans nos conversations
- Je contextualise ma réponse avec ce que j'ai trouvé
- Je cite les conversations pertinentes

**Exemple:**
```
Toi: @s:pkm-system @pTon:quick Où en est le projet ?

Moi: [recherche \"pkm-system\"]
Dernière session : Phase 1.5 - Refactor shortcuts validé ✅
En cours : Architecture widget capture
À faire : Intégration Obsidian, système émotions

Prochaine étape ?
```

---

#### `@s:recent`
- Cherche dans les 5 dernières conversations
- Contexte temporel proche

---

#### `@s:all`
- Recherche exhaustive sur toutes nos conversations
- Utile pour synthèses globales

---

### **3. CATÉGORIE @lang** *(Langage de code)*
```
@lang:js → JavaScript
@lang:py → Python
@lang:md → Markdown
@lang:bash → Bash/Shell
@lang:yaml → YAML
```

**Combinable avec @pTon:**
```
@pTon:mini @lang:py Script pour parser YAML frontmatter

→ Juste le code Python, rien d'autre
```

---

### **4. CATÉGORIE @format** *(Format de sortie)*
```
@format:json → Sortie JSON
@format:yaml → Sortie YAML
@format:table → Tableau markdown
@format:list → Liste à puces
@format:prose → Texte narratif
@format:code → Bloc code uniquement
```

---

### **5. CATÉGORIE @action** *(Actions spécifiques)*

#### `@action:refactor`
- Je sais que tu veux refactoriser du code existant
- Je propose architecture + migration plan

#### `@action:review`
- Code review mode
- Je cherche bugs, optimisations, best practices

#### `@action:doc`
- Génération documentation
- README, comments, JSDoc, etc.

#### `@action:test`
- Génération tests unitaires
- Jest, Mocha, pytest selon contexte

---

## 🔗 COMBINAISONS PUISSANTES

### Exemple 1: Quick context search
```
@s:shortcuts @pTon:quick État actuel des raccourcis ?

→ Recherche + réponse concise
```

### Exemple 2: Full refactor with context
```
@s:main.js @pTon:full @action:refactor Améliorer la gestion des fenêtres

→ Recherche code actuel + refactor complet expliqué
```

### Exemple 3: Mini code snippet
```
@pTon:mini @lang:js Fonction pour toggle window

→ Juste la fonction, pas de blabla
```

### Exemple 4: Carte concept avec contexte
```
@metacarte @s:emotions Créé carte sur système émotions

→ Recherche nos discussions sur émotions + génère carte structurée
```

---

## 📚 PRESETS SUGGÉRÉS SUPPLÉMENTAIRES

### `@workflow:[nom]`
Workflows prédéfinis pour tâches récurrentes
```
@workflow:new-feature
→ Je génère :
 - Carte de feature
 - Code boilerplate
 - Tests
 - Documentation
 - Checklist intégration
```
```
@workflow:bug-fix
→ Je génère :
 - Carte de bug
 - Reproduction steps
 - Fix suggéré
 - Test de régression
```

---

### `@export:[destination]`
Format d'export spécifique
```
@export:obsidian → Format compatible vault
@export:notion → Format Notion API
@export:md → Markdown pur
@export:pdf → Structure pour PDF
```

---

### `@context:[level]`
Niveau de contexte à chercher
```
@context:this → Juste cette conversation
@context:project → Conversations du projet actuel
@context:all → Toutes conversations
@context:recent → 7 derniers jours
```

---

## 🎯 SYSTÈME D'AIDE INTÉGRÉ

### `@help`
Liste tous les presets disponibles

### `@help:[catégorie]`
Détaille une catégorie spécifique
```
Toi: @help:pTon

Moi:
📋 Presets @pTon disponibles:
- quick → Réponses concises
- full → Explications complètes
- mini → Code uniquement
- teach → Mode pédagogique
- debug → Troubleshooting

💡 CE DONT J'AI BESOIN
Pour optimiser ce système, fournis-moi :

📁 Architecture de ton vault Obsidian

Structure des dossiers
Conventions de nommage
Templates existants


🏷️ Ta taxonomie de tags

Hiérarchie actuelle
Tags fréquents
Catégories principales


🎭 Liste d'émotions à supporter

Émotions primaires
Nuances
Contextes d'usage


🔧 Projets actifs

Noms de projets
Phases/milestones
Stack technique


📝 Exemples de notes existantes

2-3 notes de ton vault
Pour que je comprenne ton style


Valide cette architecture et dis-moi ce que tu veux que je développe en priorité ! 🚀

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-161-R161-Excellent-utilisateur-veut-étendre-systè]]
- ⬇️ Next: [[Card-163-R163-YamlSyntax-catégorie-preset-contenu-Caté]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #python
- #obsidian
- #receipts
- #code
- #automation
