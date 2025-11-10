---
type: chat-card
parent_export: '[[Export]]'
order: 907
role: assistant
created: '2025-11-10T22:56:04.743952Z'
tags:
- chat-card
- python
- code
- automation
attachments_count: 0
---

# 🤖 Message 907 - Assistant

**ID:** msg-907

## 💬 Content


**ID:** msg-907

javascript// Setup IPC listeners (depuis Electron main process)
if (window.electronAPI) {
 window.electronAPI.onNavigate((page) => {
 console.log('Navigate to:', page);
 navigateToPage(page);
 });

 window.electronAPI.onToggleSidebar(() => {
 console.log('Toggle sidebar');
 toggleSidebar();
 });
}

// Keyboard shortcuts locaux (qui ne conflictent pas avec globaux)
document.addEventListener('keydown', (e) => {
 // Arrow keys - Navigation directe (Ctrl+Up/Down)
 if (e.ctrlKey && e.key === 'ArrowDown') {
 e.preventDefault();
 selectedNavIndex = (selectedNavIndex + 1) % navItems.length;
 const selectedNav = navItems[selectedNavIndex];
 const page = selectedNav.getAttribute('data-page');
 navigateToPage(page);
 }

 if (e.ctrlKey && e.key === 'ArrowUp') {
 e.preventDefault();
 selectedNavIndex = (selectedNavIndex - 1 + navItems.length) % navItems.length;
 const selectedNav = navItems[selectedNavIndex];
 const page = selectedNav.getAttribute('data-page');
 navigateToPage(page);
 }

 // ? - Show shortcuts
 if (e.key === '?' && !e.shiftKey) {
 e.preventDefault();
 showKeyboardHints();
 }

 // 'i' - Enter insert mode (vim-like) - SI pas déjà en édition
 if (e.key === 'i' && document.activeElement.tagName !== 'TEXTAREA' && document.activeElement.tagName !== 'INPUT') {
 e.preventDefault();
 const activePage = document.querySelector('.view-page.active');
 if (activePage && activePage.id === 'page-capture') {
 const iframe = activePage.querySelector('iframe');
 if (iframe && iframe.contentWindow) {
 iframe.contentWindow.postMessage({ type: 'focus-editor' }, '*');
 }
 }
 }

 // ESC ne fait RIEN au niveau app (géré dans les iframes)
 // Pas de fermeture d'app
});

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-906-R906-Javascriptapp-will-quit-globalShortcut-u]]
- ⬇️ Next: [[Card-908-R908-MFbordel-prochain-message-dépasse-limite]]
- 📊 MOC: [[_MOC_Personal productivity widget design]]

## 🏷️ Topics

- #python
- #code
- #automation
