
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
    combined_df = get_symbol_data(choices)

    # return combined_df

def get_choices():
    """Prompts the dialog to get the Index and Crypto symbols.

    Returns:
        A list of symbols.
    """
    user_start_date = date.today()
    yesterday = user_start_date - timedelta(days=1)

    # add_selectbox = st.sidebar.selectbox(
    # "How would you like to be contacted?",
    # ("Email", "Home phone", "Mobile phone")
    # )
    
    warning_1 = st.sidebar.write("Max yrs you can go back is 5.")
    years_back = st.sidebar.number_input('How Many Years Back From Today?', min_value=0, max_value=5, value=0)

    warning_2 = st.sidebar.write("You must enter a Stock, Equity, Commodity, etc, Symbol name using letters only. Please refer to Yahoo Finance for a list of applicable symbols.  Type the symbol as provided by the broker.")
        
    first_stock_symbol = st.sidebar.text_input('Enter a security symbol only', 'SP500')

    warning_3 = st.sidebar.write("You must enter 5 Crypto Symbol names using letters only. Please refer to Bitfinex.com for a list of crypto symbols. Type the symbol as provided by the broker.")

    crypto_symbols = st.sidebar.text_input('Enter 5 crypto symbols only as below', 'BTCUSD,ETHUSD,MNAUSD,YFIUSD,SOLUSD')

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
            'first_crypto_symbol': first_stock_symbol,
            'crypto_symbols': crypto_symbols
        }
        # Load data
        load_data(choices)

def run():
    """The main function for running the script."""
    get_choices()
    # combined_df = load_data()
    print('Run works!')
    # print(combined_df)

if __name__ == "__main__":
    run()
