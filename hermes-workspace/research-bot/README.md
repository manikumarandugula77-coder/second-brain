# ResearchBot 📚

> **Research assistant bot for content aggregation and knowledge extraction.**

## Overview

ResearchBot automates:
- RSS feed monitoring (Hacker News, ArXiv, MIT Tech Review, OpenAI Blog)
- Topic-based content filtering
- Article summarization (AI-powered)
- Knowledge indexing into Obsidian vault
- Daily research summaries

## Sandbox

- **Directory**: `hermes-workspace/research-bot/`
- **Logs**: `hermes-workspace/logs/research-bot.log`
- **Config**: [[research-bot/config.yaml]]
- **Data**: `data/` subdirectory

## Setup

1. Install dependencies:
   ```bash
   pip install feedparser pyyaml python-dotenv requests beautifulsoup4
   ```

2. Edit `config.yaml` to customize RSS sources and topics.

3. Set `OBSIDIAN_VAULT_PATH` in `../config/.env`:
   ```env
   OBSIDIAN_VAULT_PATH=C:/Users/rajuc/Documents/Obsidian Vault
   ```

4. Run:
   ```bash
   python research-bot.py
   ```

## Research Sources

| Source | URL | Description |
|--------|-----|-------------|
| Hacker News | news.ycombinator.com/rss | Tech news and discussions |
| ArXiv CS | export.arxiv.org/rss/cs | Computer science papers |
| ArXiv Q-Fin | export.arxiv.org/rss/q-fin | Quantitative finance papers |
| MIT Tech Review | technologyreview.com/feed | Technology journalism |
| OpenAI Blog | openai.com/blog/rss | AI research updates |

## Topics Monitored

- AI, Machine Learning, Deep Learning
- Neural Networks, LLM, Prompt Engineering
- Trading, Algorithmic Trading
- Cybersecurity, Quantum Computing
- Automation, Reinforcement Learning

## Output

Research articles are saved as Obsidian markdown notes in `[[00 - Inbox]]`:
- `Research_<date>_<time>.md`

Each note includes:
- Auto-generated tags
- Article summary
- Key points
- Source link

## Test Results

```
ResearchBot initialized successfully.
Monitoring 5 sources for 12 topics.
Data directory: hermes-workspace/research-bot/data/
```

## Related

[[hermes-workspace/README|Hermes Workspace]]
[[TradingBot]]
[[TelegramBot]]
[[GitHubBot]]

tags: #research-bot #rss #research #ai-agent #python #bots
