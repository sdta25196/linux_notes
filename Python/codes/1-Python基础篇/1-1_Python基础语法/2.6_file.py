#!/usr/bin/env python

fd = open('/tmp/tmp.txt')

for line in fd.readlines():
	print line,
