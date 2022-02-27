
import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
from MCForecastTools import MCSimulation


def beta(stock_df):
    beta_list = []
    covariance = 0.0
    covariance_list = []
    daily_returns = stock_df['stock_df'].dropna().pct_change()
    columns = daily_returns.columns.tolist()
    
    for each_column in columns:
        # Don't calculate the index's Beta
        if each_column != columns[0]:
            covariance = daily_returns[each_column].cov(daily_returns[columns[0]])
            variance = daily_returns[columns[0]].var()
            calc_beta = covariance / variance
            beta_list.append(calc_beta)
            covariance_list.append(covariance)
        else:
            # Assign value of 1.0 to index Beta
            beta_list.append(1.0)
            covariance_list.append(1.0)

        beta = {'Assets':columns, 'Beta':beta_list}
    
    st.subheader('Beta Of Assets Compared to Index')
    st.dataframe(beta)

    return beta


def basic_portfolio(stock_df):
    daily_return = stock_df['stock_df'].dropna().pct_change()
    cumulative_return = (1+ daily_return).cumprod()

    st.subheader('Portfolio Historical Normalized Cumulative Returns')
    st.line_chart(cumulative_return)


def display_heat_map(stock_df):
    price_correlation = stock_df['stock_df'].corr()

    st.subheader('Heatmap Showing Correlation Of Assets')
    fig, ax = plt.subplots()
    sns.heatmap(price_correlation, ax=ax)
    st.write(fig)
    st.subheader('Correlation Data')
    st.dataframe(price_correlation)


def display_portfolio_return(stock_df, choices):
    user_start_date, start_date, end_date, symbols, weights, investment, forecast_years, sim_runs  = choices.values()
    
    daily_returns = stock_df['stock_df'].pct_change().dropna()
    portfolio_returns = daily_returns.dot(weights)
    cumulative_returns = (1 + portfolio_returns).cumprod()
    cumulative_profit = investment * cumulative_returns

    st.subheader('Portfolio Historical Cumulative Returns Based On Inputs!')
    st.line_chart(cumulative_profit)

 
def monte_carlo(mc_data_df, choices):
    user_start_date, start_date, end_date, symbols, weights, investment, forecast_years, sim_runs  = choices.values()
    
    simulation = MCSimulation(
    portfolio_data = mc_data_df['mc_data_df'],
    weights = weights,
    num_simulation = sim_runs,
    num_trading_days = 252 * forecast_years,
    )

    summary_results = simulation.calc_cumulative_return()
    st.subheader(f'Portfolio Simulation Summary Cumulative Returns {forecast_years} Yr(s) Outlook')
    st.line_chart(summary_results)

    simulation_summary = simulation.summarize_cumulative_return()
    
    ci_lower_cumulative_return = round(simulation_summary[8] * investment, 2)
    ci_upper_cumulative_return = round(simulation_summary[9] * investment, 2)

    # Display the result of your calculations
    st.write(f"There is a 95% chance that an initial investment of ${investment} over the next {forecast_years} years might result within the range of {ci_lower_cumulative_return} and {ci_upper_cumulative_return} USD")

    st.dataframe(simulation_summary)