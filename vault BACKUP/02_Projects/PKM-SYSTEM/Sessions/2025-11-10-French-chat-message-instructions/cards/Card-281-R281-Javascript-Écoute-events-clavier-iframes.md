---
type: chat-card
parent_export: '[[Export]]'
order: 281
role: assistant
created: '2025-11-10T21:12:06.569838Z'
tags:
- chat-card
- python
- code
- automation
attachments_count: 0
---

# 🤖 Message 281 - Assistant

**ID:** msg-281

## 💬 Content


**ID:** msg-281

javascript// Écoute les events clavier des iframes
window.addEventListener('message', (event) => {
 if (event.data.type === 'keyboard-event') {
 const keyEvent = event.data.event;

 // Simule l'événement clavier au niveau du parent
 const simulatedEvent = new KeyboardEvent('keydown', {
 key: keyEvent.key,
 code: keyEvent.code,
 ctrlKey: keyEvent.ctrlKey,
 shiftKey: keyEvent.shiftKey,
 altKey: keyEvent.altKey,
 metaKey: keyEvent.metaKey,
 bubbles: true
 });

 document.dispatchEvent(simulatedEvent);
 }
});

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-280-R280-RÉSOLU-quick-reference-html-Erreur]]
- ⬇️ Next: [[Card-282-R282-Javascript-Relay-keyboard-events-parent]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #code
- #automation
