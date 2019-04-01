from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationFrom(FlaskForm):
  username = StringField('Username', validators=[DataRequired(),Length(min=2, max=20)])

  email = StringField('Email',validators=[DataRequired(), Email()] )

  password = PasswordField('Password', validators=[DataRequired()])

  confirmPassword = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

  submit = SubmitField('Sign Up')

class LoginFrom(FlaskForm):
  email = StringField('Email',validators=[DataRequired(), Email()] )

  password = PasswordField('Password', validators=[DataRequired()])
  remember = BooleanField('Remember Me')
  submit = SubmitField('Sign Up')