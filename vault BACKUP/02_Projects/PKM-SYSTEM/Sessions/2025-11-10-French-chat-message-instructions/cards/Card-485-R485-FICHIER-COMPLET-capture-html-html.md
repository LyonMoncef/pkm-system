---
type: chat-card
parent_export: '[[Export]]'
order: 485
role: assistant
created: '2025-11-10T21:12:09.063456Z'
tags:
- chat-card
- python
- obsidian
- code
- git
- automation
attachments_count: 0
---

# 🤖 Message 485 - Assistant

**ID:** msg-485

## 💬 Content


**ID:** msg-485

📄 FICHIER COMPLET capture.html
html<!DOCTYPE html>
<html lang=\"en\">
<head>
 <meta charset=\"UTF-8\">
 <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
 <title>Quick Capture</title>
 <style>
 * {
 margin: 0;
 padding: 0;
 box-sizing: border-box;
 }

 body {
 font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
 background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
 height: 100vh;
 display: flex;
 flex-direction: column;
 overflow: hidden;
 }

 .container {
 flex: 1;
 display: flex;
 flex-direction: column;
 padding: 20px;
 max-width: 1400px;
 margin: 0 auto;
 width: 100%;
 }

 .header {
 text-align: center;
 color: white;
 margin-bottom: 20px;
 }

 .header h1 {
 font-size: 2em;
 font-weight: 600;
 text-shadow: 0 2px 4px rgba(0,0,0,0.1);
 }

 .editor-container {
 flex: 1;
 display: flex;
 gap: 20px;
 background: white;
 border-radius: 12px;
 padding: 20px;
 box-shadow: 0 8px 32px rgba(0,0,0,0.1);
 overflow: hidden;
 }

 .editor-section, .preview-section {
 flex: 1;
 display: flex;
 flex-direction: column;
 }

 .section-title {
 font-size: 1.2em;
 font-weight: 600;
 margin-bottom: 12px;
 color: #667eea;
 }

 #editor {
 flex: 1;
 width: 100%;
 padding: 16px;
 border: 2px solid #e2e8f0;
 border-radius: 8px;
 font-size: 16px;
 font-family: 'Courier New', monospace;
 resize: none;
 transition: border-color 0.3s;
 }

 #editor:focus {
 outline: none;
 border-color: #667eea;
 box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
 }

 #preview {
 flex: 1;
 padding: 16px;
 border: 2px solid #e2e8f0;
 border-radius: 8px;
 overflow-y: auto;
 background: #f8f9fa;
 }

 .controls {
 display: flex;
 gap: 12px;
 margin-top: 16px;
 }

 button {
 flex: 1;
 padding: 12px 24px;
 border: none;
 border-radius: 8px;
 font-size: 16px;
 font-weight: 600;
 cursor: pointer;
 transition: all 0.3s;
 }

 .btn-primary {
 background: #667eea;
 color: white;
 }

 .btn-primary:hover {
 background: #5568d3;
 transform: translateY(-2px);
 box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
 }

 .btn-secondary {
 background: #e2e8f0;
 color: #2d3748;
 }

 .btn-secondary:hover {
 background: #cbd5e0;
 transform: translateY(-2px);
 }

 .notification {
 position: fixed;
 top: 20px;
 right: 20px;
 padding: 16px 24px;
 background: white;
 border-radius: 8px;
 box-shadow: 0 4px 12px rgba(0,0,0,0.15);
 opacity: 0;
 transform: translateY(-20px);
 transition: all 0.3s;
 z-index: 1000;
 }

 .notification.show {
 opacity: 1;
 transform: translateY(0);
 }

 .notification.success {
 border-left: 4px solid #48bb78;
 }

 .notification.error {
 border-left: 4px solid #f56565;
 }

 .notification.info {
 border-left: 4px solid #4299e1;
 }

 /* Markdown Preview Styles */
 #preview h1, #preview h2, #preview h3 {
 margin-top: 16px;
 margin-bottom: 8px;
 color: #2d3748;
 }

 #preview p {
 margin-bottom: 12px;
 line-height: 1.6;
 }

 #preview code {
 background: #edf2f7;
 padding: 2px 6px;
 border-radius: 4px;
 font-family: 'Courier New', monospace;
 }

 #preview ul, #preview ol {
 margin-left: 24px;
 margin-bottom: 12px;
 }

 #preview li {
 margin-bottom: 4px;
 }
 </style>
