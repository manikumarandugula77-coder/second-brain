# Activity Dashboard

---
title: Activity Dashboard
type: index-note
index_key: dashboard
tags:
  - "#index"
  - "#index/dashboard"
  - "#dataview"
generated: "2026-09-25T08:35:04Z"
generated_local: "2026-09-25 14:35:04 +06:00"
date: 2026-09-25
auto_generated: true
---


*Master dashboard of all brain-capture activity.*

_Generated: 2026-09-25 14:35:04 +06:00_

## Brain-capture Pipeline Status

| Component | Status |
|-----------|--------|
| Terminal Sessions | ✅ Active |
| GitHub Activity Sync | ✅ Active |
| System Activity Logger | ✅ Active |
| Skill Capture | ✅ Active |
| Dataview Indexes | ✅ Active |

```dataviewjs
// Brain-capture content counter
const sources = {
    "Sessions": '"01 - Notes/Sessions"',
    "GitHub Sync": '"03 - Resources/GitHub"',
    "System Activity": '"00 - Inbox/System-Activity"',
    "Skills": '"02 - Projects/Skills"'
};

const rows = Object.entries(sources).map(([label, src]) => {
    const pages = dv.pages(src);
    return [label, pages.length];
});

dv.table(["Type", "Count"], rows);
```

## Recent Sessions

```dataview
TABLE file.link, session_id, command, date FROM "01 - Notes/Sessions" SORT date DESC LIMIT 10
```

## Recent Skills

```dataview
TABLE file.link, skill_name, category, date FROM "02 - Projects/Skills" WHERE type = 'skill' SORT date DESC LIMIT 10
```

## Recent GitHub Syncs

```dataview
TABLE file.link, repo, date FROM "03 - Resources/GitHub" WHERE type = 'github-sync' SORT date DESC LIMIT 10
```

## Recent System Activity

```dataview
TABLE file.link, date, event_count FROM "00 - Inbox/System-Activity" WHERE type = 'system-activity-log' SORT date DESC LIMIT 10
```

---
*Tags: #index #index/dashboard #dataview*
*Auto-generated: 2026-09-25*