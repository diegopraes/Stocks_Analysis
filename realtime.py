# Creat DATABASE of Stocks shares to buy ( 1% risk ) in real time
"""
Created on Sun Mar 4 12:44:45 2018 @author: DiegoPraes
"""

import datetime
from pandas_datareader import data as web

bov = ['BBAS3', 'ABEV3', 'PETR3', 'ITUB4', 'USIM5','VALE3', 'GGBR4', 'EMBR3', 'ELET3', 'SUZB5', 'RENT3', 'NATU3', 'MRVE3']
dj = ['XOM', 'AAPL', 'MCD', 'KO', 'CVX', 'BA', 'CAT', 'IBM', 'MMM', 'WMT', 'V', 'NKE']


date = input('Enter the date [YYYY, MM, DD]:\n\n>>> ')
dt = date.split(',')
date = datetime.datetime(int(dt[0]), int(dt[1]), int(dt[2]))

portifolio = float(input('Portifolio:\n\n>>> '))


class Data:
    def __init__(self, index, date):
        self.index = index
        self.date = date
        
    def get(self):
        return web.DataReader(self.index, 'google', self.date)    

    
user_input = input('\n Enter: \n\n [bov] for Bovespa \n\n [dj] for Dow Jones \n\n>>> ' )
while user_input not in ['bov', 'dj']:
    user_input = input('\n Enter: \n\n [bov] for Bovespa \n\n [dj] for Dow Jones \n\n>>> ')

if user_input == 'bov':
    index_list = bov

elif user_input == 'dj':
    index_list = dj

for index in index_list:
    try:
        print('\n\nIndex: {}\n'.format(index))        
        d = Data.get(Data(index, date))
        print(d)
        var = float(d['Close'][0]) - float(d['Open'][0])
        s = portifolio/100/var
        shares = float(portifolio)/float(d['Open'][0])
        print('\nDaily variation: {:.2f}'.format(var))
        print('\nBuy {:.2f} shares to 1% risk'.format(s))
        print('\nMax shares to buy (using total portifolio): {:.2f}'.format(shares))
        print('\nProfit: {:.2f}'.format(shares*var))
        print('\n')
    except:
        print('\n\nNot possible to get data for {}\n'.format(index))
