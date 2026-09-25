# Disk Space Check

---
title: Disk Space Check
note_id: SYS-23272
type: system-activity-note
date: 2026-09-25
created: "2026-09-25T08:01:12Z"
severity: INFO
category: monitoring
tags:
  - "#system-activity"
  - "#category/monitoring"
  - "#severity/INFO"
---


## Summary

| Field | Value |
|-------|-------|
| ID | `SYS-23272` |
| Category | monitoring |
| Severity | INFO |
| Timestamp | 2026-09-25 14:01:12 +06:00 |

## Details

System disk has 45GB free out of 120GB total

## Structured Data

```json
{
  "disk_free": "45GB",
  "disk_total": "120GB"
}
```

## Related Activity

```dataview
TABLE file.link, date, category, severity WHERE type = 'system-activity-note' SORT date DESC LIMIT 10
```

---
*Tags: #system-activity #category/monitoring #severity/INFO*
*Created: 2026-09-25*