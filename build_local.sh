#!/bin/bash
set -euo pipefail

export WORKDIR=/tmp/incubator-site

function fatal() {
    echo "$*" >&2
    exit 1
}

rm -rf "$WORKDIR"
mkdir -p "$WORKDIR"

# 1) Bake the site
./bake.sh -b . "$WORKDIR" || fatal "Build failed, exiting"

# 2) Generate Pagefind inputs + index under /training
python3 tools/seealso/pagefind.py tools/seealso/resources.yml \
  --out-dir "$WORKDIR/training" \
  || fatal "Pagefind item generation failed"

rm -rf "$WORKDIR/training/pagefind"
npx -y pagefind \
  --site "$WORKDIR/training" \
  --glob "_pagefind_items/*.html" \
  --output-subdir pagefind \
  || fatal "Pagefind indexing failed"

# 3) Serve the baked output
cd "$WORKDIR"
python3 -m http.server 8000