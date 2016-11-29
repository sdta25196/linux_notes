#!/usr/bin/env python
#-*- coding:utf8 -*-

from subprocess import Popen, PIPE

p = Popen('sh echo_hello.sh', shell=True)
#p = Popen([./echo_hello.sh], stdout=PIPE, stderr=PIPE)
print "python main process."

#这里就没有按照顺序执行，因为subprecess会开一个子进程，
#而是直接执行下面的语句，等上面的语句执行完后，再返回结果
"""
python 1.7_subprecess.py
python main process.
hello world.
"""

#如果想要让子进程执行完之后再执行下面的语句，那么可以使用Popen生成对象的wait()方法
p1 = Popen('echo "I\'m a subprocess, please wait me."', shell=True)
p1.wait()
print "Python main process is ended."
"""
python 1.7_subprecess.py
python main process.
I'm a subprocess, please wait me.
Python main process is ended.
hello world.
"""

```
from subprocess import PIPE, Popen

In [7]: p1 = Popen(['ls'], stdout=PIPE)

In [8]: p1.stdout.read()
Out[8]: '1.1_hashlib.py\n1.2_os_walk.py\n1.3_os_walk_with_yield.py\n1.3_yield_generator.py\n1.4_pick_out_the_same_file.py\n1.5_find_top_10_biggest_file.py\n1.7_exception.py\n1.7_subprecess.py\na\nb\necho_hello.sh\n'

In [9]: p1 = Popen(['ls'], stdout=PIPE)

In [10]: p2 = Popen(['grep', 'py'], stdin=p1.stdout, stdout=PIPE)

In [11]: result = p2.stdout

In [12]: result
Out[12]: <open file '<fdopen>', mode 'rb' at 0x104a68f60>

In [13]: for i in result:
    print i,
	   ....:     
	   1.1_hashlib.py
	   1.2_os_walk.py
	   1.3_os_walk_with_yield.py
	   1.3_yield_generator.py
	   1.4_pick_out_the_same_file.py
	   1.5_find_top_10_biggest_file.py
	   1.7_exception.py
	   1.7_subprecess.py
```
