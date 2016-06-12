# StockCodes
This project scraps and stores price and volume data from yahoo finance during market's working time for 259 stocks listed on NSE

Scripts follow this sequence.
* divideDF.py
* central.py
* dfi.py
* runScripts.sh

#### divideDF.py  
takes a list of 259 stocks as input all listed at NSE and divides them into 9 different .csv files for further uses.

#### central.py  
takes a list of data frames as created in divideDF.py as input and generates correspnding python scripts to scrap data for
those stocks. These scripts are named in sequence as dfi.py

#### dfi.py
These are the main scripts that perform the data scraping task. Output for price and volume data are stored in csv format.

#### runScripts.sh
is a bash scripts that runs all the dfi.py files in parallel.

#### Libraries used
pandas, BeautifulSoup, requests, csv, numpy, datetime
