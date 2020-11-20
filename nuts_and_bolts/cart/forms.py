from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email


class CartForm(FlaskForm):
    email = StringField('Email Address', validators=[
        Email(message=('Not a valid email address.')),
        DataRequired()])
    checkout = SubmitField('Checkout')
    clear_cart = SubmitField('Clear Cart')
