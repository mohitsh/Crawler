import pandas as pd
import numpy as np


def createScripts(fname):
    """
        for each data set containing tickers (df1, df2, ..... df9)
        this method created individual scripts for processing

        Arguments:
            fname = Name of the file storing tickers

        Output:
           for each dfi.csv => dfi.py  

    """
    data1 = pd.read_csv(fname, header=None)
    data = data1[0]
    for name in data:
        fout = ''.join(['data/output/',name,'.py'])
        file = open(fout,'w')
        dfCode = open('data/input/dfProgram.txt').readlines()
        codeString = ''
        for line in dfCode:
            codeString += line
        file.write(codeString.format(str(name),str(name)))
        file.close()



if __name__ == "__main__":
    fname = 'data/input/scriptNames.csv'
    createScripts(fname)
