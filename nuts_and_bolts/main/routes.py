from flask import Blueprint, render_template, redirect, flash, session, abort, request, url_for
from flask.helpers import url_for
from nuts_and_bolts import db, mail
from nuts_and_bolts.models import Product, Testimonial
from nuts_and_bolts.main.forms import QuestionsForm, TestimonialForm
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


@main.route('/search', methods=['GET', 'POST'])
def search():
    products = []
    search = request.form['search']
    if search:
        products = db.session.query(Product).filter(Product.name.contains(search))
    return render_template('search.html', search=search, products=products)

@main.route('/testimonials', methods=['GET', 'POST'])
def testimonials():
    testimonial_list = db.session.query(Testimonial).order_by(Testimonial.name)
    form = TestimonialForm()
    if form.validate_on_submit():
        new_testimonial = Testimonial(
            name=form.name.data,
            text=form.text.data
        )
        db.session.add(new_testimonial)
        db.session.commit()
        flash(f'Entry created for {form.name.data}!', 'success')
        return redirect(url_for('main.testimonials'))
    form.submit.label.text = 'Add Testimonial'
    return render_template('testimonials.html', form=form, testimonial_list=testimonial_list)
