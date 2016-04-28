#! /bin/bash

get_a_num()
{
    n=$[$RANDOM%10]
    echo $n
}

get_numbers()
{
    for i in 1 2 3; do
        a[$i]=`get_a_num`
    done
    temp=`echo ${a[@]} | sed 's/ //g'`
    echo $temp
}

if [ -n "$1" ]; then
    m=`echo $1 | sed 's/[0-9]//g'`
    if [ -n "$m" ]; then
        echo "Usage bash $0 n, n is a number, i.e. bash $0 3"
        exit
    else
        for i in `seq 1 $1`
        do
            get_numbers
        done
    fi
else
    get_numbers
fi
