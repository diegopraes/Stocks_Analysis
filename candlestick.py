from pandas_datareader import data as web
from matplotlib.finance import candlestick2_ohlc
import matplotlib.pyplot as plt
import datetime as datetime


def candlestick():    
    
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
    
    start = input('Enter the initial date [YYYY, MM, DD]:\n\n>>> ')
    dt = start.split(',')
    start = datetime.datetime(int(dt[0]), int(dt[1]), int(dt[2]))    
    
    end = input('Enter the end date [YYYY, MM, DD]:\n\n>>> ')
    st = end.split(',')
    end = datetime.datetime(int(st[0]), int(st[1]), int(st[2]))
    
    # dateRange = pd.date_range(start, end, freq='D')
    
    
    quotes = Data.get(Data(index, start, end))    
    
    fig, ax = plt.subplots(figsize=(8,6))
    candlestick2_ohlc(ax, quotes['Open'], quotes['High'], quotes['Low'], quotes['Close'], width=0.6)
    plt.xticks(rotation = 45)
    plt.title('Stock Index {}'.format(index))
    plt.xlabel('Days in period [{} - {}]'.format(start, end))
    plt.ylabel('{} Price'.format(index))
    
    plt.show()



def candlestick_rol_mean():    
    
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
    
    start = input('Enter the initial date [YYYY, MM, DD]:\n\n>>> ')
    dt = start.split(',')
    start = datetime.datetime(int(dt[0]), int(dt[1]), int(dt[2]))    
    
    end = input('Enter the end date [YYYY, MM, DD]:\n\n>>> ')
    st = end.split(',')
    end = datetime.datetime(int(st[0]), int(st[1]), int(st[2]))
    
    # dateRange = pd.date_range(start, end, freq='D')
    
    column = input('Define values to Moving Average [ Open, Close, High or Low ]:\n\n>>> ')
    
    if int(dt[1])-2 < 0:
        month = 1
    else:
        month = int(dt[1])-2
    quotes_total = Data.get(Data(index, datetime.datetime(int(dt[0]),month,int(dt[2])), end))
    quotes = Data.get(Data(index, start, end))
    
    window1 = int(input('Enter the moving average window 1:\n\n>>> '))
    quotes['MA{}'.format(window1)] = quotes_total[column].rolling(window1).mean()
    window2 = int(input('Enter the moving average window 2:\n\n>>> '))
    quotes['MA{}'.format(window2)] = quotes_total[column].rolling(window2).mean()
    
    quotes['MA10'] = quotes_total[column].rolling(10).mean()
    
    quotes.reset_index(inplace=True)
    
    fig, ax = plt.subplots(figsize=(8,6))
    plt.xticks(rotation = 45)
    plt.title('Stock Index {}'.format(index))
    plt.xlabel('Days in period [{} - {}]'.format(start, end))
    plt.ylabel('{} Price'.format(index))
    
    candlestick2_ohlc(ax, quotes['Open'], quotes['High'], quotes['Low'], quotes['Close'], width=0.6)
    quotes['MA{}'.format(window1)].plot(ax=ax)
    quotes['MA{}'.format(window2)].plot(ax=ax)
    quotes['MA10'].plot(ax=ax)
    
    plt.legend(['Rolling Mean {} days'.format(window1), 'Rolling Mean {} days'.format(window2)], loc='upper left')    
    plt.show()
