from flask import session
from nuts_and_bolts import db
from nuts_and_bolts.models import Products

def get_cart():
    if 'cart' in session:
        _cart = {}
        for x in session['cart']:
            curr_product = db.session.query(Products).filter_by(id=x)
            _cart[x] = {"name" : curr_product.name,
            "price" : curr_product.price,
            "sku" : curr_product.sku,
            "quantity" : session['cart[x]']}
        return _cart

    else:
        _cart = {}
        return _cart