#!/usr/bin/env python

class People(object):
	color = 'yellow'

	def think(self):
		self.color = 'white'
		print "I am a %s people" % self.color
		print "I am thinking"

people = People()

print people.color
people.think()
