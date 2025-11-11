#!/usr/bin/env python3
"""
Extract Tickets from Atomized Cards - MVP v1
============================================

Parse les cartes de la conv ticket/receipt et extrait les données.

Usage:
    python extract_tickets_from_cards.py \
        --cards-dir "path/to/cards" \
        --output ../data/processed/transactions.csv
"""

import argparse
import json
import re
from pathlib import Path
from datetime import datetime
import csv
from typing import List, Dict, Optional


def extract_json_from_card(content: str) -> Optional[Dict]:
    """
    Extrait bloc JSON d'une carte.
    Nettoie les backslashes échappés.
    """
    # Pattern pour bloc JSON
    pattern = r'json\s*(\{.*?\})\s*(?:```|$)'
    
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        return None
    
    json_text = match.group(1)
    
    # Nettoyer les backslashes échappés du markdown
    json_text = json_text.replace('\\"', '"')
    json_text = json_text.replace('\\n', '')
    
    try:
        data = json.loads(json_text)
        return data
    except json.JSONDecodeError as e:
        print(f"  ⚠️  JSON parse error: {e}")
        return None


def extract_csv_from_card(content: str) -> List[Dict]:
    """
    Extrait lignes CSV d'une carte.
    """
    transactions = []
    
    # Pattern pour lignes CSV
    pattern = r'csv\s*(.*?)(?:\n\n|---|\Z)'
    
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        return []
    
    csv_text = match.group(1).strip()
    lines = csv_text.split('\n')
    
    if len(lines) < 2:
        return []
    
    # Parser CSV
    reader = csv.DictReader(lines)
    for row in reader:
        transactions.append(row)
    
    return transactions


def json_to_transaction(data: Dict) -> Dict:
    """
    Convert JSON ticket to flat transaction dict.
    """
    # Calculer total des articles
    total = data.get('total_ttc', 0)
    
    # Si pas de total, calculer depuis articles
    if not total and 'articles' in data:
        total = sum(float(art.get('prix_total', 0)) for art in data['articles'])
    
    return {
        'date': data.get('date', ''),
        'heure': data.get('heure', ''),
        'merchant': data.get('enseigne', ''),
        'magasin': data.get('magasin', ''),
        'amount': float(total),
        'category': 'auto',  # À catégoriser après
        'payment_method': data.get('mode_paiement', ''),
        'articles_count': len(data.get('articles', [])),
        'source': 'json',
        'raw_data': json.dumps(data)
    }


def csv_to_transaction(row: Dict) -> Dict:
    """
    Convert CSV row to transaction dict.
    """
    return {
        'date': row.get('date', ''),
        'heure': row.get('heure', ''),
        'merchant': row.get('enseigne', ''),
        'magasin': row.get('magasin', ''),
        'amount': float(row.get('total_ttc', row.get('prix_total', 0))),
        'category': 'auto',
        'payment_method': '',
        'articles_count': 1,  # CSV = 1 ligne par article généralement
        'source': 'csv',
        'raw_data': json.dumps(row)
    }


def process_card(card_path: Path) -> List[Dict]:
    """
    Process une carte et extrait transactions.
    Returns list car une carte peut avoir plusieurs articles CSV.
    """
    content = card_path.read_text(encoding='utf-8')
    transactions = []
    
    # Essayer JSON d'abord
    json_data = extract_json_from_card(content)
    if json_data:
        trans = json_to_transaction(json_data)
        transactions.append(trans)
        return transactions
    
    # Sinon essayer CSV
    csv_rows = extract_csv_from_card(content)
    if csv_rows:
        for row in csv_rows:
            trans = csv_to_transaction(row)
            transactions.append(trans)
        return transactions
    
    return []


def extract_all_transactions(cards_dir: Path) -> List[Dict]:
    """Extract toutes les transactions de toutes les cartes."""
    all_transactions = []
    
    card_files = sorted(cards_dir.glob('*.md'))
    print(f"📂 Processing {len(card_files)} cards...")
    
    cards_with_data = 0
    
    for card_file in card_files:
        try:
            transactions = process_card(card_file)
            
            if transactions:
                cards_with_data += 1
                all_transactions.extend(transactions)
                
                # Afficher premiers résultats
                if cards_with_data <= 5:
                    for trans in transactions:
                        print(f"  ✅ {card_file.name}: {trans['merchant']} - {trans['amount']}€ ({trans['date']})")
        
        except Exception as e:
            print(f"  ⚠️  {card_file.name}: {e}")
    
    print(f"\n📊 Summary:")
    print(f"  Cards with data: {cards_with_data}")
    print(f"  Total transactions: {len(all_transactions)}")
    
    return all_transactions


def deduplicate_transactions(transactions: List[Dict]) -> List[Dict]:
    """
    Déduplique les transactions (même date/merchant/montant).
    """
    seen = set()
    unique = []
    
    for trans in transactions:
        key = (trans['date'], trans['merchant'], trans['amount'])
        if key not in seen:
            seen.add(key)
            unique.append(trans)
    
    print(f"  Removed {len(transactions) - len(unique)} duplicates")
    return unique


def save_to_csv(transactions: List[Dict], output_path: Path):
    """Sauvegarde en CSV."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    fieldnames = [
        'date', 'heure', 'merchant', 'magasin', 'amount',
        'category', 'payment_method', 'articles_count', 'source', 'raw_data'
    ]
    
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(transactions)
    
    print(f"\n✅ Saved to: {output_path}")
    print(f"   {len(transactions)} transactions")


def main():
    parser = argparse.ArgumentParser(description='Extract transactions from cards')
    parser.add_argument('--cards-dir', type=Path, required=True,
                       help='Directory with card .md files')
    parser.add_argument('--output', type=Path, required=True,
                       help='Output CSV file')
    
    args = parser.parse_args()
    
    print("=" * 70)
    print("🎫 TICKET EXTRACTION - MVP v1")
    print("=" * 70)
    print()
    
    # Extract
    transactions = extract_all_transactions(args.cards_dir)
    
    if not transactions:
        print("❌ No transactions found!")
        return 1
    
    # Deduplicate
    print("\n🔄 Deduplicating...")
    transactions = deduplicate_transactions(transactions)
    
    # Save
    save_to_csv(transactions, args.output)
    
    # Stats
    print("\n📈 Quick Stats:")
    merchants = {}
    total_amount = 0
    for trans in transactions:
        merchant = trans['merchant']
        merchants[merchant] = merchants.get(merchant, 0) + 1
        total_amount += trans['amount']
    
    print(f"  Total amount: {total_amount:.2f}€")
    print(f"  Unique merchants: {len(merchants)}")
    print(f"\n  Top merchants:")
    for merchant, count in sorted(merchants.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"    - {merchant}: {count} transactions")
    
    return 0


if __name__ == '__main__':
    exit(main())
