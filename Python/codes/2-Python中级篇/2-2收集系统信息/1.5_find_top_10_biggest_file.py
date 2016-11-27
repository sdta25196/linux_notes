#!/usr/bin/env python
#-*- coding:utf8 -*-

import os, operator, sys

def gen_dic( topdir ):
    dic = {}
    p_d_f = os.walk( topdir )

    for roots, dirs, files in p_d_f:
        for name in files:
            fn = os.path.join(roots, name)
            try:
                file_size = os.path.getsize( fn )
            except OSError:
                print 'OSError [Errno 2] No such file or directory: %s' % fn

            dic[fn] = file_size

    return dic

if '__main__' == __name__:
    file_dic =  gen_dic( sys.argv[1] )

    sorted_list = sorted(file_dic.iteritems(), key=operator.itemgetter(1), reverse=True)
    #print sorted_list
    for k,v in sorted_list[:10]:
        print k,v
