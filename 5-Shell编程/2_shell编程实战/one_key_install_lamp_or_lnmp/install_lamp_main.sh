#! /bin/bash
##########################################################################################
# Date:			2016-04-07 18:00 Thu
# Author:		Feng.ch
# Description:	You can one key install lamp or lnmp, enjoy it...
# 
# NOTICE: If bellow file or directories is used for you, Just operation it easy by easy.
# Keep your directories is clean
# rm -rf /etc/my.cnf 
function stop_service() {
	service_pid=`ps aux | grep -i "$1" | grep -v grep | awk -F ' ' '{print $2}'`
 	if [ -z "$service_pid" ]; then
 		echo "No Such Process for $service_pid...."
 	else
 		kill -9 `echo $service_pid`
 	fi
}
 #/etc/init.d/mysqld stop
 rm -rf /etc/init.d/mysqld 
# rm -rf /data/mysql
# rm -rf /usr/local/mysql*
##########################################################################################
echo -e "\t\tIt will be install lamp or lnmp."
sleep 1
echo -e "\t\tSTART ........ ............"

## check last command status is okay or not ok.
function check_last_status() {
	if [ $? != 0 ]; then
		echo "Error, The last command status haven some errors, please see the correct logs."
		exit 1
	fi
}

## get the architecture from the system, i686 or x86_64, or used the system command arch is okay too.
arch=`uname -r | awk -F '.' '{print $NF}'`

## close the SElinux
sed -i 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/selinux/config
selinux_staus=`getenforce`
if [ $selinux_staus == "enforcing" ]; then
	setenforce 0
fi

## close iptables
iptables-save > /etc/sysconfig/iptables_`date +%s`
ip6tables-save > /etc/sysconfig/ip6tables_`date +%s`
iptables -F
ip6tables -F
service iptables save
service ip6tables save

## if the package is already installed, then continue, omit it.
function myum() {
	if ! rpm -qa | grep "^$1"; then
		yum install -y $1
		check_last_status
	else
		echo -e "\tWARNNING:The software [ --> $1 <-- ] is already installed."
	fi
}

## install some condition packages.
for soft in gcc wget perl perl-devel libaio libaio-devel pcre-devel zlib-devel; do
	myum $soft
done

## install epel
if rpm -qa epel-release > /dev/null; then
	rpm -e elepl-release
fi

if ls /etc/yum.repos.d/epel* &> /dev/null; then
	rm -f /etc/yum.repos.d/epel*
fi
wget -P /etc/yum.repos.d/ http://mirrors.aliyun.com/repo/epel-6.repo

## function of check service is running or not, example nginx, httpd, mysqld, php-fpm
check_service () {
	if [ "$1" == "phpfpm" ]; then
		s='php-fpm'
	else
		s=$1
	fi

	n=`ps aux | grep "$s" | grep -v grep | wc -l`
	if [ $n -gt 0 ]; then
		echo "$1 service is already started...\n"
	else
		if [ -f /etc/init.d/$1 ]
			/etc/init.d/$1 start
			check_last_status
		else
			/bin/bash /root/shell/install_$1.sh
		fi
	fi
}

## install mysql
/bin/bash /root/shell/install_mysql.sh
/bin/bash /root/shell/install_httpd.sh
