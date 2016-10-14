#!/bin/bash
# Date: 2016-10-14 13:18
# Purpose: Test the bash builtin variables
# Output: 
##########################################################
# sh 1.4_variables.sh 1 a 2 b 3 c 4 d "hello'\n'"
# echo $0... ...
# 1.4_variables.sh
# echo $1... ...
# 1
# echo $2... ..
# a
# echo $3... ...
# 2
# echo $*... ...
# 1 a 2 b 3 c 4 d hello'\n'
# echo $#... ...
# 9
# echo $@... ...
# 1 a 2 b 3 c 4 d hello'\n'
##########################################################

echo 'echo $0... ...'
echo $0

echo 'echo $1... ...'
echo $1

echo 'echo $2... ..'
echo $2

echo 'echo $3... ...'
echo $3

echo 'echo $*... ...'
echo $*

echo 'echo $#... ...'
echo $#

echo 'echo $@... ...'
echo $@
