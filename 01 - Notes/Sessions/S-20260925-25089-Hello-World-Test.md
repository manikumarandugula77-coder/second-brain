# Hello World Test

---
title: Hello World Test
session_id: S-20260925-25089
type: terminal-session
command: echo hello-world
exit_code: 0
captured_at: "2026-09-25T08:31:29Z"
captured_local: "2026-09-25 14:31:29 +06:00"
date: 2026-09-25
tags:
  - "#e2e"
  - "#session/terminal"
description: Full pipeline E2E test
duration_seconds: 0.04
---


## Session Overview

| Field | Value |
|-------|-------|
| Session ID | S-20260925-25089 |
| Command | `echo hello-world` |
| Exit Code | 0 |
| Captured | 2026-09-25 14:31:29 +06:00 |
| Duration | 0.04s |
| Tags | #e2e #session/terminal |

## Description

Full pipeline E2E test

## Terminal Output

```bash
$ echo hello-world
hello-world


[exit code: 0]
```

## Key Findings

- [ ] What did this session accomplish?
- [ ] What errors or issues were found?
- [ ] What follow-up actions are needed?

## Related Sessions

```dataview
TABLE file.link, session_id, command, date FROM "01 - Notes/Sessions" WHERE date = date('2026-09-25') and session_id != "S-20260925-25089" SORT date DESC LIMIT 10
```

## All Sessions

```dataview
TABLE file.link, session_id, command, date, exit_code FROM "01 - Notes/Sessions" SORT date DESC LIMIT 20
```

---
*Tags: #e2e #session/terminal*  
*Created: 2026-09-25*