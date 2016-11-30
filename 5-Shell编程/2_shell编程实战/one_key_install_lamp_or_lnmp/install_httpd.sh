#! /bin/bash
function check_last_status() {
    if [ $? != 0 ]; then
		echo "Error, The last command status haven some errors, please see the correct logs."
		exit 1
	fi
}

echo -e "####################### INSTALL APACHE HTTPD STARTED #######################"
echo -e "\nThe Version is 2.2.31"
echo -e "\n\n"

cd /usr/local/src/
[ -f httpd-2.2.31.tar.gz ] || wget http://mirrors.cnnic.cn/apache//httpd/httpd-2.2.31.tar.gz
tar zxf httpd-2.2.31.tar.gz
check_last_status
cd httpd-2.2.31

./configure \
--prefix=/usr/local/apache2 \
--with-included-apr \
--enable-so \
--enable-deflate=shared \
--enable-expires=shared \
--enable-rewrite=shared \
--with-pcre
check_last_status

make
check_last_status
make install
check_last_status

echo -e "\n\n"
echo -e "####################### INSTALL APACHE HTTPD COMPLETED #####################"
