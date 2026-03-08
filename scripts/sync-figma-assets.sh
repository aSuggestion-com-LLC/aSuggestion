#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

HTML_FILES=(index.html about.html community.html contact.html payment.html)

for f in assets/images/*; do
  [ -f "$f" ] || continue
  b="$(basename "$f")"
  id="$(echo "$b" | grep -oE '[0-9a-f-]{36}' || true)"
  ext="${b##*.}"
  if [ -n "$id" ]; then
    new="assets/images/$id.$ext"
    if [ "$f" != "$new" ]; then
      mv "$f" "$new"
      b="$(basename "$new")"
    fi
  fi
done

for f in assets/images/*; do
  [ -f "$f" ] || continue
  b="$(basename "$f")"
  id="${b%.*}"
  for html in "${HTML_FILES[@]}"; do
    perl -i -pe "s#https://www\\.figma\\.com/api/mcp/asset/$id#assets/images/$b#g" "$html"
  done
done

echo "Sincronizacao concluida."
echo "Links restantes do Figma:"
rg -o "https://www\\.figma\\.com/api/mcp/asset/[a-z0-9-]+" "${HTML_FILES[@]}" | sort -u || true
