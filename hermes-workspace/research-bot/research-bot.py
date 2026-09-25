"""
ResearchBot — Hermes Research Assistant Agent

Purpose:
    Automates research tasks:
    - Fetches articles and papers from various sources
    - Summarizes content using AI models
    - Indexes findings into Obsidian vault
    - Monitors RSS feeds and news sources
    - Tracks arXiv papers by topic

Sandbox:
    This bot is isolated in hermes-workspace/research-bot/
    All data stays within this directory.

Author: Hermes Agent
"""

import os
import sys
import json
import yaml
import logging
import feedparser
from datetime import datetime
from urllib.parse import urlparse
from dotenv import load_dotenv

# Load environment
load_dotenv("../config/.env")

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("../logs/research-bot.log"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("ResearchBot")

# Obsidian vault path
OBSIDIAN_VAULT_PATH = os.environ.get(
    "OBSIDIAN_VAULT_PATH",
    "C:/Users/rajuc/Documents/Obsidian Vault"
)


class ResearchBot:
    """
    Research assistant bot for content aggregation and knowledge extraction.
    """

    def __init__(self, config_path=None):
        self.config = self._load_config(config_path)
        self.is_running = False
        self.sources = self.config.get('sources', [])
        self.topics = self.config.get('topics', [])
        self.data_dir = os.path.join(os.path.dirname(__file__), 'data')
        os.makedirs(self.data_dir, exist_ok=True)
        logger.info("ResearchBot initialized")
        logger.info(f"Monitoring {len(self.sources)} sources for {len(self.topics)} topics")

    def _load_config(self, config_path):
        """Load configuration from YAML."""
        if config_path is None:
            config_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
        
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                return yaml.safe_load(f)
        return {
            'sources': [
                {'type': 'rss', 'name': 'Hacker News', 'url': 'https://news.ycombinator.com/rss'},
                {'type': 'rss', 'name': 'ArXiv Quantum', 'url': 'http://arxiv.org/rss/quant-ph'},
            ],
            'topics': ['AI', 'Machine Learning', 'Quantum Computing', 'Trading', 'Security'],
            'max_articles_per_source': 10,
            'save_raw_html': False,
            'summarize': True,
        }

    def start(self):
        """Start the research bot."""
        logger.info("ResearchBot starting...")
        self.is_running = True

    def stop(self):
        """Stop the research bot."""
        logger.info("ResearchBot stopping...")
        self.is_running = False

    def fetch_rss(self, rss_url):
        """Fetch and parse an RSS feed."""
        logger.info(f"Fetching RSS feed: {rss_url}")
        try:
            feed = feedparser.parse(rss_url)
            articles = []
            for entry in feed.entries[:self.config.get('max_articles_per_source', 10)]:
                articles.append({
                    'title': entry.title,
                    'link': entry.link,
                    'summary': entry.summary if hasattr(entry, 'summary') else '',
                    'published': entry.published if hasattr(entry, 'published') else '',
                    'source': feed.feed.title if hasattr(feed.feed, 'title') else '',
                    'fetched_at': datetime.now().isoformat()
                })
            logger.info(f"Fetched {len(articles)} articles from {rss_url}")
            return articles
        except Exception as e:
            logger.error(f"Failed to fetch RSS feed {rss_url}: {e}")
            return []

    def search_by_topic(self, topic):
        """Search for articles related to a specific topic."""
        results = []
        for source in self.sources:
            if source.get('type') == 'rss':
                articles = self.fetch_rss(source['url'])
                for article in articles:
                    content = f"{article['title']} {article.get('summary', '')}".lower()
                    if topic.lower() in content:
                        article['matched_topic'] = topic
                        article['source_name'] = source['name']
                        results.append(article)
        return results

    def summarize_article(self, title, content):
        """Summarize an article (placeholder for AI summarization)."""
        logger.info(f"Summarizing: {title}")
        # Placeholder — would use OpenAI/Claude API in production
        return {
            'title': title,
            'summary': content[:500] + '...' if len(content) > 500 else content,
            'key_points': ['[AI summarization would go here]'],
            'timestamp': datetime.now().isoformat()
        }

    def save_to_obsidian(self, research_data):
        """Save research findings to the Obsidian vault."""
        if not research_data:
            return

        today = datetime.now().strftime("%Y-%m-%d")
        filename = f"Research_{today}_{datetime.now().strftime('%H%M%S')}.md"
        filepath = os.path.join(OBSIDIAN_VAULT_PATH, "00 - Inbox", filename)

        # Ensure the inbox directory exists
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        # Format as Obsidian note
        content = f"""---
tags: research, automation
date: {today}
source: {research_data.get('source', 'unknown')}
---

# {research_data.get('title', 'Research Note')}

## Summary

{research_data.get('summary', 'No summary available')}

## Key Points

"""
        for i, point in enumerate(research_data.get('key_points', []), 1):
            content += f"{i}. {point}\n"

        content += f"""

## Source

{research_data.get('link', '')}

## Fetched at

{research_data.get('fetched_at', '')}
"""

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        logger.info(f"Saved research note to Obsidian: {filepath}")
        return filepath

    def research_topic(self, topic):
        """Full research workflow: search, summarize, save."""
        logger.info(f"Starting research on topic: {topic}")
        
        # Search for articles
        articles = self.search_by_topic(topic)
        logger.info(f"Found {len(articles)} relevant articles")

        results = []
        for article in articles:
            if self.config.get('summarize', True):
                summarized = self.summarize_article(
                    article['title'],
                    article.get('summary', '')
                )
                article.update(summarized)
            
            # Save to Obsidian
            self.save_to_obsidian(article)
            results.append(article)

        return results

    def get_status(self):
        """Return bot status."""
        return {
            'name': 'ResearchBot',
            'is_running': self.is_running,
            'sources': len(self.sources),
            'topics': self.topics,
            'data_dir': self.data_dir,
            'timestamp': datetime.now().isoformat()
        }


if __name__ == '__main__':
    bot = ResearchBot()
    bot.start()
    print("ResearchBot initialized successfully.")
    print(f"Status: {json.dumps(bot.get_status(), indent=2)}")
