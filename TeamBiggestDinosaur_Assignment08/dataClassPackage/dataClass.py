# dataClass.py
# Name: TeamBiggestDinosaur (Harsh Shah, Ian Cunninghan, and Elizabeth Stapelton)
# email: shahh4@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date: 03/28/2024
# Course/Section: IS4010-002
# Semester/Year: Spring 2024
# Brief Description of the assignment: It prints the data from grocery store stimulator database online. 
# Anything else that's relevant: Used worked done in class as a reference. 

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
    
    