import pandas as pd

def divide_dataFrame(df):
    """
    data frame df is divided into smaller datasets 
    in order to facilitate the processing

    Arguments:
    df : pandas data frame containing Ticker Names
    
    Output:
    df is divided into 9 smaller data frames and saved on the disk
    all of them are named as dfi.csv (i being the sequence number)

    """

    i=0
    count = 1
    while i<=259:
            name='df'+str(count)
            foutput = ''.join(['data/output/',name,'.csv'])
            if i==9:
                    df1=df[i:i+18]
                    df1.to_csv(foutput)
            else:
                    df1=df[i:i+31]
                    df1.to_csv(foutput)
            i=i+31
            count = count+1


if __name__ == "__main__":
    df = pd.read_csv('data/input/TickerNames.csv')
    divide_dataFrame(df)
