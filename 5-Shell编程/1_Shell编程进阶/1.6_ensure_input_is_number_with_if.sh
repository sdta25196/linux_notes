#!/bin/bash

read -p "Please input a number: " n
m=`echo $n | sed 's/[0-9]//g'`

if [ -n "$m" ]; then
    echo "The character you input is not a number, please retry."
else
    echo "Your input character is: $n"
fi
