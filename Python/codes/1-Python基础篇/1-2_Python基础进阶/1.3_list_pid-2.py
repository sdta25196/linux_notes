#!/usr/bin/env python

import sys
import os

def isNum(s):
	for i in s:
		if i in '0123456789':
			pass
		else:
			#print "%s i NOT a number" % s
			break
	else:
		print s,

for i in os.listdir('/proc'):
	isNum(i)
