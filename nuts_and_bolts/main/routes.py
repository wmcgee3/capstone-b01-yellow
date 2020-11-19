from flask import Blueprint, render_template, redirect, flash, session, abort, request, url_for
from .forms import QuestionsForm
from flask.helpers import url_for
from nuts_and_bolts import db, mail
from nuts_and_bolts.models import Product
from nuts_and_bolts.main.forms import QuestionsForm
from flask_mail import Message

main = Blueprint('main', __name__)


@main.route('/')
def home():
    return render_template('home.html')


@main.route('/contact_us', methods=['GET', 'POST'])
def contact_us():
    form = QuestionsForm()
    if form.validate_on_submit():
        msg = Message('Question about ' + form.subject.data + ' Sent',
                      sender='noreply.nutsandboltshardware@gmail.com',
                      recipients=[form.email.data],
                      bcc=['noreply.nutsandboltshardware@gmail.com'])
        msg.body = f''' Your question about {form.subject.data} has been sent to our staff!
Your question was:

{form.text.data}

We will reach out in a few days after review.    
Thank you.

- Nuts and Bolts Staff
'''
        mail.send(msg)
        flash(f'Question submitted! Check email for confirmation.', 'success')
        return redirect(url_for('main.contact_us'))
    return render_template('contact_us.html', form=form)


@main.route('/product_list')
def product_list():
    products = db.session.query(Product).order_by(Product.sku)
    return render_template('product_list.html', products=products)


@main.route('/faq')
def faq():
    return render_template('faq.html')


@main.route('/show_cart')
def show_cart():
    cart = {}
    if session['cart']:
        products = db.session.query(Product).filter(
            Product.id.in_(session['cart']))
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
    product = db.session.query(Product).filter_by(id=id).first()
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
    return redirect(url_for('cart.show_cart'))


@main.route('/clear_cart')
def clear_cart():
    session['cart'] = {}
    flash('Your cart has been cleared!', 'success')
    return redirect(url_for('main.home'))


@main.route('/search', methods=['GET', 'POST'])
def search():
    search = request.form['search']
    products = db.session.query(Product).filter(Product.name.contains(search))
    return render_template('search.html', search=search, products=products)


@main.route('/remove_item/<id>')
def remove_item(id):
    if id in session['cart']:
        session['cart'].pop(id, None)
        product = db.session.query(Product).filter_by(id=id).first()
        flash(product.name + 'has been removed from cart!', 'success')
        return redirect(url_for('main.show_cart'))
    else:
        abort(404)
