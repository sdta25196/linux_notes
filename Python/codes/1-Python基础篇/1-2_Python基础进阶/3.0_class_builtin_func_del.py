#!/usr/bin/env python
#-*- coding:utf-8 -*-
#时间：2016-10-16 Sun 14:59
#目的：测试析构函数
#运行结果：
"""
Initializating....
This is People class return result.
F
Last line...................................
Releasing...
"""

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

	def __init__(self, colour='CCCCccc'):
		print '... Initializating ....'
		self.fd = open('/etc/hosts')

	def __del__(self):
		print '... Releasing ...' #本行会在脚本的最后执行 
		self.fd.close()

people = People()
print people
print people.gender
print 'Last line...................................'
