#!/bin/bash - 
#===============================================================================
#
#          FILE: 求阶乘.sh
# 
#         USAGE: ./求阶乘.sh 
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 05/15/2016 10:40
#      REVISION:  ---
#===============================================================================

echo "Enter a n;umber"
read num
factorial=1
n=$num

while [ $num -ge 1 ]; do
    factorial=`echo $factorial \* $num | bc`
    let num--
done

echo "factorial of $n is $factorial"
