import os 
import sys
import pyodbc
import datetime 
file_sir = os.path.dirname(__file__)
sys.path.append("C:/DataBusiness/avramsimo1a/Desktop/MAB")

from app.models import User
from config import Config
#user = User('wert','wert',1,33,'wert','wert')




#print("INSERT INTO [railway].[dbo].[user] ([mail],[password],[first_name], [last_name], [gender],[age]) VALUES ('"+ str(user.mail) +"','"+str(user.password)+"','"+ str(user.first_name)+"','"+ str(user.last_name) +"',"+ str(user.gender)+","+str(user.age)+");")


#Config.cursor.execute("INSERT INTO [railway].[dbo].[user] ([mail],[password],[first_name], [last_name], [gender],[age]) VALUES ('"+ str(user.mail) +"','"+str(user.password)+"','"+ str(user.first_name)+"','"+ str(user.last_name) +"',"+ str(user.gender)+","+str(user.age)+");")
#Config.cursor.commit()
#INSERT INTO [railway].[dbo].[user] ([mail],[password],[first_name], [last_name], [gender],[age]) VALUES ('+ str(user.mail) +','okopwkep','fer','erf',1,1);


Config.cursor.execute("SELECT * FROM [railway].[dbo].[user] WHERE [mail] LIKE 'kwitel@ gmail.com' AND [password] LIKE '1259755379'")

row = Config.cursor.fetchone()
if row is None:
    print('null')
else:
    print('name:', row[1])