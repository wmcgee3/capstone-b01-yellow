from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email


class QuestionsForm(FlaskForm):
    subject = SelectField('Subject: ', choices=[('Order Status', 'Order Status'), ('Order Cancelation', 'Order Cancelation'),
                                                ('Current Order', 'Current Order'), (
                                                    'Current Promotions', 'Current Promotions'),
                                                ('Product Warranty', 'Product Warranty'), ('Website Errors', 'Website Errors'), ('Other', 'other')])
    text = TextAreaField('Enter text here: ', validators=[DataRequired()])
    email = StringField('Email: ', validators=[
        Email(message=('Not a valid email address.')),
        DataRequired()])
    submit = SubmitField('Submit')
