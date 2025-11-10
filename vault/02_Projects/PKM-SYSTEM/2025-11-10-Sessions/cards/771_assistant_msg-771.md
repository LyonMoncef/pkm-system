---
type: chat-card
parent_export: '[[Export]]'
order: 771
role: assistant
created: '2025-11-10T03:56:38.087756Z'
tags:
- chat-card
- python
- receipts
- code
- automation
attachments_count: 0
---

# 🤖 Message 771 - Assistant

**ID:** msg-771

## 💬 Content


**ID:** msg-771

📋 RAPPEL ARCHITECTURE SHORTCUTS

🏗️ ARCHITECTURE ACTUELLE (3 LAYERS)
LAYER 1 - Global OS Shortcuts (main.js)
Registered via: globalShortcut.register()
Fonctionnent:

✅ App fermée/cachée
✅ App minimisée
✅ App en background

Communication: main.js → IPC → preload.js → app.html
Shortcuts actuels:
javascriptCtrl+Shift+Space → smartToggle('capture')
Ctrl+Shift+F → smartToggle('reference')
Ctrl+Shift+H → smartToggle('hub')
Ctrl+W → send IPC 'quick-save-and-hide'
Ctrl+Shift+W → app.quit()
F1/Ctrl+//Ctrl+Shift+L → send IPC 'show-shortcuts' (❌ CASSÉ)

LAYER 2 - Internal App Shortcuts (app.html)
Registered via: document.addEventListener('keydown')
Fonctionnent:

✅ App ouverte et focused SEULEMENT
✅ Communication directe (pas d'IPC)

Shortcuts actuels:
javascriptCtrl+1/2/3 → navigateToPage() (✅ MARCHENT)
Ctrl+B → toggleSidebar() (✅ MARCHE)

LAYER 3 - Page-Specific (capture.html, etc.)
Dans les iframes → Relayés via postMessage
Shortcuts actuels:
javascriptEsc → Normal mode
Ctrl+I → Insert mode
Ctrl+S → Save
Ctrl+K → Clear
Ctrl+1/2/3/B → Relay to parent
```

---

## 🐛 POURQUOI Ctrl+1/2/3 MARCHENT MAIS PAS F1 ?

**Ctrl+1/2/3 = LAYER 2** (internal)
- Gérés directement dans app.html
- Pas d'IPC → Aucune chaîne à casser

**F1/Ctrl+/ = LAYER 1** (global)
- Nécessitent IPC chain complète
- Si 1 maillon cassé → Tout casse

---

## 🔍 DIAGNOSTIC

**La chaîne IPC est cassée quelque part :**
```
✅ main.js capte F1 → logs OK
✅ main.js envoie IPC 'show-shortcuts'
❓ preload.js expose onShowShortcuts ?
❓ app.html écoute l'IPC ?
❓ showKeyboardHints() existe et marche ?

🧪 TEST RAPIDE - BYPASS IPC
Pour confirmer que c'est bien l'IPC le problème, teste ça :
Dans app.html, ajoute un listener INTERNAL (Layer 2) :
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

🚀 ACTION IMMÉDIATE
1. Teste le bypass IPC dans app.html
2. Balance-moi si F1 marche en internal
3. On fixe l'IPC chain ou on repense l'archi
Dis-moi le résultat du test ! 💪

---


## 🔗 Navigation

- ⬆️ Previous: [[770_assistant_msg-770]]
- ⬇️ Next: [[772_assistant_msg-772]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #receipts
- #code
- #automation
