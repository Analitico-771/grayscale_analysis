
"""Helper functions to work with Alpaca api.

This contains helper functions for alpaca api calls.

"""

import pandas as pd
import streamlit as st
from datetime import datetime, date
import yfinance as yf
# from MCForecastTools import MCSimulation


def get_symbol_data(choices):
    """The function that gets all the data for a symbol

    Discriminates between a crypto request and others
    
    Returns:
        The historical data from the respective API, conducts ETL, saves to a db.
    """
    # deconstruct object
    user_start_date, start_date, end_date, tickers, crypto_symbols  = choices.values()
    # print(user_start_date)
    # print(start_date)
    # print(end_date)

    combined_tickers_df = []
    symbols = tickers.split(",")
    print(symbols)

    for each_ticker in symbols:
            data = yf.download(
                    each_ticker,
                    start="2017-02-17", end="2022-02-17"
            )
            # Drop the NaaN and extra columns from the Crypto DataFrame
            data = data.dropna().drop(columns=['Open','High','Low','Close','Volume'])
            # Rename column to ticker name
            data = data.rename(columns = {'Adj Close' : each_ticker})
            # Save data to csv
            data.to_csv(f'./{each_ticker}.csv')
            # Append each ticker to a list
            combined_tickers_df.append(data)

    # Concatenate the crypto dataframes
    combined_df = pd.concat(combined_tickers_df, axis="columns", join="inner")

    return combined_df
