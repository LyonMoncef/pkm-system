# 📋 Guide - Générateur de Cartes Obsidian

## 🎯 Vue d'Ensemble

Ce script génère des **cartes atomiques Obsidian** à partir d'un chat export Claude.ai.

### Fonctionnalités

✅ **Métadonnées complètes** (frontmatter YAML)  
✅ **Tags canoniques** (selon TAG_REGISTRY.md)  
✅ **Navigation inter-cartes** (← prev | ↑ MOC | next →)  
✅ **MOC de session** automatique  
✅ **Titres temporaires** (facilement renommables)  
✅ **Détection automatique** des tags pertinents

---

## 🚀 Utilisation

### 1. Prérequis

```bash
# Assure-toi d'avoir :
- Python 3.6+
- Le fichier export_conv.md
- Accès au vault Obsidian
```

### 2. Configuration

**Modifie les chemins dans le script** (lignes 18-20) :

```python
BASE_PATH = Path("/mnt/c/Users/idsmf/Projects/pkm-system/vault BACKUP")
EXPORT_FILE = Path("/mnt/c/Users/idsmf/Projects/pkm-system/export_conv.md")
```

### 3. Lancement

```bash
cd /mnt/c/Users/idsmf/Projects/pkm-system
python3 generate_obsidian_cards.py
```

### 4. Options Disponibles

```
1. DRY RUN - Aperçu détaillé (pas de création)
2. CRÉER 5 premières cartes (test)
3. CRÉER 10 premières cartes
4. CRÉER TOUTES les cartes (106 messages)
5. Annuler
```

**Conseil** : Commence par option **1** (dry run) ou **2** (5 cartes test) !

---

## 📁 Structure Créée

```
vault BACKUP/
└── 02_Projects/
    └── Finances-Personnelles-EUR/
        └── Sessions/
            └── 2025-11-05-PowerBI-Tickets/
                ├── MOC-Session-2025-11-05-PowerBI-Tickets.md
                └── Cards/
                    ├── Card-001-Q001-Question-Extraction-Tickets.md
                    ├── Card-002-R002-Reponse-Structure-JSON.md
                    ├── Card-003-Q003-Question-User.md
                    └── ... (jusqu'à 106 cartes)
```

---

## 🔄 Renommer les Cartes (Après Création)

### Option A : Renommage Manuel dans Obsidian

1. Ouvre la carte dans Obsidian
2. `Ctrl+P` → "Rename this file"
3. Change le nom : `Card-001-Q001-Question-Extraction-Tickets.md`  
   → `Card-001-Extraction-Tickets-Caisse.md`
4. Obsidian met à jour automatiquement tous les liens !

### Option B : Script de Renommage en Batch

Si tu veux renommer **plusieurs cartes** d'un coup, je peux te faire un script Python qui :

1. Lit une liste `renames.txt` :
   ```
   Card-001 → Extraction-Tickets-Caisse
   Card-002 → Structure-JSON-Leclerc
   Card-003 → Question-Format-Donnees
   ```

2. Renomme les fichiers
3. Met à jour tous les liens dans le MOC et les autres cartes

**Veux-tu ce script de renommage ?**

---

## 🏷️ Tags Générés Automatiquement

Le script détecte automatiquement les tags selon le contenu :

| Contenu | Tags Ajoutés |
|---------|-------------|
| "ticket", "caisse", "reçu" | `receipt`, `expense` |
| "comptabilité", "budget" | `compta` |
| "python", code Python | `python` |
| "json", code JSON | `export` |
| "power bi", "dax" | `powerbi` |

**Tous les messages** reçoivent le tag `chat-card`.

---

## 🎨 Exemple de Carte Générée

```markdown
---
created: 2025-11-05T19:30:00
updated: 2025-11-05T19:30:00
type: chat-card
chat_message_id: msg-36
chat_message_number: 36
role: user
session: [[MOC-Session-2025-11-05-PowerBI-Tickets]]
tags: [chat-card, receipt, expense]
attachments: 1
---

# Card-001-Q001-Question-Extraction-Tickets

[[MOC-Session-2025-11-05-PowerBI-Tickets|↑ Session]] | [[Card-002]] →

---

J'ai des photos de tickets de caisse,
Tu es capable de m'extraire une table avec chaque article, 
et son montant, Avec les autres infos comme le total, 
la tva si elle y est, le nom de l'enseigne etc....

Faut que ce soit un format exploitable rapidement pour 
analyse via excel ou coda ou en python, bref un csv ou 
json avec le plus d'informations possible...

---

**Card 1/10** | Message #36 | Role: user
```

---

## ✅ Checklist Post-Génération

Après avoir créé les cartes :

- [ ] Vérifier l'aperçu dans Obsidian
- [ ] Tester la navigation entre cartes
- [ ] Vérifier le MOC de session
- [ ] Renommer 2-3 cartes pour tester
- [ ] Valider les tags automatiques
- [ ] Ajuster les tags manuellement si besoin
- [ ] Commit Git !

---

## 🆘 Problèmes Courants

### Les liens ne fonctionnent pas

→ Vérifie que les cartes sont bien dans `Cards/`  
→ Vérifie que le MOC est au niveau de `Sessions/`

### Les tags ne s'affichent pas

→ Les tags sont dans le frontmatter YAML  
→ Utilise la vue "Tags" d'Obsidian pour les voir

### Je veux modifier la structure

→ Édite les constantes en haut du script :
```python
PROJECT_NAME = "Finances-Personnelles-EUR"
SESSION_NAME = "2025-11-05-PowerBI-Tickets"
```

---

## 🎯 Prochaines Étapes Suggérées

1. **Générer 5 cartes** (mode test)
2. **Valider** la structure dans Obsidian
3. **Renommer** les 2-3 premières cartes
4. **Générer le reste** (toutes les cartes)
5. **Créer des liens** entre concepts
6. **Ajouter au MOC principal** du projet Finance

---

**Questions ? Besoin du script de renommage en batch ?**  
Demande à Claude ! 🚀
