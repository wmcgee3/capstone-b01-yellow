from nuts_and_bolts.main.routes import clear_cart
from flask.app import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class CartForm(FlaskForm):
    email = StringField('Email Address')
    checkout = SubmitField('Checkout')
    clear_cart = SubmitField('Clear Cart')
