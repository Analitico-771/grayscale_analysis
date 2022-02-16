
"""Helper functions to work with Alpaca api.

This contains helper functions for alpaca api calls.

"""

import pandas as pd
from datetime import datetime, date
from alpaca_trade_api.rest import TimeFrame
# from MCForecastTools import MCSimulation
from rest_api.helpers import (
    stock_api,
    crypto_api,
    get_bitfinex_data
)

def get_symbol_data(choices):
    """The function that gets all the data for a symbol

    Discriminates between a crypto request and others
    
    Returns:
        The historical data from the respective API, conducts ETL, saves to a db.
    """
    # deconstruct object
    user_start_date, start_date, end_date, first_stock_symbol, crypto_symbols  = choices.values()
    # print(user_start_date)
    # print(start_date)
    # print(end_date)

    # Set limit_rows to 1000 to retreive the maximum amount of rows
    limit_rows = 1000

    stock_ticker_data = stock_api.get_bars(
        first_stock_symbol,
        # stock_tickers,
        TimeFrame.Day,
        start=start_date,
        end=end_date,
        # adjustment='raw',
        limit=limit_rows,
    ).df

    # QUANDL Fetch Crypto Instrument Data
    res = get_bitfinex_data(crypto_symbols, start_date, end_date)
     #BTCUSD ETHUSD MNAUSD YFIUSD SOLUSD MATICUSD LUNAUSD LTCUSD
    crypto_ticker_data = pd.DataFrame(
        res['data'],
        columns=["Date","High","Low","Mid","Last","Bid","Ask","Volume"]
    )
    # End QUANDL Fetch Crypto Instrument Data

    # Convert Date into datetime format and set as index
    crypto_ticker_data = crypto_ticker_data.set_index('Date')
    crypto_ticker_data.index = pd.to_datetime(crypto_ticker_data.index)
    crypto_ticker_data.sort_index(ascending=True, inplace=True)
    # End Convert Date into datetime format and set as index


    # Drop time from datetime
    stock_ticker_data.index = stock_ticker_data.index.date
    crypto_ticker_data.index = crypto_ticker_data.index.date

    # Save df to csv
    stock_ticker_data.to_csv(f'./resources/{first_stock_symbol}_historical_{user_start_date}.csv')
    crypto_ticker_data.to_csv(f'./resources/{crypto_symbols}_bitfinex_historical_{user_start_date}.csv')

    # Drop the NaaN and extra columns from the DataFrame
    stock_ticker_data = stock_ticker_data.dropna().drop(columns=['open', 'high', 'low', 'volume', 'trade_count', 'vwap'])
    
    crypto_ticker_data = crypto_ticker_data.dropna().drop(columns=['High', 'Low', 'Mid', 'Bid', 'Ask', 'Volume'])

    # Rename columns
    stock_ticker_data = stock_ticker_data.rename(columns = {'close' : first_stock_symbol})
    
    crypto_ticker_data = crypto_ticker_data.rename(columns = {'Last' : crypto_symbols})

    # Combine the dataframes
    combined_df = pd.concat([stock_ticker_data, crypto_ticker_data], axis="columns", join="inner")

    # Save combined df to csv
    combined_df.to_csv(f'./resources/combined_df__historical_{user_start_date}.csv')
    
    print(combined_df)

    return combined_df
