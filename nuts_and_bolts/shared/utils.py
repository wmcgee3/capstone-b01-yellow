from flask import session
from nuts_and_bolts import db
from nuts_and_bolts.models import Products

def get_cart():
    if not 'cart' in session:
        session['cart'] = {}
    return session['cart']