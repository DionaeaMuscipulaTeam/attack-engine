#!/usr/bin/python


#checking env
from datetime import datetime
try :
	import os
except :
	print "error importing os"
try :
	from Colour import Colour
except :
	print "error importing colour"
try :
	from check import checkLink
except :
	print "error importing checkLink"
try :
	from sqlinj import SqlInject
except :
	print "error importing sqlInject"
try :
	from xssinj import XSSInject
except :
	print "error importing xssInject"
try :
	from brutehtml import BrutforceHtml
except :
	print "error importing BruteforceHtml"
try :
	from check import checkAvailable
except :
	print "error importing checkAvailable"
try :
	from datagathring import getData
except :
	print "error importing getData"
try :
	from datagathring import saveData
except :
	print "error importing saveData"
try :
	from datagathring import nslookup
except :
	print "error importing nslookup"
try :
	from bypassurl import LoginSearch

except :
	print "error importing loginSearch"

try :
	from bypassurl import ResourceSearch
except :
	print "error importing resourceSearch"
try :
	from bypassurl import getRobotsContents
except :
	print "error importing getRobotsContent"
try :
	from verbTempring import getMethodHttpAttributs
except :
	print "error importing getMethodHttpAttributs"
try :
	from toolusageSQLmap import SqlmapCall
except :
	print "error importing SqlMapCall"
try :
	from toolusageCMSmap import CMSmapCall
except :
	print "error importing CMSmapCall"
try :
	from genrateReport import genrateReport
except :
	print "error importing generateReport"

#----------------------------------------* 1 insertion du lien *------------------------------------------------------------
try:
	url = raw_input("please provide the url of the website to attack  ? \n")
	url = checkLink(url)
	try :
		while checkAvailable(url) == False :
			url = raw_input("please provide a valid url  ? \n")
			url = checkLink(url)
	except :
		print 'there is a problem in checking  url ...'

except :
	print 'there is a problem in the reading input module ...'
path = os.path.join(os.path.expanduser('~'), 'attack-engine1', 'outputFiles/')		
if (os.path.exists('~/attack-engine1/outputFiles/url.txt') == False):
	os.system ('touch ~/attack-engine1/outputFiles/url.txt')
	with open(path+'url.txt', 'w') as f:
		f.write(url)
# ---------------------------------------* 2 collect des informations nessesaires *-----------------------------------------

print Colour.CYAN+"+------------------------------------------------------+"
print Colour.CYAN+"|"+Colour.RED+" ~~~~~~~~~~~~~~~~~~~~ data gatharing  ~~~~~~~~~~~~~~~ "+Colour.CYAN+"|"
print Colour.CYAN+"+------------------------------------------------------+"+Colour.END+"\n"
try :
	data = getData(url)
except :
	print 'data gathring using whois is down ..'

try :
	print saveData(data)
except :
	print 'the saving of the data gathring result ...'
print Colour.CYAN+"+------------------------------------------------------+"
print Colour.CYAN+"|"+Colour.RED+" ~~~~~~~~~~~~~~~~~~ nslookup result  ~~~~~~~~~~~~~~~~ "+Colour.CYAN+"|"
print Colour.CYAN+"+------------------------------------------------------+"+Colour.END+"\n"
try :
	nslookup = nslookup(url)
except :
	print 'nslookup problem ..'
print Colour.CYAN+"+------------------------------------------------------+"
print Colour.CYAN+"|"+Colour.RED+" ~~~~~~~~~~~~~~~~~~~~ robots txt   ~~~~~~~~~~~~~~~~~~ "+Colour.CYAN+"|"
print Colour.CYAN+"+------------------------------------------------------+"+Colour.END+"\n"
try:
	robots = getRobotsContents(url)
except :
	print 'there is a problem the get contents of the robots file ...'
print Colour.CYAN+"+------------------------------------------------------+"
print Colour.CYAN+"|"+Colour.RED+" ~~~~~~~~~~~~~~~ search admin panel  ~~~~~~~~~~~~~~~~ "+Colour.CYAN+"|"
print Colour.CYAN+"+------------------------------------------------------+"+Colour.END+"\n"
try :	
	adminpanel = LoginSearch(url)
	print adminpanel
