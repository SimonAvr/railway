from flask_wtf import FlaskForm
from wtforms import*
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    mail = StringField('mail', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class RegistrationForm(FlaskForm):
    mail = StringField('mail', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    