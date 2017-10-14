from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
	name = StringField('你叫什么名字？', validators=[DataRequired()])
	submit = SubmitField('提交')
