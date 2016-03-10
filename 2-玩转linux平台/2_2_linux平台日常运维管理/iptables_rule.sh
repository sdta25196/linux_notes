#/bin/bash
ipt="/sbin/iptables"
$ipt -F
$ipt -P INPUT DROP
$ipt -P OUTPUT ACCEPT
$ipt -P FORWARD ACCEPT

$ipt -A INPUT -s 192.168.3.0/24 -p tcp --dport 22 -j ACCEPT
$ipt -A INPUT -d 192.168.3.0/24 -j ACCEPT
$ipt -A INPUT -p tcp --dport 80 -j ACCEPT
$ipt -A INPUT -p tcp --dport 21 -j ACCEPT
