"""Utility functions"""

import os
import pandas as pd
import matplotlib.pyplot as plt

# covers lesson 3

def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        # TODO: Read and join data for each symbol
        df_temp=pd.read_csv("data/{}.csv".format(symbol), index_col='Date', parse_dates=True,usecols=['Date','Adj Close'], na_values=['nan'])
        df_temp=df_temp.rename(columns={'Adj Close':symbol})
        df = df.join(df_temp)
        df=df.dropna()
    return df

def plot_data(df,title="Stock Prices"):
    ax =  df.plot(title=title,fontsize=15)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()

def plot_selected(df, columns, start_index, end_index):
    """Plot the desired columns over index values in the given range."""
    # TODO: Your code here
    # Note: DO NOT modify anything else!
    df1= df.ix[start_index:end_index, columns]
    plot_data(df1,"Selected Plot")

def normalize_data(df):
    return df/df.ix[0,:]

def test_run():
    # Define a date range
    dates = pd.date_range('2010-01-01', '2010-12-31')

    # Choose stock symbols to read
    symbols = ['GOOG', 'IBM', 'GLD']

    # Get stock data
    df = get_data(symbols, dates)
    #print df


    #row slicing
    #print df.ix['2010-01-01':'2010-01-31']

    # col slicing
    #print df['GOOG']
    #print df[['IBM','GLD']]

    # row and col slicing
    print df.ix['2010-03-10':'2010-03-15', ['SPY','IBM']]

    plot_data(df)

    # Slice and plot
    plot_selected(df, ['SPY', 'IBM'], '2010-03-01', '2010-04-01')

    #normalize data so that all stocks start with one dollar
    # add a funciton to divide all the data by the first row
    normdf = normalize_data(df)
    plot_data(normdf)

if __name__ == "__main__":
    test_run()
