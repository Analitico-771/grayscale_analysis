
"""Helper functions to work with alpaca api.

This contains helper functions for working with alpaca api.

"""
import os
import requests as req
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
    url = f"https://data.nasdaq.com/api/v3/datasets/BITFINEX/{crypto_symbols}?start_date={start_date}&end_date={end_date}&api_key={os.getenv('QUANDL_API_KEY')}"
    res = req.get(url).json()
    res = res["dataset"]
    return res
"""End QUANDL Fetch Crypto Instrument Data"""