#!/bin/bash

for i in `seq 0 9`; do
    array[$i]=$RANDOM
done

echo "Before delete a element, The array length is: ${#array[@]}"
unset array[2]
echo "After delete a element, The array length is: ${#array[@]}"

echo ${array[@]} | sed 's/\ /\n/g' | sort -n

