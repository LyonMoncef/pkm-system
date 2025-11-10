---
type: chat-card
parent_export: '[[Export]]'
order: 539
role: assistant
created: '2025-11-10T21:12:09.775466Z'
tags:
- chat-card
- python
- obsidian
- code
- automation
attachments_count: 0
---

# 🤖 Message 539 - Assistant

**ID:** msg-539

## 💬 Content


**ID:** msg-539

📄 PARTIE 2/3 - Auto-save + Load from cache
javascript // === AUTO-SAVE TO CACHE ===
 let saveTimeout;
 editor.addEventListener('input', () => {
 clearTimeout(saveTimeout);
 saveTimeout = setTimeout(() => {
 const content = editor.value;
 if (content.trim()) {
 localStorage.setItem('pkm-quick-note', content);
 localStorage.setItem('pkm-quick-note-timestamp', Date.now());
 console.log('💾 Auto-saved to cache');
 }
 }, 2000);
 });

 // === LOAD FROM CACHE ON STARTUP ===
 let hasLoadedFromCache = false;

 function loadFromCache() {
 if (!hasLoadedFromCache) {
 const savedNote = localStorage.getItem('pkm-quick-note');
 if (savedNote) {
 editor.value = savedNote;
 updatePreview();
 console.log('📂 Loaded from cache');
 }
 hasLoadedFromCache = true;
 }
 }

 if (document.readyState === 'loading') {
 document.addEventListener('DOMContentLoaded', loadFromCache);
 } else {
 loadFromCache();
 }

 // === CTRL+S - SAVE TO VAULT (CLEAR AFTER) ===
 async function saveNote() {
 const content = editor.value.trim();

 if (!content) {
 showNotification('⚠️ Nothing to save', 'info');
 return;
 }

 const now = new Date();
 const timestamp = now.toISOString().replace(/[:.]/g, '-').slice(0, -5);
 const filename = `quick-capture-${timestamp}.md`;

 try {
 const result = await window.electronAPI.saveNote(filename, content);

 if (result.success) {
 showNotification('✅ Saved + Ready for new note');

 editor.value = '';
 updatePreview();
 localStorage.removeItem('pkm-quick-note');
 localStorage.removeItem('pkm-quick-note-timestamp');

 console.log('🗑️ Cleared after save to vault');
 } else {
 showNotification('❌ Save failed', 'error');
 }
 } catch (error) {
 console.error('Save error:', error);
 showNotification('❌ Save error', 'error');
 }
 }

 // === QUICK SAVE TO CACHE (KEEP CONTENT) ===
 function quickSaveToCache() {
 const content = editor.value.trim();
 if (content) {
 localStorage.setItem('pkm-quick-note', content);
 localStorage.setItem('pkm-quick-note-timestamp', Date.now());
 showNotification('💾 Saved to cache', 'info');
 console.log('💾 Quick saved to cache');
 } else {
 showNotification('📦 Window hidden', 'info');
 }
 }

 window.addEventListener('message', (event) => {
 if (event.data.type === 'quick-save-and-hide') {
 quickSaveToCache();
 }
 });
CONTINUE AVEC PARTIE 3 (finale)... 👇

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-538-R538-PARTIE-Auto-save-Load-from]]
- ⬇️ Next: [[Card-540-R540-Javascript-AUTO-SAVE-CACHE-saveTimeout]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #obsidian
- #code
- #automation
