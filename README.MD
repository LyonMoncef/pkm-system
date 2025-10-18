# 🧠 PKM System

> A modern Personal Knowledge Management system with quick-capture widget, graph-based navigation, and collaborative features. Built in public.

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Build in Public](https://img.shields.io/badge/Build-In%20Public-brightgreen)](https://github.com/LyonMoncef/pkm-system)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

---

## 🎯 What is PKM System?

PKM System is a **personal knowledge management** tool designed for rapid thought capture, intelligent organization, and seamless knowledge navigation. It combines the power of local-first note-taking with collaborative features and AI-powered insights.

**Core Philosophy:**
- **Local-first**: Your data lives on your machine (or NAS)
- **Privacy by design**: You own 100% of your data
- **Build in public**: Transparent development, community-driven
- **Extensible**: Plugin architecture for endless possibilities

---

## ✨ Features

### Phase 1 - MVP (Current)
- ⚡ **Quick Capture Widget**: Desktop overlay for instant note-taking
- 📋 **Quick Reference Overlay**: Access cheatsheets, commands, and snippets instantly
- 🗂️ **Obsidian Integration**: Markdown-based local storage
- 🔍 **Fast Search**: Tag-based and text search
- ⌨️ **Global Hotkeys**: `Ctrl+Shift+Space` (capture), `Ctrl+Shift+Q` (quick ref)

### Phase 2 - Planned
- 🎨 **Dashboards**: Health, finance, projects tracking
- 🔗 **NAS Integration**: Centralized storage with sync
- 🤖 **AI Synthesis**: Automatic note summarization
- 🌐 **Selective Sharing**: Share notes with your circle
- 📊 **Analytics**: Insights on your knowledge patterns

### Phase 3 - Vision
- 👥 **Collaborative Network**: Connect with circles, contribute to shared knowledge
- 🧠 **Neural Index**: AI-powered semantic search and recommendations
- 🌍 **Public Platform**: Discover, share, and learn from the community
- 🔌 **API**: Build on top of PKM System

---

## 🚀 Quick Start

### Prerequisites
- [Obsidian](https://obsidian.md) installed
- Node.js 18+ (for widget)
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/LyonMoncef/pkm-system.git
cd pkm-system

# Setup Obsidian vault
# Point Obsidian to the ./vault directory (or your NAS path)

# Install widget dependencies
cd widget
npm install

# Run the widget
npm start
```

**Detailed setup:** See [SETUP.md](docs/SETUP.md)

---

## 📚 Documentation

- [Setup Guide](docs/SETUP.md) - Get started in 10 minutes
- [Architecture](docs/ARCHITECTURE.md) - How it all fits together
- [Roadmap](docs/ROADMAP.md) - What's next
- [Contributing](docs/CONTRIBUTING.md) - Join the journey

---

## 🏗️ Architecture

```
┌─────────────────────────────────────┐
│         NAS / Local Storage         │
│    (Obsidian Vault - Markdown)      │
└─────────────────────────────────────┘
              ↕
┌─────────────────────────────────────┐
│      PKM Widget (Electron)          │
│  • Quick Capture                    │
│  • Quick Reference                  │
│  • Search & Navigation              │
└─────────────────────────────────────┘
              ↕
┌─────────────────────────────────────┐
│      Future: Backend API            │
│  • Collaboration                    │
│  • AI Features                      │
│  • Analytics                        │
└─────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

**Current (MVP):**
- **Storage**: Obsidian (Markdown files)
- **Widget**: Electron + HTML/CSS/JS
- **Sync**: Manual / NAS

**Planned:**
- **Backend**: Node.js + Express
- **Database**: PostgreSQL
- **AI**: OpenAI / Anthropic Claude
- **Auth**: Supabase

---

## 📖 The Story

This project started from a simple need: **stop losing thoughts in the chaos of daily life**.

After years of trying different PKM tools (Notion, Roam, Evernote...), I realized what was missing:
1. A **quick capture** that doesn't interrupt flow
2. **Local-first** storage (no vendor lock-in)
3. **Easy access** to frequently needed info (cheatsheets, commands)
4. **Potential to collaborate** without sacrificing privacy

So I'm building it. In public. One commit at a time.

Follow the journey: [LinkedIn](https://linkedin.com/in/your-profile) | [Twitter](https://twitter.com/your-handle)

---

## 🤝 Contributing

This is a **#BuildInPublic** project. Contributions, ideas, and feedback are welcome!

**Ways to contribute:**
- 🐛 Report bugs
- 💡 Suggest features
- 📝 Improve documentation
- 🔧 Submit pull requests
- ⭐ Star the repo (it helps!)

See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines.

---

## 📅 Roadmap

**Phase 1 - MVP** (Weeks 1-2) ✅ In Progress
- Quick Capture Widget
- Quick Reference Overlay
- Obsidian integration

**Phase 2 - Functional** (Months 1-2)
- Dashboards (health, finance, projects)
- NAS sync
- AI synthesis

**Phase 3 - Collaborative** (Months 3-6)
- Circle network
- Sharing features
- Public platform

See [ROADMAP.md](docs/ROADMAP.md) for details.

---

## 📜 License

This project is licensed under the **GNU Affero General Public License v3.0 (AGPL-3.0)**.

**What this means:**
- ✅ Use it freely for personal use
- ✅ Fork and modify
- ✅ Contribute back to the community
- ⚠️ Commercial use requires separate license (contact for details)

See [LICENSE](LICENSE) for full terms.

---

## 🙏 Acknowledgments

**Inspiration:**
- [Obsidian](https://obsidian.md) - Local-first philosophy
- [Notion](https://notion.so) - UX excellence
- [Roam Research](https://roamresearch.com) - Graph thinking

**Built with the help of:**
- Claude (Anthropic) - Architecture guidance & pair programming
- The PKM community - Endless inspiration
- Coffee ☕ - Essential fuel

---

## 📬 Contact

- **GitHub**: [@LyonMoncef](https://github.com/LyonMoncef)
- **Email**: tats@datasaillance.fr
- **LinkedIn**: [Your LinkedIn](https://linkedin.com/in/your-profile)

---

## ⭐ Support

If you find this project useful, consider:
- ⭐ Starring the repo
- 🐦 Sharing on social media
- 💬 Joining discussions
- 🤝 Contributing

---

**Built with ❤️ and ☕ in France** 🇫🇷

*Last updated: October 2025*


===================================
-- Le 18/10/2025 à 06:59

## 🗓️ Development Timeline

### ✅ Phase 1 - Browser MVP (Week 1) - COMPLETED
- Quick Capture widget with markdown support
- Quick Reference overlay with cheatsheets
- Hub navigation system
- Multi-language support (EN/FR)
- Multi-theme support (Mac/Windows)

### 🚀 Phase 1.5 - Electron Migration (Week 2) - NEXT
- Native desktop application
- System-wide hotkeys
- Direct filesystem access
- Tray icon integration
- Auto-start capability

### 📈 Phase 2+ - Advanced Features (Month 2+)
- Dashboards (health, finance, projects)
- NAS integration & sync
- AI-powered synthesis
- Collaboration features



