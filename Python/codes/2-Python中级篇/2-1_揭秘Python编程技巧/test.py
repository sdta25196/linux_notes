#!/usr/bin/env python

import sys

fd = sys.stdin
print fd.next()
print fd.next()

try:
	print fd.next()
except:
	print 'end of line'
