---
type: chat-card
parent_export: '[[Export]]'
order: 775
role: assistant
created: '2025-11-10T21:12:15.804434Z'
tags:
- chat-card
- python
- receipts
- code
- automation
attachments_count: 0
---

# 🤖 Message 775 - Assistant

**ID:** msg-775

## 💬 Content


**ID:** msg-775

javascript// TEST - Shortcut internal pour show shortcuts
document.addEventListener('keydown', (e) => {
 // F1 en internal (bypass IPC)
 if (e.key === 'F1') {
 e.preventDefault();
 console.log('🔑 F1 internal caught');
 showKeyboardHints();
 }
});
```

**Si F1 marche avec ce code, c'est que :**
- ✅ La fonction `showKeyboardHints()` existe et marche
- ❌ L'IPC chain est cassée

---

## 💡 IMPLICATIONS POUR REFACTOR

### **Choix stratégiques:**

**Option A - Tout en Global (Layer 1)**
- ✅ Marche app cachée
- ❌ Plus complexe (IPC)
- ❌ Plus de points de failure

**Option B - Tout en Internal (Layer 2)**
- ✅ Plus simple, pas d'IPC
- ❌ Ne marche QUE si app focused

**Option C - Hybride (actuel)**
- Toggle/Navigation → Global (Layer 1)
- Actions UI → Internal (Layer 2)

---

## 🎯 RECOMMANDATION REFACTOR

### **Architecture propre à venir:**
```
/src
├── main/
│ ├── main.js (process principal)
│ └── shortcuts.js (global shortcuts centralisés)
├── renderer/
│ ├── app.html
│ ├── pages/
│ │ ├── capture.html
│ │ ├── hub.html
│ │ └── reference.html
│ ├── styles/
│ │ ├── global.css
│ │ ├── sidebar.css
│ │ └── pages.css
│ └── scripts/
│ ├── shortcuts.js (internal shortcuts)
│ ├── navigation.js
│ └── utils.js
└── preload/
 └── preload.js

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-774-R774-JavascriptEsc-Normal-mode-Ctrl-Insert]]
- ⬇️ Next: [[Card-776-R776-DOCTYPE-html-html-lang-head]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #receipts
- #code
- #automation
