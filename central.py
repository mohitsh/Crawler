#!/root/anaconda3/bin/python3

import pandas as pd
import numpy as np

data1 = pd.read_csv('scriptNames.csv',header=None)
data = data1[0]

for name in data:
    #url = data1.loc[dude][0]
    file = open(''.join([name,'.py']),'w')
    file.write(
"#!/root/anaconda3/bin/python3 \
\n\nfrom bs4 import BeautifulSoup,SoupStrainer \
\nimport requests,csv \
\nfrom datetime import datetime \
\nimport time as tm \
\nimport pandas as pd \
\nimport numpy as np \
\nimport threading \
\nimport re \
\nimport signal \
\ndf=pd.DataFrame() \
\ndata1=pd.read_csv('{0}.csv') \
\ndata=data1['Ticker'] \
\ndf1Price=pd.DataFrame(columns=data) \
\ndf1Price['time']='' \
\n\ndef handler(signum,frame): \
\n\tprint('time is over!') \
\n\traise Exception('end of time') \
\n\ndef foo(): \
\n\tglobal df1Price \
\n\ta=[] \
\n\ts=pd.Series() \
\n\tthreading.Timer(60.0,foo).start() \
\n\tctime = tm.strftime('%Y:%m:%d %H:%M:%S') \
\n\tfor i in range(len(data)): \
\n\t\telem=data[i] \
\n\t\tr1=requests.get('https://in.finance.yahoo.com/q?s='+data[i]) \
\n\t\tsmallElem=elem.lower() \
\n\t\tsoup=BeautifulSoup(r1.text,'lxml') \
\n\t\tif '%26' in smallElem: \
\n\t\t\tsmallElem=re.sub('%26','&',smallElem) \
\n\t\tdude=soup.select(''.join(['#yfs_l84_',smallElem]))\
\n\t\tvolume=soup.select(''.join(['#yfs_v53_',smallElem])) \
\n\t\tcprice=dude[0].getText() \
\n\t\ta.append(cprice) \
\n\t\tcvolume=volume[0].getText() \
\n\t\tprint('Stock: ',elem,'\t','Price: ',cprice,'\t','Volume: ',cvolume) \
\n\ta.append(ctime) \
\n\tps=pd.Series(a,index=df1Price.columns) \
\n\tdf1Price=df1Price.append(ps,ignore_index=True) \
\n\tdf1Price.to_csv('{1}Price.csv') \
\n\nsignal.signal(signal.SIGALRM,handler) \
\nsignal.alarm(300) \
\n\ntry: \
\n\tfoo() \
\nexcept Exception: \
\n\tprint(exc)".format(str(name),str(name))   
    )
    file.close()

