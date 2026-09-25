# Dataview Queries

---
title: Dataview Queries
skill_name: Dataview Queries
type: skill
category: data
difficulty: intermediate
description: Writing Dataview queries for Obsidian
steps_count: 3
examples_count: 1
source_session: S-20260925-25089
related_skills:
  - "Git Rebase"
tags:
  - "#dataview"
  - "#skill"
  - "#learned"
  - "#category/data"
  - "#difficulty/intermediate"
created: "2026-09-25T08:34:27Z"
created_local: "2026-09-25 14:34:27 +06:00"
date: 2026-09-25
---


## Skill Overview

| Field | Value |
|-------|-------|
| Name | Dataview Queries |
| Category | data |
| Difficulty | intermediate |
| Created | 2026-09-25 14:34:27 +06:00 |
| Source Session | S-20260925-25089 |

## Description

Writing Dataview queries for Obsidian

## Steps

1. Use TABLE query for lists
2. Use FROM to specify source
3. Add WHERE for filtering

## Examples

### Example 1

```

```

## Additional Notes

Dataview is a powerful Obsidian plugin

## Related Skills

- [[Git Rebase]]

## Source Session

```dataview
TABLE file.link AS "Session", command, exit_code
FROM "01 - Notes/Sessions"
WHERE contains(session_id, "S-20260925-25089")
LIMIT 1
```

## Skill Index

```dataview
TABLE file.link, skill_name, category, difficulty, date FROM "02 - Projects/Skills" WHERE skill_name != "Dataview Queries" SORT date DESC LIMIT 20
```

## Category Index

```dataview
TABLE file.link, skill_name, difficulty, date FROM "02 - Projects/Skills" WHERE category = "data" and skill_name != "Dataview Queries" SORT date DESC LIMIT 20
```

---
*Tags: #dataview #skill #learned #category/data #difficulty/intermediate*
*Learned: 2026-09-25*