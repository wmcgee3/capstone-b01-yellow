from flask import session
from nuts_and_bolts import db
from nuts_and_bolts.models import Products

def get_cart():
    if 'cart' in session:
        _cart = session['cart']
    else:
        _cart = {}
    return _cart