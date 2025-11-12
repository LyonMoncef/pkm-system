#!/usr/bin/env python3
"""
Load Transactions to DuckDB - MVP v1.2
======================================

Charge le CSV dans DuckDB avec auto-increment ID.
"""

import argparse
import duckdb
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description='Load CSV to DuckDB')
    parser.add_argument('--csv', type=Path, required=True)
    parser.add_argument('--db', type=Path, required=True)
    
    args = parser.parse_args()
    
    print("=" * 70)
    print("💾 LOAD TO DUCKDB - MVP v1.2")
    print("=" * 70)
    print()
    
    # Create database
    args.db.parent.mkdir(parents=True, exist_ok=True)
    conn = duckdb.connect(str(args.db))
    
    # Drop table si existe (fresh start)
    conn.execute("DROP TABLE IF EXISTS transactions")
    
    # Créer table SANS id dans la définition initiale
    print("📋 Creating table...")
    conn.execute("""
    CREATE TABLE transactions AS
    SELECT 
        ROW_NUMBER() OVER () as id,
        TRY_CAST(date AS DATE) as date,
        TRY_CAST(heure AS TIME) as heure,
        merchant,
        magasin,
        CAST(amount AS DECIMAL(10,2)) as amount,
        category,
        payment_method,
        CAST(articles_count AS INTEGER) as articles_count,
        source,
        raw_data,
        CURRENT_TIMESTAMP as created_at
    FROM read_csv_auto(?)
    WHERE 
        merchant IS NOT NULL 
        AND amount IS NOT NULL
        AND date NOT LIKE '%XX%'
    """, [str(args.csv)])
    
    # Stats
    result = conn.execute("SELECT COUNT(*) FROM transactions").fetchone()
    count = result[0]
    
    print(f"✅ Loaded {count} transactions")
    
    # Analytics
    print("\n📊 Quick Analytics:")
    
    result = conn.execute("""
    SELECT 
        COUNT(*) as transactions,
        SUM(amount) as total,
        AVG(amount) as avg,
        MIN(amount) as min,
        MAX(amount) as max
    FROM transactions
    """).fetchone()
    
    print(f"  Transactions: {result[0]}")
    print(f"  Total: {result[1]:.2f}€")
    print(f"  Average: {result[2]:.2f}€")
    print(f"  Range: {result[3]:.2f}€ - {result[4]:.2f}€")
    
    # By merchant
    print("\n  By merchant:")
    results = conn.execute("""
    SELECT merchant, COUNT(*) as count, SUM(amount) as total
    FROM transactions
    GROUP BY merchant
    ORDER BY total DESC
    """).fetchall()
    
    for merchant, count, total in results:
        print(f"    - {merchant}: {count} trans, {total:.2f}€")
    
    # By month
    print("\n  By month:")
    results = conn.execute("""
    SELECT 
        DATE_TRUNC('month', date) as month,
        COUNT(*) as count,
        SUM(amount) as total
    FROM transactions
    WHERE date IS NOT NULL
    GROUP BY month
    ORDER BY month DESC
    """).fetchall()
    
    for month, count, total in results:
        print(f"    - {month}: {count} trans, {total:.2f}€")
    
    conn.close()
    
    print(f"\n✅ Database ready: {args.db}")
    print("🎯 Next: Connect Power BI!")
    
    return 0


if __name__ == '__main__':
    exit(main())
