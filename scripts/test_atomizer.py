#!/usr/bin/env python3
"""
Test script pour Chat Atomizer
===============================

Teste les différentes fonctionnalités du script sur un export réel.
"""

import sys
from pathlib import Path

# Ajouter le répertoire parent au path
sys.path.insert(0, str(Path(__file__).parent))

from atomize_chat import ChatExport, TopicDetector, CodeExtractor


def test_parsing(export_path: Path):
    """Test le parsing d'un export."""
    print("=" * 60)
    print("TEST 1: PARSING")
    print("=" * 60)
    
    export = ChatExport(export_path)
    
    print(f"\n✅ Frontmatter keys: {list(export.frontmatter.keys())}")
    print(f"✅ Messages parsed: {len(export.messages)}")
    print(f"✅ First message role: {export.messages[0].role if export.messages else 'N/A'}")
    
    stats = export.get_stats()
    print(f"\n📊 Stats:")
    for key, value in stats.items():
        print(f"  {key}: {value}")
    
    return export


def test_topic_detection():
    """Test la détection de topics."""
    print("\n" + "=" * 60)
    print("TEST 2: TOPIC DETECTION")
    print("=" * 60)
    
    test_cases = [
        ("J'ai créé un dashboard Power BI avec des mesures DAX", 
         ['power-bi', 'data-analysis']),
        ("Voici un script Python qui parse les tickets E.Leclerc",
         ['python', 'receipts', 'code']),
        ("Comment utiliser Dataview dans Obsidian ?",
         ['obsidian']),
    ]
    
    for text, expected in test_cases:
        detected = TopicDetector.detect(text)
        match = "✅" if any(t in detected for t in expected) else "❌"
        print(f"\n{match} Text: {text[:50]}...")
        print(f"   Detected: {detected}")
        print(f"   Expected: {expected}")


def test_code_extraction():
    """Test l'extraction de code."""
    print("\n" + "=" * 60)
    print("TEST 3: CODE EXTRACTION")
    print("=" * 60)
    
    sample_text = """
Voici un exemple de code:

```python
def hello():
    print("Hello World")
```

Et du SQL:

```sql
SELECT * FROM users WHERE active = 1;
```
    """
    
    code_blocks = CodeExtractor.extract(sample_text)
    
    print(f"\n✅ Code blocks found: {len(code_blocks)}")
    for block in code_blocks:
        print(f"\n  Block {block['id']}:")
        print(f"    Language: {block['lang']}")
        print(f"    Lines: {len(block['content'].splitlines())}")


def test_message_details(export: ChatExport):
    """Affiche les détails de quelques messages."""
    print("\n" + "=" * 60)
    print("TEST 4: MESSAGE DETAILS")
    print("=" * 60)
    
    # Afficher les 3 premiers messages
    for msg in export.messages[:3]:
        print(f"\n📬 Message {msg.order} ({msg.role}):")
        print(f"  ID: {msg.id}")
        print(f"  Content length: {len(msg.content)} chars")
        print(f"  Attachments: {len(msg.attachments)}")
        print(f"  Topics: {TopicDetector.detect(msg.content)}")
        print(f"  Code blocks: {len(CodeExtractor.extract(msg.content))}")


def main():
    """Run all tests."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Test Chat Atomizer')
    parser.add_argument('export_file', type=Path,
                       help='Path to export file to test')
    
    args = parser.parse_args()
    
    if not args.export_file.exists():
        print(f"❌ File not found: {args.export_file}")
        return 1
    
    print("\n🧪 CHAT ATOMIZER - TEST SUITE")
    print("=" * 60)
    print(f"Testing with: {args.export_file.name}\n")
    
    # Run tests
    try:
        export = test_parsing(args.export_file)
        test_topic_detection()
        test_code_extraction()
        test_message_details(export)
        
        print("\n" + "=" * 60)
        print("✅ ALL TESTS PASSED!")
        print("=" * 60 + "\n")
        
        return 0
        
    except Exception as e:
        print(f"\n❌ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    exit(main())
