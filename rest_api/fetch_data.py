
"""Helper functions to work with Api.

This contains helper functions for Api Calls.

"""

import pandas as pd
import yfinance as yf
import streamlit as st
from datetime import datetime, date


def get_symbol_data(choices):
    """The function that gets all the data for a symbol

    Discriminates between a crypto request and others, conducts ETL.
    Two DataFrames are created: stock_df and mc_data_df.  They have similar information but have a different format.  The API Call gets all the data at one time and formats both dataframes for efficiency and then later another column is added for the Monte Carlo Simulation code. Then both objects are returned as one.
    
    Returns:
        Two dataframes with the historical data from Yahoo API.
    """
    # deconstruct object choices
    user_start_date, start_date, end_date, symbols, weights, investment, forecast_years, sim_runs  = choices.values()

    mc_data_list = []
    combined_tickers_list = []

    try:
        for each_ticker in symbols:
            data = yf.download(
                each_ticker,
                start=start_date,
                end=end_date
            )
            # dropna() from df
            data = data.dropna()
            #append unchanged data into mc_data_list
            mc_data_list.append(data)
            data = data.drop(columns=['Open','High','Low','Close','Volume'])
            # Rename column to ticker name
            data = data.rename(columns = {'Adj Close' : each_ticker})
            # Append each ticker to a list
            combined_tickers_list.append(data)

    except Exception as error:
        print(error)

    # Concatenate the dataframes
    stock_df = pd.concat(combined_tickers_list, axis="columns", join="inner")
    mc_data_df = pd.concat(mc_data_list, axis="columns", join="inner")
    
    # Create the multi level column tuple
    multi_columns = []
    # Change the "Adj Close" column name to "close" for Monte Carlo simulation code
    columns = ['Open','High','Low','Close','close','Volume']
    for each_symbol in symbols:
        for each_column in columns:
            multi_columns.append((each_symbol, each_column))

    # Create multi level index
    mc_data_df.columns = pd.MultiIndex.from_tuples(multi_columns)

    return {
        'stock_df': stock_df,
        'mc_data_df': mc_data_df
    }