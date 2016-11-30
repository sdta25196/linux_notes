#! /bin/bash

for ip in `cat ip.list`; do
    cat "The Current ip address is: $ip"
    /usr/bin/expect exe.exp $ip "ls -l /tmp; w; free -h; uptime"
done
