---
type: chat-card
parent_export: '[[Export]]'
order: 715
role: assistant
created: '2025-11-10T21:12:15.072510Z'
tags:
- chat-card
- python
- automation
attachments_count: 0
---

# 🤖 Message 715 - Assistant

**ID:** msg-715

## 💬 Content


**ID:** msg-715

🔧 CTRL+/ POUR SHORTCUTS - FIX RAPIDE
Pas besoin de research ici, juste modifier le shortcut !

📝 FIX - Dans main.js
Dans la fonction registerGlobalShortcuts(), remplace le Ctrl+Shift+I par :
javascript // Ctrl+/ - Show keyboard shortcuts
 globalShortcut.register('CommandOrControl+/', () => {
 if (mainWindow && mainWindow.isVisible()) {
 mainWindow.webContents.send('show-shortcuts');
 } else if (mainWindow) {
 mainWindow.show();
 setTimeout(() => {
 mainWindow.webContents.send('show-shortcuts');
 }, 300);
 } else {
 createMainWindow();
 setTimeout(() => {
 mainWindow.webContents.send('show-shortcuts');
 }, 800);
 }
 });

📝 UPDATE - Dans app.html
Trouve le texte du status bar (en bas) et change :
html<div class=\"status-right\">
 Press Ctrl+/ for shortcuts
</div>
Et dans les keyboard hints, update la section globale :
html<div class=\"hint-section\">
 <strong>🌍 Global (work when app closed):</strong><br>
 <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>Space</kbd> Toggle Capture<br>
 <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>F</kbd> Toggle Reference<br>
 <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>H</kbd> Toggle Hub<br>
 <kbd>Ctrl</kbd>+<kbd>/</kbd> Show shortcuts (this!)<br>
 <kbd>Ctrl</kbd>+<kbd>W</kbd> Quick save + hide<br>
 <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>W</kbd> Quit app completely
</div>

🚀 APPLIQUE + TESTE

Modifie main.js
Update status bar dans app.html
Update keyboard hints dans app.html
Restart
Teste Ctrl+/

Confirme quand ça marche ! 💪

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-714-R714-CTRL-POUR-SHORTCUTS-RAPIDE-besoin]]
- ⬇️ Next: [[Card-716-R716-CTRL-POUR-SHORTCUTS-RAPIDE-besoin]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #automation
