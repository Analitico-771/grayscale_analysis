
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
    user_start_date, start_date, end_date, symbols  = choices.values()
    # print(user_start_date)
    # print(start_date)
    # print(end_date)

    combined_tickers_df = []
    # symbols = tickers.split(",")
    # print(symbols)

    try:
        for each_ticker in symbols:
                data = yf.download(
                        each_ticker,
                        start=start_date,
                        end=end_date
                )
                # Save data to csv
                # data.to_csv(f'./files/{each_ticker}.csv')
                # Drop the NaaN and extra columns from the Crypto DataFrame
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

    # Concatenate the crypto dataframes
    combined_df = pd.concat(combined_tickers_df, axis="columns", join="inner")
    # Save data to csv
    # data.to_csv(f'./files/combined_df_{user_start_date}.csv')
    data.to_csv(f'files/combined_df.csv')
#     print(combined_df) grayscale_analysis\rest_api\files\combined_df.csv
    return combined_df
