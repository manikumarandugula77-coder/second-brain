"""
GitHubBot — Hermes GitHub Automation Bot

Purpose:
    Automates GitHub repository management tasks:
    - Issue triage and labeling
    - Pull request monitoring
    - Repository health checks
    - Code quality scanning
    - Automated issue response

Sandbox:
    This bot is isolated in hermes-workspace/github-bot/
    All data stays within this directory.

Author: Hermes Agent
"""

import os
import sys
import json
import logging
import yaml
from datetime import datetime
from github import Github
from dotenv import load_dotenv

# Load environment
load_dotenv("../config/.env")

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("../logs/github-bot.log"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("GitHubBot")


class GitHubBot:
    """
    GitHub automation bot for repository management.
    """

    def __init__(self, config_path=None):
        self.token = os.environ.get("GITHUB_TOKEN")
        if not self.token:
            logger.error("GITHUB_TOKEN not set in environment variables")
            raise ValueError("GITHUB_TOKEN is required")
        
        self.github = Github(self.token)
        self.owner = os.environ.get("GITHUB_OWNER", "")
        self.repo_name = os.environ.get("GITHUB_REPO", "")
        
        if self.owner and self.repo_name:
            self.repo = self.github.get_repo(f"{self.owner}/{self.repo_name}")
        else:
            self.repo = None
            
        self.config = self._load_config(config_path)
        self.is_running = False
        logger.info(f"GitHubBot initialized for {self.owner}/{self.repo_name}")

    def _load_config(self, config_path):
        """Load configuration from YAML."""
        if config_path is None:
            config_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
        
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                return yaml.safe_load(f)
        return {
            'auto_label': True,
            'auto_respond_issues': True,
            'auto_respond_prs': True,
            'check_pr_builds': True,
            'label_rules': {
                'bug': ['bug', 'error', 'fix'],
                'enhancement': ['feature', 'enhancement', 'improve'],
                'documentation': ['docs', 'documentation', 'readme'],
                'question': ['question', 'help'],
            }
        }

    def start(self):
        """Start the GitHub bot."""
        logger.info("GitHubBot starting...")
        self.is_running = True
        logger.info(f"Monitoring repository: {self.owner}/{self.repo_name}")

    def stop(self):
        """Stop the GitHub bot."""
        logger.info("GitHubBot stopping...")
        self.is_running = False

    def get_issues(self, state='open'):
        """Get issues from the repository."""
        if not self.repo:
            logger.error("Repository not configured")
            return []
        
        issues = self.repo.get_issues(state=state)
        return list(issues)

    def get_pull_requests(self, state='open'):
        """Get pull requests from the repository."""
        if not self.repo:
            logger.error("Repository not configured")
            return []
        
        prs = self.repo.get_pulls(state=state)
        return list(prs)

    def label_issue(self, issue_number, labels):
        """Add labels to an issue."""
        if not self.repo:
            return False
        
        try:
            issue = self.repo.get_issue(issue_number)
            issue.add_to_labels(*labels)
            logger.info(f"Labeled issue #{issue_number} with {labels}")
            return True
        except Exception as e:
            logger.error(f"Failed to label issue #{issue_number}: {e}")
            return False

    def auto_label_issues(self):
        """Automatically label new issues based on content."""
        if not self.config.get('auto_label', True):
            return
        
        issues = self.get_issues(state='open')
        for issue in issues:
            # Skip if already labeled
            if issue.labels:
                continue
            
            title = issue.title.lower()
            body = (issue.body or '').lower()
            content = f"{title} {body}"
            
            labels_to_add = []
            for label, keywords in self.config.get('label_rules', {}).items():
                if any(kw in content for kw in keywords):
                    labels_to_add.append(label)
            
            if labels_to_add:
                self.label_issue(issue.number, labels_to_add)

    def create_issue(self, title, body, labels=None, assignees=None):
        """Create a new issue."""
        if not self.repo:
            logger.error("Repository not configured")
            return None
        
        try:
            issue = self.repo.create_issue(
                title=title,
                body=body,
                labels=labels or [],
                assignees=assignees or []
            )
            logger.info(f"Created issue #{issue.number}: {title}")
            return issue
        except Exception as e:
            logger.error(f"Failed to create issue: {e}")
            return None

    def get_repo_stats(self):
        """Get repository statistics."""
        if not self.repo:
            return None
        
        return {
            'name': self.repo.name,
            'full_name': self.repo.full_name,
            'description': self.repo.description,
            'stars': self.repo.stargazers_count,
            'forks': self.repo.forks_count,
            'open_issues': self.repo.open_issues_count,
            'language': self.repo.language,
            'created_at': self.repo.created_at.isoformat(),
            'updated_at': self.repo.updated_at.isoformat(),
            'is_private': self.repo.private,
            'default_branch': self.repo.default_branch,
            'timestamp': datetime.now().isoformat()
        }

    def get_status(self):
        """Return bot status."""
        return {
            'name': 'GitHubBot',
            'is_running': self.is_running,
            'repo': f"{self.owner}/{self.repo_name}" if self.repo else None,
            'stats': self.get_repo_stats() if self.repo else None,
        }


if __name__ == '__main__':
    bot = GitHubBot()
    bot.start()
    print("GitHubBot initialized successfully.")
    print(f"Status: {json.dumps(bot.get_status(), indent=2, default=str)}")
