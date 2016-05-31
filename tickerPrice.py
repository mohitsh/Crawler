#!/root/anaconda3/bin/python3

from bs4 import BeautifulSoup
import requests,csv
from datetime import datetime
import time as tm
import pandas as pd
import numpy as np

then = tm.time()
#data = csv.reader(open('TickerNSE.csv'))
data1 = pd.read_csv('TickerNSE.csv',header=None)
data = data1[0]
"""
for elem in data:
    print(elem)

priceData = open('StockPrice','w')
priceData.close()

volumeData= open('StockVolume','w')
volumeData.close()
"""
now = datetime.now()
today = now.date()
moment = now.time()
cdate = str(today)
ctime = str(moment)[:8]
priceList = [ctime]
volumeList = [ctime]

appender = priceList.append
appender1 = volumeList.append


for elem in data:
    flag = False
    if '&' in elem:
        flag = True
        oldElem = elem
        elem = elem.replace('&','%26')
    r1 = requests.get(''.join(['https://in.finance.yahoo.com/q?s=',elem]))
    r = r1.text
    soup = BeautifulSoup(r,"lxml")
    if flag:
        smallElem = oldElem.lower()
    else:
        smallElem = elem.lower()
    dude = soup.select(''.join(['#yfs_l84_',smallElem]))
    volume = soup.select(''.join(['#yfs_v53_',smallElem]))
    cprice = dude[0].getText()
    cvolume = volume[0].getText()
    """
    now = datetime.now()
    today = now.date()
    moment = now.time()
    cdate = str(today)
    ctime = str(moment)[:8]
    output = [ctime,cprice,cvolume]
    """
    print("Stock: ",elem,"\t","Price: ",cprice,"\t","Volume: ",cvolume)
    appender(cprice)
    appender1(cvolume)
"""
for p in priceList:
    print(p)
"""
d1 = open('StockTickerPrice.csv','a',newline='')
wr = csv.writer(d1,delimiter='\t')
wr.writerow(priceList)
#wr.writerow('\n')
d1.close()

d2 = open('StockTickerVolume.csv','a',newline='')
wr = csv.writer(d2,delimiter='\t')
wr.writerow(volumeList)
#wr.writerow('\n')
d2.close()

now = tm.time()
print(now-then)
"""

"""
