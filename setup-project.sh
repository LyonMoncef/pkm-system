#!/bin/bash

# ===================================
# PKM System - Project Setup Script
# ===================================

echo "🧠 PKM System - Setting up project structure..."
echo ""

# Create main directories
echo "📁 Creating directory structure..."

mkdir -p widget/src
mkdir -p widget/assets/icons
mkdir -p scripts/setup
mkdir -p scripts/sync
mkdir -p scripts/export
mkdir -p scripts/automation
mkdir -p obsidian/templates
mkdir -p obsidian/plugins-config
mkdir -p obsidian/dataview-queries
mkdir -p docs/screenshots
mkdir -p config
mkdir -p vault/00_Inbox
mkdir -p vault/01_Journal
mkdir -p vault/02_Projects
mkdir -p vault/03_Areas/Santé
mkdir -p vault/03_Areas/Finance
mkdir -p vault/03_Areas/Pro
mkdir -p vault/03_Areas/Perso
mkdir -p vault/04_Resources
mkdir -p vault/05_Archives
mkdir -p vault/06_Meta

# Create .gitkeep files for empty directories
find . -type d -empty -exec touch {}/.gitkeep \;

# Create config examples
echo "⚙️  Creating config examples..."

cat > config/.env.example << 'EOF'
# NAS Configuration (DO NOT COMMIT REAL VALUES)
NAS_HOST=your-nas-ip-or-domain
NAS_PORT=5000
NAS_PROTOCOL=https
NAS_USERNAME=your-username
NAS_VAULT_PATH=/volume1/PKM_Vault

# API Keys (DO NOT COMMIT REAL KEYS)
OPENAI_API_KEY=sk-your-key-here
ANTHROPIC_API_KEY=sk-ant-your-key-here

# Widget Configuration
WIDGET_HOTKEY=CommandOrControl+Shift+Space
WIDGET_AUTOSAVE_INTERVAL=5000
WIDGET_OPACITY=0.95

# Sync Configuration
SYNC_INTERVAL=300000
SYNC_ENABLED=true

# Development
DEV_MODE=false
LOG_LEVEL=info
EOF

cat > config/config.example.json << 'EOF'
{
  "app": {
    "name": "PKM System Widget",
    "version": "0.1.0",
    "author": "Moncef Lyon"
  },
  "paths": {
    "vault": "/path/to/your/obsidian/vault",
    "inbox": "00_Inbox",
    "exports": "/path/to/exports"
  },
  "widget": {
    "hotkey": "CommandOrControl+Shift+Space",
    "defaultOpacity": 0.95,
    "alwaysOnTop": true,
    "frameless": true,
    "startMinimized": false
  },
  "editor": {
    "theme": "dark",
    "fontSize": 14,
    "fontFamily": "Monaco, Courier New, monospace",
    "autosave": true,
    "autosaveInterval": 5000
  }
}
EOF

# Create widget package.json
echo "📦 Creating widget package.json..."

cat > widget/package.json << 'EOF'
{
  "name": "pkm-widget",
  "version": "0.1.0",
  "description": "Quick capture widget for PKM System",
  "main": "src/index.html",
  "scripts": {
    "start": "echo 'Widget ready! Open src/index.html in your browser'"
  },
  "keywords": ["pkm", "knowledge-management", "note-taking"],
  "author": "Moncef Lyon",
  "license": "AGPL-3.0"
}
EOF

# Create basic widget structure
echo "🎨 Creating widget files..."

cat > widget/src/index.html << 'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PKM Widget - Quick Capture</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="widget-container">
        <h1>🧠 PKM Quick Capture</h1>
        <p>Coming soon...</p>
    </div>
    <script src="app.js"></script>
</body>
</html>
EOF

cat > widget/src/styles.css << 'EOF'
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Monaco', 'Courier New', monospace;
    background: #1a1a2e;
    color: #eee;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
}

.widget-container {
    text-align: center;
    padding: 40px;
}

h1 {
    font-size: 2rem;
    margin-bottom: 20px;
}
EOF

cat > widget/src/app.js << 'EOF'
console.log('🧠 PKM Widget loaded!');
EOF

# Create documentation files
echo "📝 Creating documentation..."

cat > docs/SETUP.md << 'EOF'
# Setup Guide

## Quick Start

1. Clone the repository
2. Install Obsidian
3. Point Obsidian to the `vault/` directory
4. Open `widget/src/index.html` in your browser

More details coming soon...
EOF

cat > docs/ARCHITECTURE.md << 'EOF'
# Architecture

Documentation coming soon...
EOF

cat > docs/CONTRIBUTING.md << 'EOF'
# Contributing

Thank you for your interest in contributing to PKM System!

Guidelines coming soon...
EOF

# Create Obsidian templates
echo "📋 Creating Obsidian templates..."

cat > obsidian/templates/daily-note.md << 'EOF'
---
date: {{date}}
tags: #daily
---

# {{date:YYYY-MM-DD}}

## 📝 Notes

## ✅ Tasks

## 💡 Ideas

## 🔗 Links
EOF

cat > obsidian/templates/project.md << 'EOF'
---
title: 
status: planning
tags: #project
created: {{date}}
---

# {{title}}

## 🎯 Objective

## 📋 Tasks

## 🗓️ Timeline

## 🔗 Resources
EOF

echo ""
echo "✅ Project structure created successfully!"
echo ""
echo "📂 Directory structure:"
tree -L 2 -I 'node_modules' 2>/dev/null || find . -type d -maxdepth 2 | sed 's|^\./||' | grep -v '^\.$'
echo ""
echo "🚀 Next steps:"
echo "   1. Review the created files"
echo "   2. Copy config/.env.example to .env and fill in your values"
echo "   3. Initialize git: git init"
echo "   4. Make your first commit!"
echo ""
echo "💡 Tip: Check README.md for full setup instructions"
echo ""
