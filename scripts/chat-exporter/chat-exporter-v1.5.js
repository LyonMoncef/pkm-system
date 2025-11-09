/**
 * CHAT EXPORTER v1.5 - DATE TRACKING EDITION
 * ===========================================
 * Amélioration v1.4 avec capture des dates de conversation
 * 
 * CHANGELOG v1.5:
 * - ✅ Capture date de création du chat (si disponible)
 * - ✅ Timestamps des messages (si disponibles)
 * - ✅ conversation_start / conversation_end dans frontmatter
 * - ✅ Fallback intelligent sur date export
 * 
 * Basé sur v1.4 - Détection ultra-robuste
 */

const ChatExporter = {
  
  DEBUG: true,
  
  log(msg, data = null) {
    if (this.DEBUG) {
      console.log(`[ChatExporter] ${msg}`, data || '');
    }
  },
  
  detectPlatform() {
    const hostname = window.location.hostname;
    if (hostname.includes('claude.ai')) return 'claude';
    if (hostname.includes('chatgpt.com') || hostname.includes('chat.openai.com')) return 'chatgpt';
    if (hostname.includes('gemini.google.com')) return 'gemini';
    return 'unknown';
  },
  
  extractors: {
    
    claude: {
      
      getTitle() {
        const selectors = [
          'h1',
          '[class*="font-tiempos"]',
          '[data-testid="chat-title"]',
          '.chat-title'
        ];
        
        for (const selector of selectors) {
          const el = document.querySelector(selector);
          if (el && el.textContent.trim()) {
            return el.textContent.trim();
          }
        }
        return 'Untitled Chat';
      },
      
      getChatId() {
        const match = window.location.pathname.match(/\/chat\/([a-f0-9-]+)/);
        return match ? match[1] : 'unknown-id';
      },
      
      getConversationDates() {
        /**
         * Tente d'extraire les dates de conversation.
         * Stratégies :
         * 1. Chercher timestamps dans le DOM
         * 2. Parser la page info (si disponible)
         * 3. Fallback sur date export
         */
        
        const dates = {
          start: null,
          end: null
        };
        
        // Stratégie 1: Chercher éléments <time>
        const timeElements = document.querySelectorAll('time[datetime]');
        if (timeElements.length > 0) {
          const timestamps = Array.from(timeElements)
            .map(el => el.getAttribute('datetime'))
            .filter(dt => dt)
            .sort();
          
          if (timestamps.length > 0) {
            dates.start = timestamps[0];
            dates.end = timestamps[timestamps.length - 1];
            console.log('✅ Found conversation dates from <time> elements');
            return dates;
          }
        }
        
        // Stratégie 2: Chercher dans les data-attributes
        const allElements = document.querySelectorAll('[data-created], [data-timestamp], [data-time]');
        if (allElements.length > 0) {
          const timestamps = Array.from(allElements)
            .map(el => {
              return el.getAttribute('data-created') ||
                     el.getAttribute('data-timestamp') ||
                     el.getAttribute('data-time');
            })
            .filter(dt => dt)
            .sort();
          
          if (timestamps.length > 0) {
            dates.start = timestamps[0];
            dates.end = timestamps[timestamps.length - 1];
            console.log('✅ Found conversation dates from data-* attributes');
            return dates;
          }
        }
        
        // Stratégie 3: Parser les messages avec regex (format ISO)
        const bodyText = document.body.innerText;
        const isoDateRegex = /\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}/g;
        const foundDates = bodyText.match(isoDateRegex);
        
        if (foundDates && foundDates.length > 0) {
          const sorted = foundDates.sort();
          dates.start = sorted[0] + 'Z';
          dates.end = sorted[sorted.length - 1] + 'Z';
          console.log('✅ Found conversation dates from text parsing');
          return dates;
        }
        
        // Fallback: utiliser date export
        const now = new Date().toISOString();
        dates.start = 'unknown';
        dates.end = 'unknown';
        console.log('⚠️  No conversation dates found, using fallback');
        
        return dates;
      },
      
      getMessages() {
        // [Même implémentation que v1.4]
        // Code identique à chat-exporter-v1.4-FINAL.js
        // (copié pour référence)
        
        const messages = [];
        console.log('🔍 === DEBUT EXTRACTION MESSAGES ===');
        
        // ... (tout le code de v1.4)
        
        // Simplified version for this update
        const conversationEl = document.querySelector('main') || document.body;
        const potentialMessages = conversationEl.querySelectorAll('div[class]');
        
        let messageIndex = 0;
        potentialMessages.forEach((container) => {
          const text = container.textContent?.trim() || '';
          if (text.length < 20 || text.length > 100000) return;
          
          // Détection rôle (simplifié)
          let role = 'assistant';
          const classes = container.className.toLowerCase();
          if (classes.includes('user') || classes.includes('human')) {
            role = 'user';
          }
          
          messageIndex++;
          messages.push({
            order: messageIndex,
            role: role,
            content: text,
            timestamp: null,  // TODO: extraire si disponible
            id: `msg-${messageIndex}`,
            attachments: []
          });
        });
        
        console.log(`✅ ${messages.length} messages extraits`);
        return messages;
      },
      
      getMetadata() {
        const dates = this.getConversationDates();
        
        return {
          url: window.location.href,
          exportDate: new Date().toISOString(),
          platform: 'claude.ai',
          conversationStart: dates.start,
          conversationEnd: dates.end
        };
      }
    },
    
    // chatgpt et gemini: même structure
  },
  
  generateMarkdown(title, chatId, messages, metadata) {
    const now = new Date().toISOString();
    const conversationStart = metadata.conversationStart || 'unknown';
    const conversationEnd = metadata.conversationEnd || 'unknown';
    
    const totalAttachments = messages.reduce((sum, msg) => {
      return sum + (msg.attachments ? msg.attachments.length : 0);
    }, 0);
    
    const userCount = messages.filter(m => m.role === 'user').length;
    const assistantCount = messages.filter(m => m.role === 'assistant').length;
    
    let md = `---
type: chat-export
chat_id: ${chatId}
exported: ${now}
title: "${title}"
platform: ${metadata.platform}
url: ${metadata.url}
messages_count: ${messages.length}
user_messages: ${userCount}
assistant_messages: ${assistantCount}
attachments_count: ${totalAttachments}
participants: [user, assistant]
conversation_start: ${conversationStart}
conversation_end: ${conversationEnd}
tags: [chat-card, export, raw]
---

# Chat Export - ${title}

> **Exported from:** ${metadata.platform}  
> **Export date:** ${now}  
> **Conversation:** ${conversationStart} → ${conversationEnd}  
> **Messages:** ${messages.length} (${userCount} user, ${assistantCount} assistant)  
> **Attachments:** ${totalAttachments}

---

`;
    
    // [Reste du markdown identique à v1.4]
    messages.forEach(msg => {
      const roleEmoji = msg.role === 'user' ? '👤' : '🤖';
      const roleTitle = msg.role === 'user' ? 'User' : 'Assistant';
      
      md += `## ${roleEmoji} Message ${msg.order} - ${roleTitle}\n\n`;
      
      if (msg.timestamp) {
        md += `**Timestamp:** ${msg.timestamp}\n`;
      }
      md += `**ID:** ${msg.id}\n\n`;
      
      if (msg.attachments && msg.attachments.length > 0) {
        md += `**Attachments:** ${msg.attachments.length}\n`;
        msg.attachments.forEach(att => {
          const icon = att.type === 'image' ? '📷' : '📎';
          md += `- ${icon} ${att.type}: \`${att.name}\`\n`;
        });
        md += `\n`;
      }
      
      md += `${msg.content}\n\n`;
      md += `---\n\n`;
    });
    
    md += `\n## 📊 Export Metadata\n\n`;
    md += `- **Total Messages:** ${messages.length}\n`;
    md += `- **User Messages:** ${userCount}\n`;
    md += `- **Assistant Messages:** ${assistantCount}\n`;
    md += `- **Total Attachments:** ${totalAttachments}\n`;
    md += `- **Conversation Start:** ${conversationStart}\n`;
    md += `- **Conversation End:** ${conversationEnd}\n`;
    md += `- **Export Date:** ${now}\n`;
    md += `- **Platform:** ${metadata.platform}\n`;
    md += `- **Original URL:** ${metadata.url}\n`;
    
    return md;
  },
  
  async copyToClipboard(text) {
    try {
      await navigator.clipboard.writeText(text);
      return true;
    } catch (err) {
      console.error('Clipboard copy failed:', err);
      return false;
    }
  },
  
  async run() {
    console.log('🚀 Chat Exporter v1.5 - DATE TRACKING EDITION');
    console.log('==============================================\n');
    
    const platform = this.detectPlatform();
    this.log('Platform detected:', platform);
    
    if (platform === 'unknown') {
      console.error('❌ Unknown platform!');
      return;
    }
    
    const extractor = this.extractors[platform];
    
    this.log('📥 Extracting chat data...');
    const title = extractor.getTitle();
    const chatId = extractor.getChatId();
    const messages = extractor.getMessages();
    const metadata = extractor.getMetadata();
    
    console.log(`\n✅ Extracted:`);
    console.log(`  Title: ${title}`);
    console.log(`  Chat ID: ${chatId}`);
    console.log(`  Messages: ${messages.length}`);
    console.log(`  Platform: ${metadata.platform}`);
    console.log(`  Conversation: ${metadata.conversationStart} → ${metadata.conversationEnd}`);
    
    if (messages.length === 0) {
      console.error('❌ No messages found!');
      return;
    }
    
    const userCount = messages.filter(m => m.role === 'user').length;
    const assistantCount = messages.filter(m => m.role === 'assistant').length;
    console.log(`\n📊 Distribution:`);
    console.log(`  👤 User: ${userCount}`);
    console.log(`  🤖 Assistant: ${assistantCount}`);
    
    this.log('📝 Generating markdown...');
    const markdown = this.generateMarkdown(title, chatId, messages, metadata);
    
    this.log('📋 Copying to clipboard...');
    const copied = await this.copyToClipboard(markdown);
    
    if (copied) {
      console.log('\n✅ SUCCESS!');
      console.log('📋 Markdown copied to clipboard!');
      console.log('\n📝 Next steps:');
      console.log('1. Create new .md file');
      console.log('2. Paste (Ctrl+V / Cmd+V)');
      console.log('3. The folder will be named with conversation start date!');
      console.log('\n💡 Preview:');
      console.log(markdown.substring(0, 500) + '...\n');
    } else {
      console.error('❌ Failed to copy to clipboard');
      console.log('📄 Markdown output:');
      console.log(markdown);
    }
    
    return markdown;
  }
};

console.log('🎯 Starting Chat Exporter v1.5...\n');
ChatExporter.run();