from flask import Blueprint, render_template, redirect, flash, session
from flask.helpers import url_for
from nuts_and_bolts import db
from nuts_and_bolts.models import Products

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
    if session['cart']:
        products = db.session.query(Products).filter(
            Products.id.in_(session['cart']))
        for product in products:
            cart[str(product.id)] = {
                "name": product.name,
                "price": product.price,
                "sku": product.sku,
                "quantity": session['cart'][str(product.id)]
            }
    return render_template('show_cart.html', cart=cart)


@main.route('/add_to_cart/<string:id>')
def add_to_cart(id):
    product = db.session.query(Products).filter_by(id=id).first()
    if product:
        if id in session['cart']:
            if session['cart'][id] + 1 <= product.quantity:
                session['cart'][id] = session['cart'][id] + 1
                flash(product.name + ' added to cart!', 'success')
            else:
                session['cart'][id] = product.quantity
                flash('Unable to add ' + product.name + ' to cart. There are only ' +
                      str(product.quantity) + ' left in stock.', 'danger')
        else:
            if product.quantity >= 1:
                session['cart'][id] = 1
                flash(product.name + ' added to cart!', 'success')
            else:
                flash('Unable to add ' + product.name +
                      ' to cart. That product is not currently available', 'danger')
    else:
        flash('Unable to add to cart. That product does not exist.', 'danger')
    return redirect(url_for('main.show_cart'))


@main.route('/clear_cart')
def clear_cart():
    session['cart'] = {}
    flash('Your cart has been cleared!', 'success')
    return redirect(url_for('main.home'))


@main.route('/checkout')
def checkout():
    errors = []
    products = db.session.query(Products).filter(
        Products.id.in_(session['cart']))
    for id in session['cart'].keys():
        for product in products:
            if product.id == int(id):
                if product.quantity < session['cart'][id]:
                    errors.add(product.name)

    if errors:
        message = errors.join(', ')
        flash('Error. In stock quantity of ' + message +
              ' less than amount in cart. Amounts in cart have been adjusted to current stock.', 'danger')
        return redirect(url_for('main.show_cart'))
    else:
        for id in session['cart'].keys():
            for product in products:
                if product.id == int(id):
                    product.quantity -= session['cart'][id]
        db.session.commit()
        session['cart'] = {}
        flash('Products purchased successfully.', 'success')
        return redirect(url_for('main.home'))
