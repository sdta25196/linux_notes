#!/usr/bin/env python
#-*- coding:utf8 -*-

import hashlib
import sys

def md5sum( f ):
    md5 = hashlib.md5()
    fd = open(f)

    while True:
        data = fd.read( 1024 * 4)
        if data:
            md5.update( data )
        else:
            break

    fd.close()

    return md5.hexdigest()

if __name__ == "__main__":
    try:
        print md5sum( sys.argv[1] )
    except IndexError:
        # __file__　equivement sys.argv[0]，即打印出程序的名字
        print "%s must be append a argument." % __file__
