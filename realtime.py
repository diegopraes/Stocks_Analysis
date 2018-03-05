# Creat DATABASE of Stocks shares to buy ( 1% risk ) in real time
"""
Created on Sun Mar 4 12:44:45 2018 @author: DiegoPraes
"""

import datetime
from pandas_datareader import data as web

bov = ['BBAS3', 'ABEV3', 'PETR3', 'ITUB4', 'USIM5','VALE3', 'GGBR4', 'EMBR3', 'ELET3', 'SUZB5', 'RENT3', 'NATU3', 'MRVE3']
dj = ['XOM', 'AAPL', 'MCD', 'KO', 'CVX', 'BA', 'CAT', 'IBM', 'MMM', 'WMT', 'V', 'NKE']


start = input('Enter the initial date [YYYY, MM, DD]:\n\n>>> ')
end = input('Enter the final date [YYYY, MM, DD]:\n\n>>> ')
st = start.split(',')
nd = end.split(',')
start_date = datetime.datetime(int(st[0]), int(st[1]), int(st[2]))
end_date = datetime.datetime(int(nd[0]), int(nd[1]), int(nd[2]))

portifolio = float(input('Portifolio:\n\n>>> '))


class Data:
    def __init__(self, index, start, end):
        self.index = index
        self.start = start
        self.end = end
        
    def get(self):
        return web.DataReader(self.index, 'google', self.start, self.end)    

    
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
        print(Data.get(Data(index, start_date, end_date)))
        d = Data.get(Data(index, start_date, end_date))
        print('\nShares to buy [start date]:\n')
        print(portifolio/100/(float(d['Close'][0]) - float(d['Open'][0])))
        print('\n')
        print('Shares to buy [end date]:\n')
        print(portifolio/100/(float(d['Close'][1]) - float(d['Open'][1])))
        print('\n')
    except:
        print('\n\nNot possible to get data for {}\n'.format(index))
