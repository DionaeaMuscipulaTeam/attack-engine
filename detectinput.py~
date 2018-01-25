#!/usr/bin/env python
from lxml import etree
from bs4 import BeautifulSoup
import requests


def DetectFormInput(url) :

	response = requests.get(url)
	h = response.content
	soup = BeautifulSoup(h, "lxml")
	forms = soup.find_all('form')
	if str(forms)=="[]" :
		print"no forms were detected here"
	else :
		for form in forms :
			attrs = form.attrs
			try:
				formaction = attrs['action']
				formmethod = attrs['method']
				print formaction
				print formmethod
			except:
				formaction = '#'
			try :
				formname = attrs['name']
			except :
				print "form have no name"
			formstr = str(form)
			f = BeautifulSoup(formstr, "lxml")
			inputs = soup.find_all('input')
			inputnames = []
			inputtypes = []
			inputvalues = []
			typerange = 0
			for inputt in inputs :
				attrsi = inputt.attrs
				try :
					inputname = attrsi['name']
					inputnames.append(inputname)
				except :
					inputnames.append("null")
				try :
					inputtype = attrsi['type']
					typerange = typerange + 1
					inputtypes.append(inputtype)
				except :
					inputtypes.append("null")
				try :
					value = attrsi['value']
					inputvalues.append(value)
				except :
					inputvalues.append("null")
	return inputnames,inputtypes,inputvalues,formaction,formmethod

def RandomInput(url):
	response = requests.get(url)
	h = response.content
	soup = BeautifulSoup(h, "lxml")
	inputs = soup.find_all('input')
	if str(inputs)=="[]" :
		print"no inputs were detected here"
	inputs = soup.find_all('input')
	for inputt in inputs :
		attrsi = inputt.attrs
		try :
			inputname = attrsi['name']
			inputtypes.append(inputname)
		except :
			inputnames.append("null")
		try :
			inputtype = attrsi['type']
			typerange = typerange + 1
			inputtypes.append(inputtype)
		except :
			inputvalues.append("null")
		try :
			value = attrsi['value']
			value = attrsi['value']
			inputvalues.append(inputvalue)
		except :
			inputvalues.append("null")

	return inputnames,inputtypes,inputvalues


