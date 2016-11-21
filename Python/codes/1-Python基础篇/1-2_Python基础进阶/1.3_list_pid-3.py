#!/usr/bin/env python

import sys
import os

def isNum(s):
	if s.isdigit():
		return True
	else:
		return False

for i in os.listdir('/proc'):
	if isNum(i):
		print i,
