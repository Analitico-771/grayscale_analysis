
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
