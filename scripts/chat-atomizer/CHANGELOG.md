# Changelog - Chat Atomizer

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [1.0.0] - 2025-11-09

### Added - Core Features ✅

#### Parsing
- ✅ Parse export markdown files with YAML frontmatter
- ✅ Extract messages (user + assistant) with regex patterns
- ✅ Detect attachments (images, files) from message blocks
- ✅ Handle timestamps and message IDs
- ✅ Compute statistics (message counts, attachment counts)

#### Atomic Cards Generation
- ✅ Create one markdown file per message
- ✅ Generate YAML frontmatter with metadata
- ✅ Add emoji indicators (👤 user, 🤖 assistant)
- ✅ Include attachments section when present
- ✅ Apply canonical tags from TAG_REGISTRY

#### Navigation
- ✅ Automatic prev/next links between messages
- ✅ Link to parent MOC from each card
- ✅ Sequential numbering (001, 002, 003...)
- ✅ Descriptive filenames (order_role_id.md)

#### Map of Content (MOC)
- ✅ Auto-generated MOC with statistics
- ✅ Dataview queries for all messages
- ✅ Queries by role (user/assistant)
- ✅ Queries by topic
- ✅ Queries for attachments
- ✅ Timeline section

#### Topic Detection
- ✅ Keyword-based topic extraction
- ✅ Support for 10+ domains (power-bi, python, obsidian, finance, etc.)
- ✅ Multi-topic detection per message
- ✅ Extensible keyword dictionary

#### Code Extraction
- ✅ Extract code blocks with language detection
- ✅ Support for multiple languages (python, js, sql, dax, yaml, etc.)
- ✅ Preserve code formatting
- ✅ Index code blocks per message

#### CLI Interface
- ✅ Argument parsing (input, output)
- ✅ --dry-run mode for testing
- ✅ Informative output messages
- ✅ Progress indicators
- ✅ Error handling

### Documentation 📚

- ✅ README with full feature list
- ✅ Quick Start guide
- ✅ Usage examples
- ✅ Troubleshooting section
- ✅ Test suite documentation
- ✅ Changelog (this file)

### Testing 🧪

- ✅ Test script (test_atomizer.py)
- ✅ Parsing tests
- ✅ Topic detection tests
- ✅ Code extraction tests
- ✅ Message details inspection

---

## [Unreleased] - Future Versions

### Planned for v1.1

#### Export Support
- [ ] ChatGPT export parser
- [ ] Gemini export parser
- [ ] Generic markdown conversation parser

#### Features
- [ ] Configurable templates (YAML config)
- [ ] Custom topic keywords via config file
- [ ] Image extraction & copy to vault
- [ ] Attachment files handling

#### Code Extraction
- [ ] Save code blocks as separate files
- [ ] Organize code by language in folders
- [ ] Add syntax highlighting hints

#### Performance
- [ ] Parallel processing for large exports
- [ ] Progress bar for long operations
- [ ] Memory optimization for huge conversations

### Planned for v1.2

#### Intelligence
- [ ] NLP-based topic detection (spaCy/NLTK)
- [ ] Automatic theme grouping
- [ ] Generate theme cards (synthesis)
- [ ] Detect key insights

#### Thematic Cards
- [ ] Auto-generate theme synthesis cards
- [ ] Group related messages by topic
- [ ] Create theme MOCs

#### Visualization
- [ ] Timeline generation (Mermaid/Timeline plugin)
- [ ] Conversation flow diagram
- [ ] Topic distribution chart

### Planned for v2.0

#### GUI
- [ ] Tkinter/PyQt interface
- [ ] Drag & drop export files
- [ ] Visual configuration
- [ ] Preview before generation

#### Automation
- [ ] Watch folder mode (auto-process new exports)
- [ ] Batch processing multiple exports
- [ ] Scheduled processing

#### Integration
- [ ] Obsidian plugin (TypeScript)
- [ ] Direct clipboard import
- [ ] In-app export button
- [ ] Live sync mode

---

## Version History Summary

| Version | Date | Features | Status |
|---------|------|----------|--------|
| 1.0.0 | 2025-11-09 | Core MVP - Parsing, Cards, MOC, Topics | ✅ Released |
| 1.1.0 | TBD | Multi-platform, Templates, Images | 📋 Planned |
| 1.2.0 | TBD | NLP, Themes, Visualization | 🔮 Future |
| 2.0.0 | TBD | GUI, Automation, Plugin | 💭 Vision |

---

## Notes

### Design Decisions

**Why atomic cards instead of grouped by theme?**
- More flexible - can be grouped later with queries
- Easier navigation (prev/next)
- Better for granular linking
- Respects Zettelkasten principles

**Why YAML frontmatter?**
- Obsidian native support
- Queryable with Dataview
- Extendable metadata
- Human-readable

**Why keyword-based topics (not NLP)?**
- No heavy dependencies
- Fast processing
- Predictable results
- Good enough for v1.0
- NLP can be added in v1.2

### Breaking Changes

None yet - this is v1.0

---

## Contributors

- **Moncef** - Initial development

---

## License

MIT License - See LICENSE file for details
