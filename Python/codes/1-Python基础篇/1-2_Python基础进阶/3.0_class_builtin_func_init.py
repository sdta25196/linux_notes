#!/usr/bin/env python
#-*- coding:utf-8 -*-
#时间：2016-10-16 Sun 24:47
#目的：测试构造函数__init__
#运行结果：
"""
I'm thinking....
This is People class return result.
White
yellow
**************************************************
instance no args: White
I'm thinking....
instance with args: Green
instance with args: I'm thinking....
Wonderful
"""

class People(object):
	color = 'yellow'
	gender = 'F'
	high = 183
	height = '65kg'

	class Chinese(object):
		name = "I am a Chinese"		

	def think(self):
		print "I'm thinking...."

	#这个方法并不需要手动调用，如果返回对象为People类的实例，则会自动调用此方法
	def __str__(self):
		return "This is People class return result."

	#def __init__(self):
	#	self.color = 'Xxxxxx'
	def __init__(self, colour='White'):
		self.color = colour
		#构造函数中也可以调用类的方法
		self.think()

people = People()
print people
print people.color #通过对象会调用__init__方法
print People.color #通过类来调用属性则不会调用__init__方法
print '*' * 50
print "instance no args:", people.color
jack = People('Green')
print "instance with args:", jack.color
print "instance with args:", People("Wonderful").color
