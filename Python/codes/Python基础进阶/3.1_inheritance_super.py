#!/usr/bin/env python
#-*- coding:utf-8 -*-
#运行结果如下
"""enter B
This message is generated by Parent Class.
enter A
level A
level B
132 Moon
"""

class A(object):
	color = '132'

	def __init__(self, args):
		print 'This message is generated by Parent Class.'
		print 'enter A'
		print 'level A'
		self.dwell = 'Moon'

class B(A):
	def __init__(self):
		print 'enter B'
		super(B, self).__init__('Earth')
		print 'level B'

b = B()
print b.color, b.dwell
