#!/usr/bin/env bash
set -euo pipefail

TARGET="${1:-incubator}"

if [ -d "$TARGET/.git" ]; then
  echo "incubator repo already present: $TARGET"
  exit 0
fi

git clone --filter=blob:none --no-checkout https://github.com/apache/incubator.git "$TARGET"
cd "$TARGET"
git sparse-checkout init --cone
git sparse-checkout set tools/health/reports
git checkout main
