# dataClass.py
import pyodbc

class Data:

    def Connect(self, myDatabase):
        '''
        Connect to the database and create a cursor
        @return: The cursor object
        '''
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                              'Database=' + myDatabase + ';'
                              'uid=IS4010Login;'
                              'pwd=P@ssword2;')
    
        cursor = conn.cursor()
        return cursor
    
    