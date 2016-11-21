#!/usr/bin/env python
#-*- coding:utf8 -*-

fd = open('/etc/hosts')

while True:
    data = fd.readline()

    if not data:
        break
    else:
        print data,

fd.close()
