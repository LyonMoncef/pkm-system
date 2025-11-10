---
type: chat-card
parent_export: '[[Export]]'
order: 517
role: assistant
created: '2025-11-10T22:56:00.987912Z'
tags:
- chat-card
- python
- obsidian
- code
- automation
attachments_count: 0
---

# 🤖 Message 517 - Assistant

**ID:** msg-517

## 💬 Content


**ID:** msg-517

javascript// Save note to file system
async function saveNote() {
 const content = editor.value;
 if (!content.trim()) {
 alert('Nothing to save!');
 return;
 }

 // Si pas de vault configuré, demander de le configurer
 if (!vaultDirHandle) {
 alert('Please configure vault first by clicking \"⚙️ Configure Vault\"');
 const configured = await initVault();
 if (!configured) {
 downloadNote();
 return;
 }
 }

 try {
 // Vérifier qu'on a toujours la permission
 const permission = await vaultDirHandle.queryPermission({ mode: 'readwrite' });
 if (permission !== 'granted') {
 const newPermission = await vaultDirHandle.requestPermission({ mode: 'readwrite' });
 if (newPermission !== 'granted') {
 alert('Permission denied. Please reconfigure vault.');
 vaultDirHandle = null;
 downloadNote();
 return;
 }
 }

 // Créer le nom de fichier
 const now = new Date();
 const timestamp = now.toISOString().slice(0, 19).replace('T', '_').replace(/:/g, '-');

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

 // Sauvegarder DIRECTEMENT dans le dossier configuré (pas de sous-dossier)
 const fileHandle = await vaultDirHandle.getFileHandle(filename, { create: true });

 const writable = await fileHandle.createWritable();
 await writable.write(content);
 await writable.close();

 localStorage.removeItem('pkm-autosave');

 showNotification(`✅ Note saved: ${filename}`);
 lastSaved.textContent = `Saved at ${now.toLocaleTimeString()}`;

 if (confirm('Note saved to vault! Clear editor for new note?')) {
 clearEditor();
 }

 } catch (err) {
 console.error('Error saving file:', err);
 alert('Error saving to vault. Downloading instead.');
 downloadNote();
 }
}

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-516-R516-Vois-problème-PROBLÈME-IDENTIFIÉ-Deux]]
- ⬇️ Next: [[Card-518-R518-Changé-navigateur-défaut-essayé-avec]]
- 📊 MOC: [[_MOC_Personal productivity widget design]]

## 🏷️ Topics

- #python
- #obsidian
- #code
- #automation
