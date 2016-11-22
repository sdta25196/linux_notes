# !/usr/bin/env python
# -*- coding:utf8 -*-
# Author: zhang.wen
# Date: 2016-11-22 22:47
# Result: See below

import sys, os

if len( sys.argv ) == 1:
	data = sys.stdin.read()
else:
	data = open( sys.argv[1] ).read()

lines = data.count('\n')
words = len( data.split() )
chars = len( data )

print "%(lines)s %(words)s %(chars)s" % locals()
