# Bash Path Conversion

---
title: Bash Path Conversion
skill_name: Bash Path Conversion
type: skill
category: cli
difficulty: beginner
description: Convert MSYS paths to native Windows
steps_count: 1
examples_count: 1
source_session: 
related_skills: 
tags:
  - "#bash"
  - "#skill"
  - "#learned"
  - "#category/cli"
  - "#difficulty/beginner"
created: "2026-09-25T08:31:34Z"
created_local: "2026-09-25 14:31:34 +06:00"
date: 2026-09-25
---


## Skill Overview

| Field | Value |
|-------|-------|
| Name | Bash Path Conversion |
| Category | cli |
| Difficulty | beginner |
| Created | 2026-09-25 14:31:34 +06:00 |

## Description

Convert MSYS paths to native Windows

## Steps

1. Use cygpath -w to convert

## Examples

### Example 1

```
cygpath -w /c/Users
```

## Skill Index

```dataview
TABLE file.link, skill_name, category, difficulty, date FROM "02 - Projects/Skills" WHERE skill_name != "Bash Path Conversion" SORT date DESC LIMIT 20
```

## Category Index

```dataview
TABLE file.link, skill_name, difficulty, date FROM "02 - Projects/Skills" WHERE category = "cli" and skill_name != "Bash Path Conversion" SORT date DESC LIMIT 20
```

---
*Tags: #bash #skill #learned #category/cli #difficulty/beginner*
*Learned: 2026-09-25*