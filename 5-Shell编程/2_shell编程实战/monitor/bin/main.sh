#!/bin/bash
## Writed by: ChangFeng
## Date: 2016-04-05 21:51

# 是否发送邮件
export send=1

# 过滤ip地址
export addr=`/sbin/ifconfig | grep -A 1 'eth1 ' | grep 'inet addr:' | awk -F ':' '{print $2}' | awk '{print $1}'`
dir=`pwd`

# 显示最后的一级目录，其实basename就可以搞定
# last_dir=`echo $dir | awk -F '/' '{print $NF}'
base_dir=`/bin/basename $dir`

# 下面的判断目的是，保证执行脚本的时候，我们所在的目录是在./bin目录下，不然监控、日志脚本可能找不到
if [ $base_dir == "bin" ] || [ $last_dir == "bin/"]; then
    conf_file="../conf/mon.conf"
else
    echo "you should be change dir to the bin directory"
    exit
fi
#  这一行就是定义了本脚本及所有子脚本的输出都是在指定的日志里
exec 1>> ../log/mon.log 2>> ../log/err.log

echo "`date +%F\ %T` load average"
/bin/bash ../shares/load.sh

# 先检测配置文件是否需要监控502
if grep -q 'to_mon_502=1' $conf_file; then
    export log=`grep 'logfile=' $conf_file | awk -F '=' '{print $2}' sed 's/ //g'`
    /bin/bash ../shares/502.sh
fi
