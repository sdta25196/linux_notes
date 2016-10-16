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

"""这是一段中文注释，
主要目的就是来测试类的内置变量的
时间：2016-10-17 11:39 Sun
End...
"""
peo = People()
print '通过实例来调用实例的属性和方法'
print '#' * 40
print peo.color
peo.think()

print '下面是打印实例的内置属性'
print '#' * 40
print peo.__dict__
print peo.__doc__
#print peo.__name__ //这样会报错，提示没有‘__name__’这个属性
#print peo._People__name__ //这样也不是可以的
print '#' * 40
#通过类来调用类的属性
print '通过类来说类的属性'
print People.color
#print People.__age
"""
Traceback (most recent call last):
  File "2.8_class_property_private.py", line 30, in <module>
      print People.__age
	  AttributeError: type object 'People' has no attribute '__age'
"""

#通过实例来修改属性的值
print '通过实例来修改属性的值'
print '#' * 40
peo.color = '黄种人'
print peo.color
print People.color

print 'People类的内置属性'
print '#' * 40
print People.__dict__
print People.__doc__