except :
	print 'there is a problem in the construction of the panel admin link ...'

print Colour.CYAN+"+------------------------------------------------------+"
print Colour.CYAN+"|"+Colour.RED+" ~~~~~~~~~~~~~~~~~ resources search  ~~~~~~~~~~~~~~~~ "+Colour.CYAN+"|"
print Colour.CYAN+"+------------------------------------------------------+"+Colour.END+"\n"
try :
	ResourceSearch(url)
except :
	print 'researching resources problem ...'

RES=[[]]

print Colour.CYAN+"+------------------------------------------------------+"
print Colour.CYAN+"|"+Colour.RED+" ~~~~~~~~~~~~~~~ HTTP verb tempring  ~~~~~~~~~~~~~~~~ "+Colour.CYAN+"|"
print Colour.CYAN+"+------------------------------------------------------+"+Colour.END+"\n"

#try :
hhtp_attr = getMethodHttpAttributs(url,RES)
#except :
#	print 'there is a problem of the attack HTTP verb tampering ...'


# ---------------------------------------* 3 scan des vulnerabilitees *-----------------------------------------------------

print Colour.CYAN+"+------------------------------------------------------+"
print Colour.CYAN+"|"+Colour.RED+" ~~~~~~~~~~~~~~~~ launching sqlmap  ~~~~~~~~~~~~~~~~~ "+Colour.CYAN+"|"
print Colour.CYAN+"+------------------------------------------------------+"+Colour.END+"\n"

try :
	sqlmapresult = SqlmapCall(url)
except :
	print 'there is a problem in the sqlmap analyse '

print Colour.CYAN+"+------------------------------------------------------+"
print Colour.CYAN+"|"+Colour.RED+" ~~~~~~~~~~~~~~~~ launching CMSmap  ~~~~~~~~~~~~~~~~~ "+Colour.CYAN+"|"
print Colour.CYAN+"+------------------------------------------------------+"+Colour.END+"\n"
try :
	cmsmapresult = CMSmapCall(url)
except :
	print 'there is a problem in the cms map ...'

# ---------------------------------------* 4 essai d'attaques *-------------------------------------------------------------
print Colour.CYAN+"+------------------------------------------------------+"
print Colour.CYAN+"|"+Colour.RED+" ~~~~~~~~~~~~ preforming sql injection  ~~~~~~~~~~~~~ "+Colour.CYAN+"|"
print Colour.CYAN+"+------------------------------------------------------+"+Colour.END+"\n"


try :
	sqlinject_login = SqlInject(url)
except :
	print 'there is a problem of the sql injection attack '

res=''
path = os.path.join(os.path.expanduser('~'), 'attack-engine1', 'outputFiles', 'bypassRepport.txt')	
with open(path, "r") as f:
	res = f.read().splitlines() 

link=url+res[0]

print 'the link of the panel admin is :'+link

try:
	sqlinject_admin = SqlInject(link)
except :
	print 'there is a problem of the panel admin sql injection ..'

print Colour.CYAN+"+------------------------------------------------------+"
print Colour.CYAN+"|"+Colour.RED+" ~~~~~~~~~~~~ preforming xss injection  ~~~~~~~~~~~~~ "+Colour.CYAN+"|"
print Colour.CYAN+"+------------------------------------------------------+"+Colour.END+"\n"

try :
	xssinjection=XSSInject(url)
	
except :
	print 'there is a problem in the xss injection ..'

print "Brute Force Html ..."

if link != "" :
	choice = raw_input(Colour.RED+"would you like to preform a bruteForce html on the admin login panel ? \n please note that this may take a long time to accomplich !"+Colour.CYAN+" [Y,n] : "+Colour.END)
	if choice=="Y" or choice =="y" or choice=="yes" :
		 bruteforce = BrutforceHtml(adminpanel)

if link != "" :
	choice = raw_input(Colour.RED+"would you like to preform a DOS attack ? \n please note that this may take forever to accomplich ! "+Colour.CYAN+"[Y,n] : "+Colour.END)
	if choice=="Y" or choice =="y" or choice=="yes" :
		 import jackob

# ---------------------------------------* 5 generation de rapport  *-------------------------------------------------------
try:
	genrateReport()
except :
	print 'there is a problem in  the generation of the report ...'
