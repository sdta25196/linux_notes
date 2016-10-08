#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
with open …… as 这是一个固定语法，下面要求缩进,这种方法并不需要自己添加关闭文件流的操作
'''

with open('/tmp/tmp.txt') as fd:
	while True:
		per_line =  fd.readline()
		if not per_line:
			break
		print per_line,
