#!/bin/bash

read -p "Please input a number: " n
m=`echo $n | sed 's/[0-9]//g'`

if [ -z "$m" ]; then
    echo "Your input character is: $n"
else
    echo "The character you input is not a number, please retry."
fi
