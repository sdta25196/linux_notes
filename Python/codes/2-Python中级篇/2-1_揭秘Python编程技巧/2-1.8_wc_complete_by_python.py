#!/usr/bin/env python
#-*- coding:utf8 -*-

import sys
import os
from optparse import OptionParser

def opt_fun():
    parser = OptionParser()
    """这里还是不可以出现中文，不然会有如下提示
                        Traceback (most recent call last):
                        ... ...
                        UnicodeDecodeError: 'ascii' codec can't decode byte 0xe7 in position 113: ordinal not in range(128)
    """
    parser.add_option("-c", "--char",
                        dest = "characters",
                        action = "store_true",
                        default = False,
                        #help = "统计字符个数"
                        help = "Count the characters number."
            )

    parser.add_option("-w", "--word",
                        dest = "words",
                        action = "store_true",
                        default = False,
                        #help = "统计字母个数"
                        help = "Counter the number of words"
            )

    parser.add_option("-l", "--line",
                        dest = "lines",
                        action = "store_true",
                        default = False,
                        #help = "统计行数"
                        help = "Counter the lines."
            )

    options, args = parser.parse_args()

    return options, args

def get_count( data ):
    chars = len( data )
    words = len( data.split() )
    lines = data.count('\n')

    return chars, words, lines

def show(options, chars, words, lines, filename):
    if options.lines:
        print lines,
    if options.words:
        print words,
    if options.characters:
        print chars,
    print filename

def main():
    options, args = opt_fun()
    if not ( options.characters or options.words or options.lines ):
        options.characters, options.words, options.lines = True, True, True

    if args:
        file_len = len( args )
        total_lines, total_words, total_chars = 0, 0, 0
        for fn in args:
            if os.path.isfile( fn ):
                with open( fn ) as fd:
                    data = fd.read()
                chars, words, lines = get_count( data )
                show(options, chars, words, lines, fn)
                if file_len > 1:
                    total_lines += lines
                    total_words += words
                    total_chars += chars
            elif os.path.isdir( fn ):
                print >> sys.stdout,  "IOError: [Errno 21] Is a directory: \'%s\'" % fn
            else:
                #print >> sys.stderr, "%s: [Errno 21] Is not a file or directory: \'%s\'" % (sys.argv[0], fn)
                sys.stderr.write("%s: [Errno 21] Is not a file or directory: \'%s\'\n" % (sys.argv[0], fn))
        if file_len > 1:
            show(options, total_chars, total_words, total_lines, "total")
    else:
        data = sys.stdin.read()
        fn = ''
        chars, words, lines = get_count( data )
        show(options, chars, words, lines, fn)

if '__main__' == __name__:
    main()
