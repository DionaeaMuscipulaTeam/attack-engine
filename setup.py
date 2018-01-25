#!/usr/bin/python
from subprocess import call
from subprocess import Popen
import subprocess
try : 
	import os
except :
	print ("if something went wrong that mean you are missing (os) package \n please install that requirement in order to use the app")

#check kernel type
try :
	output = subprocess.check_output("uname -a", shell=True)
	if output.find('Ubuntu') != -1 :
		try:
			pipens = Popen("/usr/lib/update-notifier/apt-check", shell=True, stdout=subprocess.PIPE).stdout
			updateResult = pipens.read()
			if updateResult.find('0;0')!=-1 :
				os.system('sudo apt-get update')
				print 'updating system ...'
		except :	
			print 'Updating system problem ...'

		try :
			os.system ('sudo -H pip2 install --upgrade pip')
		except :
			print 'installing pip'
	
			try:
				os.system('sudo apt-get -y install python-pip')
			except :
				print 'there is a problem in installing pip'
	
	elif output.find('fedora') != -1:
		print 'you are using fedora ..'
		pipens = Popen("echo ~/attack-engine1", shell=True, stdout=subprocess.PIPE).stdout
		Path = pipens.read()
		Path = Path.rstrip()
		if os.path.exists(Path) == False :
			try :
				os.system('sudo dnf upgrade --refresh')
			except :
				print 'there is a problem in the update of your fedora system '
			try :	
				os.system('dnf clean all')
				os.system('dnf -y update')
				os.system('dnf -y install python-pip')
			except :
				print 'there is a problem in the install of the pip ...'

except :
	print "there is a problem in the check of the system kernel "

	


try :
	import platform
except :
	print("installing platform package ... ")
	os.system('sudo pip install platform')
try :
	import subprocess
except :
	print("installing subprocess package ... ")
	os.system('sudo pip install subprocess')
try:
	import lxml
except :
	print("installing lxml package ... ")
	os.system('sudo pip install lxml')
try:
	import bs4
except :
	print("installing bs4 package ... ")
	os.system('sudo pip install bs4')
try:
	import requests
except :
	print("installing requests package ... ")
	os.system('sudo pip install requests')
try:
	import mechanize
except :
	print("installing mechanize package ... ")
	os.system('sudo pip install mechanize')
try:
	import urllib
except :
	print("installing urllib package ... ")
	os.system('sudo pip install urllib')
try:
	import itertools
except :
	print("installing itertools package ... ")
	os.system('sudo pip install itertools')
try:
	import BeautifulSoup
except :
	print("installing BeautifulSoup package ... ")
	os.system('sudo pip install BeautifulSoup')





pipens = Popen("echo ~/attack-engine1", shell=True, stdout=subprocess.PIPE).stdout
Path = pipens.read()
Path = Path.rstrip()

pipens = Popen("echo ~/attack-engine1/inputFiles", shell=True, stdout=subprocess.PIPE).stdout
PathInputFile = pipens.read()
PathInputFile = PathInputFile.rstrip()

pipens = Popen("echo ~/attack-engine1/outputFiles", shell=True, stdout=subprocess.PIPE).stdout
PathOutputFile = pipens.read()
PathOutputFile = PathOutputFile.rstrip()



if (os.path.exists(Path)==True):
		
	if (os.path.exists(PathInputFile)==False):
		os.system(' mkdir ~/attack-engine1/inputFiles')

	if (os.path.exists(PathOutputFile)==False):
		os.system(' mkdir ~/attack-engine1/outputFiles')

elif (os.path.exists(Path)==False) :
	print "creating directory ..."
	os.system('mkdir ~/attack-engine1')
	os.system(' mkdir ~/attack-engine1/inputFiles')
	os.system(' mkdir ~/attack-engine1/outputFiles')



Path="~/attack-engine1/inputFiles/bypassLib.txt"
if (os.path.exists(Path)==False):
	os.system("cp bypassLib.txt ~/attack-engine1/inputFiles")

Path="~/attack-engine1/inputFiles/sqlword.txt"
if (os.path.exists(Path)== False ):
	os.system("cp sqlword.txt ~/attack-engine1/inputFiles")


Path="~/attack-engine1/inputFiles/ResourcesLib.txt"
if (os.path.exists(Path)== False ):
	os.system("cp ResourcesLib.txt ~/attack-engine1/inputFiles")


Path="~/attack-engine1/inputFiles/xssword.txt"
if (os.path.exists(Path)== False ):
	os.system("cp xssword.txt ~/attack-engine1/inputFiles")


try: 
	pipegit = Popen("which git", shell=True, stdout=subprocess.PIPE).stdout
	git = pipegit.read()
except: 
	git =""
	print "something went wrong with git "





try: 
	pipens = Popen("which nslookup", shell=True, stdout=subprocess.PIPE).stdout
	ns = pipens.read()
except: 
	pipens =""	
	print "something went wrong with nslookup"


if git=="":
	#install git
	print "installing sqlmap ..."
        os.system("sudo apt-get install git")

if os.path.exists('~/Desktop/FinalApp/sqlmap')== 'False':
	#install sql
	print "installing sqlmap ..."
        os.system("sudo wget 'https://github.com/sqlmapproject/sqlmap/tarball/master' --output-document=sqlmap.tar.gz")
	os.system("tar -xvf sqlmap.tar.gz")
	print "SQLMAP is installed ..."
	print "cleaning env ..."
	os.system ("sudo rm -rf sqlmap.tar.gz")
	os.system ("sudo mv sqlmapproject* sqlmap")


pipens = Popen("echo ~/arsenal", shell=True, stdout=subprocess.PIPE).stdout
Path = pipens.read()
Path = Path.rstrip()
if os.path.exists(Path)== False:
	#install cms
	print "installing CMSmap ..."
	if (os.path.exists('~/arsenal')==False) :
		os.system("mkdir ~/arsenal")
	os.system("git clone https://github.com/Dionach/CMSmap.git ~/arsenal")
	#os.system("cd CMSmap")
#	os.system("python cmsmap.py -t http://www.google.com")

if ns=="" :
	#install ns
	print"installing nslookap ..."
	os.system("apt-get install dnsutils")



os.system('sudo chmod -R +x ./*')


