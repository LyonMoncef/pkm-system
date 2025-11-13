#!/usr/bin/env python3
"""
Export DuckDB to Excel for Power BI - MVP v1.1
==============================================

Export avec fix timezone pour Excel.
"""

import duckdb
import pandas as pd
from pathlib import Path


def remove_timezone(df):
    """Remove timezone from datetime columns for Excel compatibility."""
    for col in df.columns:
        if pd.api.types.is_datetime64_any_dtype(df[col]):
            if df[col].dt.tz is not None:
                df[col] = df[col].dt.tz_localize(None)
    return df


def main():
    print("=" * 70)
    print("📊 EXPORT FOR POWER BI - MVP v1.1")
    print("=" * 70)
    print()
    
    db_path = Path("finance-system/data/finance.duckdb")
    export_dir = Path("finance-system/exports/powerbi")
    export_dir.mkdir(parents=True, exist_ok=True)
    
    if not db_path.exists():
        print(f"❌ Database not found: {db_path}")
        return 1
    
    print(f"📂 Database: {db_path}")
    print(f"📂 Export to: {export_dir}\n")
    
    conn = duckdb.connect(str(db_path))
    
    # 1. Transactions complètes
    print("📋 Exporting transactions...")
    df_trans = conn.execute("SELECT * FROM transactions ORDER BY date, heure").df()
    
    # Remove timezone pour Excel
    df_trans = remove_timezone(df_trans)
    
    excel_path = export_dir / "transactions.xlsx"
    df_trans.to_excel(excel_path, index=False, engine='openpyxl')
    print(f"  ✅ {excel_path}")
    print(f"     {len(df_trans)} rows")
    
    # 2. Aggregation par merchant
    print("\n📋 Exporting by merchant...")
    df_merchant = conn.execute("""
    SELECT 
        merchant,
        COUNT(*) as transaction_count,
        SUM(amount) as total_amount,
        AVG(amount) as avg_amount,
        MIN(amount) as min_amount,
        MAX(amount) as max_amount
    FROM transactions
    GROUP BY merchant
    ORDER BY total_amount DESC
    """).df()
    
    merchant_path = export_dir / "by_merchant.xlsx"
    df_merchant.to_excel(merchant_path, index=False, engine='openpyxl')
    print(f"  ✅ {merchant_path}")
    print(f"     {len(df_merchant)} merchants")
    
    # 3. Timeline quotidienne
    print("\n📋 Exporting daily timeline...")
    df_daily = conn.execute("""
    SELECT 
        date,
        COUNT(*) as transaction_count,
        SUM(amount) as daily_total,
        AVG(amount) as daily_avg
    FROM transactions
    WHERE date IS NOT NULL
    GROUP BY date
    ORDER BY date
    """).df()
    
    daily_path = export_dir / "daily_timeline.xlsx"
    df_daily.to_excel(daily_path, index=False, engine='openpyxl')
    print(f"  ✅ {daily_path}")
    print(f"     {len(df_daily)} days")
    
    # 4. Stats globales
    print("\n📋 Exporting summary stats...")
    df_stats = conn.execute("""
    SELECT 
        COUNT(*) as total_transactions,
        COUNT(DISTINCT merchant) as unique_merchants,
        SUM(amount) as total_amount,
        AVG(amount) as avg_amount,
        MIN(date) as first_date,
        MAX(date) as last_date
    FROM transactions
    WHERE date IS NOT NULL
    """).df()
    
    stats_path = export_dir / "summary_stats.xlsx"
    df_stats.to_excel(stats_path, index=False, engine='openpyxl')
    print(f"  ✅ {stats_path}")
    
    conn.close()
    
    # Résumé
    print("\n" + "=" * 70)
    print("✅ EXPORT COMPLETE")
    print("=" * 70)
    print(f"\n📂 Files in: {export_dir.absolute()}")
    print("\nFiles created:")
    print("  1. transactions.xlsx       - All transactions")
    print("  2. by_merchant.xlsx        - Merchant aggregations")
    print("  3. daily_timeline.xlsx     - Daily totals")
    print("  4. summary_stats.xlsx      - Global stats")
    
    print("\n🎯 Next steps:")
    print("  1. Open Power BI Desktop")
    print("  2. Get Data → Excel Workbook")
    print("  3. Select: transactions.xlsx")
    print("  4. Load data")
    print("  5. Create visualizations!")
    
    print(f"\n📊 Quick preview:")
    print(f"  Total amount: {df_trans['amount'].sum():.2f}€")
    print(f"  Transactions: {len(df_trans)}")
    print(f"  Date range: {df_trans['date'].min()} to {df_trans['date'].max()}")
    
    return 0


if __name__ == '__main__':
    exit(main())
