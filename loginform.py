from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField, BooleanField, StringField
from wtforms.validators import DataRequired

class Loginform(FlaskForm):
    username  =  StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')
