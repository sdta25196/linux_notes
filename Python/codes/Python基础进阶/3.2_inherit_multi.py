#!/usr/bin/env python
#-*- coding:utf-8 -*-
#时间：2016-10-16 Sun 21:46
#运行结果：
"""
============================================================
************************************************************
This is a public method. ----->People.think()
HongKong AAAAAAAAAAAAAA
"""

class Person(object):
	color = 'grown'

	def __init__(self):
		self.dwell = 'HongKong'
		self.color = 'AAAAAAAAAAAAAA'

	def think(self):
		print 'This is a public method. ----->Person.think()'

class People(object):
	sea = 'Water'

	def __init__(self):
		self.dwell = 'East sea'

	def think(self):
		print 'This is a public method. ----->People.think()'

#class Chinese(Person, People):
class Chinese(People, Person):
	def __init__(self):
		Person.__init__(self)

print '===' * 20
changFeng = Chinese()
print '***' * 20
changFeng.think()
print changFeng.dwell, changFeng.color

