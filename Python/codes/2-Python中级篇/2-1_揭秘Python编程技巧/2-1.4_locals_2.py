#!/usr/bin/env python
# Date: 2016-11-22 16:58
# Author: Chang.Feng
# Result: See below

"""
"""
def fun():
	a = 'abc'
	b = 'def'
	print locals()

fun()
print '* ' * 50
print fun
print '* ' * 50
print locals()
