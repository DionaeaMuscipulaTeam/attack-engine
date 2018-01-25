#!/usr/bin/python
# -*- coding: utf-8 -*-

from Colour import Colour
with open("name.txt","r") as f:
	print Colour.CYAN
	for line in f:
		line = line.rstrip()
		print line
	print Colour.END
a = '\n                                  '+Colour.RED+'      攻击引擎 \n \n '+Colour.END
print a.decode('utf-8')
