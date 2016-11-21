#!/usr/bin/env python

def isNum():
	sth = raw_input("Please input a number: ")
	try:
		if type(1) == type( int(sth) ):
			print "%s is a number, congratulations :)" % sth
	except:
		print "%s is not a number:(" % sth

isNum()
