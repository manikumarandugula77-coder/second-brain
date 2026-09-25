# Hermes Agent Workspace

> **A sandboxed environment for autonomous AI agents integrated with your Obsidian second brain.**

## Overview

This workspace connects four autonomous AI bots directly to your Obsidian vault, allowing them to read, write, and organize knowledge automatically.

## Connected Bots

| Bot | Type | Purpose | Status |
|-----|------|---------|--------|
| 🤖 **[[TradingBot]]** | Python | Automated trading via Alpaca API | Running (paper trading) |
| 💬 **[[TelegramBot]]** | Node.js | Telegram notifications & control | Ready (needs token) |
| 🔧 **[[GitHubBot]]** | Python | GitHub automation (issues, PRs) | Running (connected to this repo) |
| 📚 **[[ResearchBot]]** | Python | RSS monitoring & knowledge extraction | Running (5 source feeds) |

## Architecture

```
hermes-workspace/
├── config/              # Shared configuration
├── tradingbot/          # [[TradingBot]] agent
├── telegram-bot/        # [[TelegramBot]] agent
├── github-bot/          # [[GitHubBot]] agent
├── research-bot/        # [[ResearchBot]] agent
├── logs/                # Runtime logs
└── README.md            # This file
```

## How Bots Interact with Obsidian

- **[[ResearchBot]]** saves articles as notes in `00 - Inbox/`
- **[[GitHubBot]]** can create issue notes and update task boards
- **[[TelegramBot]]** sends notifications about vault activity
- **[[TradingBot]]** logs trades and performance metrics

## Configuration

See [[hermes-workspace/config/README]] for configuration details.

## Related Notes

[[Dashboard]]
[[Meta/SETUP COMPLETE]]

## Bot Notes

- [[TradingBot]]
- [[TelegramBot]]
- [[GitHubBot]]
- [[ResearchBot]]

## Vault Integration

This workspace is part of the Obsidian vault that syncs with:
- **Repo**: `manikumarandugula77-coder/brain-`
- **Branch**: `main`
- **Plugin**: [[Obsidian Git]] for auto-sync

tags: #hermes #workspace #bots #automation #second-brain
