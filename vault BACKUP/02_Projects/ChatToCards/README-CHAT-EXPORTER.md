# 💬 Chat Exporter v1.4 - Documentation

> Export tes conversations Claude.ai vers Obsidian en un clic !

---

## 🎯 Vue d'ensemble

**Chat Exporter** est un script JavaScript qui s'exécute dans la console du navigateur pour extraire et formater tes conversations Claude.ai en fichiers Markdown compatibles Obsidian.

### Fonctionnalités

✅ **Export complet** - Tous les messages (user + assistant)  
✅ **Détection intelligente** - Distingue automatiquement user vs assistant  
✅ **YAML frontmatter** - Métadonnées structurées pour Obsidian  
✅ **Attachments tracking** - Détecte les images/fichiers  
✅ **Debug mode** - Logs détaillés pour troubleshooting  
✅ **Zero config** - Copie-colle et c'est tout

---

## 🚀 Quick Start

### 1. Ouvre la console

Sur la page de conversation Claude.ai :

- **Windows/Linux:** `F12` ou `Ctrl + Shift + J`
- **Mac:** `Cmd + Option + J`

### 2. Colle le script

Copie TOUT le contenu de `chat-exporter-v1.4-FINAL.js` et colle-le dans la console.

### 3. Appuie sur Entrée

Le script s'exécute automatiquement et copie le markdown dans ton clipboard.

### 4. Crée la note Obsidian

Dans ton vault Obsidian :

1. Crée un nouveau fichier : `04_Resources/Chat-Exports/YYYY-MM-DD-titre.md`
2. Colle le contenu (`Ctrl+V` / `Cmd+V`)
3. Sauvegarde

**C'est tout ! 🎉**

---

## 📊 Format de Sortie

### Frontmatter YAML

```yaml
---
type: chat-export
status: raw
chat_id: 2d8f02e5-487d-464e-9d08-5a34658b28bc
title: "Titre de la conversation"
created: 2025-11-09T01:15:30.152Z
exported: 2025-11-09T01:15:30.152Z
platform: claude.ai
url: https://claude.ai/chat/xxx
messages_count: 143
user_messages: 77
assistant_messages: 66
attachments_count: 9
tags:
  - chat-card
  - export
  - raw
---
```

### Structure des messages

```markdown
## 👤 Message 1 - User

**ID:** msg-1
**Timestamp:** 2025-11-09T01:00:00Z

[Contenu du message]

---

## 🤖 Message 2 - Assistant

**ID:** msg-2

[Contenu de la réponse]

---
```

---

## 🔧 Configuration

### Variables modifiables

Dans le script, tu peux ajuster :

```javascript
const ChatExporter = {
  DEBUG: true,  // false pour désactiver les logs
  // ...
}
```

### Filtres personnalisés

Pour exclure certains messages :

```javascript
// Dans getMessages(), après extraction
messages = messages.filter(msg => 
  msg.content.length > 50  // Minimum 50 caractères
);
```

---

## 🐛 Troubleshooting

### Problème : Tous les messages détectés comme "assistant"

**Solution :** Active le mode DEBUG et regarde les logs de la console :

```javascript
const ChatExporter = {
  DEBUG: true,  // ← Met true
  // ...
}
```

Cherche dans les logs :

```
🔍 INSPECTION DOM:
📊 Top 10 des patterns de classes:
🏷️ Data attributes trouvés:
```

Copie ces infos et crée une issue.

### Problème : Aucun message trouvé

**Cause probable :** La structure DOM de Claude.ai a changé.

**Solution :**

1. Vérifie que tu es bien sur une page de conversation
2. Scroll jusqu'au début de la conversation
3. Réessaye le script
4. Si ça persiste, vérifie les logs debug

### Problème : Caractères bizarres dans le markdown

**Cause :** Problème d'encodage UTF-8.

**Solution :** Dans le script, assure-toi que :

```javascript
navigator.clipboard.writeText(text)  // Gère automatiquement UTF-8
```

---

## 📁 Structure de Fichiers

```
scripts/chat-exporter/
├── chat-exporter-v1.4-FINAL.js    # Script principal
├── README.md                       # Cette doc
├── CHANGELOG.md                    # Historique versions
└── examples/
    └── export-example.md           # Exemple d'export
```

---

## 🔄 Workflow Complet

### 1. Export (ce script)

```bash
# Console Browser
chat-exporter-v1.4-FINAL.js
→ Copie markdown dans clipboard
```

### 2. Import Obsidian

```bash
# Vault Obsidian
04_Resources/Chat-Exports/2025-11-09-conversation.md
→ Colle le contenu
```

### 3. Atomisation (futur script Python)

```bash
# Terminal
python atomize_chat.py --input export.md
→ Génère cartes atomiques + MOC
```

### 4. Exploitation

```bash
# Obsidian
- Recherche Dataview
- Liens bidirectionnels
- Tags canoniques
- MOC de sessions
```

---

## 🎨 Templates Disponibles

### Template Export Raw

- `template-chat-export-raw.md` - Structure de base

### Template Carte Atomique

- À venir avec le script Python d'atomisation

### Template MOC Session

- À venir avec le script Python d'atomisation

---

## 🔐 Sécurité & Vie Privée

### Le script :

- ✅ S'exécute **uniquement localement** (dans TON navigateur)
- ✅ **Aucune donnée envoyée** sur internet
- ✅ **Aucun tracking**
- ✅ **Open source** (tu peux lire le code)

### Données exportées :

- ⚠️ Contiennent TOUT le texte de la conversation
- ⚠️ Conservées **localement** dans ton vault Obsidian
- ⚠️ À toi de sécuriser ton vault (encryption, backup)

---

## 🚀 Roadmap

### v1.4 (Actuel) ✅

- [x] Export complet user + assistant
- [x] Détection intelligente des rôles
- [x] YAML frontmatter structuré
- [x] Debug mode avec inspection DOM

### v1.5 (À venir)

- [ ] Support ChatGPT
- [ ] Support Gemini
- [ ] Extraction automatique des code blocks
- [ ] Détection des topics

### v2.0 (Futur)

- [ ] Extension Chrome
- [ ] Auto-export périodique
- [ ] Sync direct avec Obsidian
- [ ] API integration

---

## 🤝 Contribuer

### Rapporter un bug

Crée une issue avec :

1. **Version** : v1.4
2. **Plateforme** : Claude.ai / ChatGPT / Gemini
3. **Problème** : Description + logs debug
4. **Attendu** : Ce qui devrait se passer

### Proposer une amélioration

1. Fork le repo
2. Crée une branche : `feature/nouvelle-fonction`
3. Code + tests
4. Pull request avec description claire

---

## 📚 Ressources

- **TAG_REGISTRY.md** - Tags canoniques Obsidian
- **Template Chat Export Raw** - Structure des exports
- **TASK-atomize-chat-script.md** - Specs du script Python

---

## 📝 Changelog

### v1.4 - 2025-11-09

- ✅ Détection user/assistant fiable
- ✅ Inspection DOM détaillée
- ✅ Multi-stratégies de détection
- ✅ Logs debug complets
- ✅ Support attachments

### v1.3 - 2025-11-08

- Amélioration détection
- Ajout logs debug

### v1.2 - 2025-11-08

- Tentative fix détection

### v1.0-1.1 - 2025-11-08

- Version initiale

---

## ⚖️ Licence

**MIT License**

Tu peux utiliser, modifier, distribuer librement ce script.

---

## 📧 Contact

**Questions ?** Ouvre une issue ou contacte l'auteur.

---

**Dernière mise à jour :** 2025-11-09 **Version :** 1.4 **Status :** ✅ Production Ready