import pyodbc

print('101')

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LPOL250044;'
                      'Database=test;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT TOP (1000) [Id],[Name],[Password] FROM [test].[dbo].[Table]')

for row in cursor:
    print(row)