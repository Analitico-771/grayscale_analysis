
import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
from MCForecastTools import MCSimulation


def basic_portfolio(stock_df):
    # st.subheader('Initial Portfolio Historical Data')
    #st.line_chart(stock_df['stock_df'])

    st.subheader('Initial Portfolio Historical Data')
    #st.line_chart(stock_df['stock_df'])
    daily_return = stock_df['stock_df'].pct_change().dropna()
    cumulative_return = (1+ daily_return).cumprod()
    st.line_chart(cumulative_return)

def display_heat_map(stock_df):
    price_correlation = stock_df['stock_df'].corr()
    #sns.heatmap(price_correlation, vmin=-1, vmax=1)

    with st.container():
        st.subheader('Heatmap Showing Correlation Of Assets')
        fig, ax = plt.subplots()
        sns.heatmap(price_correlation, ax=ax)
        st.write(fig)

        st.dataframe(price_correlation)


def beta(stock_df):
    daily_returns = stock_df['stock_df'].pct_change().dropna()
    columns = daily_returns.columns.tolist()
    beta = []
    for each_column in columns:
        if each_column != columns[0]:
            covariance = daily_returns[each_column].cov(daily_returns[columns[0]])
            variance = daily_returns[columns[0]].var()
            calc_beta = covariance / variance
            beta.append({each_column:calc_beta})

    st.subheader('Beta Of Assets Comapred to Index')
    st.json(beta)


def display_portfolio_return(stock_df, choices):
    user_start_date, start_date, end_date, symbols, weights, investment  = choices.values()
    
    daily_returns = stock_df['stock_df'].pct_change().dropna()
    portfolio_returns = daily_returns.dot(weights)
    cumulative_returns = (1 + portfolio_returns).cumprod()
    cumulative_profit = investment * cumulative_returns

    st.subheader('Forward Analysis Based On Your Input!')
    st.line_chart(cumulative_profit)

 
def monte_carlo(mc_data_df, choices):
    user_start_date, start_date, end_date, symbols, weights, investment  = choices.values()
    
    forecast_years = 15

    simulation = MCSimulation(
    portfolio_data = mc_data_df['mc_data_df'],
    weights = weights,
    num_simulation = 10,
    num_trading_days = 252*forecast_years,
    )

    summary_results = simulation.calc_cumulative_return()
    st.subheader('Portfolio Cumulative Returns 15 Yr Outlook')
    st.line_chart(summary_results)

    simulation_summary = simulation.summarize_cumulative_return()
    st.subheader('Portfolio Simulation Summary Cumulative Returns 15 Yr Outlook')
    
    ci_lower_cumulative_return = round(simulation_summary[8] * investment, 2)
    ci_upper_cumulative_return = round(simulation_summary[9] * investment, 2)

    # Display the result of your calculations
    st.write(f"There is a 95% chance that an initial investment of ${investment:.2f} over the next 15 years will end within in the range between {str(ci_lower_cumulative_return)} and {str(ci_upper_cumulative_return)} USD")

    st.dataframe(simulation_summary)