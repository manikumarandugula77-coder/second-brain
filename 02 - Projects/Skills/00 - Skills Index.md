# Skills Index

---
title: Skills Index
type: index-note
index_key: skills
tags:
  - "#index"
  - "#index/skills"
  - "#dataview"
generated: "2026-09-25T08:35:04Z"
generated_local: "2026-09-25 14:35:04 +06:00"
date: 2026-09-25
auto_generated: true
---


*Index of all learned skills.*

_Generated: 2026-09-25 14:35:04 +06:00_

## All Skills

```dataview
TABLE file.link AS Skill, skill_name, category, difficulty, date FROM "02 - Projects/Skills" WHERE type = 'skill' SORT date DESC LIMIT 50
```

## Skills by Category

```dataview
TABLE rows.file.link AS Skill, rows.difficulty AS Level FROM "02 - Projects/Skills" SORT rows.length DESC GROUP BY category
```

## Skills by Difficulty

```dataview
TABLE rows.file.link AS Skill, rows.category AS Category FROM "02 - Projects/Skills" SORT rows.length DESC GROUP BY difficulty
```

---
*Tags: #index #index/skills #dataview*
*Auto-generated: 2026-09-25*