# FINANCE ANALYSIS
"""
Created on Wed Feb 28 17:39:13 2018   @author: DiegoPraes
"""

import numpy as np
import pandas as pd
import datetime
from pandas_datareader import data as web
import matplotlib.pyplot as plt
 

INDEX1 = input('Enter the Index 1 code:\n\n>>> ') 
INDEX2 = input('Enter the Index 2 code:\n\n>>> ')
column = input('Define: [ Open, Close, High or Low ]:\n\n>>> ')

INDEXES = []
INDEXES.append(INDEX1)
INDEXES.append(INDEX2)

start = input('Enter the initial date [YYYY, MM, DD]:\n\n>>> ')
end = input('Enter the final date [YYYY, MM, DD]:\n\n>>> ')
st = start.split(',')
nd = end.split(',')
start_date = datetime.datetime(int(st[0]), int(st[1]), int(st[2]))
end_date = datetime.datetime(int(nd[0]), int(nd[1]), int(nd[2]))


class Data:
    def __init__(self, index, start, end):
        self.index = index
        self.start = start
        self.end = end
        
    def get(self):
        return web.DataReader(self.index, 'google', self.start, self.end)


dataframe1 = Data.get(Data(INDEX1, start_date, end_date))
dataframe2 = Data.get(Data(INDEX2, start_date, end_date))

# Save to CVS **Economia/Minhas Análises/Data/
dataframe1.to_csv('C:/Users/Asus/Desktop/Economia/Análises/Data/{}.txt'.format(INDEXES[0]),
                  sep='\t', encoding='utf-8')
dataframe2.to_csv('C:/Users/Asus/Desktop/Economia/Análises/Data/{}.txt'.format(INDEXES[1]),
                  sep='\t', encoding='utf-8')

dataframe1[column].plot(subplots=False, grid=True, style='r', figsize=(8, 6))
plt.title('Stock Market {}'.format(INDEXES[0]))
plt.legend()
plt.show()

print('\n\n\n')

dataframe2[column].plot(subplots=False, grid=True, style='r', figsize=(8, 6))
plt.title('Stock Market {}'.format(INDEXES[1]))
plt.legend()
plt.show()


# DATA CONVERSION ---------------------------------------------------------------------------

class conversion:
    def __init__(self, data):
        self.data = data
    
    def to_list(self):
        return self.data.tolist()
    
    def to_array(self):        
        return np.array(self.data.tolist())



# REGRESSION ------------------------------------------------------------------------------

# Returns:

class Returns:
    def __init__(self, data):
        self.data = data
        
    def daily_return(self):
        return self.data.pct_change(1)
    
    def monthly_return(self):
        return self.data.pct_change(21)
    
    def annual_return(self):
        return self.data.pct_change(252)
    
    def all_returns(self):
        return self.data.pct_change(1)
        return self.data.pct_change(21)
        return self.data.pct_change(252)


returns_df1 = Returns.all_returns(Returns(pd.DataFrame(dataframe1[column])))
returns_df1.plot(subplots=True, grid=True, style='g', figsize=(7, 5))
plt.title('Stock Market {} Returns'.format(INDEXES[0]))
xret = conversion.to_list(conversion(returns_df1[column]))


returns_df2 = Returns.all_returns(Returns(pd.DataFrame(dataframe2[column])))
returns_df2.plot(subplots=False, grid=True, style='b', figsize=(7, 5))
plt.title('Stock Market {} Returns'.format(INDEXES[1]))
yret = conversion.to_list(conversion(returns_df2[column]))


# Regression

if len(returns_df1) > len(returns_df2):
    limit = len(returns_df2)
else:
    limit = len(returns_df1)
   
ydata = xret[1:limit]
xdata = yret[1:limit]


fit = np.polyfit(xdata, ydata, 1)
fit_fn = np.poly1d(fit)


plt.figure(num=None, figsize=(7, 5), dpi=80, facecolor='w', edgecolor='k')
plt.plot(xdata, ydata, 'o', xdata, fit_fn(xdata), '-')
plt.legend(['Data', ' Regression'], loc='best')
plt.xlabel('{} Returns'.format(INDEXES[0]))
plt.ylabel('{} Returns'.format(INDEXES[1]))
plt.title('Returns Linear Regression: \n\n y = {:.5f} * x + {:.5f}'.format(fit[0],fit[1]))
