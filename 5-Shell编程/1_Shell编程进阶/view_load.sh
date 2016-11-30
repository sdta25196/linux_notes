#!/bin/bash

while : ;do
    load=`uptime | awk '{print $(NF-2)}' | cut -d '.' -f 1`
    if [ $load -gt 10 ]; then
        echo "system is load average high" | mail -s "system load" hienha@163.com
    fi
    sleep 15
done
