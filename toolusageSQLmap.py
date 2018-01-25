#!/usr/bin/python
import os
from subprocess import Popen

def SqlmapCall(url):
	try :
		# print "sqlmap analyse is launched ..."
		os.system('touch ~/attack-engine1/outputFiles/Sqlmap_Repports ')
		os.system('sqlmap -u' +url)
	except:
		print ("there is a problem in sqlmap install please contact us")
	return 0


