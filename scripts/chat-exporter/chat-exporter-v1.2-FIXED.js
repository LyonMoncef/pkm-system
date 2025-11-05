/**
 * CHAT EXPORTER - Multi-Platform
 * Version: 1.2.0
 * Date: 2025-11-05
 * 
 * CHANGELOG v1.2.0:
 * - 🔧 Fixed DOM selectors for Claude.ai (2025 UI)
 * - ✅ More robust message detection
 * - ✅ Better fallback strategies
 */

const ChatExporter = {
  
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
      
      getMessages() {
        const messages = [];
        
        // Strategy 1: Find all message containers
        let messageBlocks = document.querySelectorAll('[class*="font-claude"]');
        
        // Strategy 2: If strategy 1 fails, try broader search
        if (messageBlocks.length === 0) {
          console.log('Strategy 1 failed, trying strategy 2...');
          messageBlocks = document.querySelectorAll('div[class*="group"]');
        }
        
        // Strategy 3: Last resort - find by structure
        if (messageBlocks.length === 0) {
          console.log('Strategy 2 failed, trying strategy 3...');
          const allDivs = document.querySelectorAll('div');
          messageBlocks = Array.from(allDivs).filter(div => {
            const text = div.textContent.trim();
            return text.length > 20 && text.length < 50000;
          });
        }
        
        console.log(`Found ${messageBlocks.length} potential message blocks`);
        
        let messageIndex = 0;
        const seenContent = new Set();
        
        messageBlocks.forEach((block, idx) => {
          // Try to determine role
          const classList = block.className || '';
          const parentClass = block.parentElement?.className || '';
          
          // User detection heuristics
          const isUser = classList.includes('bg-') && classList.includes('surface') ||
                        parentClass.includes('user') ||
                        block.querySelector('img') !== null ||
                        classList.includes('black') ||
                        classList.includes('gray-');
          
          const role = isUser ? 'user' : 'assistant';
          
          // Extract content
          let content = '';
          let attachments = [];
          
          // Try to get clean text content
          const textContent = block.textContent?.trim() || '';
          
          // Skip if too short or duplicate
          if (textContent.length < 10 || seenContent.has(textContent)) {
            return;
          }
          
          content = textContent;
          seenContent.add(textContent);
          
          // Look for attachments
          const images = block.querySelectorAll('img[alt]');
          images.forEach(img => {
            const alt = img.getAttribute('alt') || 'image';
            attachments.push({
              type: 'image',
              name: alt
            });
          });
          
          // Add message
          if (content) {
            messageIndex++;
            messages.push({
              order: messageIndex,
              role: role,
              content: content,
              attachments: attachments.length > 0 ? attachments : undefined,
              timestamp: null,
              id: `msg-${messageIndex}`
            });
          }
        });
        
        console.log(`Extracted ${messages.length} messages`);
        return messages;
      },
      
      getMetadata() {
        return {
          url: window.location.href,
          exportDate: new Date().toISOString(),
          platform: 'claude.ai'
        };
      }
    },
    
    chatgpt: {
      getTitle() {
        const titleEl = document.querySelector('h1, .text-2xl');
        return titleEl ? titleEl.textContent.trim() : 'Untitled Chat';
      },
      
      getChatId() {
        const match = window.location.pathname.match(/\/c\/([a-f0-9-]+)/);
        return match ? match[1] : 'unknown-id';
      },
      
      getMessages() {
        const messages = [];
        const messageEls = document.querySelectorAll('[data-message-author-role]');
        
        messageEls.forEach((el, index) => {
          const role = el.getAttribute('data-message-author-role');
          const content = el.querySelector('.markdown, .whitespace-pre-wrap')?.textContent.trim() || '';
          
          if (content) {
            messages.push({
              order: index + 1,
              role: role,
              content: content,
              timestamp: null,
              id: `msg-${index + 1}`
            });
          }
        });
        
        return messages;
      },
      
      getMetadata() {
        return {
          url: window.location.href,
          exportDate: new Date().toISOString(),
          platform: 'chatgpt.com'
        };
      }
    },
    
    gemini: {
      getTitle() {
        return 'Gemini Chat';
      },
      
      getChatId() {
        return 'unknown-id';
      },
      
      getMessages() {
        console.warn('Gemini extractor not fully implemented yet');
        return [];
      },
      
      getMetadata() {
        return {
          url: window.location.href,
          exportDate: new Date().toISOString(),
          platform: 'gemini.google.com'
        };
      }
    }
  },
  
  generateMarkdown(title, chatId, messages, metadata) {
    const now = new Date().toISOString();
    const dateStart = messages[0]?.timestamp || 'unknown';
    const dateEnd = messages[messages.length - 1]?.timestamp || 'unknown';
    
    const totalAttachments = messages.reduce((sum, msg) => {
      return sum + (msg.attachments ? msg.attachments.length : 0);
    }, 0);
    
    let md = `---
type: chat-export
chat_id: ${chatId}
exported: ${now}
title: "${title}"
platform: ${metadata.platform}
url: ${metadata.url}
messages_count: ${messages.length}
user_messages: ${messages.filter(m => m.role === 'user').length}
assistant_messages: ${messages.filter(m => m.role === 'assistant').length}
attachments_count: ${totalAttachments}
participants: [user, assistant]
date_start: ${dateStart}
date_end: ${dateEnd}
tags: [chat-card, export, raw]
---

# Chat Export - ${title}

> **Exported from:** ${metadata.platform}  
> **Date:** ${now}  
> **Messages:** ${messages.length} (${messages.filter(m => m.role === 'user').length} user, ${messages.filter(m => m.role === 'assistant').length} assistant)  
> **Attachments:** ${totalAttachments}

---

`;
    
    messages.forEach(msg => {
      const roleEmoji = msg.role === 'user' ? '👤' : '🤖';
      const roleTitle = msg.role === 'user' ? 'User' : 'Assistant';
      
      md += `## ${roleEmoji} Message ${msg.order} - ${roleTitle}\n\n`;
      
      if (msg.timestamp) {
        md += `**Timestamp:** ${msg.timestamp}  \n`;
      }
      md += `**ID:** ${msg.id}\n\n`;
      
      if (msg.attachments && msg.attachments.length > 0) {
        md += `**Attachments:** ${msg.attachments.length}\n`;
        msg.attachments.forEach((att, idx) => {
          if (att.type === 'image') {
            md += `- 📷 Image: \`${att.name}\`\n`;
          } else {
            md += `- 📎 File: \`${att.name}\`\n`;
          }
        });
        md += `\n`;
      }
      
      md += `${msg.content}\n\n`;
      md += `---\n\n`;
    });
    
    md += `\n## 📊 Export Metadata\n\n`;
    md += `- **Total Messages:** ${messages.length}\n`;
    md += `- **User Messages:** ${messages.filter(m => m.role === 'user').length}\n`;
    md += `- **Assistant Messages:** ${messages.filter(m => m.role === 'assistant').length}\n`;
    md += `- **Total Attachments:** ${totalAttachments}\n`;
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
    console.log('🚀 Chat Exporter v1.2.0');
    console.log('========================\n');
    
    const platform = this.detectPlatform();
    console.log(`📍 Platform detected: ${platform}`);
    
    if (platform === 'unknown') {
      console.error('❌ Unknown platform! This script works on Claude.ai, ChatGPT, or Gemini.');
      return;
    }
    
    const extractor = this.extractors[platform];
    
    console.log('📥 Extracting chat data...');
    const title = extractor.getTitle();
    const chatId = extractor.getChatId();
    const messages = extractor.getMessages();
    const metadata = extractor.getMetadata();
    
    console.log(`\n✅ Extracted:
  Title: ${title}
  Chat ID: ${chatId}
  Messages: ${messages.length}
  Platform: ${metadata.platform}
`);
    
    if (messages.length === 0) {
      console.error('❌ No messages found! Check DOM selectors.');
      return;
    }
    
    console.log('📝 Generating markdown...');
    const markdown = this.generateMarkdown(title, chatId, messages, metadata);
    
    console.log('📋 Copying to clipboard...');
    const copied = await this.copyToClipboard(markdown);
    
    if (copied) {
      console.log('\n✅ SUCCESS!');
      console.log('📋 Markdown copied to clipboard!');
      console.log('\n📝 Next steps:');
      console.log('1. Create new .md file in Obsidian');
      console.log('2. Paste (Ctrl+V / Cmd+V)');
      console.log('3. Save as: Chat-Export-[date].md');
      console.log('\n💡 Preview first lines:');
      console.log(markdown.substring(0, 500) + '...\n');
    } else {
      console.error('❌ Failed to copy to clipboard');
      console.log('📄 Markdown output:');
      console.log(markdown);
    }
    
    return markdown;
  }
};

console.log('🎯 Starting Chat Exporter...\n');
ChatExporter.run();
