#!/usr/bin/env python

x = ''
while 'q' != x and 'quit' != x:
	print 'hello' 
	x = raw_input('Please input some character, "q" or "quit" for exit: ')
	if x:
		continue
else:
	print 'world'
