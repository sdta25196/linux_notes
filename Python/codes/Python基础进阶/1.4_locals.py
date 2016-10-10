#!/usr/bin/env python

def fun():
	x = 1
	y = 2
	print locals():

fun()
print 'OUT OF THE FUNCTION CALL THE FUNCTION NAMED locals():',
print locals()
