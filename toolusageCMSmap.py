#!/usr/bin/python
import os
from subprocess import *
from Colour import Colour
def CMSmapCall(url):
	try :
		time = str(datetime.now())
		print time + "\n"
	#	print "cmsmap analyse is launched ..."
		os.system('touch ~/attack-engine1/outputFiles/CMSmap_Repports ')
		os.system('python ~/arsenal/cmsmap.py -t ' +url)#+' -f W >~/attack-engine1/outputFiles/CMSmap_Repports ')
		print Colour.RED+"\n[!] ==>this is not a cms website "+Colour.END
	except:
		print ("there is a problem in CMSmap install please contact us")
	
	return 0


