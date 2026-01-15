#!/bin/bash
# Sync script to keep English translation updated with Chinese upstream

echo "🔄 Syncing English translation with Chinese upstream..."
echo ""

# Fetch latest changes from origin (Chinese repo)
echo "1️⃣ Fetching latest changes from upstream..."
git fetch origin main

# Check if there are any new commits
if [ $(git rev-parse HEAD) = $(git rev-parse origin/main) ]; then
    echo "✅ Already up to date! No new changes to sync."
    exit 0
fi

# Show what changed
echo ""
echo "2️⃣ Files changed since last sync:"
git log HEAD..origin/main --oneline | head -10

echo ""
echo "3️⃣ New or modified markdown files:"
git diff --name-only HEAD..origin/main | grep "\.md$" | grep -v "node_modules" | head -20

# Ask for confirmation
echo ""
read -p "Do you want to merge these changes? (y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "❌ Sync cancelled."
    exit 0
fi

# Merge the changes
echo ""
echo "4️⃣ Merging upstream changes..."
git merge origin/main --no-edit

echo ""
echo "✅ Sync complete! Next steps:"
echo "   1. Review changed files in Chinese"
echo "   2. Translate new/modified content to English"
echo "   3. Test the site: npm run docs:dev"
echo "   4. Commit translations: git add . && git commit -m 'docs: translate new content'"
echo "   5. Push to your branch: git push origin english"
