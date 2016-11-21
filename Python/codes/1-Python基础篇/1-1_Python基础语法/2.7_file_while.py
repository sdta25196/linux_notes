#!/usr/bin/env python

fd = open('/tmp/tmp.txt')

while True:
	per_line =  fd.readline()
	if not per_line:
		break
	print per_line,

fd.close()
