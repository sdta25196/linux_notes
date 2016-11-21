#!/usr/bin/env python

def fun():
	inputChr = raw_input("Please input some characters: ")
	try:
		if type( int(inputChr) ) == type( int(1) ):
			print "%s is a number" % inputChr
	except ValueError:
		print "%s is NOT number" % inputChr

fun()
