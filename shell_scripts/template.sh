#!/bin/bash
# Author: zhang.wen
# Date: 2016-8-3 13:27:38
# Version: v0.0.1

# Disabled the selinux
setenforce 0
sed -i 's/SELINUX=.*/SELINUX=disabled/' /etc/selinux/config

# set the network configuration
cd /etc/sysconfig/network-scripts/
cp ifcfg-eth0{,.bak}

hw_addr=`ifconfig eth0 | grep -i hwaddr | awk '{print $5}'`
echo "============== Please input your network information =======================\n"
read -p "Please input the ip address: " ip_addr
read -p "Input the netmask: " netmask
read -p "Then give the correct gateway: " gateway
read -p "now is the first dns address: " dns1
read -p "now is the second dns address: " dns2

> ifcfg-eth0
cat >> ifcfg-eth0 << EOF
DEVICE=eth0
HWADDR=$hw_addr
TYPE=Ethernet
ONBOOT=yes
NM_CONTROLLED=yes
BOOTPROTO=static

IPADDR=$ip_addr
NETMASK=$netmask
GATEWAY=$gateway
DNS1=$dns1
DNS2=$dns2
EOF

echo "Your network information is:\n"
cat ifcfg-eth0
echo "Network information is configuration complete..."
echo "\n=========================================================\n"

