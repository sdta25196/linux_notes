#!/usr/bin/env python

x = 'This variable is a glabal var'

def fun():
	x = 100
	print x
	x += 1
	print x

fun()
print "outside of the function call: %s" % x
