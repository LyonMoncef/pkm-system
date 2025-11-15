#!/usr/bin/env python3
"""
Export Clean for Power BI - with id column
"""
import duckdb
import pandas as pd
from pathlib import Path

db_path = Path("finance-system/data/finance.duckdb")
export_dir = Path("finance-system/exports/powerbi")

print("="*70)
print("📊 CLEAN EXPORT FOR POWER BI")
print("="*70)

conn = duckdb.connect(str(db_path))

# Export articles_detail avec TOUTES colonnes
print("\n📋 Exporting articles_detail...")

df = conn.execute("""
SELECT 
    id,
    transaction_id,
    date,
    merchant,
    magasin,
    article,
    quantite,
    prix_unitaire,
    prix_total,
    category_main,
    category_sub,
    tags
FROM articles_detail
ORDER BY id
""").df()

# Remove timezone pour Excel
for col in df.columns:
    if pd.api.types.is_datetime64_any_dtype(df[col]):
        if df[col].dt.tz is not None:
            df[col] = df[col].dt.tz_localize(None)

# Save
excel_path = export_dir / "articles_detail.xlsx"
df.to_excel(excel_path, index=False, engine='openpyxl')

print(f"  ✅ {excel_path}")
print(f"     {len(df)} rows, {len(df.columns)} columns")

# Export transactions aussi
print("\n📋 Exporting transactions...")

df_trans = conn.execute("""
SELECT 
    id,
    date,
    heure,
    merchant,
    magasin,
    amount,
    category,
    payment_method,
    articles_count,
    source,
    raw_data
FROM transactions
ORDER BY date, heure
""").df()

# Remove timezone
for col in df_trans.columns:
    if pd.api.types.is_datetime64_any_dtype(df_trans[col]):
        if df_trans[col].dt.tz is not None:
            df_trans[col] = df_trans[col].dt.tz_localize(None)

trans_path = export_dir / "transactions.xlsx"
df_trans.to_excel(trans_path, index=False, engine='openpyxl')

print(f"  ✅ {trans_path}")
print(f"     {len(df_trans)} rows")

conn.close()

print("\n" + "="*70)
print("✅ EXPORT COMPLETE - Ready for Power BI")
print("="*70)
print("\nNext steps:")
print("1. Open Power BI Desktop")
print("2. Click 'Refresh' (Actualiser)")
print("3. Should work now!")
