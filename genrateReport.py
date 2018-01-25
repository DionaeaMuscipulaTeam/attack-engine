#!/usr/bin/python
import os
from Colour import Colour

def genrateReport():
	if (os.path.exists('~/attack-engine1/outputFiles/FinalRapport.txt') == False):
		os.system ('touch ~/attack-engine1/outputFiles/FinalRapport.txt')
	path = os.path.join(os.path.expanduser('~'), 'attack-engine1', 'outputFiles/')	
	print path
        file_names = os.listdir(path)
   	output = ''
    	for fi in file_names:
        	with open(path+fi) as f:
			content = f.read().strip('\n')
       			output += content + '\n'  #  This will use a placeholder of 0 for all labels.
	with open(path+'FinalRapport.txt', 'w') as f:
		f.write(output)
	choice=raw_input(Colour.RED+"if you want to read the final report"+Colour.CYAN+" [Y/n] ?"+Colour.END)
	if choice=="Y" or choice =="y" or choice=="yes" :
		os.system('sudo gedit ~/attack-engine1/outputFiles/FinalRapport.txt')
	else :
		print 'thank you for using our app '
	return 0

