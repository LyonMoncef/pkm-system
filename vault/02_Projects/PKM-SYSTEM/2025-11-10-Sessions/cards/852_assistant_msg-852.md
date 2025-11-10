---
type: chat-card
parent_export: '[[Export]]'
order: 852
role: assistant
created: '2025-11-10T03:56:39.012583Z'
tags:
- chat-card
- python
- code
- automation
attachments_count: 0
---

# 🤖 Message 852 - Assistant

**ID:** msg-852

## 💬 Content


**ID:** msg-852

javascript // === FOCUS MANAGEMENT + TEST SHORTCUTS ===
 window.addEventListener('message', (event) => {
 // Test shortcuts relay
 if (event.data.type === 'show-shortcuts-test') {
 console.log('🧪 app.html received: show-shortcuts-test');
 console.log('🧪 Calling showKeyboardHints()');
 showKeyboardHints();
 }

 // Keyboard events relay (existing)
 if (event.data.type === 'keyboard-event') {
 const keyEvent = event.data.event;

 if (keyEvent.ctrlKey && ['1', '2', '3'].includes(keyEvent.key)) {
 const pages = ['capture', 'hub', 'reference'];
 const pageIndex = parseInt(keyEvent.key) - 1;
 if (pages[pageIndex]) {
 navigateToPage(pages[pageIndex]);
 }
 }

 if (keyEvent.ctrlKey && keyEvent.key === 'b') {
 toggleSidebar();
 }
 }
 });

---


## 🔗 Navigation

- ⬆️ Previous: [[851_assistant_msg-851]]
- ⬇️ Next: [[853_assistant_msg-853]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #code
- #automation
