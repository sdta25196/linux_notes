#!/usr/bin/env python
#-*- encoding:utf-8 -*- 

import sys
import os

"""最简单的方法就是 [i for i in os.listdir('/proc') if i.isdigit()] """

def isNum(s):
	for i in s:
		if i in '0123456789':
			pass
		else:
			#print "%s i NOT a number" % s
			break
	else:
		print "%s is a number" % s

for i in os.listdir('/proc'):
	isNum(i)
