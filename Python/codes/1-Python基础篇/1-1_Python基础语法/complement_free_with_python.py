#!/usr/bin/env python

with open('/proc/meminfo') as fd:
	for line in fd:
		if line.startswith('MemTotal'):
			mem_total = line.split()[1]
			continue
		if line.startswith('MemFree'):
			mem_free = line.split()[1]
			break

	mem_total = float( mem_total )
	mem_free = float( mem_free )
	print "MemTotal: %.2f M\nMemFree: %.2f M" % (mem_total / 1024, mem_free / 1024)
	print "MemFree percent rate is: %.2f%%" % (mem_free / mem_total * 100)

