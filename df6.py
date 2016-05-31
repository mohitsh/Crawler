#!/root/anaconda3/bin/python3 

from bs4 import BeautifulSoup,SoupStrainer 
import requests,csv 
from datetime import datetime 
import time as tm 
import pandas as pd 
import numpy as np 
import threading 
import re 
import signal 
df=pd.DataFrame() 
data1=pd.read_csv('df6.csv') 
data=data1['Ticker'] 
df1Price=pd.DataFrame(columns=data) 
df1Price['time']='' 

def handler(signum,frame): 
	print('time is over!') 
	raise Exception('end of time') 

def foo(): 
	global df1Price 
	a=[] 
	s=pd.Series() 
	threading.Timer(60.0,foo).start() 
	ctime = tm.strftime('%Y:%m:%d %H:%M:%S') 
	for i in range(len(data)): 
		elem=data[i] 
		r1=requests.get('https://in.finance.yahoo.com/q?s='+data[i]) 
		smallElem=elem.lower() 
		soup=BeautifulSoup(r1.text,'lxml') 
		if '%26' in smallElem: 
			smallElem=re.sub('%26','&',smallElem) 
		dude=soup.select(''.join(['#yfs_l84_',smallElem]))
		volume=soup.select(''.join(['#yfs_v53_',smallElem])) 
		cprice=dude[0].getText() 
		a.append(cprice) 
		cvolume=volume[0].getText() 
		print('Stock: ',elem,'	','Price: ',cprice,'	','Volume: ',cvolume) 
	a.append(ctime) 
	ps=pd.Series(a,index=df1Price.columns) 
	df1Price=df1Price.append(ps,ignore_index=True) 
	df1Price.to_csv('df6Price.csv') 

signal.signal(signal.SIGALRM,handler) 
signal.alarm(300) 

try: 
	foo() 
except Exception: 
	print(exc)