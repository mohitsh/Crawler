#!/root/anaconda3/bin/python3

from bs4 import BeautifulSoup,SoupStrainer
import requests,csv
from datetime import datetime
import time as tm
import pandas as pd
import numpy as np
import threading #new
#from apscheduler.scheduler import Scheduler #new
import threading
import signal

elem = '3MINDIA.NS'
df = pd.DataFrame()

def add_data(ctime,cprice):
        print(ctime,cprice)
        global df
        print(elem)
        df.append({'time':ctime,'price':cprice},ignore_index=True)
        #df.to_csv(''.join([elem,'.csv']))
        return(df)
         
def handler(signum,frame):
        print("time is over!")
        raise Exception("end of time")


def foo(): #new
        threading.Timer(10.0,foo).start()
        then = tm.time()    
        #ctime = str(datetime.now().time())[:8]
        ctime = datetime.now()
        ctime = ctime.strftime('%Y-%m-%d %H:%M:%S')
        #appender(ctime)
        #appender1(ctime)
        param={'s':'3MINDIA.NS'}
        r1 = requests.get('https://in.finance.yahoo.com/q/',params=param)
        smallElem = elem.lower()
        soup = BeautifulSoup(r1.text,"lxml")
        dude = soup.select(''.join(['#yfs_l84_',smallElem]))
        volume = soup.select(''.join(['#yfs_v53_',smallElem]))
        cprice = dude[0].getText()
        cvolume = volume[0].getText()
        print("Stock: ",elem,"\t","Price: ",cprice,"\t","Volume: ",cvolume)
        global df
        df = df.append({'time':ctime,'price':cprice},ignore_index=True)
        #add_data(ctime,cprice)
        #now=tm.time()
        #print(now-then)
        df.to_csv(''.join([elem,'.csv']))

signal.signal(signal.SIGALRM,handler)
signal.alarm(20)


try:
        foo()
except Exception:
        #global df
        #df.to_csv(''.join([elem,'.csv']))
        print(exc)
