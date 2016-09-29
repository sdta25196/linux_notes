#!/bin/bash

while :
do
    read -p "Please input a number: " num
    m=`echo $num | sed 's/[0-9]//g'`
    #下面的这种写法是不正确的，sed并不能识别这种写法，所以只能用上面管道的方式
    #n=`sed 's/[0-9]//g "$num"'`
    echo $n

    if [ -z "$m" ]; then
        echo "Your input number is: $num" 
        exit
    else 
        echo "Please retry, only input a numberic..."
    fi
done
