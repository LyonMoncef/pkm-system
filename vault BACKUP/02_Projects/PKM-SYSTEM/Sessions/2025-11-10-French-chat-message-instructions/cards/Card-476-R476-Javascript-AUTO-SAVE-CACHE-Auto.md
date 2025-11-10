---
type: chat-card
parent_export: '[[Export]]'
order: 476
role: assistant
created: '2025-11-10T21:12:08.940351Z'
tags:
- chat-card
- python
- obsidian
- code
- automation
attachments_count: 0
---

# 🤖 Message 476 - Assistant

**ID:** msg-476

## 💬 Content


**ID:** msg-476

javascript // === AUTO-SAVE TO CACHE ===
 // Auto-save to localStorage every 2 seconds while typing
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
 // Load from localStorage ONCE on page load
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

 // Load on DOMContentLoaded
 if (document.readyState === 'loading') {
 document.addEventListener('DOMContentLoaded', loadFromCache);
 } else {
 loadFromCache();
 }

 // === CTRL+S - SAVE TO VAULT (CLEAR AFTER) ===
 async function saveNote() {
 const content = editor.value.trim();

 if (!content) {
 showNotification('⚠️ Nothing to save');
 return;
 }

 // Generate filename
 const now = new Date();
 const timestamp = now.toISOString().replace(/[:.]/g, '-').slice(0, -5);
 const filename = `quick-capture-${timestamp}.md`;

 try {
 const result = await window.electronAPI.saveNote(filename, content);

 if (result.success) {
 showNotification('✅ Saved + Ready for new note');

 // CLEAR editor after successful save
 editor.value = '';
 updatePreview();

 // CLEAR localStorage
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
 // Triggered by Ctrl+W global shortcut
 function quickSaveToCache() {
 const content = editor.value.trim();
 if (content) {
 localStorage.setItem('pkm-quick-note', content);
 localStorage.setItem('pkm-quick-note-timestamp', Date.now());
 showNotification('💾 Saved to cache');
 console.log('💾 Quick saved to cache');
 } else {
 showNotification('📦 Window hidden');
 }
 }

 // Listen for quick save command from parent (Ctrl+W)
 window.addEventListener('message', (event) => {
 if (event.data.type === 'quick-save-and-hide') {
 quickSaveToCache();
 }
 });

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-475-R475-PARFAIT-OPTION-CODE-FINAL-capture]]
- ⬇️ Next: [[Card-477-R477-Bashcomt-save-behaviors-Ctrl-clears]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #obsidian
- #code
- #automation
