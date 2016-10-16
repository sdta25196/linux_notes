#!/usr/bin/env python
#-*- coding:utf-8 -*-
#时间：2016-10-16 Sun 15:18
#目的：
#运行结果：

class People(object):
	color = 'yellow'
	gender = 'F'
	high = 183
	height = '65kg'

	class Chinese(object):
		name = "I am a chinese"	

	def __takl(object):
		print 'I\'m talking with Tom'

	@classmethod
	def cm(self):
		print "this is class method"

	@staticmethod
	def stm():
		print "This is static method"

people = People()
print '测试内部类访问的几种方式：'
print '**' * 20
print "内部类实例化，外部类没有实例化：\t", people.Chinese.name
print "内部、外部类都进行了实例化：\t\t", people.Chinese().name
print "内部、外部类都没有实例化：\t\t", People.Chinese.name
print "外部类没有被实例化，内部类行了实例化：\t", People.Chinese().name
print "外部类实例化，内部类没有：\t\t", People().Chinese.name
print "内外都进行了实例化：\t\t\t", People().Chinese().name
print '**' * 20
