from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User

class LoginForm(FlaskForm):
	email = StringField('E-mail', validators=[Required(), Length(1, 64), Email(message='无效的E-mail地址')])
	password = PasswordField('密码', validators=[Required()])
	remember_me = BooleanField('记住我')
	submit = SubmitField('登录')

class RegistrationForm(FlaskForm):
	email = StringField('E-mail', validators=[Required(), Length(1, 64), Email(message='无效的E-mail地址')])
	username = StringField('用户名', validators=[Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
	                                                                           '用户名中只能包含字母、数字、\'.\'、\'_\'')])
	password = PasswordField('密码', validators=[Required(), EqualTo('password2', message='密码必须一致')])
	password2 = PasswordField('确认密码', validators=[Required()])
	submit = SubmitField('注册')

def validate_email(self, field):
	if User.query.filter_by(email=field.data).first():
		raise ValidationError('该E-mail已经被注册。')

def validate_username(self, field):
	if User.query.filter_by(username=field.data).first():
		raise ValidationError('该用户名已经被注册。')


