# Git Rebase

---
title: Git Rebase
skill_name: Git Rebase
type: skill
category: git
difficulty: advanced
description: Interactive rebasing to squash commits
steps_count: 3
examples_count: 2
source_session: S-20260925-23007
related_skills:
  - "Git Commit"
tags:
  - "#git-workflow"
  - "#skill"
  - "#learned"
  - "#category/git"
  - "#difficulty/advanced"
created: "2026-09-25T08:00:53Z"
created_local: "2026-09-25 14:00:53 +06:00"
date: 2026-09-25
---


## Skill Overview

| Field | Value |
|-------|-------|
| Name | Git Rebase |
| Category | git |
| Difficulty | advanced |
| Created | 2026-09-25 14:00:53 +06:00 |
| Source Session | S-20260925-23007 |

## Description

Interactive rebasing to squash commits

## Steps

1. Run git rebase -i HEAD~n
2. Mark commits as 'squash' or 'reword
3. Save and exit the editor

## Examples

### Example 1

```
git rebase -i HEAD~3
```

### Example 2

```
git push --force-with-lease
```

## Additional Notes

Remember to communicate rebases to the team

## Related Skills

- [[Git Commit]]

## Source Session

```dataview
TABLE file.link AS "Session", command, exit_code
FROM "01 - Notes/Sessions"
WHERE contains(session_id, "S-20260925-23007")
LIMIT 1
```

## Skill Index

```dataview
TABLE file.link, skill_name, category, difficulty, date FROM "02 - Projects/Skills" WHERE skill_name != "Git Rebase" SORT date DESC LIMIT 20
```

## Category Index

```dataview
TABLE file.link, skill_name, difficulty, date FROM "02 - Projects/Skills" WHERE category = "git" and skill_name != "Git Rebase" SORT date DESC LIMIT 20
```

---
*Tags: #git-workflow #skill #learned #category/git #difficulty/advanced*
*Learned: 2026-09-25*