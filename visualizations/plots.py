import pandas as pd
import streamlit as st
import hvplot.pandas
import seaborn as sns
from bokeh.plotting import figure
import matplotlib.pyplot as plt
from MCForecastTools import MCSimulation
import yfinance as yf

# x is combined_df
def basic_portfolio(combined_df):
    #st.line_chart(data = combined_df, width=20, height = 10)
    st.line_chart(combined_df)


# x is combined_df and y is weights, z is initial investment
def display_portfolio_return(combined_df, weights, initial_investment):
   daily_returns = combined_df.pct_change().dropna()
   portfolio_returns = daily_returns.dot(weights)
   cumulative_returns = (1 + portfolio_returns).cumprod()
   cumulative_profit = initial_investment * cumulative_returns
   st.line_chart(cumulative_profit)


# x is combined_df
def display_heat_map(combined_df):
    price_correlation = combined_df.corr()
    #sns.heatmap(price_correlation, vmin=-1, vmax=1)

    fig, ax = plt.subplots()
    sns.heatmap(price_correlation, ax=ax)
    st.write(fig)

def beta(combined_df):
    daily_returns = combined_df.pct_change().dropna()
    columns = daily_returns.columns.tolist()
    beta = []
    for each_column in columns:
        if each_column != columns[0]:
            covariance = daily_returns[each_column].cov(daily_returns[columns[0]])
            variance = daily_returns[columns[0]].var()
            calc_beta = covariance / variance
            beta.append(calc_beta)



            
def monte_carlo():
    #user_start_date, start_date, end_date, symbols  = choices.values()
    
    weights = [0.2, 0.2, 0.2, 0.2, 0.1, 0.1]
    forecast_years = 15
    tickers = 'SPY,AMZN,TSLA,NVDA,BTC-USD,ETH-USD'
    # tickers = ['SOL-USD']

    combined_tickers_df = []
    symbols = tickers.split(",")
    
    combined_data = []
    individual_data = {}
    for each_asset in symbols:
        data = yf.download(
            each_asset,
            start="2017-02-17", end="2022-02-17"
        )
        data = data.dropna()
        data = data.rename(columns={'Close':'close'})
        combined_data.append(data)
        individual_data[each_asset] = data

    combined_mc_data = pd.concat(combined_data, axis="columns", join="inner")

    combined_mc_data_new = pd.concat([
        individual_data[symbols[0]],
        individual_data[symbols[1]],
        individual_data[symbols[2]],
        individual_data[symbols[3]],
        individual_data[symbols[4]],
        individual_data[symbols[5]],
    ], keys=symbols, axis=1)

    combined_mc_data_new.dropna(inplace=True)

    simulation = MCSimulation(
    portfolio_data = combined_mc_data_new,
    weights = weights,
    num_simulation = 50,
    num_trading_days = 252*forecast_years,
    )
    simulation.calc_cumulative_return()

    #st.container(simulation.plot_simulation())

    simulation_summary = simulation.summarize_cumulative_return()
    st.json(simulation_summary)

    
