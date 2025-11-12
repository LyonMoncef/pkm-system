#!/usr/bin/env python3
"""
Load Transactions to DuckDB - MVP v1.1
======================================

Charge le CSV dans DuckDB avec gestion des dates invalides.

Usage:
    python load_to_duckdb.py \
        --csv ../data/processed/transactions.csv \
        --db ../data/finance.duckdb
"""

import argparse
import duckdb
from pathlib import Path


def create_database(db_path: Path):
    """Crée la database et les tables."""
    
    conn = duckdb.connect(str(db_path))
    
    # Table transactions
    conn.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY,
        date DATE,
        heure TIME,
        merchant TEXT NOT NULL,
        magasin TEXT,
        amount DECIMAL(10,2) NOT NULL,
        category TEXT,
        payment_method TEXT,
        articles_count INTEGER,
        source TEXT,
        raw_data TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    # Table categories
    conn.execute("""
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        parent_id INTEGER REFERENCES categories(id),
        type TEXT DEFAULT 'expense'
    )
    """)
    
    # Insérer catégories de base
    conn.execute("""
    INSERT OR IGNORE INTO categories (id, name, type) VALUES
        (1, 'Alimentation', 'expense'),
        (2, 'Transport', 'expense'),
        (3, 'Loisirs', 'expense'),
        (4, 'Autre', 'expense')
    """)
    
    print("✅ Database structure created")
    
    return conn


def load_csv(conn, csv_path: Path):
    """Charge le CSV dans la table transactions."""
    
    print(f"📥 Loading CSV: {csv_path}")
    
    # Compter lignes d'abord
    result = conn.execute(f"""
    SELECT COUNT(*) as count
    FROM read_csv_auto('{csv_path}')
    """).fetchone()
    
    csv_count = result[0]
    print(f"  Found {csv_count} rows in CSV")
    
    # Charger dans table avec TRY_CAST pour dates invalides
    conn.execute(f"""
    INSERT INTO transactions 
        (date, heure, merchant, magasin, amount, category, 
         payment_method, articles_count, source, raw_data)
    SELECT 
        TRY_CAST(date AS DATE),
        TRY_CAST(heure AS TIME),
        merchant,
        magasin,
        CAST(amount AS DECIMAL(10,2)),
        category,
        payment_method,
        CAST(articles_count AS INTEGER),
        source,
        raw_data
    FROM read_csv_auto('{csv_path}')
    WHERE 
        merchant IS NOT NULL 
        AND amount IS NOT NULL
        AND date NOT LIKE '%XX%'
    """)
    
    # Vérifier
    result = conn.execute("SELECT COUNT(*) FROM transactions").fetchone()
    db_count = result[0]
    
    # Compter lignes rejetées
    rejected = csv_count - db_count
    
    print(f"✅ Loaded {db_count} transactions into database")
    if rejected > 0:
        print(f"⚠️  Skipped {rejected} rows (invalid dates or data)")
    
    return db_count


def run_analytics(conn):
    """Quelques analytics de base."""
    
    print("\n📊 Quick Analytics:")
    
    # Total amount
    result = conn.execute("""
    SELECT 
        COUNT(*) as transactions,
        SUM(amount) as total_amount,
        AVG(amount) as avg_amount,
        MIN(amount) as min_amount,
        MAX(amount) as max_amount
    FROM transactions
    """).fetchone()
    
    print(f"  Transactions: {result[0]}")
    print(f"  Total: {result[1]:.2f}€")
    print(f"  Average: {result[2]:.2f}€")
    print(f"  Min: {result[3]:.2f}€")
    print(f"  Max: {result[4]:.2f}€")
    
    # By merchant
    print("\n  By merchant:")
    results = conn.execute("""
    SELECT 
        merchant,
        COUNT(*) as count,
        SUM(amount) as total
    FROM transactions
    GROUP BY merchant
    ORDER BY total DESC
    """).fetchall()
    
    for merchant, count, total in results:
        print(f"    - {merchant}: {count} trans, {total:.2f}€")
    
    # By date (only valid dates)
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
    
    # Invalid dates count
    result = conn.execute("""
    SELECT COUNT(*) FROM transactions WHERE date IS NULL
    """).fetchone()
    
    if result[0] > 0:
        print(f"\n  ⚠️  {result[0]} transactions with invalid/missing dates")


def main():
    parser = argparse.ArgumentParser(description='Load CSV to DuckDB')
    parser.add_argument('--csv', type=Path, required=True,
                       help='Input CSV file')
    parser.add_argument('--db', type=Path, required=True,
                       help='Output DuckDB database file')
    
    args = parser.parse_args()
    
    print("=" * 70)
    print("💾 LOAD TO DUCKDB - MVP v1.1")
    print("=" * 70)
    print()
    
    # Create/connect database
    args.db.parent.mkdir(parents=True, exist_ok=True)
    conn = create_database(args.db)
    
    # Load CSV
    count = load_csv(conn, args.csv)
    
    if count == 0:
        print("❌ No data loaded!")
        return 1
    
    # Analytics
    run_analytics(conn)
    
    # Close
    conn.close()
    
    print(f"\n✅ Database ready: {args.db}")
    print(f"   {count} transactions loaded")
    print("\n🎯 Next: Connect Power BI to this database!")
    
    return 0


if __name__ == '__main__':
    exit(main())
