#!/bin/bash
 
echo "Preprocessing the Board report content" 

# Use fold to wrap lines within 76 chars
# And sed to escape HTML characters
fold -s -w 76 < report.txt | sed 's/&/\&amp;/g; s/</\&lt;/g; s/>/\&gt;/g; s/"/\&quot;/g; s/'"'"'/\&#39;/g' > report-processed.txt