# Hermes Workspace Configuration

> **Shared configuration for all Hermes bots within the Obsidian wallet.**

## File Structure

```
config/
├── .env              # Environment variables (DO NOT COMMIT - gitignored)
├── settings.yaml     # [[settings.yaml|Central bot configuration]]
├── requirements.txt  # Python dependencies
└── package.json      # Node.js dependencies
```

## Environment Variables

Create a `.env` file with the following structure:

```env
# GitHub
GITHUB_TOKEN=your_github_token
GITHUB_OWNER=manikumarandugula77-coder
GITHUB_REPO=brain-

# Telegram
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id

# Trading (Alpaca)
ALPACA_API_KEY=your_key
ALPACA_API_SECRET=your_secret
ALPACA_PAPER_TRADING=true

# AI Models
OPENAI_API_KEY=your_key
ANTHROPIC_API_KEY=your_key

# Obsidian
OBSIDIAN_VAULT_PATH=C:/Users/rajuc/Documents/Obsidian Vault
```

## Bot Configuration

Central settings in `settings.yaml`:

| Setting | Value |
|---------|-------|
| Workspace Name | hermes-workspace |
| Vault Path | C:\Users\rajuc\Documents\Obsidian Vault |
| Log Level | INFO |
| Log Directory | hermes-workspace/logs/ |

### Bot Enable/Disable

All bots are configurable in [[settings.yaml]]:
- **TradingBot**: ✅ Enabled
- **TelegramBot**: ✅ Enabled
- **GitHubBot**: ✅ Enabled
- **ResearchBot**: ✅ Enabled

## Dependencies

### Python
Install all at once:
```bash
pip install -r config/requirements.txt
```

Key packages:
- `PyGithub` — GitHub API
- `feedparser` — RSS feeds
- `beautifulsoup4` — Web scraping
- `python-telegram-bot` — Telegram integration
- `alpaca-trade-api` — Trading API

### Node.js
For TelegramBot:
```bash
cd hermes-workspace/telegram-bot
npm install
```

## Security

- `.env` file is gitignored — never commit API keys
- Bots are sandboxed — no cross-contamination between bot types
- All API calls are logged in `hermes-workspace/logs/`
- Rotate tokens every 90 days

## Related

[[hermes-workspace/README|Hermes Workspace]]
[[TradingBot]]
[[TelegramBot]]
[[GitHubBot]]
[[ResearchBot]]

tags: #config #hermes #workspace #setup #security
