#!/usr/bin/env python

import sys

def factorial(n):
	sum = 1
	for i in range(1, n+1):
		sum *= i

	return sum

print factorial( int(sys.argv[1]) )
