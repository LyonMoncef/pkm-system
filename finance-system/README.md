# 💰 Finance System MVP

> Personal Finance Management System - Extract, Load, Analyze

## 📊 Overview

Système de gestion financière personnelle extrayant des données de tickets OCR, les chargeant dans DuckDB, et les exportant pour Power BI.

**Status:** ✅ MVP Complete
**Version:** 1.0.0
**Date:** 2025-11-13

## 🎯 Features

- ✅ Extraction tickets depuis cartes atomisées
- ✅ Base de données DuckDB analytics-ready
- ✅ Exports Excel pour Power BI
- ✅ 96 transactions, 996.78€ tracked

## 📁 Structure
```
finance-system/
├── data/
│   ├── processed/
│   │   └── transactions.csv          # CSV nettoyé
│   └── finance.duckdb                # Database principale
├── scripts/
│   ├── extract_tickets_from_cards.py # Parse cartes → CSV
│   ├── load_to_duckdb.py             # CSV → DuckDB
│   └── export_for_powerbi.py         # DuckDB → Excel
└── exports/
    └── powerbi/
        ├── transactions.xlsx          # Transactions complètes
        ├── by_merchant.xlsx           # Agrégations enseignes
        ├── daily_timeline.xlsx        # Timeline quotidienne
        └── summary_stats.xlsx         # Stats globales
```

## 🚀 Usage

### 1. Extract Tickets from Cards
```bash
python3 scripts/extract_tickets_from_cards.py \
    --cards-dir "../vault BACKUP/.../cards" \
    --output data/processed/transactions.csv
```

### 2. Load to DuckDB
```bash
python3 scripts/load_to_duckdb.py \
    --csv data/processed/transactions.csv \
    --db data/finance.duckdb
```

### 3. Export for Power BI
```bash
python3 scripts/export_for_powerbi.py
```

### 4. Open Power BI

- Get Data → Excel
- Select: `exports/powerbi/transactions.xlsx`
- Create visualizations

## 📊 Data Summary

- **Transactions:** 96
- **Total:** 996.78€
- **Period:** 2025-09-23 to 2025-10-14
- **Merchants:** 5 (Leclerc, Action, Carrefour, Total, McDonald's)

## 🔧 Requirements
```bash
pip install duckdb pandas openpyxl
```

## 📝 Next Steps

- [ ] Power BI Dashboard creation
- [ ] More tickets scanning
- [ ] Manual categorization
- [ ] Budgets tracking
- [ ] ODBC connection (see backlog)

## 🔗 Related

- Backlog: ODBC Direct Connection
- Vault: `03_Finance/` (future)
- Conv: `2025-11-11-Ticket-receipt-data-extraction`
