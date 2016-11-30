#!/bin/bash - 
#===============================================================================
#
#          FILE: factorial.sh
# 
#         USAGE: ./factorial.sh 
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 05/15/2016 11:59
#      REVISION:  ---
#===============================================================================

read -p "Total no of factorial wants" fact

ans=1
counter=0
while [ $fact -ne $counter ]; do
    counter=`expr $counter + 1`
    ans=`expr $ans \* $counter`
done

echo "Total of factorial is $ans"
