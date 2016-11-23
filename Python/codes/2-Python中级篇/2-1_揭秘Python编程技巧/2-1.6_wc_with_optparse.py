#!/usr/bin/env python
#-*- coding:utf8 -*-

from optparse import OptionParser
import sys

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

#print options, args #options接收一个字典类型的数据，args则是一个列表
#print options.words #打印出字典中，words对应的值

data = sys.stdin.read()
chars = len(data)
words = len( data.split() )
lines = data.count('\n')

if not (options.characters or options.words or options.lines):
	options.lines, options.words, options.characters = True, True, True
if options.lines:
	print lines,
if options.words:
	print words,
if options.characters:
	print chars,
