#!/usr/bin/env python 
#-*- coding:utf-8 -*-

class Parent(object):
	def fun(self):
		print "I'm parent class."

class MyClass(Parent):
	def func(self):
		print "I'm inherited parent class."

test = MyClass()
test.fun()
test.func()
