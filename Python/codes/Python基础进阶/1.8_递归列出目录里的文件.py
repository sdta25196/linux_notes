#!/usr/bin/env python

import os
import sys

def print_files(path):
	lsdir = os.listdir( path )
	files = [ i for i in lsdir if os.path.isfile( os.path.join(path, i) ) ]
	dirs = [ i for i in lsdir if os.path.isdir( os.path.join(path,i) ) ]

	if files:
		for f in files:
			print os.path.join(path, f)
	
	if dirs:
		for d in dirs:
			print_files( os.path.join(path, d) )

print_files( sys.argv[1] )
