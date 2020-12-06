from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, HiddenField
from wtforms.validators import DataRequired, ValidationError
from nuts_and_bolts.models import Product
from nuts_and_bolts import db


def check_name(form, field):
    product = db.session.query(Product).filter_by(id=form.id.data).first()
    if product:
        if (product.name != field.data and
                db.session.query(Product.name).filter_by(name=field.data).scalar() is not None):
            raise ValidationError('Name must be unique')
    else:
        if db.session.query(Product.name).filter_by(name=field.data).scalar() is not None:
            raise ValidationError('Name must be unique')


def check_sku(form, field):
    if len(field.data) != 9:
        raise ValidationError(
            'SKU must be 9 digits long and not start with 0.')
    product = db.session.query(Product).filter_by(id=form.id.data).first()
    if product:
        if (str(product.sku) != field.data and
                db.session.query(Product.sku).filter_by(sku=field.data).scalar() is not None):
            raise ValidationError('SKU must be unique.')
    else:
        if db.session.query(Product.sku).filter_by(sku=field.data).scalar() is not None:
            raise ValidationError('SKU must be unique.')


def check_price(_, field):
    if '.' not in field.data or len(field.data.rsplit('.')[-1]) != 2:
        raise ValidationError('Price must have 2 decimal places.')


def check_quantity(_, field):
    try:
        int(field.data)
    except:
        raise ValidationError('Quantity must be a number.')
    if int(field.data) < 0:
        raise ValidationError('Quantity must be a positive number.')


class InventoryForm(FlaskForm):
    id = HiddenField('ID')
    name = StringField('Name', validators=[DataRequired(), check_name])
    description = TextAreaField('Description', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired(), check_price])
    sku = StringField('sku', validators=[DataRequired(), check_sku])
    quantity = StringField('Quantity', validators=[
                           DataRequired(), check_quantity])
    submit = SubmitField('Submit')
