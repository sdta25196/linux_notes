#!/bin/bash

read -p "Please input a number: " num
m=`echo "$num" | sed 's/[0-9]//g'`
if [ -n "$m" ]; then
    echo "Please only input the numbers."
    exit 10
fi

m=$[ $num % 2 ]
case $m in
    0)
        echo "This number is even number"
        ;;
    1)
        echo "This number is odd number"
        ;;
    *)
    echo "This is the default message."
    ;;
esac
