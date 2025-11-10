---
type: chat-card
parent_export: '[[Export]]'
order: 1670
role: assistant
created: '2025-11-10T21:46:27.344430Z'
tags:
- chat-card
- python
- obsidian
- code
- automation
attachments_count: 0
---

# 🤖 Message 1670 - Assistant

**ID:** msg-1670

## 💬 Content


**ID:** msg-1670

bashpython scripts/generate-context.py --scope full
```

**Output:** Markdown avec:
- Structure vault actuelle
- Tags extraits de TAG_REGISTRY
- Notes récentes
- État tasks

**Avantages:**
- Toujours synchronisé
- Automatique

**Inconvénients:**
- Faut dev le script
- Maintenance

---

### **Option D: Hybrid (RECOMMANDÉ)** ⭐⭐⭐⭐⭐

**Combinaison A + B:**

1. **CONTEXT.md maintained** dans vault
2. **Upload au début session:** CONTEXT.md + TAG_REGISTRY.md
3. **Use conversation_search** pour décisions passées
4. **Prompt structuré** pour task du jour

**Process:**
```
Nouvelle session:
1. Upload CONTEXT.md
2. Upload TAG_REGISTRY.md
3. Prompt: \"Context uploaded. Task: [X]. Reference: [Chat Y si besoin]\"
4. Je lis les docs
5. On démarre avec le bon contexte

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-1669-R1669-Markdown-Context-System-Phase-Refactor]]
- ⬇️ Next: [[Card-1671-R1671-Bashnvim-vault-CONTEXT-Copier-template]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #python
- #obsidian
- #code
- #automation
