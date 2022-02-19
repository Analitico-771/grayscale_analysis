
import pandas as pd
import streamlit as st
from datetime import date, timedelta
from rest_api.fetch_data import (get_symbol_data)
from utils.fileio import (
    read_csv,
    write_csv
)

def load_data(choices):
    """The function that gets all the data from all APIs / CSV files.

    Asks for the Index Symbol and Crypto Symbols for analysis, and fetches other functions to complete tasks.
    
    Returns:
        The historical data from the respective API, conducts ETL, saves to a db.
    """
    # combined_df = get_symbol_data(choices)

    return 

def get_choices():
    """Prompts the dialog to get the Index and Crypto symbols.

    Returns:
        A list of symbols.
    """
    choices = {}
    user_start_date = date.today()
    yesterday = user_start_date - timedelta(days=1)

    # add_selectbox = st.sidebar.selectbox(
    # "How would you like to be contacted?",
    # ("Email", "Home phone", "Mobile phone")
    # )
    
    warning_1 = st.sidebar.write("Max yrs you can go back is 5.")
    years_back = st.sidebar.number_input('How Many Years Back From Today?', min_value=1, max_value=5, value=1)

    warning_2 = st.sidebar.write("You must enter 1 Index such as SPY, 3 Stock, and 2 Crypto Symbol names. Please refer to Yahoo Finance for a list of applicable ticker symbols.  Type the symbol EXACTLY as provided by Yahoo Finance.")
        
    tickers = st.sidebar.text_input('Enter 1 index and 3 stock symbols.', 'SPY,AMZN,TSLA,NVDA')

    warning_3 = st.sidebar.write("Enter 2 Crypto Symbol names.")

    crypto_symbols = st.sidebar.text_input('Enter 2 crypto symbols only as below', 'BTC-USD,ETH-USD')
    # 'SPY,AMZN,TSLA,NVDA,AAPL,BTC-USD,ETH-USD'
    # Set the start_date to years_back  
    years = user_start_date.replace(year=(yesterday.year - years_back), month=yesterday.month, day=yesterday.day)
    start_date = pd.Timestamp(f"{years}", tz="America/New_York").isoformat()
    # Set the end_date to yesterday
    end_date = pd.Timestamp(f"{yesterday}", tz="America/New_York").isoformat()

    # Every form must have a submit button.
    submitted = st.sidebar.button("Submit")

    if submitted:
        # Submit an object with choices
        choices = {
            'user_start_date': user_start_date,
            'start_date': start_date,
            'end_date': end_date,
            'first_crypto_symbol': tickers,
            'crypto_symbols': crypto_symbols
        }
        # Load data
        combined_df = get_symbol_data(choices)
        return {
            'choices': choices,
            'combined_df': combined_df
        }

def run():
    """The main function for running the script."""
    print('Run works!')
    get_choices()
    # combined_df = load_data(choices)
    # print(combined_df)

if __name__ == "__main__":
    run()
