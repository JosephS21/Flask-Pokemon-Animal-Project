from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Email

class PokemonCatcherForm(FlaskForm):
    pokemon_name =StringField('Pokemon Name', validators=[DataRequired()], render_kw={'autofocus':True})
    submit = SubmitField("Catch Pokemon")


class RegisterForm(FlaskForm):
    username = StringField('Username', validators= [DataRequired()])
    email = StringField('Email', validators =[DataRequired(), Email()])
    password = PasswordField('Password', validators= [DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators= [DataRequired(), EqualTo('password', message='Passwords must match!')])
    submit = SubmitField('Register')

class LoginInForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me= BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class BlogForm(FlaskForm):
    blogblock = TextAreaField('', validators=[DataRequired()])
    submit = SubmitField('Submit Post')





