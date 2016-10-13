#!/usr/bin/env python

def add(x, y):
	return x + y

print reduce(add, range(1,11))

print reduce(lambda x, y: x + y, range(1,101))
