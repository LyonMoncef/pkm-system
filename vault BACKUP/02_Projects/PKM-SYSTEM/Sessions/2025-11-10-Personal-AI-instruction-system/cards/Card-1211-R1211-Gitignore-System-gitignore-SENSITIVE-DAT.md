---
type: chat-card
parent_export: '[[Export]]'
order: 1211
role: assistant
created: '2025-11-10T21:46:22.048062Z'
tags:
- chat-card
- obsidian
- git
attachments_count: 0
---

# 🤖 Message 1211 - Assistant

**ID:** msg-1211

## 💬 Content


**ID:** msg-1211

gitignore# ===================================
# PKM System - .gitignore
# ===================================

# ====================
# SENSITIVE DATA (NEVER COMMIT!)
# ====================
.env
.env.local
.env.production
config.json
nas-config.json
*.key
*.pem
credentials/
secrets/
api-keys/

# ====================
# PERSONAL NOTES & VAULT
# ====================

# Ignorer tout le vault par défaut
vault/*
notes/
*.md.backup

# EXCEPTIONS: Fichiers système critiques à versionner
!vault/06_Meta/
vault/06_Meta/*
!vault/06_Meta/TAG_REGISTRY.md
!vault/06_Meta/Claude-Instructions.md

!vault/04_Resources/
vault/04_Resources/*
!vault/04_Resources/Templates/
!vault/04_Resources/Templates/**

# Obsidian workspace (personnel)
.obsidian/workspace*
.obsidian/workspace.json
.obsidian/workspaces.json

# Keep template structure but ignore content
!vault/.gitkeep
!notes/.gitkeep

# ====================
# USER DATA
# ====================
data/
exports/personal/
backups/
*.db
*.sqlite

# ====================
# NODE / NPM
# ====================
node_modules/
npm-debug.log
yarn-error.log
package-lock.json
yarn.lock
.pnpm-debug.log

# ====================
# BUILD OUTPUTS
# ====================
dist/
build/
out/
.next/
*.log
coverage/

# ====================
# OS FILES
# ====================
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db
Desktop.ini

# ====================
# IDEs & EDITORS
# ====================
.vscode/
!.vscode/extensions.json
!.vscode/settings.json.example
.idea/
*.swp
*.swo
*~
.project
.classpath
.c9/
*.launch
.settings/
*.sublime-workspace

# ====================
# TEMPORARY FILES
# ====================
tmp/
temp/
*.tmp
*.bak
*.cache
.cache/

# ====================
# ELECTRON
# ====================
electron-builder.yml
dist_electron/

# ====================
# TESTING
# ====================
.nyc_output/
coverage/
*.lcov

# ====================
# MISC
# ====================
.env.test
.vercel
.turbo

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-1210-R1210-Gitignore-COMPLET-AVEC-EXCEPTIONS-VAULT]]
- ⬇️ Next: [[Card-1212-R1212-Bashcd-system-Remplacer-gitignore-nvim]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #obsidian
- #git
