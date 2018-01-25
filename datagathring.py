#!/usr/bin/python
import requests
import subprocess
from subprocess import call
import os


def getData(url):
	response = requests.get("https://www.whois.com/whois/"+url)
	bruteData=response.content
	indicedebut=bruteData.index('<pre class="df-raw" id="registrarData">')
	indicedebut+=39
	indicefin=bruteData.index("For more information on Whois status codes, please visit")
	data= bruteData[indicedebut:indicefin]
	print data
	return data

def saveData(data):
	subprocess.call("sudo touch ~/attack-engine1/outputFiles/dataGathring.txt", shell=True)
	path = os.path.join(os.path.expanduser('~'), 'attack-engine1', 'outputFiles', 'dataGathring.txt')
	f = open(path,"w") #opens file with name of "test.txt"
	f.write(data)
	print "data gathred has been saved succefuly \n"
	return 0

def nslookup(url):

	if 'http://' in url :
		url = url.replace('http://','')
	if 'https://' in url :	
		url = url.replace('https://','')

	subprocess.call("sudo touch ~/attack-engine1/outputFiles/serverGathring.txt", shell=True)
	subprocess.call("sudo chmod 777 ~/attack-engine1/outputFiles/serverGathring.txt", shell=True)
	path = os.path.join(os.path.expanduser('~'), 'attack-engine1', 'outputFiles', 'serverGathring.txt')
	f = open(path,"w") #opens file with name of "test.txt"
	process = subprocess.Popen(["nslookup","-type=mx",url], stdout=subprocess.PIPE)
	Result=''
	output = process.communicate()[0].split('\n')
	for list in output :
		if list.find('127.0')==-1:
			Result+=list+'\n'
	process = subprocess.Popen(["nslookup","-type=any",url], stdout=subprocess.PIPE)
	output = process.communicate()[0].split('\n')
	for list in output :
		if list.find('127.0')==-1:
			Result+=list+'\n'		
	print Result
	f.write(Result)
	f.close
	
	return Result
