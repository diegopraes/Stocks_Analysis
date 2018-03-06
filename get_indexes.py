# Creat DATABASE of Stocks shares to buy ( 1% risk ) in real time
"""
Created on Sun Mar 4 12:44:45 2018 @author: DiegoPraes
"""

import datetime
from pandas_datareader import data as web
import matplotlib.pyplot as plt

bov = ['BBAS3', 'ABEV3', 'PETR3', 'ITUB4', 'USIM5','VALE3', 'GGBR4', 'EMBR3', 'ELET3', 'SUZB5', 'RENT3', 'NATU3', 'MRVE3']
dj = ['XOM', 'AAPL', 'MCD', 'KO', 'CVX', 'BA', 'CAT', 'IBM', 'MMM', 'WMT', 'V', 'NKE']

user_input = input('\n Enter: \n\n [bov] for Bovespa \n\n [dj] for Dow Jones \n\n>>> ' )

print('\n\nData parameters:\n')
date = input('Enter the date [YYYY, MM, DD]:\n\n>>> ')
dt = date.split(',')
date = datetime.datetime(int(dt[0]), int(dt[1]), int(dt[2]))
portifolio = float(input('\nPortifolio:\n\n>>> '))

print('\n\nPlot parameters:')
column = input('Define Plot: [ Open, Close, High or Low ]:\n\n>>> ')
start = input('Enter the start date [YYYY, MM, DD]:\n\n>>> ')
st = start.split(',')
start = datetime.datetime(int(st[0]), int(st[1]), int(st[2]))

class Data:
    
    def __init__(self, index, start, date):
        self.index = index
        self.start = start
        self.date = date
        
    def get(self):
        return web.DataReader(self.index, 'google', self.start, self.date)


class Data_synt:  
    def __init__(self, index, date):
        self.index = index
        self.date = date
        
    def get(self):
        return web.DataReader(self.index, 'google', self.date)    
    

while user_input not in ['bov', 'dj']:
    user_input = input('\n Enter: \n\n [bov] for Bovespa \n\n [dj] for Dow Jones \n\n>>> ')

if user_input == 'bov':
    index_list = bov

elif user_input == 'dj':
    index_list = dj

for index in index_list:
    try:                
        ds = Data_synt.get(Data_synt(index, date))        
        var = float(ds['Close'][0]) - float(ds['Open'][0])
        s = portifolio/100/var
        shares = float(portifolio)/float(ds['Open'][0])
        print('\n\nIndex: {}\n'.format(index))
        print(ds)
        print('\nDaily variation: {:.2f}'.format(var))
        print('\nBuy {:.2f} shares to 1% risk'.format(s))
        print('\nMax shares to buy (using total portifolio): {:.2f}'.format(shares))
        print('\nProfit: {:.2f}'.format(shares*var))
        print('\n')
        plt.figure()
        d = Data.get(Data(index, None, date))
        plt.title('Stock Market {} [{}]'.format(index, column))
        d[column].plot(subplots=False, grid=True, style='r', figsize=(8, 6))
        plt.figure()
        (d['Close'][:]-d['Open'][:]).plot(subplots=False, grid=True, style='g', figsize=(8, 6))
        plt.title('Stock Market {} Daily Variation'.format(index))
        data1 = d[column]
        data2 = d['Close'][:]-d['Open'][:]
        data3 = data1.join(data2)
        
    except:
        print('\n\nNot possible to get data for {}\n'.format(index))

