from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SearchForm():
    text = StringField('Search Terms', validators=[DataRequired()])
    submit = SubmitField('Search')
