---
type: chat-card
parent_export: '[[Export]]'
order: 934
role: assistant
created: '2025-11-10T21:46:18.657924Z'
tags:
- chat-card
- git
attachments_count: 0
---

# 🤖 Message 934 - Assistant

**ID:** msg-934

## 💬 Content


**ID:** msg-934

bash# 1. Voir ce qui a changé (sans rien toucher)
git fetch origin
git log main..origin/main --oneline

# 2. Si tu veux voir les diffs détaillés
git diff main origin/main

# 3. Pull avec rebase (propre)
git pull --rebase origin main

# 4. Si conflit → Résous (voir ci-dessus)

# 5. Push
git push origin main

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-933-R933-Bashgit-push-origin-main]]
- ⬇️ Next: [[Card-935-R935-Bash-Sauvegarder-état-actuel-branch]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #git
