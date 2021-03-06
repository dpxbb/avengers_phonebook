from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField 
from wtforms.validators import DataRequired, EqualTo, Email

class UserInfoForm(FlaskForm):
    name = StringField('Name', validators = [DataRequired()])
    phone = StringField('Phone', validators = [DataRequired()])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    confirm_pass = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField()