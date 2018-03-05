import psycopg2
from psycopg2 import pool


class Database:
    __connection_pool = None
    
    @classmethod    
    def initialise(cls, **kwargs):
        cls.__connection_pool = pool.SimpleConnectionPool(1, 
                                    10,
                                    **kwargs)
    @classmethod
    def get_connection(cls):
        return cls.__connection_pool.getconn()
    
    @classmethod
    def return_connection(cls, connection):
        Database.__connection_pool.putconn(connection)
        
    @classmethod
    def close_all_connections(cls):
        Database.__connection_pool.closeall()


Database.initialise(database='learning',        # **kwargs
                    host='localhost', 
                    user='postgres', 
                    password='database_password' 
                    )


class CursorFromConnectionFromPool:    
    def __init__(self):
        self.conection = None
        self.cursor = None
        
    def __enter__(self):
        self.connection = Database.get_connection()
        self.cursor = self.connection.cursor()  
        return self.cursor
    
    def __exit__(self, exc_type, exc_val, exc_tb):      # exception(type, value, traceback)	retorna informacoes sobre erros
        if exc_val is not None:
            self.connection.rollback()
        else:            
            self.cursor.close()
            self.connection.commit()
        Database.return_connection(self.connection)


def database_access():
    connection = psycopg2.connect(database = 'learning', user='postgres', password='u6j2p2a3', host='localhost')
    cursor = connection.cursor()
    
    def create_table(table):
        return cursor.execute("CREATE TABLE {} (id SERIAL PRIMARY KEY,stock_index CHARACTER VARYING(255), open_val CHARACTER VARYING(255), close_val CHARACTER VARYING(255))".format(table))
        connection.commit()    
    
    question = input('Create table [yes or no] ?\n\n>>> ')
    while question not in ['yes', 'no']:
        question = input('Create table [yes or no] ?\n\n>>> ')
        

    if question == 'yes':
        table = input('Enter table name:\n\n')
        create_table(table)
        connection.commit()
    
    
    user_input = input("Enter 'a' to add stock Index [name, open, close], 'd' to delete, 'p' to print or 'q' to quit: \n\n>>> ")
    
    while user_input != 'q':
    
        if user_input == 'a':
            table = input('enter table name:\n\n>>>')
            stock = input('enter stock name:\n\n>>>')
            open_val = input('enter open value:\n\n>>>')
            close_val = input('enter close value:\n\n>>>')
            try:
                with CursorFromConnectionFromPool() as cursor:
                    cursor.execute("INSERT INTO {} (stock_index, open_val, close_val) VALUES ('{}', '{}', '{}')".format(table, stock, open_val, close_val))
                    connection.commit()
            except:
                print('\nThis table doesnt exists in database!')
                
        elif user_input == 'd':
            table = input('enter table name:\n\n>>>')
            stock = input('enter stock name:\n\n>>>')
            try:
                with CursorFromConnectionFromPool() as cursor:
                    cursor.execute("DELETE FROM {} WHERE stock_index = '{}';".format(table, stock))
                    connection.commit()
            except:
                print('\nThis table doesnt exists in database!')
                
        elif user_input == 'p':
            table = input('enter table name:\n\n>>>')
            stock = input('enter stock name:\n\n>>>')
            try:
                with CursorFromConnectionFromPool() as cursor:
                    cursor.execute("SELECT * FROM {} WHERE stock_index = '{}';".format(table, stock))
                    stock_data = cursor.fetchone()
                    print('\n\n>>> stock Index: {}, Open Value: {}, Close Value: {}\n\n'.format(stock_data[1], stock_data[2], stock_data[3]))
                    connection.commit()
            except:
                print('\nThis table or column doesnt exists in database!')       
        
            
        user_input = input("Enter 'a' to add stock Index [name, open, close], 'd' to delete, 'p' to print or 'q' to quit: \n\n>>> ")
        
database_access()