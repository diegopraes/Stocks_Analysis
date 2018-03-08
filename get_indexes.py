# Creat DATABASE of Stocks shares to buy ( 1% risk ) in real time
"""
Created on Sun Mar 4 12:44:45 2018 @author: DiegoPraes
"""

import datetime
from pandas_datareader import data as web
import matplotlib.pyplot as plt
import numpy as np


def data_index():
    
    class Data_synt:  
        def __init__(self, index, date):
            self.index = index
            self.date = date
            
        def get(self):
            return web.DataReader(self.index, 'google', self.date)   
    
    index = input('\nEnter the Index:\n\n>>> ')
    date = input('Enter the date [YYYY, MM, DD]:\n\n>>> ')
    dt = date.split(',')
    date = datetime.datetime(int(dt[0]), int(dt[1]), int(dt[2]))    
    portifolio = float(input('\nEnter the Portifolio Value:\n\n>>> '))
    
    try:
        ds = Data_synt.get(Data_synt(index, date))        
        var = float(ds['Close'][0]) - float(ds['Open'][0])
        s = abs(portifolio/100/var)
        shares = float(portifolio)/float(ds['Open'][0])
        print('\n\nIndex: {}\n'.format(index))
        print(ds)
        print('\n\ndate: {}'.format(date))
        print('\n\nPortifolio: R$ {:.2f}'.format(portifolio))
        print('\n>>> Risk : {:.2f}'.format(abs(s*var)))
        print('\n>>> Daily variation: {:.2f}'.format(var))        
        print('\n>>> Shares to buy (1% risk): {:.2f}'.format(s))        
        print('\n>>> Profit: {:.2f}'.format(s*var))
        print('\nMax shares to buy (using total portifolio): {:.2f}'.format(shares))
        print('\n>>> Maximum Profit: {:.2f}'.format(shares*var))
        print('\n')
    except:
        print('Error getting data!')


    
def all_index():
    
    class Data_synt:  
        def __init__(self, index, date):
            self.index = index
            self.date = date
            
        def get(self):
            return web.DataReader(self.index, 'google', self.date)
    
    bov = ['BBAS3', 'ABEV3', 'PETR3', 'ITUB4', 'USIM5','VALE3', 'GGBR4', 'EMBR3', 'ELET3', 'SUZB5', 'RENT3', 'NATU3', 'MRVE3']
    dj = ['XOM', 'AAPL', 'MCD', 'KO', 'CVX', 'BA', 'CAT', 'IBM', 'MMM', 'WMT', 'V', 'NKE']
    
    user_input = input('\n Enter: \n\n [bov] for Bovespa \n\n [dj] for Dow Jones \n\n>>> ' )
    while user_input not in ['bov', 'dj']:
        user_input = input('\n Enter: \n\n [bov] for Bovespa \n\n [dj] for Dow Jones \n\n>>> ')
    if user_input == 'bov':
        index_list = bov    
    elif user_input == 'dj':
        index_list = dj
        
    date = input('Enter the date [YYYY, MM, DD]:\n\n>>> ')
    dt = date.split(',')
    date = datetime.datetime(int(dt[0]), int(dt[1]), int(dt[2]))
    
    portifolio = float(input('\nEnter the Portifolio Value:\n\n>>> '))
    
    for index in index_list:
        try:                
            ds = Data_synt.get(Data_synt(index, date))        
            var = float(ds['Close'][0]) - float(ds['Open'][0])
            s = portifolio/100/var
            shares = float(portifolio)/float(ds['Open'][0])
            print('\n\nIndex: {}\n'.format(index))
            print(ds)
            print('\n\ndate: {}'.format(date))
            print('\n\nPortifolio: R$ {:.2f}'.format(portifolio))
            print('\n>>> Risk : {:.2f}'.format(abs(s*var)))
            print('\n>>> Daily variation: {:.2f}'.format(var))        
            print('\n>>> Shares to buy (1% risk): {:.2f}'.format(s))        
            print('\n>>> Profit: {:.2f}'.format(s*var))
            print('\nMax shares to buy (using total portifolio): {:.2f}'.format(shares))
            print('\n>>> Maximum Profit: {:.2f}'.format(shares*var))
            print('\n')
        except:
            print('\n\nNot possible to get data for {}\n'.format(index))
        
        

