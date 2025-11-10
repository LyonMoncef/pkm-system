---
type: chat-card
parent_export: '[[Export]]'
order: 181
role: assistant
created: '2025-11-10T21:46:08.002837Z'
tags:
- chat-card
- python
- code
- automation
attachments_count: 0
---

# 🤖 Message 181 - Assistant

**ID:** msg-181

## 💬 Content


**ID:** msg-181

javascript// Pseudo-code
async function askClaude(userMessage, presets) {
 const fullPrompt = `
 ${loadPresetsFile()}

 User message: ${userMessage}
 `;

 return await claude.messages.create({
 model: \"claude-sonnet-4.5\",
 messages: [{ role: \"user\", content: fullPrompt }]
 });
}

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-180-R180-Markdown-PRESETS-MONCEF-CLAUDE]]
- ⬇️ Next: [[Card-182-R182-Espace-projects-viens-créer-pour]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #python
- #code
- #automation
