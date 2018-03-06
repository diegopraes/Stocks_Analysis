# Sotck Analysis
# =============================================================================
# Analysis of stocks data: data plot, rolling mean, returns, correlation.
# Database connection pool and table query and construction.
# Realtime data of stocks values and shares to buy.
# =============================================================================
"""
Created on Sun Mar  4 17:50:47 2018   @author: DiegoPraes
"""
# BOVESPA:
# 'BBAS3', 'ABEV3', 'PETR3', 'ITUB4', 'USIM5','VALE3', 'GGBR4', 'EMBR3', 'ELET3',
# 'SUZB5', 'RENT3', 'NATU3', 'MRVE3'

# DOW JONES:
# 'XOM', 'AAPL', 'MCD', 'KO', 'CVX', 'BA', 'CAT', 'IBM', 'MMM', 'WMT', 'V', 'NKE'

def menu():
    print('==================================================================')
    print('Stocks Analysis Python')
    print('==================================================================')
    print('\nMenu():')
    
    user_input = input(" 'r' real time data\n\n 'a' to correlation analysis\n\n 'd' to database access\n\n 'q' to quit\n\n>>> ")
    
    while user_input not in ['r', 'a', 'd', 'q']:
        user_input = input("\n 'r' real time data\n\n 'a' to correlation analysis\n\n 'd' to database access\n\n 'q' to quit\n\n>>> ")
    
    if user_input != 'q':   
        if user_input == 'r':
            import realtime
        
        elif user_input == 'a':
            import analysis
        
        elif user_input == 'd':
            from database import database_access
            database_access()
            
menu()
