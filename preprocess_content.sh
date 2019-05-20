#!/bin/bash
 
IN=report.txt
OUT=report-processed.txt

# Use fold to wrap lines within 76 chars
# cat -s to get single-space output
# And sed to escape HTML characters
echo "Preprocessing the Board report content, $IN -> $OUT ..."
fold -s -w 76 < $IN | cat -s | sed 's/&/\&amp;/g; s/</\&lt;/g; s/>/\&gt;/g; s/"/\&quot;/g; s/'"'"'/\&#39;/g' > $OUT