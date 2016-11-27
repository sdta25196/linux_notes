#!/usr/bin/env python
#-*- coding:utf8 -*-

import os
import sys
import hashlib

def md5sum(file):
    md5 = hashlib.md5()
    fd = open(file)
    while True:
        data = fd.read( 1024 * 4 )
        if data:
            md5.update(data)
        else:
            break
    fd.close()

    return md5.hexdigest()

def file_md5( topdir ):
    pdf = os.walk(topdir)
    
    for root, dirs, files in pdf:
        for name in files:
            #print os.path.join( root, name )
            filename = os.path.join(root, name)
            md5_sum = md5sum(filename)
            yield "%s  %s" % (md5_sum, filename)

if '__main__' == __name__:
    try:
        topdir = sys.argv[1]
    except IndexError:
        print "%s must be append 1 args" % sys.argv[0]
        sys.exit()
    gen = file_md5( topdir )

    for i in gen:
        print i
