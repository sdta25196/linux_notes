#!/usr/bin/env python
#-*- encoding:utf-8 -*-
import sys

''' sys.argv用来打印参数，类似于shell中的$1, $2, $n'''
#print sys.argv[0], sys.argv[1], sys.argv[2]

def isNum(s):
	for i in s:
		if i in '0123456789':
			pass
		else:
			print "%s is NOT a number" % s
			sys.exit()
	else:
		print "%s is a number" % s

isNum( sys.argv[1] )
