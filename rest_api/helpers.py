
"""Helper functions to work with alpaca api.

This contains helper functions for working with alpaca api.

"""
import os
import requests as req
import streamlit as st
from dotenv import load_dotenv
from alpaca_trade_api.rest import REST
load_dotenv()

"""ALPACA Fetch Crypto Instrument Data"""
stock_api = REST(
    os.getenv("ALPACA_API_KEY"),
    os.getenv("ALPACA_SECRET_KEY"),
    api_version = "v2"
)

crypto_api = REST(
    os.getenv("ALPACA_API_KEY"),
    os.getenv("ALPACA_SECRET_KEY"),
    api_version = "v1beta1"
)
"""End ALPACA Fetch Crypto Instrument Data"""


"""QUANDL Fetch Crypto Instrument Data"""
def get_bitfinex_data(crypto_symbols, start_date, end_date):
    
    crypto_data = []

    symbols = crypto_symbols.split(",")
    
    for each_symbol in symbols:
        try:
            url = f"https://data.nasdaq.com/api/v3/datasets/BITFINEX/{each_symbol}?start_date={start_date}&end_date={end_date}&api_key={os.getenv('QUANDL_API_KEY')}"
            res = req.get(url).json()
            res = res["dataset"]
            # pd.DataFrame() create dataframe here for each crypto
            crypto_data.append(res)

        except Exception as error:
            # If an exception occurs in the try portion, the code in this branch will be executed.
            warning_6 = st.sidebar.write(
                f"""
                Error Fetching Crypto {symbol} data.\n
                Refresh the browser and try again!\n
                Error: {error}"""
            )

    return crypto_data

"""End QUANDL Fetch Crypto Instrument Data"""