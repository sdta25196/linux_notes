#!/bin/bash

for i in `seq 1 10`; do
    echo "before break the '$i' is $i"
    if [ $i -eq 4 ]; then
        continue
    fi
        echo $i
done

echo "The for loop is completed..."
