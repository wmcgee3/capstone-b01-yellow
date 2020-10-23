from flask import session
from nuts_and_bolts import db
from nuts_and_bolts.models import Products

def get_cart():
    return session['cart'] if 'cart' in session else {}