#!/usr/bin/env /python
# -*- coding:utf-8 -*-

info = {}
name = raw_input("Please input name: ")
age = raw_input("Please input age: ")
gender = raw_input("Please input genter(M/F): ")
#print type(name)

info['name'] = name
info['age'] = age
info['gender'] = gender
items = info.items()

print "Input information is %s, Generation objectis %s, and objectname is %s" % (info, items, type( items ))
print '\n'

'''第一种方法打印，这时取出来的对象是一个元组，输出内容如下
Please input name: zw
Please input age: 29
Please input genter(M/F): F
Input information is {'gender': 'F', 'age': '29', 'name': 'zw'}, Generation objectis [('gender', 'F'), ('age', '29'), ('name', 'zw')], and objectname is <type 'list'>

('gender', 'F')
('age', '29')
('name', 'zw')

'''
for i in info.items():
	print i	

print '\n----------- 我是一条华丽的分隔线 ----------\n'
'''第二种方法就是使用两个变量来接收字典里面的内容
如下
Please input name: Rose
Please input age: 21
Please input genter(M/F): F
Input information is {'gender': 'F', 'age': '21', 'name': 'Rose'}, Generation objectis [('gender', 'F'), ('age', '21'), ('name', 'Rose')], and objectname is <type 'list'>


('gender', 'F')
('age', '21')
('name', 'Rose')
gender: F
age: 21
name: Rose
The end...
'''
for k, v in info.items():
	print "%s: %s" % (k, v)
print "The end..."
