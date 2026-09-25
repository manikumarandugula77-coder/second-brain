# Second Brain Setup Guide

## 📥 Initial Setup

### 1. Repository Connection
- Repository: `manikumarandugula77-coder/brain-`
- Local Path: `C:\Users\rajuc\Documents\brain-`
- Branch: `main`

### 2. Obsidian Configuration
- Vault Name: `brain-`
- Core Plugins Enabled:
  - Graph View
  - Backlinks
  - Outgoing Links
  - Tag Pane
  - Search
  - Daily Notes
  - File Explorer
  - Markdown Preview

## 🔧 Git Integration

### Initial Push Commands
```bash
cd C:\Users\rajuc\Documents\brain-
git add .
git commit -m "Initial vault setup with templates and structure"
git push origin main
```

### Sync Workflow
1. Pull latest changes: `git pull`
2. Make your notes
3. Commit changes: `git add . && git commit -m "Updated notes"`
4. Push changes: `git push`

## 📁 Vault Structure

### 00 - Inbox
Quick capture area for:
- Fleeting notes
- Ideas
- Tasks
- References to process

### 01 - Notes
Permanent knowledge base:
- Concepts
- Resources
- Reference materials
- Linked notes

### 02 - Projects
Active work:
- Project plans
- Task lists
- Progress tracking
- Outcomes

### 03 - Resources
External materials:
- Articles
- Books
- Videos
- Tools

### 04 - Templates
Standard formats:
- Daily journal
- Zettelkasten notes
- Project plans
- Meeting notes

### 05 - Archive
Historical content:
- Completed projects
- Outdated notes
- Reference materials

### Daily Notes
Time-based entries:
- Daily reflections
- Journal entries
- Mood tracking
- Progress updates

### Meta
Vault management:
- Configuration
- Style guides
- Documentation
- Templates

## 🎯 Best Practices

### Capturing Notes
1. Use Inbox for everything initially
2. Process Inbox daily
3. Convert to permanent notes
4. Link to existing knowledge

### Linking Strategy
- Always link when referencing other notes
- Use backlinks to discover connections
- Create hub notes for topics
- Maintain consistent naming

### Tagging System
- Use hierarchical tags: `#topic/subtopic`
- Keep tag list in Meta folder
- Consistent across all notes
- Use tags for filtering

## 🔄 Sync Schedule
- Commit daily
- Push weekly
- Review monthly
- Archive quarterly

## 📡 Troubleshooting

### Git Conflicts
```bash
git status
git pull --rebase
# Resolve conflicts in files
git add .
git rebase --continue
```

### Remote Tracking Issues
```bash
git push -u origin main
```