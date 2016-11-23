#!/usr/bin/env python

import sys

def counts(s):
	n = 0
	for i in s.readlines():
		n += 1
		print i,  n,
	return n

fd = sys.stdin
print fd
print counts( fd )
