from flask import Blueprint, render_template, redirect, flash, session
from flask.helpers import url_for
from nuts_and_bolts import db
from nuts_and_bolts.models import Products
from nuts_and_bolts.shared.utils import get_cart

main = Blueprint('main', __name__)


@main.route('/')
def home():
    return render_template('home.html')


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
        products = db.session.query(Products).filter(
            Products.id.in_(simple_cart))
        for product in products:
            cart[str(product.id)] = {
                "name": product.name,
                "price": product.price,
                "sku": product.sku,
                "quantity": simple_cart[str(product.id)]
            }
    return render_template('show_cart.html', cart=cart)


@main.route('/add_to_cart/<string:id>')
def add_to_cart(id):
    cart = get_cart()
    if id in cart:
        cart[id] = cart[id] + 1
    else:
        cart[id] = 1
    print(session['cart'])
    product = db.session.query(Products).filter_by(id=id).first()
    flash(product.name + ' added to cart!', 'success')
    return redirect(url_for('main.show_cart'))
