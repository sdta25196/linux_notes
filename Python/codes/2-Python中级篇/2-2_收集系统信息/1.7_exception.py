#!/usr/bin/env python
#-*- coding:utf8 -*-

"""
# python 1.7_exception.py 
a
The else statement printed.
I am terminator, Did not care any thing."""

class FuncError(Exception):
	def __str__(self):
		return "Custom Exception ... ..."

def fun():
	raise FuncError()
"""在上面的代码会 优先执行，如果抛出异常，那么后面的就不会再判断了"""
try:
	#print tmp 
	print 'a'
	#fun()
except FuncError, e:
	print e
except NameError:
	print "the name is not define"
else:
	print "The else statement printed."
finally:
	print "I am terminator, Did not care any thing."
