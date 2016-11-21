#!/usr/bin/env python

macaddr = '1A:0C:49:3E:A5:FF'
last_two = macaddr[-2:]
prefix_mac = macaddr[:-3]
plus_one = int(last_two, 16) + 1

if plus_one in range(10):
	new_last_two = hex(plus_one)[2:]
	new_last_two = '0' + new_last_two
else:
	new_last_two = hex(plus_one)[2:]
	if len(new_last_two) == 1:
		new_last_two = '0' + new_last_two
	
new_mac = prefix_mac + ':' + new_last_two

print new_mac.upper()
