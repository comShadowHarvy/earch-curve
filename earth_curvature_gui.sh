#!/usr/bin/env bash
# earth_curvature_gui.sh - Launch the interactive Earth Curvature Calculator in your browser

SCRIPT_DIR="$(cd "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")" && pwd)"
if [[ -f "$SCRIPT_DIR/index.html" ]]; then
  HTML_FILE="$SCRIPT_DIR/index.html"
elif [[ -f "$SCRIPT_DIR/earth_curvature_calculator.html" ]]; then
  HTML_FILE="$SCRIPT_DIR/earth_curvature_calculator.html"
else
  echo "Error: HTML calculator not found in $SCRIPT_DIR." >&2
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
