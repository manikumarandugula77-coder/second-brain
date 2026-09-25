# GitHub Activity Index

---
title: GitHub Activity Index
type: index-note
index_key: github
tags:
  - "#index"
  - "#index/github"
  - "#dataview"
generated: "2026-09-25T08:35:04Z"
generated_local: "2026-09-25 14:35:04 +06:00"
date: 2026-09-25
auto_generated: true
---


*Index of all synced GitHub repository activity.*

_Generated: 2026-09-25 14:35:04 +06:00_

## All GitHub Repos

```dataview
TABLE file.link AS Repo, repo, language, stars, date FROM "03 - Resources/GitHub" SORT stars DESC LIMIT 50
```

## Recently Synced

```dataview
TABLE file.link AS Repo, repo, sync_date FROM "03 - Resources/GitHub" WHERE type = 'github-sync' SORT sync_date DESC LIMIT 20
```

---
*Tags: #index #index/github #dataview*
*Auto-generated: 2026-09-25*