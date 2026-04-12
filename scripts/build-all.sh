#!/usr/bin/env bash
# Master build script for the Investment Tutorial
# Usage: bash scripts/build-all.sh
set -e

cd "$(dirname "$0")/.."
echo "Project root: $(pwd)"
echo ""

echo "=== Step 1: Translation Status ==="
py -3 scripts/translate.py --check
echo ""

echo "=== Step 2: Auto-Translate ==="
if [ -n "$ANTHROPIC_API_KEY" ]; then
    echo "ANTHROPIC_API_KEY detected. Running translation..."
    node scripts/translate-batch.js --locale all
else
    echo "ANTHROPIC_API_KEY not set. Skipping auto-translation."
    echo "To translate: export ANTHROPIC_API_KEY=sk-... && node scripts/translate-batch.js --locale all"
fi
echo ""

echo "=== Step 3: Build Website ==="
node scripts/build.js
echo ""

echo "=== Done ==="
