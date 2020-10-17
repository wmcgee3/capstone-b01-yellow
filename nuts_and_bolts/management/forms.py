from flask_wtf import FlaskForm
from wtforms import StringField, TextField, IntegerField, DecimalField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError

def sku_check(form, field):
    if len(str(field.data)) != 9:
        raise ValidationError('sku must be 9 digits long!')    
    
    
class InventoryForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextField('Description', validators=[DataRequired()])
    price = DecimalField('Price', places=2, validators=[DataRequired()])
    sku = IntegerField('sku', validators=[DataRequired(), sku_check])
    quantity = IntegerField('Quantity', validators=[DataRequired(), NumberRange(min=1, max=10000, message='quantity must be between 1 and 10,000')])
    submit = SubmitField('Submit')
