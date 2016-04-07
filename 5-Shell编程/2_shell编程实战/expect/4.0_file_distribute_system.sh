#! /bin/bash

for ip in `cat ip.list`; do
    echo $ip
    ./4.0_file_distribute_system.exp $ip file
done
