# Directory Listing

---
title: Directory Listing
session_id: S-20260925-23007
type: terminal-session
command: ls -la
exit_code: 0
captured_at: "2026-09-25T07:56:47Z"
captured_local: "2026-09-25 13:56:47 +06:00"
date: 2026-09-25
tags:
  - "#session"
  - "#terminal"
  - "#session/terminal"
description: Listing current directory
duration_seconds: 0.11
---


## Session Overview

| Field | Value |
|-------|-------|
| Session ID | S-20260925-23007 |
| Command | `ls -la` |
| Exit Code | 0 |
| Captured | 2026-09-25 13:56:47 +06:00 |
| Duration | 0.11s |
| Tags | #session #terminal #session/terminal |

## Description

Listing current directory

## Terminal Output

```bash
$ ls -la
total 20
drwxr-xr-x 1 rajuc 197609    0 Sep 25 13:26 .
drwxr-xr-x 1 rajuc 197609    0 Sep 25 13:22 ..
drwxr-xr-x 1 rajuc 197609    0 Sep 25 13:22 brain_capture
-rwxr-xr-x 1 rajuc 197609 1477 Sep 25 13:26 brain-capture


[exit code: 0]
```

## Key Findings

- [ ] What did this session accomplish?
- [ ] What errors or issues were found?
- [ ] What follow-up actions are needed?

## Related Sessions

```dataview
TABLE file.link, session_id, command, date FROM "01 - Notes/Sessions" WHERE date = date('2026-09-25') and session_id != "S-20260925-23007" SORT date DESC LIMIT 10
```

## All Sessions

```dataview
TABLE file.link, session_id, command, date, exit_code FROM "01 - Notes/Sessions" SORT date DESC LIMIT 20
```

---
*Tags: #session #terminal #session/terminal*  
*Created: 2026-09-25*