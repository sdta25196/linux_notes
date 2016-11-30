#!/bin/bash - 
#===============================================================================
#
#          FILE: 1.4_interactive.sh
# 
#         USAGE: ./1.4_interactive.sh 
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 04/02/2016 23:46
#      REVISION:  ---
# read:
# -p prompot output the string PROMPT without a trailing newline before attempting to read
# -t time out and return failure if a complete line of input is not read within TIMEOUT seconds.  The value of the TMOUT variable is the default timeout.  TIMEOUT may be a fractional number.  If TIMEOUT is 0, read returns immediately, without trying to read any data, returning success only if input is available on the specified file descriptor.  The exit status is greater than 128 if the timeout is exceeded
#===============================================================================

#!/bin/bash
read -t 5 -p  "Please input a number: " number
echo "Your intput number is: $number"

