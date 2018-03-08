import datetime
from pandas_datareader import data as web
import matplotlib.pyplot as plt
import numpy as np

bov = ['BBAS3', 'ABEV3', 'PETR3', 'ITUB4', 'RADL3', 'USIM5','VALE3', 'GGBR4', 'EMBR3', 'ELET3', 'RENT3', 'NATU3', 'MRVE3', 'FIBR', 'CMIG4', 'CPLE6']
dj = ['XOM', 'AAPL', 'MCD', 'KO', 'CVX', 'BA', 'CAT', 'IBM', 'MMM', 'WMT', 'V', 'NKE']

user_input = input('\n Enter: \n\n [bov] for Bovespa \n\n [dj] for Dow Jones \n\n>>> ' )
while user_input not in ['bov', 'dj']:
    user_input = input('\n Enter: \n\n [bov] for Bovespa \n\n [dj] for Dow Jones \n\n>>> ')
if user_input == 'bov':
    index_list = bov    
elif user_input == 'dj':
    index_list = dj   

portifolio = float(input('\nEnter the Portifolio Value:\n\n>>> '))     

start = input('Enter the initial date [YYYY, MM, DD]:\n\n>>> ')
dt = start.split(',')    

end = input('Enter the end date [YYYY, MM, DD]:\n\n>>> ')
st = end.split(',')
        
if user_input == 'bov':
    for i in bov:
        
        start = datetime.datetime(int(dt[0]), int(dt[1]), int(dt[2]))
        end = datetime.datetime(int(st[0]), int(st[1]), int(st[2]))
        
        class Data:    
            def __init__(self, index, start, end):
                self.index = i
                self.start = start
                self.end = end
                
            def get(self):
                return web.DataReader(self.index, 'google', self.start, self.end)
    
        class rol_mean_plot:
            def __init__(self, data, window):
                self.data = data
                self.window = window    
               
            def rol_mean(self):
                return self.data.rolling(window=self.window).mean().plot(subplots=False, 
                                        grid=True, figsize=(8, 6)) 
                
            def plot(y, window):
                rol_mean_plot.rol_mean(rol_mean_plot(y, window))
        
        d = Data.get(Data(i, start, end))
        data = d['Close'].tolist()
        data_array = np.array(data)        
        x = []
        j = 0            
        while len(x) < len(data):
            x.append(j+1)
            j = j+1        
        try:
            fit = np.polyfit(x, data_array, deg=1)
            fit_fn = np.poly1d(fit)                
        except:
            print('Regression error!')
        
        if fit[0] > 0:
            
            class Data_synt:  
                def __init__(self, index, date):
                    self.index = i
                    self.date = end
                    
                def get(self):
                    return web.DataReader(self.index, 'google', self.date)    
            try:
                ds = Data_synt.get(Data_synt(i, end))        
                var = float(ds['Close'][0]) - float(ds['Open'][0])
                s = portifolio/100/var
                shares = float(portifolio)/float(ds['Open'][0])
            except:
                print('Error getting data!')
            
            if s > 100:
                print('\n\nIndex: {}\n'.format(i))
                print(ds)
                print('\n\ndate: {}'.format(end))
                print('\n\nPortifolio: R$ {:.2f}'.format(portifolio))
                print('\n>>> Risk : {:.2f}'.format(abs(s*var)))
                print('\n>>> Daily variation: {:.2f}'.format(var))        
                print('\n>>> Shares to buy (1% risk): {:.2f}'.format(s))        
                print('\n>>> Profit: {:.2f}'.format(s*var))
                print('\n>>> Max shares to buy: {:.2f}'.format(shares))
                print('\n>>> Maximum Profit: {:.2f}'.format(shares*var))
                print('\n')
            
            
            

               
if user_input == 'dj':
    for i in dj:
        
        start = datetime.datetime(int(dt[0]), int(dt[1]), int(dt[2]))
        end = datetime.datetime(int(st[0]), int(st[1]), int(st[2]))
        
        class Data:    
            def __init__(self, index, start, end):
                self.index = i
                self.start = start
                self.end = end
                
            def get(self):
                return web.DataReader(self.index, 'google', self.start, self.end)
    
        class rol_mean_plot:
            def __init__(self, data, window):
                self.data = data
                self.window = window    
               
            def rol_mean(self):
                return self.data.rolling(window=self.window).mean().plot(subplots=False, 
                                        grid=True, figsize=(8, 6)) 
                
            def plot(y, window):
                rol_mean_plot.rol_mean(rol_mean_plot(y, window))
        
        d = Data.get(Data(i, start, end))
        data = d['Close'].tolist()
        data_array = np.array(data)        
        x = []
        j = 0            
        while len(x) < len(data):
            x.append(j+1)
            j = j+1        
        try:
            fit = np.polyfit(x, data_array, deg=1)
            fit_fn = np.poly1d(fit)                
        except:
            print('Regression error!')
        
        if fit[0] > 0:
            
            class Data_synt:  
                def __init__(self, index, date):
                    self.index = i
                    self.date = end
                    
                def get(self):
                    return web.DataReader(self.index, 'google', self.date)    
            try:
                ds = Data_synt.get(Data_synt(i, end))        
                var = float(ds['Close'][0]) - float(ds['Open'][0])
                s = portifolio/100/var
                shares = float(portifolio)/float(ds['Open'][0])
            except:
                print('Error getting data!')
            
            if s > 100:
                print('\n\nIndex: {}\n'.format(i))
                print(ds)
                print('\n\ndate: {}'.format(end))
                print('\n\nPortifolio: R$ {:.2f}'.format(portifolio))
                print('\n>>> Risk : {:.2f}'.format(abs(s*var)))
                print('\n>>> Daily variation: {:.2f}'.format(var))        
                print('\n>>> Shares to buy (1% risk): {:.2f}'.format(s))        
                print('\n>>> Profit: {:.2f}'.format(s*var))
                print('\n>>> Max shares to buy: {:.2f}'.format(shares))
                print('\n>>> Maximum Profit: {:.2f}'.format(shares*var))
                print('\n')
            
