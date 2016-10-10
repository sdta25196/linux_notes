#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""这里就来测试下中文，第一将领使用这咱方法的注释，之前一直是在用#encoding:utf-8的"""
'''Okay, 测试没有问题，以后就这样写吧，好像官网也是推荐这么写的'''

dic = dict(a = 1, b = 2, c = 3)

print "The generate dict is: %s" % (dic)

for k in dic:
	print "The key is %s, and the value is %s" % (k, dic[k])
