from datetime import datetime
from app import db,login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config


class User():

    phone_number = ''
    mail =''
    age =''
    password =''
    gender =''
    last_name = ''
    first_name = ''

    def __init__(self,first_name,last_name,gender,age,mail,password, phone_number):
        self.first_name =first_name
        self.last_name =last_name
        self.age = age
        self.mail = mail
        self.phone_number = phone_number
        self.password = hash(password)

        if gender == 'Male':
            self.gender = '1'
        else:
            self.gender = '0'
    
    
    def insertUser(self):
        Config.cursor.execute("INSERT INTO [railway].[dbo].[user] ([mail],[password],[first_name], [last_name], [gender],[age], [phone_number]) VALUES ('"+ str(self.mail) +"','"+str(self.password)+"','"+ str(self.first_name)+"','"+ str(self.last_name) +"',"+ str(self.gender)+","+str(self.age)+","+ str(self.phone_number)+");")
        Config.cursor.commit()

    def __repr__(self):
        return '<User {}>'.format(self.username)


    def check_password(mail,password):
        Config.cursor.execute("SELECT * FROM [railway].[dbo].[user] WHERE [mail] LIKE '"+ str(mail) +"' AND [password] LIKE '"+ str(hash(password))+"'")
        user = Config.cursor.fetchone()
        if user is None:
            print('null')

        return user


@login.user_loader
def load_user(id):
    return User.query.get(int(id))