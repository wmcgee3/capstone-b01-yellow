from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField

class ProductForm(FlaskForm):
    quantity = SelectField('Quantity', validate_choice=False)
    add = SubmitField('Add to cart')
    