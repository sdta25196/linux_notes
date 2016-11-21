#!/usr/bin/env python
# -*- coding:utf-8 -*-

with open('/proc/meminfo') as fd:
	for line in fd:
		if line.startswith('MemTotal'):
			MemTotal = line.split()[1]
			continue
		if line.startswith('MemFree'):
			MemFree = line.split()[1]
			break
MemTotal = int(MemTotal) / 1024.0
MemFree = int(MemFree) / 1024.0
print "The Total Mem is:\t%.2fM\nUsed Mem is:\t\t%.2fM\nThe Percent rate is:\t%%%.2f" % (MemTotal, MemFree, MemTotal / MemFree)
#print "总共内存: %f" + 'M' % MemTotal
#print "剩余内存: %s" + 'M' % MemFree
#print "内存使用百分比: %s" % (MemTotal / MemFree)
