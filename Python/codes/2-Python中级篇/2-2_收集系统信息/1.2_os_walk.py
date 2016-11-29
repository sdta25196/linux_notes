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

pdf = os.walk( sys.argv[1] )

for root, dirs, files in pdf:
    for name in files:
        #print os.path.join( root, name )
        filename = os.path.join(root, name)
        print md5sum(filename) + '  ' +  filename
    """
    for name in dirs:
        print os.path.join( root, name )
    """

