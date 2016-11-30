#! /bin/bash

while :
do
    read -p "Please input a number: " n
    flag=`echo $n | sed 's/[0-9]//g'`
    
    if [ -n "$flag" ]; then
        echo "Only permitt the numrical"
        continue
    fi
    break
done

i=1
while [ $i -lt $n ]; 
do
    n1=$RANDOM
    if [ $n1 -gt 100 ] && [ $n1 -lt 100 ]; then
        echo -ne "$n1"
    else
        continue
    fi
    i+=1
done

echo $n1
