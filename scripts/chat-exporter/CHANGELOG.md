# CHANGELOG - Chat Exporter

All notable changes to the chat-exporter script will be documented in this file.

## [1.1.0] - 2025-11-03

### Added
- ✅ **User message detection improved**: Now captures messages in dark background blocks (user messages)
- ✅ **Attachment extraction**: Extracts names of uploaded files (images, documents, .md files, etc.)
- ✅ **Multiple detection strategies**: Uses class names, background colors, and DOM structure to identify user vs assistant messages
- ✅ **Enhanced metadata**: Frontmatter now includes `user_messages`, `assistant_messages`, and `attachments_count`
- ✅ **Attachment display in markdown**: Shows list of attachments with emoji indicators (📷 images, 📎 files)
- ✅ **Fallback extraction method**: If primary method fails, uses backup strategy to ensure no messages are lost

### Changed
- 🔄 **Message extraction logic**: Completely rewritten to handle both user and assistant messages more reliably
- 🔄 **Markdown generation**: Updated to display attachment information

### Fixed
- 🐛 **User messages not captured**: Fixed issue where user messages in dark containers were not extracted
- 🐛 **File names missing**: Now extracts file names from multiple DOM locations and attributes

### Technical Details
- Uses multi-selector strategy: `bg-token-main-surface-secondary`, `bg-black`, `user-message` classes
- Searches for attachments in: `img[alt]`, `[class*="file"]`, `[data-filename]`, `[data-attachment-name]`
- Fallback method activates if primary extraction returns 0 messages

---

## [1.0.0] - 2025-11-03

### Added
- ✅ Initial release
- ✅ Basic Claude.ai message extraction
- ✅ Markdown generation with YAML frontmatter
- ✅ Clipboard copy functionality
- ✅ Platform detection (Claude.ai, ChatGPT, Gemini)
- ✅ Stubs for ChatGPT and Gemini extractors

### Known Limitations (v1.0)
- ⚠️ User messages not always captured (fixed in v1.1.0)
- ⚠️ Attachment names not extracted (fixed in v1.1.0)

---

## Roadmap

### [1.2.0] - Planned
- [ ] ChatGPT extractor fully implemented and tested
- [ ] Gemini extractor fully implemented and tested
- [ ] Code block preservation improvement
- [ ] Image URL extraction for inline images

### [2.0.0] - Future
- [ ] Browser extension version
- [ ] Automatic save to file (no manual paste)
- [ ] Batch export (multiple chats at once)
- [ ] Custom template support

---

**Maintained by:** PKM System Project  
**License:** MIT  
**Repository:** /scripts/chat-exporter/
