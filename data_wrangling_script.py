#!/usr/bin/python
# Importing sys to make use of Arguments
import sys

# Importing the pandas library to make use of Dataframe functions
import pandas as pd

source_df = pd.read_excel(sys.argv[1], sheet_name=sys.argv[2], skiprows=2)
source_df.columns=['Date', 'Price']

# code for populated daily file
day_df = source_df.groupby(pd.Grouper(key='Date', freq='D')).mean().resample('D').interpolate().round(2)
day_df.to_csv("daily_prices_populated.csv")

# code for monthly file
month_df = source_df.groupby(pd.Grouper(key='Date', freq='MS')).mean().resample('MS').interpolate().round(2)
month_df.to_csv("monthly_average_prices.csv")

# code for weekly file
weekly_df = source_df.groupby(pd.Grouper(key='Date', freq='W')).mean().resample('W').interpolate().round(2)
weekly_df.to_csv("weekly_average_prices.csv")

# code for yearly file
yearly_df = source_df.groupby(pd.Grouper(key='Date', freq='YS')).mean().resample('AS').interpolate().round(2)
yearly_df.to_csv("yearly_average_prices.csv")
