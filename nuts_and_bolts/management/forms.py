from flask_wtf import FlaskForm
from wtforms import StringField, TextField, IntegerField, DecimalField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError
from nuts_and_bolts.models import Products
from nuts_and_bolts import db


def check_name(form, field):
    if db.session.query(Products.name).filter_by(name=field.data).scalar() is not None:
        raise ValidationError('Name must be unique')


def check_sku(form, field):
    if len(field.data) != 9:
        raise ValidationError(
            'SKU must be 9 digits long and not start with 0.')
    if db.session.query(Products.sku).filter_by(sku=field.data).scalar() is not None:
        raise ValidationError('SKU must be unique.')


def check_price(form, field):
    if len(field.data.rsplit('.')[-1]) != 2:
        raise ValidationError('Price must have 2 decimal places.')


def check_quantity(form, field):
    try:
        int(field.data)
    except:
        raise ValidationError('Quantity must be a number.')
    if int(field.data) < 0:
        raise ValidationError('Quantity must be a positive number.')


class InventoryForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), check_name])
    description = TextField('Description', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired(), check_price])
    sku = StringField('sku', validators=[DataRequired(), check_sku])
    quantity = StringField('Quantity', validators=[
                           DataRequired(), check_quantity])
    submit = SubmitField('Submit')
