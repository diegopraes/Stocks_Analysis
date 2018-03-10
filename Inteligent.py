import datetime
from pandas_datareader import data as web
import numpy as np
from matplotlib.finance import candlestick2_ohlc
import matplotlib.pyplot as plt


bov = ['BBAS3', 'ABEV3', 'PETR3', 'ITUB4', 'RADL3', 'USIM5', 'VALE3', 'GGBR4', 'EMBR3', 'ELET3', 'RENT3', 'NATU3', 'CMIG4', 'GOAU4', 'BTOW3', 'AZUL4', 'CCRO3', 'LREN3', 'IRBR3', 'UGPA3', 'QUAL3', 'BRDT3', 'BBSE3', 'CIEL3', 'BRAP4', 'CSNA3', 'ESTC3', 'SLCE3', 'ELET3', 'LIGT3', 'OIBR3', 'BRML3', 'ENGI11', 'EQTL3', 'DMMO3', 'CVCB3', 'JBSS3', 'VIVT4', 'KLBN11', 'IGTA3', 'SULA11', 'TIMP3', 'CRFB3', 'RAIL3', 'MULT3', 'GOLL4', 'BRKM5', 'SBSP3', 'VVAR11', 'BRSR6', 'BBDC3', 'SANB11', 'FLRY3', 'PCAR4', 'CYRE3', 'MDIA3', 'WEGE3', 'CSAN3', 'CPFE3', 'MPLU3', 'LAME3', 'ECOR3', 'EGIE3', 'PSSA3', 'CSMG3', 'ARZZ3', 'HGTX3', 'TOTS3', 'PARD3']
    
dj = ['XOM', 'AAPL', 'MCD', 'KO', 'CVX', 'BA', 'CAT', 'IBM', 'MMM', 'WMT', 'V', 'NKE']      

user_input = input('\n Enter: \n\n [bov] for Bovespa \n\n [dj] for Dow Jones \n\n>>> ' )
while user_input not in ['bov', 'dj']:
    user_input = input('\n Enter: \n\n [bov] for Bovespa \n\n [dj] for Dow Jones \n\n>>> ')
if user_input == 'bov':
    index_list = bov    
elif user_input == 'dj':
    index_list = dj 
    
if user_input == 'bov':
    index_list = bov
elif user_input =='dj':
    index_list = dj 

portifolio = float(input('\nEnter the Portifolio Value:\n\n>>> '))
    
start = input('Enter the initial date [YYYY, MM, DD]:\n\n>>> ')
dt = start.split(',')    

end = input('Enter the end date [YYYY, MM, DD]:\n\n>>> ')
st = end.split(',')

selection = []
possible_to_buy = []
up_trend = []
signal = []
    
