#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
也叫列表重写
Purpose: Test the python generate a list from a loop of for
Date: 2016-10-04
Result: The Output is follow:
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[2, 4, 6, 8, 10, 12, 14, 16, 18]
[2, 4, 6, 8]
'''

print [i for i in range(1,10)]
print [i*2 for i in range(1,10)]
print [i**2 for i in range(1,10)]
for i in [i**2 for i in range(1,10)]:
	print i,
print '\n'
print [i for i in range(1,10) if i % 2 == 0]
