#!/usr/bin/env bash

SEARCH_PATTERN="$1"
OUTPUT="$2"

# Default output file
if [ -z "$OUTPUT" ]; then
  OUTPUT="results.txt"
fi

# Abort if output file exists
if [ -f "$OUTPUT" ]; then
  echo "Error: Output file already exists. Aborting."
  exit 1
fi

# Download Moby Dick
curl -s -o mobydick.txt https://gist.githubusercontent.com/StevenClontz/4445774/raw/1722a289b665d940495645a5eaaad4da8e3ad4c7/mobydick.txt

# Count occurrences (case-insensitive)
OCCURRENCES=$(grep -oi "$SEARCH_PATTERN" mobydick.txt | wc -l)

# Write summary
echo "The search pattern $SEARCH_PATTERN was found $OCCURRENCES time(s)." > "$OUTPUT"

# Write matching lines
echo "" >> "$OUTPUT"
echo "Lines containing the word:" >> "$OUTPUT"
grep -in "$SEARCH_PATTERN" mobydick.txt | cut -d: -f1-3 >> "$OUTPUT"