for i in index_list:         
    
    start = datetime.datetime(int(dt[0]), int(dt[1]), int(dt[2]))
    end = datetime.datetime(int(st[0]), int(st[1]), int(st[2]))
    
    class Data:    
        def __init__(self, index, start, end):
            self.index = i
            self.start = start
            self.end = end
            
        def get(self):
            return web.DataReader(self.index, 'google', self.start, self.end)

    
    d = Data.get(Data(i, datetime.datetime(2009,1,1), end))
    data = d['Close'].tolist()
    data_array = np.array(data)        
    x = []
    j = 0            
    while len(x) < len(data):
        x.append(j+1)
        j = j+1        
    try:
        fit_all = np.polyfit(x, data_array, deg=1)
        fit_fn = np.poly1d(fit_all)                
    except:
        print('Regression error!')     
       
    
    if fit_all[0] > 0:       
        
        class Data_synt:  
            def __init__(self, index, date):
                self.index = i
                self.date = end
                
            def get(self):
                return web.DataReader(self.index, 'google', self.date)    
        try:
            ds = Data_synt.get(Data_synt(i, end))
        except:
            print('\nError in ds!')
            
        var = float(ds['Close'][0]) - float(ds['Open'][0])
        if var != 0:
            shares = portifolio/100/var
        else:
            print('\nNo variation!')
            pass
        
        max_shares = float(portifolio)/float(ds['Open'][0])
        risk = abs(shares*var)
        profit = shares*var
        max_profit = max_shares*var
            
        try:
            d = Data.get(Data(i, start, end))
            predict = min(d['Close'][:])
        except:
            print('\nError in d!')
            
        predict_var = predict - float(ds['Open'][0])         
        predict_shares = portifolio/100/abs(predict_var)
        predict_max_loss = max_shares*predict_var                   
        
        if shares > 100:
            possible_to_buy.append(i)
            
            if max_profit > 0:
                    up_trend.append(i)
            
            if max_profit > risk:
                selection.append(i)
                try:
                    print('\n\n\n\n\nIndex: {}\n'.format(i))
                    print(ds)
                    print('\n\ndate: {}'.format(end))
                    print('\n\nPortifolio: R$ {:.2f}'.format(portifolio))
                    print('\n>>> 1 % : {:.2f}'.format(portifolio/100))
                    print('\n>>> Day variation: {:.2f}'.format(var))        
                    print('\n>>> Shares to buy (1% risk): {:.2f}'.format(shares)) 
                    print('\n>>> Risk : {:.2f}'.format(risk))
                    print('\n>>> Profit: {:.2f}'.format(profit))
                    print('\n>>> Max shares to buy: {:.2f}'.format(max_shares))
                    print('\n>>> Maximum Profit: {:.2f}'.format(max_profit))
                    print('\n')
                    print('\n Minimum Close Value: {}'.format(predict))
                    print('\n Worst Prediction:')                                
                    print('\n>>> Maximum variation: {:.2f}'.format(predict_var))        
                    print('\n>>> Shares to buy (1% risk): {:.2f}'.format(predict_shares))
                    print('\n>>> Maximum Loss: {:.2f}'.format(predict_max_loss))
                except:
                    print('Error')
                    continue

    d = Data.get(Data(i, start, end))
    data = d['Close'].tolist()
    data_array = np.array(data)        
    x = []
    j = 0            
    while len(x) < len(data):
        x.append(j+1)
        j = j+1        
    try:
        fit_last = np.polyfit(x, data_array, deg=1)
        fit_fn = np.poly1d(fit_last)                
    except:
        print('Regression error!')     
    
    if fit_last[0] < 0:
        d['MA10'] = d['Close'].rolling(10).mean() 
        n = int(len(d))-1
        if d['Close'][n] > d['MA10'][n]:
            signal.append(i)                

print('\n\n\nSelection: {}'.format(selection))              # up, +100 shares, profit > risk
print('\nPossible to buy: {}'.format(possible_to_buy))      # up, +100 shares
print('\nUp Trend: {}'.format(up_trend))                    # up, +100 shares, profit > 0
print('\nSignal: {}'.format(signal))                        # up, MA10 > Price




option = input("\nPlot the selected Indexes chart ?\n\n 'y' for yes\n\n 'n' for no\n\n>>> ")
while option not in ['y', 'n']:
    option = input("\nPlot the selected Indexes chart ?\n\n 'y' for yes\n\n 'n' for no\n\n>>> ")

if option == 'y':
    for i in signal:
    
        class Data:    
            def __init__(self, index, start, date):
                self.index = i
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
        
          
        if int(dt[1])-2 < 0:
            month = int(dt[1]) + 8
            year = int(dt[0]) - 1
        else:
            month = int(dt[1])-3
            year = int(dt[0])
        quotes_total = Data.get(Data(i, datetime.datetime(year,month,int(dt[2])), end))
        quotes = Data.get(Data(i, start, end))
        
    
        quotes['MA20'] = quotes_total['Close'].rolling(20).mean()
    
        quotes['MA40'] = quotes_total['Close'].rolling(40).mean()    
        
        quotes['MA10'] = quotes_total['Close'].rolling(10).mean()     
        
        
        quotes.reset_index(inplace=True)        
        
        fig, ax = plt.subplots(figsize=(10, 4))
        plt.xticks(rotation = 45)
        plt.title('Stock Index {}'.format(i))
        plt.xlabel('Days in period [{} - {}]'.format(start, end))
        plt.ylabel('{} Price'.format(i))
        
        candlestick2_ohlc(ax, quotes['Open'], quotes['High'], quotes['Low'], quotes['Close'], width=0.6)
        quotes['MA20'].plot(ax=ax)
        quotes['MA40'].plot(ax=ax)
        quotes['MA10'].plot(ax=ax)
        
        
        plt.legend('Rolling Mean 20 days', 'Rolling Mean 40 days', loc='upper left')    
        plt.show()
elif option == 'n':
    pass
