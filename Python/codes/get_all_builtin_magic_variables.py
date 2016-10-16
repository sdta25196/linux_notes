#!/usr/bin/env python

import gc

#all_objects = gc.get_objects()
#print "\n".join(sorted([attrname for attrname in dir(all_objects) if attrname.startswith("__")]))


print("\n".join(sorted([attrname for item in gc.get_objects() for attrname in dir(item) if attrname.startswith("__")])))


