from flask import Blueprint, render_template, session
from nuts_and_bolts import db
from nuts_and_bolts.models import Products
from nuts_and_bolts.shared.utils import get_cart

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')
    if 'cart' not in session:
        session['cart'] = {}

@main.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')


@main.route('/product_list')
def product_list():
    products = db.session.query(Products).order_by(Products.sku)
    return render_template('product_list.html', products=products)


@main.route('/faq')
def faq():
    return render_template('faq.html')


@main.route('/show_cart')
def show_cart():
    cart = {}
    simple_cart = get_cart()
    if simple_cart:
        products = db.session.query(Products).filter(Products.id.in_(simple_cart))
        for product in products:
            cart[str(product.id)] = {
                "name": product.name,
                "price": product.price,
                "sku": product.sku,
                "quantity": simple_cart[str(product.id)]
            }

    return render_template('show_cart.html', cart=cart)
