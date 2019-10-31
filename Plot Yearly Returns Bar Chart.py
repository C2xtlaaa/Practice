# -*- coding: utf-8 -*-
#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Created on Wed Oct 30 20:12:55 2019
#
#@author: Tony Amos
#
#Using Mathplotlob and tearsheet-data will generate a bar chart
#
#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#matplotlib is imported but unused so we commented the below line out
#import matplotlib.pyplot as plot
import pandas as pd

data = pd.read_csv(
    '/Users/Administrator/Desktop/tearsheet-data.csv', sep=',', index_col=0, header=0, 
    names=["Date", "Holdings", "Cash", "Total", "Returns"]
)
data.index = pd.to_datetime(data.index)
data['equity'] = (1 + data['Returns']).cumprod()

    
def aggregated_returns(returns, time_span):
    def calculate_cumulative_returns(x):
        return (1 + x).cumprod()[-1] - 1.0
    
    if time_span == "yearly":
        return returns.groupby(lambda x: x.year).apply(calculate_cumulative_returns)


def plot_yearly_returns():
    annual_rets = aggregated_returns(data['Returns'], 'yearly') * 100
    ax = annual_rets.plot(kind='bar', color='red')
    ax.set_xlabel("Year")
    ax.set_ylabel("Cumulative Returns (%)")
    ax.set_title("Yearly Returns (%)")

    
plot_yearly_returns()
