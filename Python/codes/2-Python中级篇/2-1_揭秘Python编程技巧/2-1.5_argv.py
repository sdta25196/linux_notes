#!/usr/bin/env python
#!-*- coding:utf8 -*-
# Date: 2016-11-22 22:30
# Author: FD
# Result: See below
'''
$ python 2-1.5_argv.py 
['2-1.5_argv.py']
$ python 2-1.5_argv.py a 
['2-1.5_argv.py', 'a']
$ python 2-1.5_argv.py a b
['2-1.5_argv.py', 'a', 'b']
$ python 2-1.5_argv.py a b c
['2-1.5_argv.py', 'a', 'b', 'c']
'''

import sys

print sys.argv, sys.argv[1]
