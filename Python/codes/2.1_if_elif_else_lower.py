#!/usr/bin/env python

input_str = raw_input("Please input [Yes/No]: ")
input_str = input_str.lower()

if input_str == 'y' or input_str == 'yes':
	print "Programe is running..."
elif input_str == 'n' or input_str == 'no':
	print "Programe is exiting..."
else:
	print "Please input [Yes/No]"
