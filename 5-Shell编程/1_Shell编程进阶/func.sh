#!/bin/bash

mysum () {
    sum=$[ $1 + $2 + $3 ]
    echo $sum
}

aa=1
bb=2
cc=3

mysum $aa $bb $cc
