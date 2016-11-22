#!/usr/bin/env python
#-*- coding:utf8 -*-
# Author: FD
# Date: 2016-11-22 17:02
# Result: See below
'''
python 2.1.4_simple_wc.py
eof
1 1 4
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '2.1.4_simple_wc.py', 'stdin': <open file '<stdin>', mode 'r' at 0x7f11a2e410c0>, 'lines': 1, '__package__': None, 'chars': 4, 'words': 1, '__name__': '__main__', 'data': 'eof\n', '__doc__': None}
'''

from sys import stdin

data = stdin.read()
chars = len( data )
words = len( data.split() )
lines = data.count('\n')

#print lines, words, chars
#print "%(lines)s %(words)s %(chars)s" % locals()
print "%(lines)s %(words)s %(chars)s" % {'lines':lines,  'words':words, 'chars':chars}
print locals()
