#!/bin/bash - 
#===============================================================================
#
#          FILE: fact.sh
# 
#         USAGE: ./fact.sh 
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 05/15/2016 12:09
#      REVISION:  ---
#===============================================================================

fact ()
{
    if [ $1 -gt 1 ]; then
        y=`expr $1 - 1`
        fact $y

        x=$(( $1 * $? ))
        return $x
    else
        return 1
    fi
}

echo -e "Enter a number : \c"
read num

fact $num

echo "Factorial of $num is $?."
