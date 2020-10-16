from flask_wtf import FlaskForm
from wtforms import StringField, TextField, IntegerField, DecimalField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError
from nuts_and_bolts.models import Products
from nuts_and_bolts import db

def sku_check(form, field):
    if len(str(field.data)) != 9:
        raise ValidationError('sku must be 9 digits long!')

def addproduct(name,desc,price,sku,quantity):
    addition = Products(
    name = name,
    description = desc,
    price = price,
    sku = sku,
    quantity = quantity,
    )

    db.session.add(addition)
    db.session.commit()
    
class InventoryForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextField('Description', validators=[DataRequired()])
    price = DecimalField('Price', places=2, validators=[DataRequired()])
    sku = IntegerField('sku', validators=[DataRequired(), sku_check])
    quantity = IntegerField('Quantity', validators=[DataRequired(), NumberRange(min=1, max=10000, message='quantity must be between 1 and 10,000')])
    submit = SubmitField('Submit')

    