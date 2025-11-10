---
type: chat-card
parent_export: '[[Export]]'
order: 639
role: assistant
created: '2025-11-10T22:56:02.154532Z'
tags:
- chat-card
- python
- obsidian
- code
- automation
attachments_count: 0
---

# 🤖 Message 639 - Assistant

**ID:** msg-639

## 💬 Content


**ID:** msg-639

javascript// Save note using Electron API
async function saveNote() {
 const content = editor.value;
 if (!content.trim()) {
 alert('Nothing to save!');
 return;
 }

 const now = new Date();
 const timestamp = now.toISOString().slice(0, 19).replace('T', '_').replace(/:/g, '-');

 // Extract title from first heading
 const firstLine = content.split('\
')[0];
 let title = 'note';
 if (firstLine.startsWith('#')) {
 title = firstLine.replace(/^#+\\s*/, '').trim()
 .toLowerCase()
 .replace(/[^a-z0-9]+/g, '-')
 .substring(0, 50);
 }

 const filename = `${timestamp}_${title}.md`;

 // Use Electron API if available
 if (window.electronAPI) {
 try {
 const result = await window.electronAPI.saveNote(filename, content);

 if (result.success) {
 localStorage.removeItem('pkm-autosave');
 showNotification(`✅ Note saved: ${filename}`);
 lastSaved.textContent = `Saved at ${now.toLocaleTimeString()}`;

 if (confirm('Note saved to vault! Clear editor for new note?')) {
 clearEditor();
 }
 } else {
 alert('Error saving note. Try again.');
 }
 } catch (error) {
 console.error('Save error:', error);
 alert('Error saving note.');
 }
 } else {
 // Fallback to download if not in Electron
 downloadNote();
 }
}

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-638-R638-PUTAIIIIN-OUAIS-HOTKEYS-SYSTÈME-FONCTION]]
- ⬇️ Next: [[Card-640-R640-Powershell-Relance-start]]
- 📊 MOC: [[_MOC_Personal productivity widget design]]

## 🏷️ Topics

- #python
- #obsidian
- #code
- #automation
