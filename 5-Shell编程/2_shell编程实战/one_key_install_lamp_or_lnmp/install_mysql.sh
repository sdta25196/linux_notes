#! /bin/bash
## Name:			install_mysql.sh
## Author:			Feng.ch
## Description:		This is a branch of one key install lnmp or lamp, provide a invidual function
## Date:			2016-04-07
## ChangeTime:		18:45
################################################################################################### 

## check last command status is okay or not ok.
function check_last_status() {
    if [ $? != 0 ]; then
		echo "Error, The last command status haven some errors, please see the correct logs."
		exit 1
	fi
}

## if the package is already installed, then continue, omit it.
function myum() {
		if ! rpm -qa | grep "^$1"; then
			yum install -y $1
			check_last_status
		else
			echo -e "\tWARNNING:The software [ $1 ] is already installed."
		fi
}

echo -e "############ MYSQL INSTALL STARTED ################"
echo -e "\n\n"
echo "Chose the version of mysql, just move your finger 1 or 2, then touch the Enter... HOLD ON!"
echo
select mysql_v in "5.1" "5.6"; do
case $mysql_v in
	5.1)
		cd /usr/local/src/
		[ -f mysql-5.1.73-linux-i686-glibc23.tar.gz ] || wget http://mirrors.sohu.com/mysql/MySQL-5.1/mysql-5.1.73-linux-i686-glibc23.tar.gz
		tar zxf mysql-5.1.73-linux-i686-glibc23.tar.gz
		check_last_status
		
		[ -d /usr/local/mysql ] && /bin/mv /usr/local/mysql /usr/local/mysql_`date +%s`
		mv mysql-5.1.73-linux-i686-glibc23 /usr/local/mysql
		check_last_status

		if ! grep -i '^mysql' /etc/passwd; then
			useradd -M -s /sbin/nologin mysql
			check_last_status
		fi

		myum compat-libstdc++-33

		# validation the mysql data directory
		[ -d /data/mysql ] && /bin/mv /data/mysql /data/mysql_`date +%s`
		mkdir -p /data/mysql
		chown -R mysql:mysql /data/mysql

		# initialization the mysql database
		cd /usr/local/mysql/
		./scripts/mysql_install_db --user=mysql --datadir=/data/mysql/
		check_last_status
		
		# generate a .cnf file for mysqld
		[ -d /etc/my.cnf ] && /bin/mv  /etc/my.cnf /etc/my.cnf_`date +%s`
		/bin/cp ./support-files/my-large.cnf /etc/my.cnf
		check_last_status
		# append a line after [mysqld], e.g. datadir = /data/mysql
		sed -i '/^\[mysqld]$/a\datadir = /data/mysql' /etc/my.cnf

		# generate the start script for auto start on system startup.
		/bin/cp support-files/mysql.server /etc/init.d/mysqld
		sed -i 's#^datadir=#datadir=/data/mysql#g' /etc/init.d/mysqld
		chmod 755 /etc/init.d/mysqld
		chkconfig --add mysqld
		chkconfig mysqld on

		# start the mysqld service
		/etc/init.d/mysqld start
		check_last_status
		break
		;;
	5.6)
		cd /usr/local/src/
		[ -f mysql-5.6.29-linux-glibc2.5-i686.tar.gz ] || wget http://mirrors.sohu.com/mysql/MySQL-5.6/mysql-5.6.29-linux-glibc2.5-i686.tar.gz
		tar zxf mysql-5.6.29-linux-glibc2.5-i686.tar.gz
		[ -d /usr/local/mysql/ ] && /bin/mv /usr/local/mysql /usr/local/mysql_5.6_before_reinstall_`date +%s`
		check_last_status	
		/bin/mv mysql-5.6.29-linux-glibc2.5-i686 /usr/local/mysql
		
		# check the user for mysql
		if ! grep '^mysql' /etc/passwd; then
			useradd -M -s /sbin/nologin mysql
		fi

		# install depencency package
		myum compat-libstdc++-33
		if check_last_status; then
			echo -e "\t: compat-libstdc++-33 is installed..."
			echo 
		fi


		[ -d /data/mysql ] && /bin/mv /data/mysql /data/mysql_`date +%s`
		mkdir -p /data/mysql
		chown -R mysql:mysql /data/mysql

		# initialization the mysql database...
		cd /usr/local/mysql
		[ -f /etc/my.cnf ] && /bin/mv /etc/my.cnf /etc/my.cnf_`date +%s`
		./scripts/mysql_install_db --user=mysql --datadir=/data/mysql
		check_last_status

		# copy the mysql configuration file to /etc/my.cnf
		/bin/cp support-files/my-default.cnf /etc/my.cnf
		sed -i '/^\[mysqld\]$/a\datadir = /data/mysql' /etc/my.cnf
		check_last_status

		# append a line after [mysqld]
		/bin/cp support-files/mysql.server /etc/init.d/mysqld
		check_last_status
		sed -i 's#^datadir=#datadir=/data/mysql#g' /etc/init.d/mysqld
		check_last_status
		/etc/init.d/mysqld start
		check_last_status
		break
		;;
	*)
		echo "only the version you can choose: 1(5.1) ro 2(5.6)"
		exit 1
		;;
	esac
done
echo -e "The mysql $mysql_v install completement...\t\nCongratulations..................."
echo -e "The Mysql is installed ... ...\n\n "
echo -e "############ MYSQL INSTALL COMPLETEMENTED ################"
