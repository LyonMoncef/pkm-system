---
type: chat-card
parent_export: '[[Export]]'
order: 236
role: assistant
created: '2025-11-10T23:13:23.427110Z'
tags:
- chat-card
- python
- obsidian
- code
- automation
attachments_count: 0
---

# 🤖 Message 236 - Assistant

**ID:** msg-236

## 💬 Content


**ID:** msg-236

javascript// ChatExporter - Générique multi-plateforme
const ChatExporter = {

 // Détection plateforme
 detectPlatform() {
 if (window.location.hostname.includes('claude.ai')) return 'claude';
 if (window.location.hostname.includes('chatgpt.com')) return 'chatgpt';
 if (window.location.hostname.includes('gemini.google.com')) return 'gemini';
 return 'unknown';
 },

 // Extracteurs spécifiques
 extractors: {
 claude: { /* sélecteurs DOM Claude */ },
 chatgpt: { /* sélecteurs DOM ChatGPT */ },
 gemini: { /* sélecteurs DOM Gemini */ }
 },

 // Export markdown
 generateMarkdown(messages, metadata) { /* ... */ },

 // Copie clipboard
 copyToClipboard(text) { /* ... */ },

 // Main
 run() { /* ... */ }
}

---


## 🔗 Navigation

- ⬆️ Previous: [[235_assistant_msg-235]]
- ⬇️ Next: [[237_assistant_msg-237]]
- 📊 MOC: [[_MOC_Project continuity and session planning]]

## 🏷️ Topics

- #python
- #obsidian
- #code
- #automation
