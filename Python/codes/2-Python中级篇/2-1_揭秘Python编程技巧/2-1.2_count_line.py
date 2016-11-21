#!/usr/bin/env python
#-*- coding:utf8 -*-

import sys

input = sys.stdin

def lineCount(f):
	n = 0
	
	for i in f:
		n += 1
	
	return n

print lineCount( input )

