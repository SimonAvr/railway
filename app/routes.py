from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User



@app.route("/")
def hello():
    return "Work"

@app.route("/main")
def main():
    user = {"username" : "Kupi bilet"}
    return render_template('main.html', title = 'Home', user = user)

@app.route("/login", methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        user = User.check_password(request.form['LoginFormEmail'], request.form['LoginFormPassword'])
        if user is None:
            return redirect(url_for('login'))
        return redirect(url_for('user'))
    return render_template('login.html')



@app.route("/registration", methods =['GET', 'POST'])
def registration():

    if request.method == 'POST':
        user = User(str(request.form['RegisterFormFirstName']),str(request.form['RegisterFormLastName']),str(request.form['RegisterFormGender']),str(request.form['defaultRegisterAge']),str(request.form['RegisterFormEmail']),str(request.form['RegisterFormPassword']),str(request.form['RegisterFormPhomeNumber']))
        #print(str(request.form['RegisterFormFirstName']),str(request.form['RegisterFormLastName']),str(request.form['RegisterFormGender']))#,str(request.form['defaultRegisterAge']),str(request.form['RegisterFormEmail']),str(request.form['RegisterFormPassword']),str(request.form['RegisterFormPhomeNumber']))
        #(self,first_name,last_name,gender,age,mail,password,phone_number):
        user.insertUser()
        return redirect(url_for('login'))

    if current_user.is_authenticated:
        return redirect(url_for('main'))
    
    return render_template('registration.html')

@app.route("/user")
def user():
    return render_template('user.html')
if __name__ == "__main__":
    app.run(debug=True)