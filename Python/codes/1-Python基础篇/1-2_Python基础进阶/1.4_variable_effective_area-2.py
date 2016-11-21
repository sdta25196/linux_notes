#!/usr/bin/env python

x = 200

def fun():
	global x
	x += 1
	print x
	global y
	y = 100

#fun()
print "outside of the function call: %s" % x
print y
