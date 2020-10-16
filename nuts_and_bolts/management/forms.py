from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

class InventoryForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
    price = StringField('price', validators=[DataRequired()])
    sku = IntegerField('sku', validators=[DataRequired()])
    quantity = IntegerField('quantity', validators=[DataRequired(), NumberRange(min=1, max=10000, message='quantity must be between 1 and 10,000')])
    submit = SubmitField('Submit')
    