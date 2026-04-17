#!/usr/bin/env bash
# Master build script for the Chanma Investment Tutorial
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
    py -3 scripts/translate-batch.py --locale all
else
    echo "ANTHROPIC_API_KEY not set. Skipping auto-translation."
    echo "To translate: export ANTHROPIC_API_KEY=sk-... && py -3 scripts/translate-batch.py --locale all"
fi
echo ""

echo "=== Step 3: Build Website ==="
py -3 scripts/build.py
echo ""

echo "=== Done ==="
