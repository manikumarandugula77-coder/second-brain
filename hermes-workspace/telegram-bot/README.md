# TelegramBot 💬

> **Telegram bot for notifications, control, and conversational interface.**

## Overview

TelegramBot provides:
- Real-time notifications from other Hermes bots (TradingBot, GitHubBot, ResearchBot)
- Command interface to query bot status
- Direct messaging for alerts and updates

## Sandbox

- **Directory**: `hermes-workspace/telegram-bot/`
- **Data**: Stored locally in the `data/` subdirectory
- **Logs**: `hermes-workspace/logs/telegram-bot.log`
- **Config**: Environment variables in `../config/.env`

## Setup

1. Create a Telegram bot with [@BotFather](https://t.me/BotFather)
2. Get your bot token and add it to `../config/.env`:
   ```env
   TELEGRAM_BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz
   TELEGRAM_CHAT_ID=123456789
   ```

3. Install dependencies and run:
   ```bash
   npm install
   npm start
   ```

## Commands

| Command | Description |
|---------|-------------|
| `/start` | Show welcome message |
| `/status` | Check bot status |
| `/ping` | Test connectivity |
| `/help` | Show help |
| `/echo <text>` | Repeat text |

## Notifications

Other Hermes bots can send notifications via:
```javascript
await telegramBot.sendMessage("Trading alert: AAPL hit target price");
```

## Test Results

```
TelegramBot started successfully
Status: Connected to Telegram
Waiting for /start command...
```

## Related

[[hermes-workspace/README|Hermes Workspace]]
[[TradingBot]]
[[GitHubBot]]
[[ResearchBot]]

tags: #telegram-bot #notifications #telegram #ai-agent #nodejs #bots
