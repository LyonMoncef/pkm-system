#!/usr/bin/env python3
"""
Script simplifié pour parser le chat export Power BI / Tickets de caisse
et proposer une structure de cartes atomiques.
"""

import json
import re
from typing import List, Dict

def load_chat(file_path: str) -> str:
    """Charge et déséchape le fichier export."""
    with open(file_path, 'r', encoding='utf-8') as f:
        raw = f.read()
    return json.loads(raw)  # Déséchaper la string JSON

def extract_messages(content: str, start_msg: int = 36) -> List[Dict]:
    """Extrait les messages à partir du message start_msg."""
    messages = []
    lines = content.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Détecter un header de message
        if line.startswith('## ') and 'Message' in line:
            # Extraire infos
            role_match = re.search(r'(User|Assistant)', line)
            num_match = re.search(r'Message (\d+)', line)
            
            if role_match and num_match:
                msg_num = int(num_match.group(1))
                role = role_match.group(1).lower()
                
                # Skip les messages < start_msg
                if msg_num < start_msg:
                    i += 1
                    continue
                
                # Trouver le contenu (jusqu'au prochain message)
                content_start = i + 1
                content_end = i + 1
                
                for j in range(i + 1, len(lines)):
                    if lines[j].startswith('## ') and 'Message' in lines[j]:
                        content_end = j
                        break
                else:
                    content_end = len(lines)
                
                msg_content = '\n'.join(lines[content_start:content_end]).strip()
                
                # Extraire ID
                msg_id = ""
                if content_start < len(lines):
                    id_match = re.search(r'\*\*ID:\*\* (msg-\d+)', lines[content_start])
                    if id_match:
                        msg_id = id_match.group(1)
                
                messages.append({
                    'number': msg_num,
                    'role': role,
                    'id': msg_id,
                    'content': msg_content,
                    'length': len(msg_content)
                })
                
                i = content_end
        else:
            i += 1
    
    return messages

def analyze_message(msg: Dict) -> Dict:
    """Analyse un message pour en extraire les concepts clés."""
    content = msg['content']
    
    # Titres markdown (# mais pas ##)
    titles = re.findall(r'^# ([^#\n]+)', content, re.MULTILINE)
    titles += re.findall(r'^### ([^\n]+)', content, re.MULTILINE)
    
    # Listes importantes (**Xxx:**)
    key_points = re.findall(r'^\*\*([^:]+):\*\*', content, re.MULTILINE)
    
    # Blocs de code
    code_blocks = re.findall(r'```(\w+)?\n.*?```', content, re.DOTALL)
    
    # Pièces jointes
    attachments = re.findall(r'ðŸ"· Image: `([^`]+)`', content)
    attachments += re.findall(r'ðŸ" Document: `([^`]+)`', content)
    
    # Preview intelligent (premier paragraphe substantiel)
    paragraphs = [p.strip() for p in content.split('\n\n') if len(p.strip()) > 50]
    preview = paragraphs[0][:300] if paragraphs else content[:300]
    
    return {
        **msg,
        'titles': titles,
        'key_points': key_points[:5],  # Max 5
        'code_blocks': len(code_blocks),
        'attachments': attachments,
        'preview': preview
    }

def suggest_cards(messages: List[Dict], max_cards: int = 10) -> List[Dict]:
    """Suggère des cartes atomiques basées sur les messages."""
    cards = []
    
    for msg in messages[:max_cards]:
        analysis = analyze_message(msg)
        
        # Suggérer un titre de carte
        if analysis['titles']:
            suggested_title = analysis['titles'][0]
        elif analysis['key_points']:
            suggested_title = analysis['key_points'][0]
        elif analysis['role'] == 'user':
            suggested_title = f"Question: {analysis['preview'][:50]}..."
        else:
            suggested_title = f"Response: {analysis['preview'][:50]}..."
        
        # Déterminer le type de carte
        if analysis['code_blocks'] > 0:
            card_type = "Code Example"
        elif analysis['attachments']:
            card_type = "Data Extract"
        elif len(analysis['key_points']) > 3:
            card_type = "Structured Info"
        else:
            card_type = "Concept"
        
        cards.append({
            'card_number': len(cards) + 1,
            'message_number': msg['number'],
            'role': msg['role'],
            'suggested_title': suggested_title,
            'card_type': card_type,
            'has_attachments': len(analysis['attachments']) > 0,
            'has_code': analysis['code_blocks'] > 0,
            'complexity': len(analysis['key_points']) + analysis['code_blocks']
        })
    
    return cards

