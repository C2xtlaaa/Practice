# This is first part of visualization program
# Program will import data from tearsheet-data.csv and do an equity curve
# using matplotlib
# By Tony Amos
# 10/29/2019
import pandas as pd
#Set up path to .csv file and read into memory
filepath ='/Users/Administrator/Desktop/tearsheet-data.csv'
data = pd.read_csv(filepath, sep=',', index_col=0, header=0, names=["Date", "Holdings", "Cash", "Total", "Returns"])
data.index = pd.to_datetime(data.index)
#Calculate percent change
data['Calculated'] = data['Total'].pct_change()
data['Test'] = data['Returns'] == data['Calculated']
data.loc[(~data.Test) & (data.index < '1998-06-02'), ['Returns', 'Calculated', 'Test']]
#Change precision to 20. Default is 6  
pd.set_option("display.precision", 20)
#
import numpy as np
data['IsClose'] = np.isclose(data.Returns, data.Calculated)
#
print(data.loc[~data.IsClose])
# Remove Calculated, Test, and Isclose from data set
data.drop(['Calculated', 'Test', 'IsClose'], axis=1)
#
data['Equity'] = (1 + data['Returns']).cumprod()
#
pd.set_option("display.precision", 6)
data.loc[data['Equity'] > 1, ['Cash', 'Returns', 'Equity']]
# Display equity curve using matplotlib
import matplotlib.pyplot as plt
data['Equity'].plot(title="Tony's Equity Curve")
plt.show()
