#!/usr/bin/python
from datetime import datetime
from bs4 import BeautifulSoup
from subprocess import call
from Colour import Colour
import subprocess
import requests
import os


def LoginSearch(url):
	time = str(datetime.now())
	print time + "\n"
	panel=''
	with open("bypassLib.txt","r") as f:
		res =url + '\n'
		flist = f.read().splitlines() 
   		for line in flist:
			link=str(url)+str(line)+"/"
			print Colour.BLUE+"testing : "+Colour.END+link
			r = requests.head(link)
			code = r.status_code
			if (os.path.exists('~/attack-engine1/outputFiles/bypassRepport.txt') == False ):
				os.system('touch ~/attack-engine1/outputFiles/bypassRepport.txt')
			path = os.path.join(os.path.expanduser('~'), 'attack-engine1', 'outputFiles', 'bypassRepport.txt')
			panel=''

			if code == 404 : 
				print  Colour.RED+str(code)+" not found !"+Colour.END
			if code != 404 :
				print  Colour.GREEN+str(code)+" found !"+Colour.END
				res=line
				panel=line		
	with open(path, "w") as text_file:
		text_file.write("%s" % time)
		text_file.write("\n")
		text_file.write("%s" % res)
		time = str(datetime.now())
		text_file.write("\n")
		text_file.write("%s" % time)
		print "\n"+time


	
	return panel

def ResourceSearch(url):
	time = str(datetime.now())
	print time+"\n"
	panel=''
	with open("ResourcesLib.txt","r") as f:
		res =url + '\n'
		flist = f.read().splitlines() 
   		for line in flist:
			link=str(url)+str(line)+"/"
			print Colour.BLUE+"testing : "+Colour.END+link
			r = requests.head(link)
			code = r.status_code
			if (os.path.exists('~/attack-engine1/outputFiles/ResourceSearchRepport.txt') == False ):
				os.system('touch ~/attack-engine1/outputFiles/ResourceSearchRepport.txt')
			path = os.path.join(os.path.expanduser('~'), 'attack-engine1', 'outputFiles', 'ResourceSearchRepport.txt')
			panel=''

			if code == 404 : 
				print  Colour.RED+str(code)+" not found !"+Colour.END
			if code != 404 :
				print  Colour.GREEN+str(code)+" found !"+Colour.END 
				res+=line

	with open(path, "w") as text_file:
		text_file.write("%s" % time)
		text_file.write("\n")
		text_file.write("%s" % res)
		time = str(datetime.now())
		text_file.write("\n")
		text_file.write("%s" % time)
		print "\n"+time


	return 0


def getRobotsContents(url):
	time = str(datetime.now())
	print time + "\n"
	r  = requests.get(url+"/robots.txt")
	print r
	data = r.text
	soup = BeautifulSoup(data,"lxml")
	request=str(soup)
	print request
	if (os.path.exists("~/attack-engine1/outputFiles/RobotsOutput.txt")=='False') :
		subprocess.call("touch ~/attack-engine1/outputFiles/RobotsOutput.txt", shell=True)
	path = os.path.join(os.path.expanduser('~'), 'attack-engine1', 'outputFiles', 'RobotsOutput.txt')
	with open(path, "w") as text_file:
		text_file.write("%s" % time)
		text_file.write("\n")
		text_file.write("%s" % request)
		time = str(datetime.now())
		text_file.write("\n")
		text_file.write("%s" % time)
		print "\n"+time
	return 0
