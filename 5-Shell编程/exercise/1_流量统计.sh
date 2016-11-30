#! /bin/bash

while [ "1"  ]
do
    eth=$1
    RXpre=$(cat /proc/net/dev | grep $eth | tr : " " | awk '{print $2}')
    TXpre=$(cat /proc/net/dev | grep $eth | tr : " " | awk '{print $10}')
    sleep 1
    RXnext=$(cat /proc/net/dev | grep $eth | tr : " " | awk '{print $2}')
    TXnext=$(cat /proc/net/dev | grep $eth | tr : " " | awk '{print $10}')
    clear

    echo -e "DATE: `date +%k:%M:%S`\n\t RX\t\tTX"
    echo -e "$eth \t $RX \t $TX"
    RX=$((${RXnext}-${RXpre}))
    TX=$((${TXnext}-${TXpre}))

    if [[ $RX -lt 1024 ]]; then
        RX="${RX} B/s"
    elif [[ $RX -gt 1048576 ]]; then
        RX=$(echo $RX | awk '{print $1/(1024*1024)" MB/s"}')
    else
        RX=$(echo $RX | awk '{print $1/1024" KB/s"}')
    fi

    echo -e "\t"

    if [[ $TX -lt 1024 ]]; then
        TX="${TX} B/s"
    elif [[ $TX -gt 1048576 ]]; then
        TX=$(echo $TX | awk '{print $1/(1024*1024)" MB/s"}')
    else
        TX=$(echo $TX | awk '{print $1/1024" KB/s"}')
    fi
done
