# Chat Exporter

Extract complete chat conversations from Claude.ai, ChatGPT, or Gemini into structured markdown files.

## Version

**Current:** 1.1.0 (2025-11-03)

### What's New in v1.1.0 ✨

- ✅ **User messages now captured!** Detects dark background message blocks
- ✅ **Attachment names extracted** - File names from uploaded images, documents, etc.
- ✅ **Enhanced metadata** - User/assistant message counts, attachment counts
- ✅ **Better reliability** - Multiple detection strategies + fallback method

See [CHANGELOG.md](CHANGELOG.md) for full details.

## Quick Start

1. Open chat on target platform
2. F12 → Console
3. Copy/paste entire `chat-exporter.js`
4. Press Enter
5. Markdown auto-copied to clipboard (if permissions allow)

## Supported Platforms

- ✅ Claude.ai (Full support - v1.1.0)
- ⚠️ ChatGPT (Stub - needs testing)
- ⚠️ Gemini (Stub - to implement)

## Files

- `chat-exporter.js` - Main script (v1.1.0)
- `CHANGELOG.md` - Version history
- `README.md` - This file
