---
type: chat-card
parent_export: '[[Export]]'
order: 549
role: assistant
created: '2025-11-10T22:56:01.279713Z'
tags:
- chat-card
- python
- obsidian
- code
- automation
attachments_count: 0
---

# 🤖 Message 549 - Assistant

**ID:** msg-549

## 💬 Content


**ID:** msg-549

javascript// Save note (simplified download)
function saveNote() {
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

 // Download file
 const blob = new Blob([content], { type: 'text/markdown' });
 const url = URL.createObjectURL(blob);
 const a = document.createElement('a');
 a.href = url;
 a.download = filename;
 document.body.appendChild(a);
 a.click();
 document.body.removeChild(a);
 URL.revokeObjectURL(url);

 localStorage.removeItem('pkm-autosave');
 showNotification(`✅ Note saved: ${filename}`);
 lastSaved.textContent = `Saved at ${now.toLocaleTimeString()}`;

 if (confirm('Note saved! Clear editor for new note?')) {
 clearEditor();
 }
}

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-548-R548-PUTAIN-OUAIS-OPTION-CHOIX-SAGE]]
- ⬇️ Next: [[Card-550-R550-Html-class-footer-actions-button]]
- 📊 MOC: [[_MOC_Personal productivity widget design]]

## 🏷️ Topics

- #python
- #obsidian
- #code
- #automation
