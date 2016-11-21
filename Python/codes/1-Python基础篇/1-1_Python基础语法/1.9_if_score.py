#!/usr/bin/env python

score = int( raw_input('Please input your score[integer]: ') )

if score >= 90:
	print 'A\nVery good!'
elif 80 <= score < 90:
	print 'B\nGood.'
elif 60 <= score < 80:
	print 'C\nPass.'
else:
	print 'D'
