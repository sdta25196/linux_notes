#!/usr/bin/env python
#-*- coding:utf8 -*-

import sys, time

for i in xrange(10):
    sys.stdout.write("str:%d " % i)
    time.sleep(1)
    #sys.stdout.write('\n')
    sys.stdout.flush()
