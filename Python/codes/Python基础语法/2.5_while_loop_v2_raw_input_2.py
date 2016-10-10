#!/usr/bin/env python

input_chracter = ''
while input_chracter != 'q' and input_chracter != 'quit':
	print 'hello'
	input_chracter = raw_input('Please input something, "q" or "quit:" ')
	if input_chracter == '':
		continue
