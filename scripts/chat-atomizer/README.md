# 🐍 Chat Atomizer v1.0

> Transforme les exports bruts de conversations Claude.ai en cartes atomiques Obsidian

---

## 🎯 Fonctionnalités

✅ **Parsing intelligent** - Extrait messages, frontmatter, attachments  
✅ **Cartes atomiques** - 1 fichier Markdown par message  
✅ **Navigation fluide** - Liens prev/next automatiques  
✅ **MOC auto-généré** - Map of Content avec Dataview queries  
✅ **Détection topics** - Keywords extraction automatique  
✅ **Extraction code** - Code blocks isolés avec langage  
✅ **YAML frontmatter** - Métadonnées complètes pour Obsidian  

---

## 🚀 Installation

### Prérequis

- Python 3.8+
- PyYAML

### Installation

```bash
# Cloner le repo (ou copier le script)
cd scripts/chat-atomizer/

# Installer dépendances
pip install pyyaml
```

---

## 📖 Usage

### Commande de base

```bash
python atomize_chat.py -i export.md -o vault/Chat-Exports/
```

### Arguments

```
-i, --input PATH     Chemin vers le fichier export markdown (requis)
-o, --output PATH    Dossier de sortie pour les cartes (requis)
--dry-run            Parse seulement, ne crée pas de fichiers
```

### Exemples

```bash
# Export simple
python atomize_chat.py \
  --input ~/Downloads/chat-2025-11-09.md \
  --output ~/vault/04_Resources/Chat-Exports/

# Dry run (test parsing)
python atomize_chat.py \
  -i export.md \
  -o ./test/ \
  --dry-run

# Avec chemins absolus
python atomize_chat.py \
  --input /mnt/c/Users/user/Downloads/export.md \
  --output /mnt/c/Users/user/vault/Chat-Exports/
```

---

## 📂 Structure de Sortie

```
output/
└── 2025-11-09-power-bi-tickets/
    ├── _MOC_2025-11-09-power-bi-tickets.md    # Map of Content
    └── cards/
        ├── 001_user_msg-1.md                   # Message 1 (user)
        ├── 002_assistant_msg-2.md              # Message 2 (assistant)
        ├── 003_user_msg-3.md                   # Message 3 (user)
        └── ...                                  # Tous les messages
```

---

## 🎴 Format des Cartes

### Frontmatter YAML

```yaml
---
type: chat-card
parent_export: "[[Titre Export]]"
order: 5
role: user
created: 2025-11-09T01:30:00Z
tags:
  - chat-card
  - power-bi
  - finance
attachments_count: 1
timestamp: 2025-11-09T01:05:00Z
---
```

### Contenu

```markdown
# 👤 Message 5 - User

**ID:** msg-5
**Timestamp:** 2025-11-09T01:05:00Z

## 📎 Attachments (1)

- 📷 Image: `ticket-carrefour.jpg`

## 💬 Content

[Contenu original du message...]

## 🔗 Navigation

- ⬆️ Previous: [[004_assistant_msg-4]]
- ⬇️ Next: [[006_assistant_msg-6]]
- 📊 MOC: [[_MOC_2025-11-09-power-bi-tickets]]

## 🏷️ Topics

- #finance
- #receipts
```

---

## 📊 MOC Généré

Le Map of Content contient :

### Statistiques
- Messages totaux, user, assistant
- Attachments count
- Dates export

### Queries Dataview

**Tous les messages :**
```dataview
TABLE role, order, attachments_count
FROM "cards"
WHERE type = "chat-card"
SORT order ASC
```

**Par topic :**
```dataview
TABLE count(rows) as Count
FROM "cards"
GROUP BY tags
SORT count(rows) DESC
```

**Avec attachments :**
```dataview
LIST
FROM "cards"
WHERE attachments_count > 0
```

---

## 🏷️ Détection de Topics

### Keywords par domaine

Le script détecte automatiquement :

| Topic | Keywords |
|-------|----------|
| `power-bi` | power bi, dax, measures, power query |
| `python` | python, script, def, import, pandas |
| `obsidian` | obsidian, vault, markdown, dataview |
| `finance` | ticket, receipt, transaction, budget |
| `receipts` | leclerc, carrefour, totalenergies |
| `git` | git, commit, branch, repository |
| `automation` | script, automate, workflow |

