from collections.abc import Sequence
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from books_ecommerce.models import Users




class RegisterForm(FlaskForm):
   
    username = StringField('Username', validators=[DataRequired()])
    password1 = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Confirm Password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Register')
    
    def validate_username(self, username_to_check):
        user = Users.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('That username already exists!!!. Please choose a different one.')
    
    def validate_email(self, email_to_check):
        email = Users.query.filter_by(email=email_to_check.data).first()
        if email:
            raise ValidationError('That email is already in use. Please choose a different one.')
    
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')  

class PurchaseBookForm(FlaskForm):
    submit = SubmitField('Purchase Book')