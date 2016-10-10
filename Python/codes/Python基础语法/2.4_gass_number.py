#!/usr/bin/env python

import random
import sys

i = random.randint(1,20)

print "NOTICE: You must input number range is 1~20..."
for i in xrange(1,7):
	print "Please input a number, you is %s times to input;" % i
	j = int(raw_input())
	if j <= 0 or j > 20:
		print "Please input a number range 1~20, Please try again"
	elif i > j:
		print "You number is lesser than the sys generate number."
	elif i < j:
		print "You number is larger than the sys generate number."
	else:
		print "\t\tYou win, Congratulations"
		sys.exit()
else:
	print "\t\t:(, sorry, try to play the game again.."
