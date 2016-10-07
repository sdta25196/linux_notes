#!/usr/bin/env python

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
