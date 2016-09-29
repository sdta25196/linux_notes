#!/bin/bash

n=3

if [ $n -ge 3 ]; then
    echo "$n is greater or equal 3"
fi

n=2
if [ $n -le 2 ]; then
    echo "$n is lesser or equal 3"
fi

if [ $n -lt 2 ]; then
    echo "$n is lesser 2"
fi
