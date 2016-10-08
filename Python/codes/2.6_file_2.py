#!/usr/bin/env python
# -*- coding:utf-8 -*-

fd = open('/tmp/tmp.txt')

'''因为文件对象也是可以遍历对象，所以我们可以直接遍历文件对象，
而不调用它的readlines方法，因为调用readlines时会在内存中生成一个list，而如果文件非常大时，则会消耗非常大的资源，
所以如果要遍历一个文件对象，则不需要调用它的方法，直接遍历文件即可'''
for line in fd: 
	print line,

fd.close()
