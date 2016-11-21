#!/usr/bin/env python

#mac_addr = '00:0C:29:EC:A3:5B'
mac_addr = '00:0C:29:EC:A3:5B'
prefix_mac = mac_addr[:-3]
last_two = mac_addr[-2:]
plus_one = int(last_two, 16) + 1
new_last_two = hex( plus_one )

#If have str '0x' or '0X', then split them
if new_last_two.startswith('0x'): 
	new_last_two = new_last_two[2:].upper()
	#print new_last_two, type( new_last_two ), int( new_last_two[-1], 16 )
	if int(new_last_two[-1], 16) < 16 and len( new_last_two ) < 2:
		new_last_two = '0' + new_last_two

new_mac = prefix_mac + ':' + new_last_two

print 'Current MAC address is: %s' % mac_addr
print 'The new MAC address is: %s' % new_mac
