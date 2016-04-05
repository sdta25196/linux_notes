#!/bin/bash

function myfun() {
    local sum=$[ $1 + $2 ]
    echo $sum
}

a=30
b=20
myfun $a $b

echo "Now I tried to display the founction internal variable in outside, the sum is $sum"
