#!/usr/bin/env python
#-*- coding:utf8 -*-

import sys, time

for i in xrange(10):
    sys.stdout.write("str:%d " % i)
    time.sleep(1)
    #sys.stdout.write('\n') """这是因为sys.stdout.write('\n')就相当于调用了print，所以就不会缓存了"""
    sys.stdout.flush()
