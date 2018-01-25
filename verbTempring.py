#!/usr/bin/python3.5

import requests
from Colour import Colour
from datetime import datetime

def getMethodHttpAttributs(url,RES):
	RES=[]
	time = str(datetime.now())
	print time + "\n"
	try:	
		r = requests.get(url)
		headers=r.headers
		status=r.status_code
		link=r.url
		data="get",status,headers,url
		RES.append(data)		
		print Colour.GREEN+"Get Method Accepted .."+Colour.END
	except :
		print Colour.RED+"method get was not accepted"+Colour.END
	try:
		r = requests.post(url)
		headers=r.headers
		status=r.status_code
		link=r.url
		data="post",status,headers,url
		print data
		RES.append(data)
		print Colour.GREEN+"POST Method Accepted .."+Colour.END
	except:
		print Colour.RED+"method post was not accepted"+Colour.END


	try:
		r = requests.delete(url)
		#response = requests.delete(url)
		headers=r.headers
		status=r.status_code
		link=r.url
		data="delete",status,headers,url
		RES.append(data)
		print Colour.GREEN+"delete Method Accepted .."+Colour.END
	except:
		print Colour.RED+"method delete was not accepted"+Colour.END
	try :
		r = requests.put(url)
		headers=r.headers
		status=r.status_code
		link=r.url
		data="put",status,headers,url
		RES.append(data)
		print Colour.GREEN+"put Method Accepted .."+Colour.END
	except:
		print Colour.RED+"method put was not acepted"+Colour.END


	try :
		r = requests.head(url)
		headers=r.headers
		status=r.status_code
		link=r.url
		data="head",status,headers,url
		RES.append(data)
		print Colour.GREEN+"head Method Accepted .."+Colour.END
	except:
		print Colour.RED+"method head was not acepted"+Colour.END


	try :
		r = requests.options(url)
		headers=r.headers
		status=r.status_code
		link=r.url
		data="options",status,headers,url
		RES.append(data)
		print Colour.GREEN+"options Method Accepted .."+Colour.END
	except:
		print Colour.RED+"method options was not acepted"+Colour.END	
	time = str(datetime.now())
	print time + "\n"
	return 0

RES=[[]]






