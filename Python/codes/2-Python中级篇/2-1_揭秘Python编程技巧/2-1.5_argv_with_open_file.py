#!/usr/bin/env python
#!-*- coding:utf8 -*-
# Date: 2016-11-22 22:30
# Author: FD
# Result: See below
'''
'''

import sys, os

try:
	fn = sys.argv[1]
except IndexError:
	print "We need a argument after program, ;-)"
	sys.exit()

if not os.path.exists( fn ):
	print "file %s is not exists." % fn
	sys.exit()

fd = open( sys.argv[1] )
data = fd.read()
chars = len( data )
words = len( data.split() )
lines = data.count('\n')

print "%(lines)s %(words)s %(chars)s" % locals()
fd.close()
