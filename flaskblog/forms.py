from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User


class Registration(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    confirm_password = PasswordField('confirm_password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_user(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is taken choose different one')

    def validate_email(self, email):
        email = User.query.filter_by(username=email.data).first()
        if email:
            raise ValidationError('Email is taken choose different one')


class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

