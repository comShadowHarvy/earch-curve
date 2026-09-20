#!/usr/bin/env bash
# earth_curvature_gui.sh - Launch the interactive Earth Curvature Calculator in your browser

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HTML_FILE="$(cd "$SCRIPT_DIR/../.." && pwd)/earth_curvature_calculator.html"

if [[ ! -f "$HTML_FILE" ]]; then
  echo "Error: $HTML_FILE not found." >&2
  exit 1
fi

echo "Launching Earth Curvature Calculator in browser..."
echo "Path: file://$HTML_FILE"

if command -v xdg-open >/dev/null 2>&1; then
  xdg-open "file://$HTML_FILE" >/dev/null 2>&1 &
elif command -v sensible-browser >/dev/null 2>&1; then
  sensible-browser "file://$HTML_FILE" >/dev/null 2>&1 &
else
  echo "Please open: file://$HTML_FILE in your web browser."
fi
