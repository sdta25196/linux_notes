#!/bin/bash

file=a.txt
line=`wc -l $file | awk '{print $1}'`

for i in `seq 1 $line`
do
    n=`sed -n "$i"p $file | grep -o '[0-9]' | wc -l`
    #echo "the n's value is $n"
    if [[ $n -eq 1 ]] ; then
        echo "The -> $i <- lines has only one numric, and this is bellow: "
        sed -n "$i"p $file
    fi
done
