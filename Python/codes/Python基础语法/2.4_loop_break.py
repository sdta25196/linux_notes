#!/usr/bin/env python

"""
Purpose: Test the break statement in loop.
Date: 2016-10-17 Mon 16:32
Author: Chang.Feng
Output: 0 1 3 4 5 6
"""

import sys
import time

for i in xrange(10):
	if 2 == i:
		continue
	elif i == 9:
		break
	elif 6 == i:
		pass
	elif 7 == i:
		sys.exit()
	print i,
else:
	print "program end..."
print "hello, loop"
