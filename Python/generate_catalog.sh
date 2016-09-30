#!/usr/bin/env bash

/bin/awk 'NR%2==1' tmp.txt | awk -F "" 'BEGIN { OFS="" } {for(i=4;i<=5;i++) if($i==" "){$i="_"}print }' | xargs touch {}.md
