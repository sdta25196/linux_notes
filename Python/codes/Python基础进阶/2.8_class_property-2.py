#!/usr/bin/env python
# -*- coding:utf-8 -*-

class People(object):
	color = 'black'
	__age = 30

	def think(self):
		self.color = 'brown'
		self.__age = 100
		print "My favorite color is %s," % self.color,

peo = People()
#print peo.color
#peo.think()
print peo._People__age
