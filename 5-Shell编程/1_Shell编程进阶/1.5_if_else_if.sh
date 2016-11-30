#!/bin/bash - 
#===============================================================================
#
#          FILE: 1.5_if_else_if.sh
# 
#         USAGE: ./1.5_if_else_if.sh 
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 04/03/2016 00:12
#      REVISION:  ---
#===============================================================================

#!/bin/bash

a=5

if [ $a -lt 5 ]; then
    echo "\$a < 5"
elif [ $a -eq 5 ]; then
    echo "\$a == 5"
else
    echo "\$a > 5"
fi
