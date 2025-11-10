---
type: chat-card
parent_export: '[[Export]]'
order: 137
role: assistant
created: '2025-11-10T21:12:04.873821Z'
tags:
- chat-card
- python
- data-analysis
- code
- automation
attachments_count: 0
---

# 🤖 Message 137 - Assistant

**ID:** msg-137

## 💬 Content


**ID:** msg-137

javascript// Navigation logic
const navItems = document.querySelectorAll('.nav-item');
const contentFrame = document.getElementById('content-frame');

navItems.forEach(item => {
 item.addEventListener('click', (e) => {
 e.preventDefault();

 // Update active state
 navItems.forEach(nav => nav.classList.remove('active'));
 item.classList.add('active');

 // Load page
 const page = item.dataset.page;
 const iframe = document.createElement('iframe');
 iframe.src = `${page}.html`; // ← FIX ICI (ligne 87)
 iframe.style.width = '100%';
 iframe.style.height = '100%';
 iframe.style.border = 'none';

 contentFrame.innerHTML = '';
 contentFrame.appendChild(iframe);
 });
});

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-136-R136-Html-href-data-page-capture]]
- ⬇️ Next: [[Card-138-R138-Javascriptiframe-page-html]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #data-analysis
- #code
- #automation
