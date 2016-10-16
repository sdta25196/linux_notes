#!/usr/bin/env python

def wordCount(s):
	chars = len(s)
	words = len( s.split() )
	lines = s.count('\n')

	print chars, words, lines

if '__main__' == __name__:
	fd = open('/etc/passwd').read()
	wordCount( fd )
