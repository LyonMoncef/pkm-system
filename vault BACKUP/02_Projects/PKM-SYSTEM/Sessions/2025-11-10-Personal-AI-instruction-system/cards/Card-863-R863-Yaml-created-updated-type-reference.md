---
type: chat-card
parent_export: '[[Export]]'
order: 863
role: assistant
created: '2025-11-10T21:46:17.713122Z'
tags:
- chat-card
- code
- git
- automation
attachments_count: 0
---

# 🤖 Message 863 - Assistant

**ID:** msg-863

## 💬 Content


**ID:** msg-863

yaml---
created: 2025-11-02T21:00:00
updated: 2025-11-02T21:00:00
type: reference
tags: [reference, git, aliases, zsh, bash, shortcuts]
related:
 - \"[[MOC - Git Workflows]]\"
 - \"[[Bash Aliases]]\"
---

# 🔗 Git Aliases

> **Aliases ZSH/Bash** - Raccourcis Git personnalisés

## 📋 Aliases Actifs

### Commit & Push

**`comt \"message\"`**
```bash
git add -A && git commit -m \"message\" && git push
```
**Usage:** Commit rapide tout-en-un

---

### Status & Info

**`gs`**
```bash
git status
```

**`gl`**
```bash
git log --oneline --graph --decorate -10
```

**`gd`**
```bash
git diff
```

---

## 🔧 Configuration

**Fichier:** `~/.zshrc` ou `~/.bashrc`
```bash
# Git aliases
alias comt='git add -A && git commit -m \"$1\" && git push'
alias gs='git status'
alias gl='git log --oneline --graph --decorate -10'
alias gd='git diff'
```

---

## 🔗 Liens

- [[MOC - Git Workflows]]
- [[Bash Aliases]]

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-862-R862-Yaml-created-YYYY-DDTHH-updated]]
- ⬇️ Next: [[Card-864-R864-Mermaidgraph-Début-Système-Presets-metac]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #code
- #git
- #automation
