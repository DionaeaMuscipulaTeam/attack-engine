#!/usr/bin/python
import urllib2

def checkLink(url):
#	if (url.find('www')==-1):
#		if (url.find('http')==-1 or url.find('https')==-1):
#			url='http://www.'+url
#	else :
	if (url.find('http://')==-1 and url.find('https://')==-1):
		url='http://'+url
	return url

def checkAvailable(url):
	try:
	    urllib2.urlopen(url)
	except urllib2.HTTPError, e:
		print "try https !!! "
		return False	 
	except urllib2.URLError, e:
		print "either url is not valid or there is no internet connection !!! "
		return False
	return True
