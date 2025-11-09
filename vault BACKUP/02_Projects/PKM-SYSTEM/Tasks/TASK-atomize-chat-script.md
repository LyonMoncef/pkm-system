---

type: task created: 2025-11-09T01:30:00Z priority: high status: backlog project: pkm-system tags:

- task-list
- python
- automation
- chat-export
- pkm-system estimate: 4h

---

# 🐍 Script Python - Atomisation Chat Exports

## 📋 Description

Créer un script Python qui transforme les exports bruts de conversations Claude.ai en cartes atomiques Obsidian liées.

## 🎯 Objectif

**Input:** Fichier markdown d'export complet (143 messages) **Output:**

- Cartes atomiques individuelles par message/thème
- MOC (Map of Content) de la session
- Tags canoniques appliqués
- Liens bidirectionnels créés

## ✅ Fonctionnalités Requises

### Phase 1: Parsing

- [ ] Parser le frontmatter YAML de l'export
- [ ] Extraire les messages individuels (user + assistant)
- [ ] Détecter les attachments
- [ ] Identifier les thèmes/sujets abordés

### Phase 2: Génération Cartes Atomiques

- [ ] Créer une carte par message significatif (>200 chars)
- [ ] Générer frontmatter avec tags canoniques
- [ ] Créer liens vers messages liés (contexte)
- [ ] Nommer les fichiers intelligemment (date-ordre-sujet)

### Phase 3: MOC Génération

- [ ] Créer le MOC de la session
- [ ] Lister tous les messages avec liens
- [ ] Ajouter statistiques (dataview)
- [ ] Créer timeline de la conversation

### Phase 4: Intelligence

- [ ] Détection automatique des sujets (NLP basique)
- [ ] Groupement messages par thème
- [ ] Suggestions de tags supplémentaires
- [ ] Détection de code/commandes à extraire

## 📂 Structure de Sortie

```
vault/04_Resources/Chat-Exports/
├── 2025-11-09-power-bi-tickets/
│   ├── _MOC_2025-11-09-power-bi-tickets.md
│   ├── 01-user-demande-extraction-tickets.md
│   ├── 02-assistant-json-structure.md
│   ├── 03-user-ticket-totalenergies.md
│   ├── 04-assistant-csv-export.md
│   └── ...
```

## 🔧 Stack Technique

- **Python 3.11+**
- **Libraries:**
    - `pyyaml` - Parser YAML
    - `frontmatter` - Gérer frontmatter
    - `pathlib` - Gestion fichiers
    - `re` - Regex
    - `nltk` ou `spacy` - NLP (optionnel Phase 4)

## 📝 Template Carte Atomique

```yaml
---
type: chat-card
parent_export: "[[2025-11-09-power-bi-tickets]]"
order: 1
role: user|assistant
created: 2025-11-09T01:00:00Z
tags:
  - chat-card
  - {{topic}}
attachments: 0
---

# {{emoji}} Message {{order}} - {{role}}

{{content}}

## 🔗 Liens
- ⬆️ Précédent: [[message-precedent]]
- ⬇️ Suivant: [[message-suivant]]
- 📊 MOC: [[_MOC_session]]
```

## 🎯 Utilisation

```bash
python atomize_chat.py \
  --input "path/to/export.md" \
  --output "vault/04_Resources/Chat-Exports/" \
  --min-length 200 \
  --create-moc \
  --apply-tags
```

## 🧪 Tests à Prévoir

- [ ] Export avec 10 messages
- [ ] Export avec attachments
- [ ] Export avec code blocks
- [ ] Export très long (500+ messages)
- [ ] Gestion caractères spéciaux
- [ ] Gestion doublons

## 📚 Références

- [[Template Chat Export Raw]]
- [[TAG_REGISTRY]]
- [[MOC - PKM System]]
- Documentation frontmatter Python

## 🎯 Success Criteria

1. ✅ Script génère cartes valides Obsidian
2. ✅ Tous les liens sont valides
3. ✅ Tags canoniques appliqués
4. ✅ MOC contient toutes les cartes
5. ✅ Structure dossiers respectée
6. ✅ Pas de perte d'information

## 📅 Timeline

- **Phase 1 (Parsing):** 1h
- **Phase 2 (Cartes):** 2h
- **Phase 3 (MOC):** 1h
- **Phase 4 (Intelligence):** 2h (optionnel)

**Total estimé:** 4h (core) + 2h (bonus)

---

**Priority:** 🟠 High **Status:** 📋 Backlog **Project:** [[PKM System]] **Related:** [[Chat Exporter v1.4]], [[Template Chat Export Raw]]