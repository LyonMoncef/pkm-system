---
type: chat-card
parent_export: '[[Export]]'
order: 293
role: assistant
created: '2025-11-10T21:12:06.701681Z'
tags:
- chat-card
- python
- code
- automation
attachments_count: 0
---

# 🤖 Message 293 - Assistant

**ID:** msg-293

## 💬 Content


**ID:** msg-293

javascript // === FOCUS MANAGEMENT SYSTEM ===
 // Écoute les events clavier des iframes
 window.addEventListener('message', (event) => {
 if (event.data.type === 'keyboard-event') {
 const keyEvent = event.data.event;

 // Ctrl+1/2/3 - Navigate pages
 if (keyEvent.ctrlKey && ['1', '2', '3'].includes(keyEvent.key)) {
 const pages = ['capture', 'hub', 'reference'];
 const pageIndex = parseInt(keyEvent.key) - 1;
 if (pages[pageIndex]) {
 navigateToPage(pages[pageIndex]);
 }
 }

 // Ctrl+B - Toggle sidebar
 if (keyEvent.ctrlKey && keyEvent.key === 'b') {
 toggleSidebar();
 }

 // Ctrl+Arrows - Navigate menu (à implémenter)
 if (keyEvent.ctrlKey && ['ArrowUp', 'ArrowDown'].includes(keyEvent.key)) {
 // TODO: Implement arrow navigation
 console.log('Arrow navigation:', keyEvent.key);
 }
 }
 });

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-292-R292-Implementing-focus-management-system-ifr]]
- ⬇️ Next: [[Card-294-R294-Javascript-RELAY-KEYBOARD-EVENTS-PARENT]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #code
- #automation
