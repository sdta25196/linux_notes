#!/usr/bin/env python

input_str = raw_input("Please input [Yes/No]: ")
input_str = input_str.lower()
yes = ('yes', 'y')
no = ('no', 'n')

if input_str in yes:
	print "Programe is running..."
elif input_str in no:
	print "Programe is exiting..."
else:
	print "Please input [Yes/No]"