def plot_index():
    
    class Data:    
        def __init__(self, index, start, date):
            self.index = index
            self.start = start
            self.date = date
            
        def get(self):
            return web.DataReader(self.index, 'google', self.start, self.date)
    
    index = input('\nEnter the Index:\n\n>>> ')        
    
    start = input('Enter the initial date [YYYY, MM, DD]:\n\n>>> ')
    dt = start.split(',')
    start = datetime.datetime(int(dt[0]), int(dt[1]), int(dt[2]))    
    
    end = input('Enter the end date [YYYY, MM, DD]:\n\n>>> ')
    st = end.split(',')
    end = datetime.datetime(int(st[0]), int(st[1]), int(st[2]))   

    d = Data.get(Data(index, start, end))
    
    plt.figure(figsize=(8, 6))        
    plt.title('Stock Market {}'.format(index))
    for col in ['Open', 'Close', 'High', 'Low']:
        d[col].plot(subplots=False, grid=True, figsize=(8, 6))
    plt.legend(['Open', 'Close', 'High', 'Low'])
    
    plt.figure(figsize=(8, 3))
    plt.title('Stock Market {} Trade Volume'.format(index))   
    plt.bar(np.arange(len(d['Volume'])), d['Volume'])
    plt.figure()
    (d['Close'][:]-d['Open'][:]).plot(subplots=False, grid=True, style='g', figsize=(8, 6))
    plt.title('Stock Market {} Daily Variation'.format(index))                      


def rol_mean():
    
    class Data:    
        def __init__(self, index, start, date):
            self.index = index
            self.start = start
            self.date = date
            
        def get(self):
            return web.DataReader(self.index, 'google', self.start, self.date)


    class rol_mean_plot:
        def __init__(self, data, window):
            self.data = data
            self.window = window    
           
        def rol_mean(self):
            return self.data.rolling(window=self.window).mean().plot(subplots=False, 
                                    grid=True, figsize=(8, 6)) 
            
        def plot(y, window):
            rol_mean_plot.rol_mean(rol_mean_plot(y, window))
    
    
    index = input('\nEnter the Index:\n\n>>> ')        
    column = input('Define Plot: [ Open, Close, High or Low ]:\n\n>>> ')
    
    start = input('Enter the initial date [YYYY, MM, DD]:\n\n>>> ')
    dt = start.split(',')
    start = datetime.datetime(int(dt[0]), int(dt[1]), int(dt[2]))    
    
    end = input('Enter the end date [YYYY, MM, DD]:\n\n>>> ')
    st = end.split(',')
    end = datetime.datetime(int(st[0]), int(st[1]), int(st[2]))
    
    v = int(dt[1]) - 1
    if v < 1:
        month = 1
    else:
        month = int(dt[1])-2
    d_total = Data.get(Data(index, datetime.datetime(int(dt[0]), month,int(dt[2])), end))
    d = Data.get(Data(index, start, end))    
    data = d[column]
    data.plot(subplots=False, grid=True, style='r', figsize=(8, 6))
    plt.title('Stock Market {} Index'.format(index))
    
    window1 = int(input('Enter the moving average window 1:\n\n>>> '))
    rol_mean_plot.plot(d_total[column], window1)
    
    window2 = int(input('Enter the moving average window 2:\n\n>>> '))
    rol_mean_plot.plot(d_total[column], window2)
    
    plt.legend(['Data', 'Rolling Mean {} days'.format(window1), 'Rolling Mean {} days'.format(window2)], loc='best')
    plt.show()



def regr_index():
    
    class Data:    
        def __init__(self, index, start, date):
            self.index = index
            self.start = start
            self.date = date
            
        def get(self):
            return web.DataReader(self.index, 'google', self.start, self.date)
    
    index = input('\nEnter the Index:\n\n>>> ')
    column = input('Define Plot: [ Open, Close, High or Low ]:\n\n>>> ')
    
    start = input('Enter the initial date [YYYY, MM, DD]:\n\n>>> ')
    dt = start.split(',')
    start = datetime.datetime(int(dt[0]), int(dt[1]), int(dt[2]))    
    
    end = input('Enter the end date [YYYY, MM, DD]:\n\n>>> ')
    st = end.split(',')
    end = datetime.datetime(int(st[0]), int(st[1]), int(st[2]))    

    d = Data.get(Data(index, start, end))

    data = d[column].tolist()
    data_array = np.array(data)        
    x = []
    i = 0            
    while len(x) < len(data):
        x.append(i+1)
        i = i+1
        
    try:
        fit = np.polyfit(x, data_array, deg=1)
        fit_fn = np.poly1d(fit)            
        
        plt.figure(num=None, figsize=(7, 5), dpi=80, facecolor='w', edgecolor='k')
        plt.plot(x, data_array, 'o', x, fit_fn(x), '-')
        plt.legend(['Data', ' Regression'], loc='best')
        plt.xlabel('Days in period [{} - {}]'.format(start, end))
        
        plt.ylabel('{} Returns'.format(index))
        plt.title('Returns Linear Regression: \n\n y = {:.5f} * x + {:.5f}'.format(fit[0],fit[1]))            
    except:
        print('Regression error!')





