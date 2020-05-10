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
        print(request.form['LoginFormEmail'] + request.form['LoginFormPassword'])

    return render_template('login.html')



@app.route("/registration", methods =['GET', 'POST'])
def registration():
    if request.method == 'POST':
        print(request.form['RegisterFormFirstName'] + '  emdowoifnwioefnweoifnoeiwfjoi')

    return render_template('registration.html')

@app.route("/user")
def user():
    return render_template('user.html')
if __name__ == "__main__":
    app.run()