---
created: 2025-11-10T20:00:00+01:00
updated: 2025-11-10T20:00:00+01:00
type: backlog-item
tags: [backlog-item, power-bi, duckdb, odbc, optimization, integration]
status: todo
priority: low
estimated_time: "1-2h"
category: improvement
project: compta-system
phase: phase-2
related_to: 
  - "[[finance.duckdb]]"
  - "[[Power BI Dashboard]]"
  - "[[export_for_powerbi]]"
---

# 🔌 Power BI Direct DuckDB Connection (ODBC)

> **Connexion directe Power BI ↔ DuckDB via ODBC pour refresh automatique**

---

## 📋 Description

Actuellement, Power BI charge des exports Excel statiques. Pour des dashboards plus dynamiques avec refresh automatique, établir une connexion directe via ODBC.

### Context

**MVP actuel (Option B) :**
- Export DuckDB → Excel
- Import Excel → Power BI
- ✅ Simple et fonctionnel
- ❌ Refresh manuel nécessaire

**Target (Option A) :**
- Power BI → ODBC Driver → DuckDB
- ✅ Refresh automatique
- ✅ Requêtes directes
- ❌ Setup ODBC requis

---

## 🎯 Objectif

Configurer connexion ODBC entre Power BI et DuckDB pour :
- ✅ Refresh automatique des données
- ✅ Requêtes SQL directes depuis Power BI
- ✅ Pas besoin d'exports intermédiaires
- ✅ Dashboards toujours à jour

---

## 🔧 Solution

### Phase 1 : Install ODBC Driver (30min)

**Windows :**
```powershell
# Télécharger DuckDB ODBC Driver
# https://github.com/duckdb/duckdb-odbc/releases

# Installer .msi correspondant (x64 ou x86)
# Version: Latest stable

# Vérifier installation
# ODBC Data Sources (64-bit) → User DSN
```

**Configuration DSN :**
- Name: `FinanceSystem`
- Database: `C:\...\finance-system\data\finance.duckdb`
- Driver: DuckDB

---

### Phase 2 : Power BI Connection (15min)

**Dans Power BI Desktop :**

1. Get Data → Other → ODBC
2. Data source name (DSN): `FinanceSystem`
3. Advanced options → SQL statement (optional)
4. Load tables

**Connection String :**
```
Driver={DuckDB Driver};Database=C:\path\to\finance.duckdb;
```

---

### Phase 3 : Test & Validation (15min)

**Vérifications :**
- [ ] Connexion établie
- [ ] Tables visibles
- [ ] Refresh fonctionne
- [ ] Performance OK
- [ ] Requêtes DirectQuery OK

---

## 📦 Implémentation

### Prerequisites

- [ ] Power BI Desktop installé
- [ ] Admin rights (install ODBC driver)
- [ ] DuckDB database existante

### Steps

1. **Download ODBC Driver**
   - URL: https://github.com/duckdb/duckdb-odbc/releases
   - File: `duckdb_odbc-windows-amd64.msi` (or x86)

2. **Install Driver**
   - Run installer as Admin
   - Follow wizard
   - Default settings OK

3. **Configure DSN**
   - Open: ODBC Data Source Administrator (64-bit)
   - User DSN → Add
   - Select: DuckDB Driver
   - Name: `FinanceSystem`
   - Database: Browse to `finance.duckdb`
   - Test Connection
   - OK

4. **Power BI Setup**
   - Get Data → ODBC
   - Select: `FinanceSystem`
   - Connection Mode: DirectQuery or Import
   - Load tables

5. **Test**
   - Load transactions table
   - Create simple visual
   - Refresh data
   - Verify updates

---

## 🧪 Critères d'Acceptation

### Fonctionnel

- [ ] ODBC driver installé
- [ ] DSN configuré et testé
- [ ] Power BI connecté via ODBC
- [ ] Tables chargées correctement
- [ ] Refresh manuel fonctionne

### Performance

- [ ] Initial load < 5s (96 transactions)
- [ ] Refresh < 2s
- [ ] Requêtes < 1s

### Documentation

- [ ] Guide installation ODBC
- [ ] Connection string documentée
- [ ] Troubleshooting guide

---

## 🔗 Références

**Documentation :**
- DuckDB ODBC: https://duckdb.org/docs/api/odbc/overview
- Power BI ODBC: https://learn.microsoft.com/power-bi/connect-data/desktop-connect-odbc

**Code actuel :**
- `finance-system/scripts/export_for_powerbi.py` - Workaround actuel
- `finance-system/data/finance.duckdb` - Database cible

**Alternative :**
- DuckDB REST API (future option)
- Python connector pour Power BI

---

## 💡 Notes

### Workaround Actuel

Option B (Excel export) reste valide pour :
- Snapshots historiques
- Partage fichiers standalone
- Backup des données
- Pas de dépendance ODBC

### Avantages ODBC

- Refresh automatique programmable
- Power BI Service compatible
- Requêtes optimisées
- Moins de fichiers intermédiaires

### Limitations

- Nécessite admin rights
- Driver à maintenir (updates)
- Complexité setup initiale
- Possible issues permissions fichiers

---

## 📅 Timeline Estimée

**Total : 1-2h**

| Phase | Durée | Status |
|-------|-------|--------|
| Download driver | 5min | ⬜ Todo |
| Install + config DSN | 30min | ⬜ Todo |
| Power BI setup | 15min | ⬜ Todo |
| Tests | 15min | ⬜ Todo |
| Documentation | 15min | ⬜ Todo |

---

## ✅ Checklist

### Setup

- [ ] Download ODBC driver
- [ ] Install as Admin
- [ ] Configure DSN
- [ ] Test connection

### Power BI

- [ ] Connect via ODBC
- [ ] Load tables
- [ ] Test refresh
- [ ] Validate data

### Documentation

- [ ] Installation guide
- [ ] Troubleshooting
- [ ] Connection strings

---

**Créé pendant :** [[Session 2025-11-10 - Finance System MVP]]  
**Phase projet :** Phase 2+ - Optimizations  
**Priorité :** Low (workaround Excel fonctionne)  
**Bloquant :** Non  
**Nice-to-have :** Oui
