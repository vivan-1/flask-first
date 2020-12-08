from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, Length, ValidationError, EqualTo
from wtforms import SubmitField, StringField, PasswordField
from apps.login.models import User


def email_exists(form, field):
    email = User.query.filter_by(email=field.data).first()
    if email:
        raise ValidationError('email already exists')

class regiteration(FlaskForm):
    name = StringField('enter the name', validators=[DataRequired(), Length(3,20,message='should be between 3 to 50 characters')])
    email = StringField('enter the email', validators=[DataRequired(), Email(), email_exists])
    password = PasswordField('enter the password', validators=[EqualTo('confirm', message='should be equal to password')])
    confirm = PasswordField('enter the password again', validators=[DataRequired()])
    submit = SubmitField('submit')

class loginform(FlaskForm):
    email = StringField('enter the email', validators=[DataRequired()])
    password = PasswordField('enter the password', validators=[DataRequired()])
    submit = SubmitField('submit')