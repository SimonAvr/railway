import pyodbc

print('101')

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LPOL250044;'
                      'Database=railway;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT TOP (1000) [user_id],[first_name],[password] FROM [railway].[dbo].[user]')


row = cursor.fetchone()
print('name:', row[1])

#result = cursor.fetchall()

#for row in cursor:
#    print(row)