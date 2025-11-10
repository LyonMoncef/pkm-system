---
type: chat-card
parent_export: '[[Export]]'
order: 375
role: assistant
created: '2025-11-10T03:56:33.561974Z'
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

- ⬆️ Previous: [[374_assistant_msg-374]]
- ⬇️ Next: [[376_assistant_msg-376]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #code
- #automation
