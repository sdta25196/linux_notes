#!/usr/bin/python
#coding:utf-8

import os

x='/proc/'

def fun(x):
	if x.isdigit():
		return True
	return False

def meminfo(y):
	pwd= x+y+'/status'#获取进程文件的路径
	with open(pwd) as damem:
		for p_da in damem:#对每个进程内存累加并得出总内存和占比
			if p_da.startswith('VmRSS'):
				p_mem = p_da.split()[1]
				p_mem = float(p_mem)
				return p_mem

for i in os.listdir(x):
	if fun(i):
		if meminfo(i) > 0:
			print '进程号：%s 占用内存：%s k'%(i, meminfo(i))
