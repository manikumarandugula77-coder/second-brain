# Sessions Index

---
title: Sessions Index
type: index-note
index_key: sessions
tags:
  - "#index"
  - "#index/sessions"
  - "#dataview"
generated: "2026-09-25T08:35:04Z"
generated_local: "2026-09-25 14:35:04 +06:00"
date: 2026-09-25
auto_generated: true
---


*Index of all captured terminal sessions.*

_Generated: 2026-09-25 14:35:04 +06:00_

## All Sessions

```dataview
TABLE file.link AS Session, session_id, command, exit_code, date FROM "01 - Notes/Sessions" SORT date DESC LIMIT 50
```

## Sessions by Date

```dataview
TABLE rows.file.link AS Session, rows.session_id AS ID FROM "01 - Notes/Sessions" SORT date DESC GROUP BY date
```

---
*Tags: #index #index/sessions #dataview*
*Auto-generated: 2026-09-25*