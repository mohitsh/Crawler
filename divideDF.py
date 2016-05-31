#!/root/anaconda3/bin/python

import pandas as pd
df = pd.read_csv('dudeNSE.csv')
i=0
count = 1
while i<=259:
	name='df'+str(count)
	if i==9:
		df1=df[i:i+18]
		df1.to_csv(''.join([name,'.csv']))
	else:
		df1=df[i:i+31]
		df1.to_csv(''.join([name,'.csv']))
	i=i+31
	count = count+1
#scriptdf.to_csv('scriptdf.csv')
