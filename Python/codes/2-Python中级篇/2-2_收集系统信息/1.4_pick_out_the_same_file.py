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

def gen_dict( topdir ):
    dic = {}
    pdf = os.walk(topdir)
    
    for root, dirs, files in pdf:
        for name in files:
            #print os.path.join( root, name )
            filename = os.path.join(root, name)
            md5_sum = md5sum(filename)

            if dic.has_key( md5_sum ):
                dic[md5_sum].append( filename )
            else:
                dic[md5_sum] = [filename]
    return dic

if '__main__' == __name__:
    #print gen_dict( sys.argv[1] )

    for k, v in gen_dict( sys.argv[1] ).items():
        if len(v) > 1:
            print k, v
