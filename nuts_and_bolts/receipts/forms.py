from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired


class FindOrdersForm(FlaskForm):
    email = StringField('Email address', validators=[DataRequired()])
    search = SubmitField('Search')
