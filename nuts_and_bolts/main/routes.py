from flask import Blueprint, render_template, redirect, flash, session, abort, request, url_for
from flask.helpers import url_for
from nuts_and_bolts import db, mail
from nuts_and_bolts.models import Product
from nuts_and_bolts.main.forms import QuestionsForm
from flask_mail import Message
from nuts_and_bolts.config import Config

main = Blueprint('main', __name__)


@main.route('/')
def home():
    return render_template('home.html')


@main.route('/contact_us', methods=['GET', 'POST'])
def contact_us():
    form = QuestionsForm()
    if form.validate_on_submit():
        msg = Message('Question about ' + form.subject.data + ' Sent',
                      sender=Config.MAIL_USERNAME,
                      recipients=[form.email.data],
                      bcc=[Config.MAIL_USERNAME])
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


@main.route('/faq')
def faq():
    return render_template('faq.html')


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
        return redirect(url_for('cart.show_cart'))
    else:
        abort(404)
