#! /bin/bash
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

cd /usr/local/src
[ -f nginx-1.1.8.tar.gz ] || wget http://mirrors.sohu.com/nginx/nginx-1.1.8.tar.gz
tar zxf nginx-1.1.8.tar.gz
cd nginx-1.1.8
myum pcre-devel
./configure --prefix=/usr/local/nginx
check_last_status
make
check_last_status
make install
check_last_status

if [ -f /etc/init.d/nginx ]; then
	/bin/mv /etc/init.d/nginx /etc/init.d/nginx_`date +%s`
fi

curl http://www.apelearn.com/study_v2/.nginx_init  -o /etc/init.d/nginx
check_last_status
chmod 755 /etc/init.d/nginx
chkconfig --add nginx
chkconfig nginx on
curl http://www.apelearn.com/study_v2/.nginx_conf -o /usr/local/nginx/conf/nginx.conf
check_last_status

/etc/init.d/nginx start
check_last_status

echo -e "<?php\n	phpinfo(); ?>" > /usr/local/nginx/html/index.php
check_last_status
