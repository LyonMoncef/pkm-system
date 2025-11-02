---
created: 2025-11-02T17:05:00
updated: 2025-11-02T17:05:00
type: backlog-item
category: technical-debt
priority: high
status: todo
tags: [tooling, python, tags]
estimated_time: "45min"
estimated_time_minutes: 45
parent: "[[Context Builder System]]"
phase: 1
---

# Context Builder - Tag Extractor

## 🎯 Description

Extraire tags depuis TAG_REGISTRY.md.

## 📋 Tasks

- [ ] Fonction `load_tag_registry()`
- [ ] Fonction `find_tag_info(tag_name)`
- [ ] Parse structure TAG_REGISTRY
- [ ] Return tag metadata
- [ ] Handle tag not found

## 📊 Critères

- [ ] Lit TAG_REGISTRY.md
- [ ] Parse sections par type
- [ ] Return description + type tag
- [ ] List available tags

**Parent:** [[Context Builder System]]
