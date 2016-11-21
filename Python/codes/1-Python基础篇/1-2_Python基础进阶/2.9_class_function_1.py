#!/usr/bin/env python
#-*- coding:utf-8 -*-

class People(object):
	color  = 'yellow'
	__age = 28

	#公有方法
	def think(self):
		self.color = 'blank'
		print self.color
		print 'This function name is think.'

	#方法的类的内部调用
	def test(self):
		self.think()
		self.__talk()
	
	#私有方法
	def __talk(self):
		print 'I am talking with Jack.'

	def cm_func(self):
		print "classmethod testing..."
	#把cm_func()方法变为类方法
	cm = classmethod( cm_func )

Angela = People()
#Angela.test()
"""下面的两种方式都不能调用类的私有方法，私有方法只有在类的内部才能被调用"""
#Angela.__talk()
#People.__talk()

#People.cm_func() //这样直接通过类来调用是不可以的，提示需要用实例来调用
print '下面通过类来调用自己的类方法'
People.cm()
Angela.cm()
