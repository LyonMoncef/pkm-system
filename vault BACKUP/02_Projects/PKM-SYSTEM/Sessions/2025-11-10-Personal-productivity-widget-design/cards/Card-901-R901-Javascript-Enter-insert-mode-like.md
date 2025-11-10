---
type: chat-card
parent_export: '[[Export]]'
order: 901
role: assistant
created: '2025-11-10T22:56:04.689425Z'
tags:
- chat-card
- python
- code
- automation
attachments_count: 0
---

# 🤖 Message 901 - Assistant

**ID:** msg-901

## 💬 Content


**ID:** msg-901

javascript// 'i' - Enter insert mode (vim-like)
if (e.key === 'i' && document.activeElement !== editor) {
 e.preventDefault();
 // Focus l'éditeur de la page active
 const activePage = document.querySelector('.view-page.active');
 if (activePage && activePage.id === 'page-capture') {
 // Message à l'iframe pour focus
 const iframe = activePage.querySelector('iframe');
 if (iframe && iframe.contentWindow) {
 iframe.contentWindow.postMessage({ type: 'focus-editor' }, '*');
 }
 }
}

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-900-R900-Javascript-SUPPRIME-Escape-window-electr]]
- ⬇️ Next: [[Card-902-R902-Javascript-Écoute-messages-pour-focus]]
- 📊 MOC: [[_MOC_Personal productivity widget design]]

## 🏷️ Topics

- #python
- #code
- #automation