**Extensible** - Ajoute tes propres keywords dans `TopicDetector.KEYWORDS`

---

## 💻 Extraction de Code

Le script extrait automatiquement tous les code blocks :

```python
# Détecté et taggé avec langage
code_blocks = CodeExtractor.extract(content)
# → [{'id': 1, 'lang': 'python', 'content': '...'}]
```

Langages supportés : python, javascript, bash, yaml, sql, dax, etc.

---

## 🔧 Personnalisation

### Ajouter des topics

Édite le dictionnaire `TopicDetector.KEYWORDS` :

```python
KEYWORDS = {
    'power-bi': ['power bi', 'dax'],
    'ton-topic': ['keyword1', 'keyword2'],  # ← Ajoute ici
}
```

### Modifier le template de carte

Édite la méthode `AtomicCardGenerator.generate_card()` :

```python
card_content = f"""---
{yaml.dump(frontmatter)}---

# Ton template personnalisé...
"""
```

---

## 🧪 Tests

### Test parsing

```bash
# Dry run - ne crée aucun fichier
python atomize_chat.py -i export.md -o ./test/ --dry-run
```

**Sortie attendue :**
```
✅ Parsed 143 messages from export
📊 Export Statistics:
  Total messages: 143
  User: 77
  Assistant: 66
```

### Test génération

```bash
# Créer dans dossier temporaire
python atomize_chat.py -i export.md -o /tmp/test-atomize/
```

Vérifie :
- ✅ Dossier `cards/` créé
- ✅ 143 fichiers `.md` générés
- ✅ MOC créé avec queries Dataview
- ✅ Navigation prev/next fonctionnelle

---

## ⚠️ Limitations Connues

1. **Encodage** - UTF-8 uniquement (emojis OK)
2. **Parsing** - Basé sur regex (structure export doit être stricte)
3. **Topics** - Détection par keywords (pas de NLP avancé)
4. **Code** - Extraction simple (pas d'analyse syntaxique)

---

## 🚀 Roadmap

### v1.1 (À venir)
- [ ] Support ChatGPT exports
- [ ] Support Gemini exports
- [ ] Templates configurables (YAML)
- [ ] Extraction images (copy to vault)

### v1.2 (Futur)
- [ ] Groupement thématique automatique
- [ ] Génération cartes thèmes
- [ ] NLP avancé (topic modeling)
- [ ] Timeline visualisation

### v2.0 (Vision)
- [ ] GUI interface
- [ ] Batch processing
- [ ] Watch mode (auto-import)
- [ ] Obsidian plugin intégration

---

## 🐛 Troubleshooting

### Erreur: "Input file not found"

**Cause :** Chemin incorrect

**Solution :**
```bash
# Utilise chemin absolu
python atomize_chat.py -i /full/path/to/export.md -o ./output/
```

### Erreur: "No messages found"

**Cause :** Format export non reconnu

**Solution :**
- Vérifie que l'export vient bien du script v1.4
- Check les patterns de messages (## 👤 Message X)

### Les queries Dataview ne marchent pas

**Cause :** Chemin relatif incorrect

**Solution :**
- Vérifie que les cartes sont dans `cards/` sous le MOC
- Ajuste les chemins dans les queries si structure différente

---

## 📚 Ressources

- **Export Script** : `chat-exporter-v1.4-FINAL.js`
- **Template Export** : `template-chat-export-raw.md`
- **TAG_REGISTRY** : Liste des tags canoniques
- **Documentation** : `README-CHAT-EXPORTER.md`

---

## 📝 Changelog

### v1.0 - 2025-11-09
- ✅ Parsing complet exports Claude.ai
- ✅ Génération cartes atomiques
- ✅ MOC avec Dataview queries
- ✅ Navigation prev/next
- ✅ Détection topics (keywords)
- ✅ Extraction code blocks
- ✅ Support attachments
- ✅ CLI arguments

---

## ⚖️ Licence

MIT License - Utilise, modifie, distribue librement

---

## 📧 Support

**Questions ?** Crée une issue ou contacte l'auteur.

---

**Version :** 1.0  
**Date :** 2025-11-09  
**Auteur :** Moncef  
**Status :** ✅ Production Ready
