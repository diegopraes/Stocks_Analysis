# Sotck Analysis
# =============================================================================
# Analysis of stocks data: data plot, rolling mean, returns, correlation.
# Database connection pool and table query and construction.
# Realtime data of stocks values and shares to buy.
# =============================================================================
"""
Created on Sun Mar  4 17:50:47 2018   @author: DiegoPraes
"""

def menu():
    print('\n\n\n')
    print('==================================================================')
    print('Stocks Analysis Python')
    print('==================================================================')
    print('\nMenu():')
    
    user_input = input(" 'i' to evaluate 1 Index\n\n 'g' to get index list data\n\n 'p' to plot data\n\n 'm' to plot rolling mean\n\n 'r' to regression \n\n 'a' to correlation analysis\n\n 'd' to database access\n\n 'q' to quit\n\n>>> ")
    
    while user_input not in ['g', 'i', 'p', 'm', 'r', 'a', 'd', 'q']:
        user_input = input(" 'i' to evaluate 1 Index\n\n 'g' to get index list data\n\n 'p' to plot data\n\n 'm' to plot rolling mean\n\n 'r' to regression \n\n 'a' to correlation analysis\n\n 'd' to database access\n\n 'q' to quit\n\n>>> ")
    
    if user_input != 'q':   
        if user_input == 'g':
            from get_indexes import all_index
            all_index()
            
        elif user_input == 'i':
            from get_indexes import data_index
            data_index()
              
        elif user_input == 'p':
            chart_type = input("\n 'c' to candlestick chart \n\n 'n' to normal chart\n\n>>> ")
            while chart_type not in ['c', 'n']:
                chart_type = input("\n 'c' to candlestick chart \n\n 'n' to normal chart\n\n>>> ")
            if chart_type == 'n':
                from get_indexes import plot_index
                plot_index()
            elif chart_type == 'c':
                from candlestick import candlestick            
                candlestick()           
                    
        elif user_input == 'm':
            chart_type = input("\n 'c' to candlestick chart \n\n 'n' to normal chart\n\n>>> ")
            while chart_type not in ['c', 'n']:
                chart_type = input("\n 'c' to candlestick chart \n\n 'n' to normal chart\n\n>>> ")
            if chart_type == 'n':
                from get_indexes import rol_mean
                rol_mean()
            elif chart_type == 'c':
                from candlestick import candlestick_rol_mean            
                candlestick_rol_mean()
            
        elif user_input == 'r':
            from get_indexes import regr_index
            regr_index()            
        
        elif user_input == 'a':
            import analysis
        
        elif user_input == 'd':
            from database import database_access
            database_access()    
    
menu()


# ------------------------------------------------------------------------------
# BOVESPA:
# 'BBAS3', 'ABEV3', 'PETR3', 'ITUB4', 'USIM5', 'VALE3', 'GGBR4', 'EMBR3', 'ELET3',
# 'SUZB5', 'RENT3', 'NATU3', 'MRVE3', 'RADL3'

# DOW JONES:
# 'XOM', 'AAPL', 'MCD', 'KO', 'CVX', 'BA', 'CAT', 'IBM', 'MMM', 'WMT', 'V', 'NKE'

# $$$$
# RADL3