</head>
<body>
 <div class=\"container\">
 <div class=\"header\">
 <h1>✍️ Quick Capture</h1>
 </div>

 <div class=\"editor-container\">
 <div class=\"editor-section\">
 <div class=\"section-title\">Editor</div>
 <textarea id=\"editor\" placeholder=\"Start typing your thoughts...\"></textarea>
 </div>

 <div class=\"preview-section\">
 <div class=\"section-title\">Preview</div>
 <div id=\"preview\"></div>
 </div>
 </div>

 <div class=\"controls\">
 <button class=\"btn-primary\" onclick=\"saveNote()\">💾 Save to Vault</button>
 <button class=\"btn-secondary\" onclick=\"clearEditor()\">🗑️ Clear</button>
 </div>
 </div>

 <div class=\"notification\" id=\"notification\"></div>

 <script>
 const editor = document.getElementById('editor');
 const preview = document.getElementById('preview');

 // Simple markdown parser
 function parseMarkdown(text) {
 return text
 // Headers
 .replace(/^### (.*$)/gim, '<h3>$1</h3>')
 .replace(/^## (.*$)/gim, '<h2>$1</h2>')
 .replace(/^# (.*$)/gim, '<h1>$1</h1>')
 // Bold
 .replace(/\\*\\*(.+?)\\*\\*/g, '<strong>$1</strong>')
 // Italic
 .replace(/\\*(.+?)\\*/g, '<em>$1</em>')
 // Code
 .replace(/`(.+?)`/g, '<code>$1</code>')
 // Lists
 .replace(/^\\- (.+)$/gim, '<li>$1</li>')
 // Paragraphs
 .replace(/\
\
/g, '</p><p>')
 .replace(/^(.+)$/gim, '<p>$1</p>');
 }

 // Update preview
 function updatePreview() {
 const markdown = editor.value;
 preview.innerHTML = parseMarkdown(markdown);
 }

 // Live preview update
 editor.addEventListener('input', updatePreview);

 // Auto-focus on load
 setTimeout(() => {
 editor.focus();
 }, 100);

 // Show notification
 function showNotification(message, type = 'success') {
 const notification = document.getElementById('notification');
 notification.textContent = message;
 notification.className = `notification ${type}`;
 notification.classList.add('show');

 setTimeout(() => {
 notification.classList.remove('show');
 }, 3000);
 }

 // Clear editor
 function clearEditor() {
 if (editor.value.trim() && !confirm('Clear all content?')) {
 return;
 }
 editor.value = '';
 updatePreview();
 localStorage.removeItem('pkm-quick-note');
 localStorage.removeItem('pkm-quick-note-timestamp');
 showNotification('🗑️ Cleared');
 }

 // === AUTO-SAVE TO CACHE ===
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
 showNotification('⚠️ Nothing to save', 'info');
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
 showNotification('📦 Window hidden', 'info');
 }
 }

 // Listen for quick save command from parent (Ctrl+W)
 window.addEventListener('message', (event) => {
 if (event.data.type === 'quick-save-and-hide') {
 quickSaveToCache();
 }
 });

 // === VIM-LIKE MODES ===
 let insertMode = true; // Start in insert mode

 // Keyboard shortcuts
 document.addEventListener('keydown', (e) => {
 // === ESC - Sort du mode édition ===
 if (e.key === 'Escape') {
 e.preventDefault();

 // Si on est dans le textarea, on blur (sort du mode édition)
 if (document.activeElement === editor) {
 editor.blur();
 insertMode = false;
 showNotification('Mode normal activé', 'info');
 }
 }

 // === CTRL+I - Entre en mode édition ===
 if (e.ctrlKey && e.key === 'i' && !insertMode) {
 e.preventDefault();
 editor.focus();
 insertMode = true;
 showNotification('Mode insertion activé', 'info');
 }

 // === CTRL+S - Save ===
 if ((e.ctrlKey || e.metaKey) && e.key === 's') {
 e.preventDefault();
 saveNote();
 }

 // === CTRL+K - Clear ===
 if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
 e.preventDefault();
 clearEditor();
 }

 // === RELAY TO PARENT - Ctrl+1/2/3, Ctrl+B ===
 if (e.ctrlKey && ['1', '2', '3', 'b', 'B'].includes(e.key)) {
 e.preventDefault();

 window.parent.postMessage({
 type: 'keyboard-event',
 event: {
 key: e.key.toLowerCase(),
 code: e.code,
 ctrlKey: e.ctrlKey,
 shiftKey: e.shiftKey,
 altKey: e.altKey,
 metaKey: e.metaKey
 }
 }, '*');
 }
 });

 // Sync insertMode avec le focus du textarea
 editor.addEventListener('focus', () => {
 insertMode = true;
 });

 editor.addEventListener('blur', () => {
 insertMode = false;
 });

 console.log('✅ Keyboard relay active');
 </script>
</body>
</html>

🚀 APPLIQUE + COMMIT
bashcomt \"Complete capture.html refactor: save behaviors + vim modes\"
Teste et balance ton feedback ! 💪

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-484-R484-FICHIER-COMPLET-capture-html-html]]
- ⬇️ Next: [[Card-486-R486-Html-DOCTYPE-html-html-lang]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #obsidian
- #code
- #git
- #automation
