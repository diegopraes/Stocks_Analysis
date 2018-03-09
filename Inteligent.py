import datetime
from pandas_datareader import data as web
import numpy as np

bov = ['BBAS3', 'ABEV3', 'PETR3', 'ITUB4', 'RADL3', 'USIM5', 'VALE3', 'GGBR4', 'EMBR3', 'ELET3', 'RENT3', 'NATU3', 'CMIG4', 'GOAU4', 'BTOW3', 'AZUL4', 'CCRO3', 'LREN3', 'IRBR3', 'UGPA3', 'QUAL3', 'BRDT3', 'BBSE3', 'CIEL3', 'BRAP4', 'CSNA3', 'ESTC3', 'SLCE3', 'ELET3', 'LIGT3', 'OIBR3', 'BRML3', 'ENGI11', 'EQTL3', 'DMMO3', 'CVCB3', 'JBSS3', 'VIVT4', 'KLBN11', 'IGTA3', 'SULA11', 'TIMP3', 'CRFB3', 'RAIL3', 'MULT3', 'GOLL4', 'BRKM5', 'SBSP3', 'VVAR11', 'BRSR6', 'BBDC3', 'SANB11', 'FLRY3', 'PCAR4', 'CYRE3', 'MDIA3', 'WEGE3', 'CSAN3', 'CPFE3', 'MPLU3', 'LAME3', 'ECOR3', 'EGIE3', 'PSSA3', 'CSMG3', 'ARZZ3', 'HGTX3', 'TOTS3', 'PARD3']

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
    index_list = bov
elif user_input =='dj':
    index_list = dj    

selection = []    

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
            shares = portifolio/100/var
            max_shares = float(portifolio)/float(ds['Open'][0])
            risk = abs(shares*var)
            profit = shares*var
            max_profit = max_shares*var
        except:
            print('Error getting data!')
        
        if shares > 100:
            if max_profit > risk:
                selection.append(i)
                print('\n\n\nIndex: {}\n'.format(i))
                print(ds)
                print('\n\ndate: {}'.format(end))
                print('\n\nPortifolio: R$ {:.2f}'.format(portifolio))
                print('\n>>> Risk : {:.2f}'.format(risk))
                print('\n>>> Daily variation: {:.2f}'.format(var))        
                print('\n>>> Shares to buy (1% risk): {:.2f}'.format(shares))        
                print('\n>>> Profit: {:.2f}'.format(profit))
                print('\n>>> Max shares to buy: {:.2f}'.format(max_shares))
                print('\n>>> Maximum Profit: {:.2f}'.format(max_profit))
                print('\n')

print(selection)

