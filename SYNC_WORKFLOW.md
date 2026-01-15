# English Translation Sync Workflow

This document describes how to keep the English translation in sync with the Chinese upstream repository.

## Repository Structure

- **Original Chinese Repository**: `https://github.com/liyupi/ai-guide` (upstream)
- **Your Local Translation**: Current directory with English content

## Sync Strategy

### Method 1: Track Changes via Git Branches

#### Initial Setup

```bash
# 1. Create a branch for English translations
git checkout -b english

# 2. Push to your fork (if you have one)
git push -u origin english
```

#### Ongoing Sync Process

**When new content is added to the Chinese upstream:**

```bash
# 1. Fetch latest changes from upstream (Chinese)
git fetch origin main

# 2. See what files changed
git diff main..origin/main --name-only

# 3. Merge the latest Chinese changes
git merge origin/main

# 4. Translate only the new/modified files
# (Check the git diff output to see what needs translation)

# 5. Commit your translations
git add .
git commit -m "docs: translate new content from Chinese upstream"

# 6. Push to your branch
git push
```

### Method 2: Separate Fork Repository

If you want to maintain a completely separate repository:

```bash
# 1. Fork the original repo on GitHub (your-username/ai-guide-en)

# 2. Add your fork as a remote
git remote add fork https://github.com/your-username/ai-guide-en.git

# 3. Work on your English branch
git checkout -b english

# 4. Push your English translations to your fork
git push -u fork english

# 5. Periodically sync with upstream
git fetch origin main
git merge origin/main
# Translate new content
git push fork english
```

### Method 3: Manual Sync Checklist

**Periodic sync routine (weekly or when upstream updates):**

1. **Pull latest changes:**
   ```bash
   git pull origin main
   ```

2. **Identify new/modified files:**
   ```bash
   git diff HEAD~1 --name-only --diff-filter=MAR
   # M = Modified, A = Added, R = Renamed
   ```

3. **Check which files need translation:**
   ```bash
   # Find markdown files modified in last commit
   git diff HEAD~1 HEAD --name-only | grep "\.md$"
   ```

4. **Translate new content:**
   - Read the Chinese version
   - Translate to English maintaining the same structure
   - Preserve all formatting, images, and links

5. **Test the site:**
   ```bash
   npm run docs:dev
   ```

6. **Commit and push:**
   ```bash
   git add .
   git commit -m "docs: sync translations with upstream $(date +%Y-%m-%d)"
   git push origin english
   ```

## Automation Script

Create a script to automate the sync process:

```bash
#!/bin/bash
# sync-translations.sh

echo "Fetching upstream changes..."
git fetch origin main

echo "Checking for new/modified files..."
CHANGED_FILES=$(git diff main..origin/main --name-only --diff-filter=MAR | grep "\.md$")

if [ -z "$CHANGED_FILES" ]; then
    echo "No new markdown files to translate."
    exit 0
fi

echo "Files that need translation:"
echo "$CHANGED_FILES"

echo ""
echo "Merging upstream changes..."
git merge origin/main

echo ""
echo "Translation checklist:"
for file in $CHANGED_FILES; do
    echo "  - [ ] $file"
done

echo ""
echo "After translating, commit with:"
echo "  git add ."
echo "  git commit -m 'docs: translate new content'"
echo "  git push"
```

## Best Practices

### 1. Commit Message Convention

Use consistent commit messages for translations:
- `docs: translate [filename]`
- `docs: sync translations with upstream`
- `docs: update English translation for [section]`

### 2. File Organization

Keep file structure identical to Chinese version:
- Same directory hierarchy
- Same file names (only content differs)
- Same frontmatter structure

### 3. Review Before Merging

Before syncing:
- Test the site locally: `npm run docs:dev`
- Check for broken links
- Verify all images load correctly
- Ensure translation quality

### 4. Conflict Resolution

If merge conflicts occur:

```bash
# 1. Start the merge
git merge origin/main

# 2. If conflicts occur, resolve them manually
git status  # See conflicted files

# 3. For each conflict:
#    - Open the file
#    - Choose the English version (your translation)
#    - Keep any new structure from Chinese version
#    - Mark as resolved: git add <file>

# 4. Complete the merge
git commit
```

## Monitoring Upstream Changes

### Set up GitHub notifications:

1. Go to https://github.com/liyupi/ai-guide
2. Click "Watch" → "Custom"
3. Select "Releases" and "Activity"

### RSS Feed:

```
https://github.com/liyupi/ai-guide/commits/main.atom
```

### Git Watch Command:

```bash
# Check last commit date from upstream
git log origin/main -1 --format="%H %ai %s"
```

## Translation Maintenance

### Quality Checklist

When translating new content:
- [ ] Maintain consistent terminology
- [ ] Preserve technical terms in English where appropriate
- [ ] Keep markdown formatting identical
- [ ] Preserve all code blocks
- [ ] Maintain image links
- [ ] Keep internal links updated
- [ ] Use consistent writing style

### Terminology Guide

Keep a glossary of common translations:
- 教程 → Tutorial
- 实战 → Practice / Hands-on
- 项目 → Project
- 产品 → Product
- 变现 → Monetization
- 程序员 → Programmer
- 编程 → Programming

## Quick Reference

```bash
# Check sync status
git log HEAD..origin/main --oneline

# Sync with upstream
git fetch origin main
git merge origin/main

# See what needs translation
git diff HEAD~1 HEAD --name-only | grep "\.md$"

# Build and test
npm run docs:dev

# Commit translations
git add .
git commit -m "docs: sync translations"
git push origin english
```

## Questions?

If you encounter issues:
1. Check git status: `git status`
2. Review recent commits: `git log --oneline -10`
3. Compare with upstream: `git diff main origin/main`
