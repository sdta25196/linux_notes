#!/bin/bash

echo "Generate a tmp.txt in current directory..."
echo
cat << "EOF" > tmp.txt
1 2 3 4 aa
bb
cc dd ee ff
gg
EOF
echo "Generate a tmp.txt complete..."

for i in `cat tmp.txt`; do
    echo $i
done
