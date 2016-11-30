#!/bin/bash
## Script Name: 1.4.1_how_to_add_two_variables with math opeartion
## Author Name: C.F
## Desire:	Test how to add some vairables with math operation

a=10
b=20

c=$[ $a + $b ]
echo $c

c=$(( $a * $b ))
echo $c
