#!/usr/bin/env python
#-*- coding:utf-8 -*-
#目的：测试__str__函数
#运行结果：
"""This is People class return result."""

class People(object):
	color = 'yellow'
	gender = 'F'
	high = 183
	height = '65kg'

	class Chinese(object):
		name = "I am a Chinese"		

	#这个方法并不需要手动调用，如果返回对象为People类的实例，则会自动调用此方法
	def __str__(self):
		return "This is People class return result."

people = People()
print people
