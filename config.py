import os
import pyodbc

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'test'

    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LPOL250044;'
                      'Database=test;'
                      'Trusted_Connection=yes;')
    cursor = conn.cursor() 