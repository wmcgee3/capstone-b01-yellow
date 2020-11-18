from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email

class QuestionsForm(FlaskForm):
    subject = SelectField('Subject: ', choices=[('Order Status'), ('Order Cancelation'), ('Current Order'), ('Current Promotions'), ('Product Warranty'), ('Website Errors'), ('Other')])
    text = TextAreaField('Enter text here: ', validators=[DataRequired()])
    email = StringField('Email: ', [
        Email(message=('Not a valid email address.')),
        DataRequired()])
    submit = SubmitField('Submit')
