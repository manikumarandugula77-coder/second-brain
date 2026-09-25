# TradingBot 🤖

> **Autonomous trading agent for market analysis and execution.**

## Overview

TradingBot is designed to:
- Fetch real-time market data
- Evaluate trading strategies (momentum, mean reversion)
- Execute paper trades via the Alpaca API
- Track performance metrics
- Log all activities

## Sandbox

- **Directory**: `hermes-workspace/tradingbot/`
- **Data**: Stored locally in the `data/` subdirectory
- **Logs**: Written to `hermes-workspace/logs/tradingbot.log`
- **Configuration**: [[tradingbot/config.yaml]]

## Setup

1. Install dependencies:
   ```bash
   pip install -r ../config/requirements.txt
   ```

2. Configure API keys in `../config/.env`:
   ```env
   ALPACA_API_KEY=your_api_key
   ALPACA_API_SECRET=your_api_secret
   ```

3. Edit `config.yaml` to adjust strategies and symbols.

4. Run:
   ```bash
   python tradingbot.py
   ```

## Strategies

| Strategy | Status | Description |
|----------|--------|-------------|
| Momentum | ✅ Enabled | Trades based on price momentum over lookback period |
| Mean Reversion | ❌ Disabled | Trades based on price deviation from mean |

## Risk Management

- Max 5 positions
- 2% risk per trade
- 15% max drawdown limit
- 5% stop loss per position

## Logging

All trades and system events are logged to:
- `hermes-workspace/logs/tradingbot.log`
- Console output

## Test Results

```
TradingBot initialized successfully.
Paper trading mode: True
Monitoring symbols: ['SPY', 'QQQ', 'AAPL', 'TSLA', 'NVDA', 'BTC.USD', 'ETH.USD']
```

## Related

[[hermes-workspace/README|Hermes Workspace]]
[[TelegramBot]]
[[GitHubBot]]
[[ResearchBot]]

tags: #tradingbot #trading #ai-agent #python #alpaca #bots
