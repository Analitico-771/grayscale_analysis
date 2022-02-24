
"""Helper functions to work with Alpaca api.

This contains helper functions for alpaca api calls.

"""

import pandas as pd
import yfinance as yf
import streamlit as st
from datetime import datetime, date


def get_symbol_data(choices):
    """The function that gets all the data for a symbol

    Discriminates between a crypto request and others
    
    Returns:
        The historical data from the respective API, conducts ETL, saves to a db.
    """
    # deconstruct object
    user_start_date, start_date, end_date, symbols, weights, investment, forecast_years, sim_runs  = choices.values()
    # print(user_start_date)
    # print(start_date)
    # print(end_date)

    combined_data = []
    individual_data = {}
    combined_tickers_df = []

    try:
        for each_ticker in symbols:
                data = yf.download(
                        each_ticker,
                        start=start_date,
                        end=end_date
                )
                
                # Drop the NaaN and extra columns from the Crypto DataFrame
                mc_data = data.dropna().rename(columns={'Close':'close'})
                combined_data.append(mc_data)
                individual_data[each_ticker] = mc_data
                data = data.dropna().drop(columns=['Open','High','Low','Close','Volume'])
                # Rename column to ticker name
                data = data.rename(columns = {'Adj Close' : each_ticker})
                # Append each ticker to a list
                combined_tickers_df.append(data)

    except Exception as error:
            st.sidebar.write(f"{error}")
            reset = st.sidebar.button("RESET APP")
            if reset:
                # Clears all singleton caches:
                st.experimental_singleton.clear()

    # Concatenate the dataframes
    stock_df = pd.concat(combined_tickers_df, axis="columns", join="inner")
    mc_data_df = pd.concat(combined_data, axis="columns", join="inner")
    # Add the Top Column to the Monte Carlo df
    mc_data_df = pd.concat([
        individual_data[symbols[0]],
        individual_data[symbols[1]],
        individual_data[symbols[2]],
        individual_data[symbols[3]],
        individual_data[symbols[4]],
        individual_data[symbols[5]],
        ], keys=symbols, axis=1)
    # Drop NaaN
    mc_data_df.dropna(inplace=True)
    mc_data_df = mc_data_df.copy()
    
    return {
            'stock_df': stock_df,
            'mc_data_df': mc_data_df
    }
