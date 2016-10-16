#!/usr/bin/env python 
#-*- coding:utf-8 -*-

class People(object):
	color = 'white'
	__age = 28

	#定义静态方法，静态方法不能有self参数，如果要使用需要用staticmethod()来处理
	def static_func():
		print 'static function test.'

	def static_func_2():
		"""如果要在静态方法内访问类的内部属性，那么就必有使用类名的方式来访问，
		因为静态方法没有self参数，所以没有办法使用self来访问
		"""
		print.color, People.__age

	static_fn = staticmethod( static_func )
	static_fn_2 = staticmethod( static_func_2 )

Angle = People()
#People.static_func() //提示必须要让People类的实例来调用此方法
#Angle.static_func() //提示这个方法没有参数，但是实例上给了一个参数
print '%17s' % 'People Instance :',
#Angle.static_fn()
Angle.static_fn_2()
print '%17s' % 'People class :',
#People.static_fn()
People.static_fn_2()
