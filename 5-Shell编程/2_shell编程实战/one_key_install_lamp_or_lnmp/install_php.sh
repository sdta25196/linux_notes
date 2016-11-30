#! /bin/bash
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

echo-e "############# STARTED INSTALL PHP ##################" 
echo"\n\n"
echo "Please chose the you wanna version of php."

select php_v in 5.4 5.6; do
	case $php_v in
		5.4)
			cd /usr/local/src/
			[ -f php-5.4.45.tar.bz2 ] || wget http://cn2.php.net/get/php-5.4.45.tar.bz2/from/this/mirror -O php-5.4.45.tar.bz2
			tar jxf php-5.4.45.tar.bz2
			check_last_status
			cd php-5.4.45

			for i in openssl-devel bzip2-devel libxml2-devel curl-devel libpng-devel \
					libjpeg-devel freetype-devel libmcrypt-devel libtool-ltdl-devel \
					perl-devel 
			do
				myum $i
			done
			check_last_status

			./configure \
			--prefix=/usr/local/php \
			--with-apxs2=/usr/local/apache2/bin/apxs \
			--with-config-file-path=/usr/local/php/etc  \
			--with-mysql=/usr/local/mysql \
			--with-libxml-dir \
			--with-gd \
			--with-jpeg-dir \
			--with-png-dir \
			--with-freetype-dir \
			--with-iconv-dir \
			--with-zlib-dir \
			--with-bz2 \
			--with-openssl \
			--with-mcrypt \
			--enable-soap \
			--enable-gd-native-ttf \
			--enable-mbstring \
			--enable-sockets \
			--enable-exif \
			--disable-ipv6
			check_last_status

			make 
			check_last_status
			make install
			check_last_status

			[ -f /usr/local/php/etc/php.ini ] || /bin/cp php.ini-production  /usr/local/php/etc/php.ini
			break
			;;
		5.6)
			cd /usr/local/src/
			[ -f php-5.6.6.tar.bz2 ] || wget http://cn2.php.net/get/php-5.6.6.tar.bz2/from/this/mirror -O php-5.6.6.tar.bz2	
			tar jxf php-5.6.6.tar.bz2
			cd php-5.6.6
			for i in openssl-devel bzip2-devel libxml2-devel curl-devel libpng-devel \
						libjpeg-devel freetype-devel libmcrypt-devel libtool-ltdl-devel \
						perl-devel
			do
				myum $i
			done
			check_last_status

			# check previous version of php
			[ -d /usr/local/php/ ] && /bin/mv /usr/local/php/ /usr/local/php_`date +%s`
			
			./configure \
			--prefix=/usr/local/php \
			--with-apxs2=/usr/local/apache2/bin/apxs \
			--with-config-file-path=/usr/local/php/etc  \
			--with-mysql=/usr/local/mysql \
			--with-libxml-dir \
			--with-gd \
			--with-jpeg-dir \
			--with-png-dir \
			--with-freetype-dir \
			--with-iconv-dir \
			--with-zlib-dir \
			--with-bz2 \
			--with-openssl \
			--with-mcrypt \
			--enable-soap \
			--enable-gd-native-ttf \
			--enable-mbstring \
			--enable-sockets \
			--enable-exif \
			--disable-ipv6
			check_last_status
			make 
			check_last_status
			make install
			check_last_status

			[ -f /usr/local/php/etc/php.ini ] || /bin/cp php.ini-production  /usr/local/php/etc/php.ini
			break
			;;
		*)
			echo "provide 1 or 2 offer chose..."
			;;
	esac
done

echo -e "############# INSTALL PHP ENDS #####################"
echo -e "\n\n"

echo -e "############# CONFIGURATION PHP & APACHE  START #####################"
sed -i '/AddType application.x-gzip .gz .tgz$/a\AddType application\/x-httpd-php .php' /usr/local/apache2/conf/httpd.conf
check_last_status

# generate the php index.php file.
cat > /usr/local/apache2/htdocs/index.php << EOF
<?php
	phpinfo();
?>
EOF

if /usr/local/php/bin/php -i | grep -iq 'date.timezone => no value'; then
	sed -i '/;date.timezone =$/a\date.timezone ="Asia\/Chongqing"' /usr/local/php/etc/php.ini
fi

/usr/local/apache2/bin/apachectl restart
check_last_status
echo -e "############# CONFIGURATION PHP & APACHE  ENDS ######################"
