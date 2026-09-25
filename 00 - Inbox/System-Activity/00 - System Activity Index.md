# System Activity Index

---
title: System Activity Index
type: index-note
index_key: system
tags:
  - "#index"
  - "#index/system"
  - "#dataview"
generated: "2026-09-25T08:35:04Z"
generated_local: "2026-09-25 14:35:04 +06:00"
date: 2026-09-25
auto_generated: true
---


*Index of all system activity logs and notes.*

_Generated: 2026-09-25 14:35:04 +06:00_

## Activity Notes

```dataview
TABLE file.link AS Note, note_id, category, severity, date FROM "00 - Inbox/System-Activity" WHERE type = 'system-activity-note' SORT date DESC LIMIT 50
```

## Daily Activity Logs

```dataview
TABLE file.link AS Log, event_count, date FROM "00 - Inbox/System-Activity" WHERE type = 'system-activity-log' SORT date DESC LIMIT 30
```

---
*Tags: #index #index/system #dataview*
*Auto-generated: 2026-09-25*