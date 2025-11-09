---

# === IDENTIFICATION ===

type: chat-export status: raw chat_id: {{CHAT_ID}} title: "{{TITRE}}"

# === DATES ===

created: {{date:YYYY-MM-DDTHH:mm:ss}}Z exported: {{date:YYYY-MM-DDTHH:mm:ss}}Z date_start: unknown date_end: unknown

# === SOURCE ===

platform: claude.ai url: https://claude.ai/chat/{{CHAT_ID}}

# === STATISTIQUES ===

messages_count: {{TOTAL_MESSAGES}} user_messages: {{USER_COUNT}} assistant_messages: {{ASSISTANT_COUNT}} attachments_count: {{ATTACHMENTS}} participants: [user, assistant]

# === TAGS CANONIQUES ===

tags:

- chat-card
- export
- raw
- archive
- resource

# === SUJETS ABORDÉS ===

topics:

- {{TOPIC_1}}
- {{TOPIC_2}}
- {{TOPIC_3}}

# === WORKFLOW ===

atomized: false moc_created: false linked_moc: "[[MOC - {{TITRE_MOC}}]]"

# === MÉTADONNÉES PKM ===

processed: false priority: medium quality: high

# === ALIASES ===

aliases:

- "Chat {{date:YYYY-MM-DD}} - {{TITRE_COURT}}"

---

# 💬 {{TITRE}}

> [!info] Informations de l'export
> 
> - **Plateforme** : {{platform}}
> - **Exporté le** : {{exported}}
> - **Messages** : {{messages_count}} ({{user_messages}} user, {{assistant_messages}} assistant)
> - **Attachments** : {{attachments_count}}
> - **URL** : [Voir sur Claude.ai](https://claude.ai/chat/%7B%7Burl%7D%7D)

---

## 📊 Vue d'ensemble

```dataview
TABLE WITHOUT ID
  "Messages totaux" as "Métrique",
  messages_count as "Valeur"
FROM "{{current_file}}"
WHERE file.name = this.file.name
```

### Statistiques rapides

|Métrique|Valeur|
|---|---|
|👤 Messages User|{{user_messages}}|
|🤖 Messages Assistant|{{assistant_messages}}|
|📎 Attachments|{{attachments_count}}|
|📅 Date export|{{exported}}|

---

## 🗂️ Organisation

### Liens connexes

- **MOC** : {{linked_moc}}
- **Projet** : [[]]
- **Ressources** : [[]]

### Sujets traités

```dataview
LIST
FROM #chat-card
WHERE contains(file.name, "{{CHAT_ID}}")
AND file.name != this.file.name
```

---

## 📝 Contenu Exporté

{{CONTENU_COMPLET_ICI}}

---

## 🔄 Actions à faire

- [ ] Créer le MOC de la conversation
- [ ] Atomiser en cartes individuelles
- [ ] Lier aux ressources pertinentes
- [ ] Ajouter aux projets concernés
- [ ] Mettre à jour les topics

---

## 📎 Métadonnées Export

- **Total Messages** : {{messages_count}}
- **User Messages** : {{user_messages}}
- **Assistant Messages** : {{assistant_messages}}
- **Attachments** : {{attachments_count}}
- **Export Date** : {{exported}}
- **Platform** : {{platform}}
- **Original URL** : {{url}}

---

**Créé** : {{created}} | **Exporté** : {{exported}} | **Status** : {{status}}