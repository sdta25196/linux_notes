#!/bin/bash
# Author: zhang.wen
# Date: 2016-8-3 13:27:38
# Description: Setting up the network associate information
# Version: v0.0.1

# Disabled the selinux
clear
echo "Set the SElinux to disabled."
setenforce 0 >> /dev/null
sed -i 's/SELINUX=.*/SELINUX=disabled/' /etc/selinux/config
echo 

# set the network configuration
cd /etc/sysconfig/network-scripts/
cp ifcfg-eth0{,.bak}

hw_addr=`ifconfig eth0 | grep -i hwaddr | awk '{print $5}'`
echo "============== Network configuration start ================================="
echo "============== Please input your network information ======================="
read -p "Please input the ip address: " ip_addr
read -p "Input the netmask: " netmask
read -p "Then give the correct gateway: " gateway
read -p "now is the first dns address: " dns1

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
EOF

echo "Your network information is:"
cat ifcfg-eth0
echo "============== Network information is configuration complete ======================="

echo "now restart the network services"
/etc/init.d/network restart &> /dev/null
srv_status=`echo $?`
if [ $srv_status -eq 0 ]; then
	echo "Service restart okay..."	
fi
