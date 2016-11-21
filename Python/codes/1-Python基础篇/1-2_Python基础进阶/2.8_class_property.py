#!/usr/bin/env python
# -*- coding:utf-8 -*-

class People(object):
	color = 'black'
	__age = 30

	def think(self):
		self.color = 'brown'
		self.__age = 100
		print "My favorite color is %s," % self.color,
		print "and My age is %s." % self.__age
		#print __age //这样的写法是错误的，如果要在类的内部访问一个属性则必须前面加一个self，如上面的写法

peo = People()
print peo.color
peo.think()
