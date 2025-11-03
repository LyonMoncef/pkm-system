---
created: 2025-11-02T17:05:00
updated: 2025-11-02T17:05:00
type: backlog-item
category: technical-debt
priority: high
status: todo
tags: [tooling, python, parsing]
estimated_time: "1h30"
estimated_time_minutes: 90
parent: "[[Context Builder System]]"
phase: 1
---

# Context Builder - Core Parser

## 🎯 Description

Parser YAML frontmatter et markdown files.

## 📋 Tasks

- [ ] Fonction `parse_frontmatter(file_path)`
- [ ] Fonction `parse_markdown_sections(file_path)`
- [ ] Handle errors (file not found, invalid YAML)
- [ ] Tests basiques
- [ ] Return structured dict

## 📊 Critères

- [ ] Parse YAML correct
- [ ] Handle --- delimiters
- [ ] Extract title/content
- [ ] Error handling

**Parent:** [[Context Builder System]]
