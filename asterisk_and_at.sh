#!/usr/bin/env bash

:<<EOF
运行结果如下：
root@kali:~/.pyenv# /bin/bash asterisk_and_at.sh  1 2 3 4 5 "hello world"
Listing args with "$*": 
Arg #1=1 2 3 4 5 hello world
所有的参数均认为是一个

Listing args with no double quoto $\*(没有被引用)
Arg #1=1
Arg #2=2
Arg #3=3
Arg #4=4
Arg #5=5
Arg #6=hello
Arg #7=world
所有的参数被认为是各个独立的单词

Listing args with "$\@": 
Arg #1=1
Arg #2=2
Arg #3=3
Arg #4=4
Arg #5=5
Arg #6=hello world

Listing args with $\@(没有被引用): 
Arg #1=1
Arg #2=2
Arg #3=3
Arg #4=4
Arg #5=5
Arg #6=hello
Arg #7=world
EOF

set -e
#set -x

index=1

echo "Listing args with \"\$*\": "
for arg in "$*"; do
	echo "Arg #$index=$arg"
	let index+=1
done

echo -e "所有的参数均认为是一个\n"

index=1
echo "Listing args with no double quoto \$\*(没有被引用)"
for arg in $*; do
	echo "Arg #$index=$arg"
	let index+=1
done
echo -e "所有的参数被认为是各个独立的单词\n"

index=1
echo -e "Listing args with \"\$\@\": "
for arg in "$@"; do
	echo "Arg #$index=$arg"
	let index+=1
done

echo 

index=1
echo "Listing args with \$\@(没有被引用): "
for arg in $@; do
	echo "Arg #$index=$arg"
	let index+=1
done

echo 
exit 0
