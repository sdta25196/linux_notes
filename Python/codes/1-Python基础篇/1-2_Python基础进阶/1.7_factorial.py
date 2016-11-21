#!/usr/bin/env python

def factorial(n):
	sum = 1
	for i in range(1, n+1):
		sum *= i

	return sum

print factorial(5)
