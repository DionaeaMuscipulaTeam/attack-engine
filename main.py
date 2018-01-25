#!/usr/bin/python

try :
	import os
	import draw
	import setup
except :
	print "there is some erreur in install"


try :
	# import controller
	os.system("touch rapport.txt") 
	os.system("python controller.py | tee rapport.txt ")
except :
	print "there is a problem in controller "
