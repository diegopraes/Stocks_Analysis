# Stock Analysis - CSV
"""
Created on Sat Mar 17 13:14:01 2018 @author: DiegoPraes
"""
from matplotlib.finance import candlestick2_ohlc
import os, csv
import matplotlib.pyplot as plt
import pandas as pd
from pandas_datareader import data as web
import datetime


# MARKET ANALYSIS

def analyse_CSV():

    index = input("Enter the index:")
    st = int(input('Start period:\n\n>>> '))
    end = int(input('End period:\n\n>>> '))

    path = 'C:/Users/Asus/Desktop/PROJETOS/Stocks_Analysis/Data'
    path2 = 'C:/Users/Asus/Desktop/PROJETOS/Stocks_Analysis/Data/newData'

    lines = open('%s/%s.txt' %(path,index), 'r').readlines()
    lines = [line.replace(' ', '') for line in lines]
    new_file = open('%s/%s.txt' %(path2,index), 'w')
    new_file.writelines(lines[1:])
    new_file.close()

    Dat = []
    Ope = []
    Hig = []
    Low = []
    Clo = []
    Vol = []

    for samepath, dirs, files in os.walk(path2):
         with open('{}/{}.txt'.format(path2,index), newline='') as data:
            reader = csv.reader(data, delimiter='\t')
            for linha in reader:
                try:
                    Dat.append(linha[0])
                    Ope.append(float(linha[1]))
                    Hig.append(float(linha[2]))
                    Low.append(float(linha[3]))
                    Clo.append(float(linha[4]))
                    Vol.append(float(linha[5]))
                except:
                    pass

            Datedf = pd.DataFrame({'Date': Dat})
            Opendf = pd.DataFrame({'Open': Ope})
            Highdf = pd.DataFrame({'High': Hig})
            Lowdf = pd.DataFrame({'Low': Low})
            Closedf = pd.DataFrame({'Close': Clo})
            Volumedf = pd.DataFrame({'Volume': Vol})

            quotes = Datedf.join(Opendf)
            quotes = quotes.join(Highdf)
            quotes = quotes.join(Lowdf)
            quotes = quotes.join(Closedf)
            quotes = quotes.join(Volumedf)


    quotes['MA20'] = quotes['Close'].rolling(20).mean()
    quotes['MA40'] = quotes['Close'].rolling(40).mean()
    quotes['MA10'] = quotes['Close'].rolling(10).mean()


    # AVERAGE TRUE RANGE
    a = abs(quotes['Low'][:] - quotes['Close'][:])
    b = abs(quotes['High'][:] - quotes['Close'][:])
    c = abs(quotes['High'][:] - quotes['Low'][:])
    dfa = pd.DataFrame({'a': a})
    dfb = pd.DataFrame({'b': b})
    dfc = pd.DataFrame({'c': c})
    df = dfa.join(dfb)
    df = df.join(dfc)
    ATR = []
    for i in range(len(df)):
        ATR.append(max(df['a'][i], df['b'][i], df['c'][i]))

    ATR = pd.DataFrame({'ATR' : ATR})
    quotes = quotes.join(ATR)
    quotes['ATR_MA'] = ATR.rolling(15).mean()

    quotes = quotes[:][st:end]

    fig = plt.figure(figsize=(14, 8))

    ax = fig.add_subplot(211)
    try:
        ax.plot(candlestick2_ohlc(ax, quotes['Open'], quotes['High'], quotes['Low'], quotes['Close'], width=0.6), quotes['MA20'].plot(ax=ax), quotes['MA40'].plot(ax=ax), quotes['MA10'].plot(ax=ax))
    except:
        pass

    plt.title('{} Price'.format(index))
    # plt.xlabel('Days')
    plt.ylabel('{} Price'.format(index))
    plt.legend(loc='best')

    axATR = fig.add_subplot(212)
    try:
        axATR.plot(axATR, quotes['ATR'].plot(ax=axATR), quotes['ATR_MA'].plot(ax=axATR))
    except:
        pass

    # plt.title('{} Average True Range'.format(index))
    plt.xlabel('Days')
    plt.ylabel('{} Variation Length'.format(index))
    plt.legend(loc='best')

    plt.show()
    
    # fig = plt.show()    
    # fig.savefig('graficos/{}.png'.format(index))




# GET DATA IN GOOGLE FINANCE

def get_CSV():

    class Data:
        def __init__(self, index, start, end):
            self.index = index
            self.start = start
            self.end = end

        def get(self):
            return web.DataReader(self.index, 'google', self.start, self.end)

    bov = ['BBAS3', 'ABEV3', 'PETR3', 'ITUB4', 'RADL3', 'USIM5', 'VALE3', 'GGBR4', 'EMBR3', 'ELET3', 'RENT3', 'NATU3', 'CMIG4', 'GOAU4', 'BTOW3', 'AZUL4', 'CCRO3', 'LREN3', 'IRBR3', 'UGPA3', 'QUAL3', 'BRDT3', 'BBSE3', 'CIEL3', 'BRAP4', 'CSNA3', 'ESTC3', 'SLCE3', 'ELET3', 'LIGT3', 'OIBR3', 'BRML3', 'ENGI11', 'EQTL3', 'DMMO3', 'CVCB3', 'JBSS3', 'VIVT4', 'KLBN11', 'IGTA3', 'SULA11', 'TIMP3', 'CRFB3', 'RAIL3', 'MULT3', 'GOLL4', 'BRKM5', 'SBSP3', 'VVAR11', 'BRSR6', 'BBDC3', 'SANB11', 'FLRY3', 'PCAR4', 'CYRE3', 'MDIA3', 'WEGE3', 'CSAN3', 'CPFE3', 'MPLU3', 'LAME3', 'ECOR3', 'EGIE3', 'PSSA3', 'CSMG3', 'ARZZ3', 'HGTX3', 'TOTS3', 'PARD3']

    start = input('Enter the initial date [YYYY, MM, DD]:\n\n>>> ')
    end = input('Enter the final date [YYYY, MM, DD]:\n\n>>> ')
    st = start.split(',')
    nd = end.split(',')
    start_date = datetime.datetime(int(st[0]), int(st[1]), int(st[2]))
    end_date = datetime.datetime(int(nd[0]), int(nd[1]), int(nd[2]))

    for i in bov:
        dataframe = Data.get(Data(i, start_date, end_date))

        # Save to CVS **Desktop/PROJETOS/Data
        dataframe.to_csv('C:/Users/Asus/Desktop/PROJETOS/Data/{}.txt'.format(i), sep='\t', encoding='utf-8')




def menu():
    print("\nCSV Stocks Analysis Tool\n\n")
    menu = input("\n 'g' to get data \n\n 'a' to analyse\n\n>>> ")
    while menu not in ['g', 'a']:
        menu = input("\n 'g' to get data \n\n 'a' to analyse\n\n>>> ")
    if menu == 'a':
        analyse_CSV()
    elif menu == 'g':
        get_CSV()


menu()
  
