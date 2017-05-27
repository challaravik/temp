import pandas as pd

def test_run():
    startd = '2010-01-22'
    endd = '2010-01-26'
    dates= pd.date_range(startd, endd)
    #print dates

    df1 = pd.DataFrame(index=dates)
    #print df1

    #dfspy= pd.read_csv("data/SPY.csv")
    #dfspy= pd.read_csv("data/SPY.csv",index_col="Date",parse_dates=True)

    dfspy= pd.read_csv("data/SPY.csv",index_col="Date",parse_dates=True,usecols=['Date','Adj Close'], na_values=['nan'])
    dfspy=dfspy.rename(columns={'Adj Close':'SPY'})

    #print dfspy
    df1 = df1.join(dfspy)
    df1=df1.dropna()
    symbols= ['GOOG','IBM','GLD']
    for symbol in symbols:
        df_temp=pd.read_csv("data/{}.csv".format(symbol), index_col='Date', parse_dates=True,usecols=['Date','Adj Close'], na_values=['nan'])
        df_temp=df_temp.rename(columns={'Adj Close':symbol})
        df1 = df1.join(df_temp)
        df1=df1.dropna()

    print df1
    return 0


if __name__ == '__main__':
    test_run()

