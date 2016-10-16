#!/usr/bin/env python 
#-*- coding:utf-8 -*-

class People(object):
	color = 'white'
	__age = 28

	@staticmethod
	def static_func():
		print 'This is a staic method.'

	@classmethod
	def static_func_2(self):
		print 'This is a class method.'


Angle = People()
Angle.static_func()
Angle.static_func_2()
People.static_func()
People.static_func_2()
