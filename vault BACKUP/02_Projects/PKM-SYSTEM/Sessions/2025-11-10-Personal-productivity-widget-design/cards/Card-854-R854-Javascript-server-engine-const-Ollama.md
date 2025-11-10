---
type: chat-card
parent_export: '[[Export]]'
order: 854
role: assistant
created: '2025-11-10T22:56:04.267977Z'
tags:
- chat-card
- python
- data-analysis
- code
- automation
attachments_count: 0
---

# 🤖 Message 854 - Assistant

**ID:** msg-854

## 💬 Content


**ID:** msg-854

javascript// server/ai-engine.js

const { Ollama } = require('ollama');
const ollama = new Ollama();

class LocalAI {

 async analyzeTags(noteContent) {
 const prompt = `
 Analyse cette note et génère des tags pertinents.
 Note : ${noteContent}

 Retourne uniquement une liste de tags séparés par des virgules.
 `;

 const response = await ollama.generate({
 model: 'llama3.1',
 prompt: prompt,
 stream: false
 });

 return response.response.split(',').map(t => t.trim());
 }

 async detectEmotions(noteContent) {
 const prompt = `
 Détecte les émotions présentes dans ce texte.
 Texte : ${noteContent}

 Retourne uniquement les émotions sous forme de liste.
 `;

 const response = await ollama.generate({
 model: 'llama3.1',
 prompt: prompt
 });

 return this.parseEmotions(response.response);
 }

 async naturalLanguageSearch(query, notes) {
 // Utilise embeddings pour recherche sémantique
 const queryEmbedding = await this.embed(query);

 const results = notes.map(note => ({
 note,
 similarity: this.cosineSimilarity(queryEmbedding, note.embedding)
 }))
 .sort((a, b) => b.similarity - a.similarity)
 .slice(0, 10);

 return results;
 }
}

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-853-R853-Bash-Windows-avec-Chocolatey-choco]]
- ⬇️ Next: [[Card-855-R855-Javascript-Dans-Quick-Reference-widget]]
- 📊 MOC: [[_MOC_Personal productivity widget design]]

## 🏷️ Topics

- #python
- #data-analysis
- #code
- #automation
