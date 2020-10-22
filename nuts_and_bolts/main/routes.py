from flask import Blueprint, render_template, session
from nuts_and_bolts import db
from nuts_and_bolts.models import Products

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
  