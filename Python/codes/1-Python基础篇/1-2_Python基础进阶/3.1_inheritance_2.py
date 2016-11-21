#!/usr/bin/env python
#-*- coding:utf-8 -*-
# 运行结果如下
# Init...

#以下这３种定义类的方法都没有问题
#class People(object):
#class People():
class People:
	color = 'yellow'

	def think(self):
		print 'I am a function, named think'

	def __init__(self, c):
		print 'Init...'
		self.dwell = 'Earth'

class Chinese(People):
	def __init__(self):
		People.__init__(self, 'red') #这里的__init__方法是父的的方法

Jie_Lee = Chinese()
#print Jie_Lee.color, Jie_Lee.think(), Jie_Lee.dwell
