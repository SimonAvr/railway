import os
import pyodbc

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'test'

    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LPOL250044;'
                      'Database=railway;'
                      'Trusted_Connection=yes;')
    cursor = conn.cursor() 
    SQLALCHEMY_DATABASE_URL = cursor
    SQLALCHEMY_TRACK_MODIFICATIONS = False