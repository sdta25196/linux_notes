#!/bin/bash

function get_ip_addr ()
{
    ifconfig | grep -A 1 "$1" | grep 'addr' | head -2 |  tail -1 | awk '{print $2}' | cut -d ':' -f 2
}

read -p "Please input you network interface card name: " if_name

echo "Your interface card $if_name ip address is `get_ip_addr $if_name`"
