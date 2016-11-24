##Pyton处理标准输出
- sys.stdout.write()返回一个None类型，用来输出到文件中，如果后面不跟文件名，那么就输出到标准输出，标准输出到显示器，显示器也是个文件，Ｕnix哲学
```
help( sys.stdout.write )
write(...)
    write(str) -> None.  Write string str to file.
	    
	Note that due to buffering, flush() or close() may be needed before
	the file on disk reflects the data written.
```
- sys.stderr.write()，也是输出到文件，只不过是打印标准错误输出
```
help( sys.stderr.write )
write(...)
    write(str) -> None.  Write string str to file.
	    
    Note that due to buffering, flush() or close() may be needed before
    the file on disk reflects the data written.
```

##print和stdout的区别
- print通常是调用一个stdout对象的write方法
- print会先进行格式转换
- print会在最后添上换行符
写入一个文件也可以通过print >> fd,"string ...."的方式来写入
当向一个文件写入的时候，提示必须写入字符串时，可以使用这种方式来写入f.write("%d\n" % 3)

##stdout中的buffer
```
#!/usr/bin/env python
#-*- coding:utf8 -*-

import sys, time

for i in xrange(10):
    sys.stdout.write("str:%d " % i)
    time.sleep(1)
    #sys.stdout.write('\n') #这里不知道为什么也是经过１秒后就自动输出一个数字，理论上来讲，应该是１０s后全部输出才对
	"""加了\n就相当于print了，所以就没buffer了。其实print就是调用了sys.stdout.write(obj+'\n')
	"""
```
执行结果如下
```
# python 2-1.3_sys_stderr_write_buffer.py
str:0 str:1 str:2 str:3 str:4 str:5 str:6 str:7 str:8 str:9 root@kali:
```
如果想要实现一秒输出一个数字，那么需要使用-u选项，即python -u buffer.py(假如上面的程序名为buffer.py)，也可以在代码中实现
```
#!/usr/bin/env python
#-*- coding:utf8 -*-

import sys, time

for i in xrange(10):
    sys.stdout.write("str:%d " % i)
    time.sleep(1)
    #sys.stdout.write('\n')
	sys.stdout.flush()
```
这样也可以实现拷贝文件，如果没有scp安装的情况下
```
cat ftp-0.17-54.el6.x86_64.rpm | ssh 192.168.31.128 "cat - > /tmp/ftp-0.17-54.el6.x86_64.rpm"
```
