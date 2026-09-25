# GitHubBot 🔧

> **GitHub automation bot for repository management and issue triage.**

## Overview

GitHubBot automates:
- Issue labeling based on content analysis
- Pull request monitoring
- Repository health checks
- Auto-responses to new issues/PRs
- Stats collection and reporting

## Sandbox

- **Directory**: `hermes-workspace/github-bot/`
- **Logs**: `hermes-workspace/logs/github-bot.log`
- **Config**: [[github-bot/config.yaml]]

## Setup

1. Install dependencies:
   ```bash
   pip install PyGithub pyyaml python-dotenv
   ```

2. Set environment variables in `../config/.env`:
   ```env
   GITHUB_TOKEN=your_github_token
   GITHUB_OWNER=your_github_username
   GITHUB_REPO=your_repo_name
   ```

3. Run:
   ```bash
   python github-bot.py
   ```

## Features

| Feature | Status | Description |
|---------|--------|-------------|
| Auto-labeling | ✅ | Labels issues based on keyword matching |
| Auto-respond | ✅ | Responds to new issues and PRs |
| PR monitoring | ✅ | Checks PR builds and status |
| Stats reporting | ✅ | Collects repository statistics |

## Test Results

```
GitHubBot initialized for manikumarandugula77-coder/brain-
GitHubBot starting...
Monitoring repository: manikumarandugula77-coder/brain-
Status: {"name": "GitHubBot", "is_running": true, "repo": "manikumarandugula77-coder/brain-", "stats": {"name": "brain-", "stars": 0, "forks": 0, "open_issues": 0, "language": "Python", "is_private": true}}
```

## Label Rules

| Label | Keywords |
|-------|----------|
| `bug` | bug, error, fix, crash, broken |
| `enhancement` | feature, enhancement, improve, add |
| `documentation` | docs, documentation, readme, wiki |
| `question` | question, help, how, why |
| `urgent` | urgent, critical, asap, emergency |

## Related

[[hermes-workspace/README|Hermes Workspace]]
[[TradingBot]]
[[TelegramBot]]
[[ResearchBot]]

tags: #github-bot #automation #github #ai-agent #python #bots