def print_report(messages: List[Dict], cards: List[Dict]):
    """Affiche un rapport lisible."""
    
    print("\n" + "="*80)
    print("📊 ANALYSE DU CHAT - Power BI / Tickets de Caisse")
    print("="*80)
    
    # Stats générales
    user_msgs = [m for m in messages if m['role'] == 'user']
    assistant_msgs = [m for m in messages if m['role'] == 'assistant']
    
    print(f"\n📈 STATISTIQUES")
    print("-"*80)
    print(f"Messages pertinents: {len(messages)}")
    print(f"  - User: {len(user_msgs)}")
    print(f"  - Assistant: {len(assistant_msgs)}")
    print(f"Messages skippés (UI): 35")
    
    # Cartes suggérées
    print(f"\n💎 CARTES ATOMIQUES SUGGÉRÉES ({len(cards)} premières)")
    print("="*80)
    
    for card in cards:
        role_emoji = "👤" if card['role'] == 'user' else "🤖"
        attach_emoji = "📎" if card['has_attachments'] else ""
        code_emoji = "💻" if card['has_code'] else ""
        
        print(f"\n{card['card_number']}. {role_emoji} Message #{card['message_number']} {attach_emoji}{code_emoji}")
        print(f"   Type: {card['card_type']}")
        print(f"   Titre: {card['suggested_title']}")
        print(f"   Complexité: {'⭐' * min(card['complexity'], 5)}")
    
    # Aperçu des 3 premiers messages
    print(f"\n\n🔍 APERÇU DES 3 PREMIERS MESSAGES")
    print("="*80)
    
    for i, msg in enumerate(messages[:3], 1):
        analysis = analyze_message(msg)
        role_emoji = "👤" if msg['role'] == 'user' else "🤖"
        
        print(f"\n{i}. {role_emoji} Message #{msg['number']} ({msg['length']} chars)")
        
        if analysis['attachments']:
            print(f"   📎 Pièces jointes: {len(analysis['attachments'])}")
            print(f"      {analysis['attachments'][0]}")
        
        if analysis['titles']:
            print(f"   📑 Titres: {', '.join(analysis['titles'][:2])}")
        
        if analysis['key_points']:
            print(f"   🔑 Points clés: {', '.join(analysis['key_points'][:3])}")
        
        print(f"   📝 Aperçu:")
        print(f"      {analysis['preview'][:200]}...")

def main():
    print("🚀 PARSER CHAT EXPORT - POWER BI / TICKETS")
    print("="*80)
    
    # Charger
    print("\n📂 Chargement du fichier...")
    content = load_chat('/mnt/c/Users/idsmf/Projects/pkm-system/export_conv.md')

    print(f"✅ Fichier chargé ({len(content)} caractères)")
    
    # Extraire messages (skip les 35 premiers)
    print("\n💬 Extraction des messages pertinents (à partir de #36)...")
    messages = extract_messages(content, start_msg=36)
    print(f"✅ {len(messages)} messages extraits")
    
    # Analyser et suggérer cartes
    print("\n🎯 Génération des suggestions de cartes...")
    cards = suggest_cards(messages, max_cards=10)
    print(f"✅ {len(cards)} cartes suggérées")
    
    # Afficher rapport
    print_report(messages, cards)
    
    # Sauvegarder résultats
    output = {
        'messages': [analyze_message(m) for m in messages[:10]],
        'suggested_cards': cards,
        'stats': {
            'total_messages': len(messages),
            'user_messages': len([m for m in messages if m['role'] == 'user']),
            'assistant_messages': len([m for m in messages if m['role'] == 'assistant'])
        }
    }
    
    output_file = '/mnt/c/Users/idsmf/Projects/pkm-system/chat_analysis.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    
    print(f"\n\n💾 Résultats détaillés: {output_file}")
    print("\n✅ ANALYSE TERMINÉE")
    print("="*80)
    print("\n👉 Lance le script sur ton poste et on valide ensemble les résultats !")

if __name__ == "__main__":
    main()
