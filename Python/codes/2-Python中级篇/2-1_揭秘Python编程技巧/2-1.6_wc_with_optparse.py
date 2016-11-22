#!/usr/bin/env python
#-*- coding:utf8 -*-

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-c", "--char",
					dest="characters",
					action="store_true",
					default=False,
					help="only count the characters")

parser.add_option("-w", "--word",
					dest="words",
					action="store_true",
					default=False,
					help="only count the words")

parser.add_option("-l", "--line",
					dest="lines",
					action="store_true",
					default=False,
					help="only count the lines")

options, args = parser.parse_args()

print options, args
