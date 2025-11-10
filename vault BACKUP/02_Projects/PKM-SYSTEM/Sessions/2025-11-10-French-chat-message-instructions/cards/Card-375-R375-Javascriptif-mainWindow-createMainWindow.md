---
type: chat-card
parent_export: '[[Export]]'
order: 375
role: assistant
created: '2025-11-10T21:12:07.577539Z'
tags:
- chat-card
- python
- code
- automation
attachments_count: 0
---

# 🤖 Message 375 - Assistant

**ID:** msg-375

## 💬 Content


**ID:** msg-375

javascriptif (!mainWindow) {
 createMainWindow();
 navigate(page);
} else if (!mainWindow.isVisible()) {
 mainWindow.show();
 navigate(page);
} else {
 // App déjà visible
 const currentPage = getCurrentPage(); // À implémenter
 if (currentPage === page) {
 mainWindow.hide(); // Toggle off si déjà sur la page
 } else {
 navigate(page); // Change de page si différent
 }
}

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-374-R374-JavascriptCtrl-Shift-Space-Toggle-Captur]]
- ⬇️ Next: [[Card-376-R376-JavascriptCtrl-Navigate-Capture-Ctrl-Nav]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #code
- #automation
