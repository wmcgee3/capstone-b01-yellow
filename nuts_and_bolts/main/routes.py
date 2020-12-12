from flask import Blueprint, render_template, redirect, flash, request, url_for
from flask_mail import Message
from flask_login import login_required
from nuts_and_bolts.shared.utils import admin_required
from nuts_and_bolts.config import Config
from nuts_and_bolts import db, mail
from nuts_and_bolts.models import Product, Testimonial
from nuts_and_bolts.main.forms import QuestionsForm, TestimonialForm

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
        flash('Question submitted! Check email for confirmation.', 'success')
        return redirect(url_for('main.contact_us'))
    return render_template('contact_us.html', form=form)


@main.route('/about_us')
def about_us():
    return render_template('about_us.html')


@main.route('/faq')
def faq():
    return render_template('faq.html')


@main.route('/search', methods=['GET', 'POST'])
def search():
    products = []
    _search = request.form['search']
    if _search:
        products = db.session.query(Product).filter(
            Product.name.contains(_search))
    return render_template('search.html', search=_search, products=products)


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
        flash(
            f'Thank you for your testimonial, {form.name.data}. It has been submitted for review!',
            'success'
        )
        return redirect(url_for('main.testimonials'))
    form.submit.label.text = 'Add Testimonial'
    return render_template('testimonials.html', form=form, testimonial_list=testimonial_list)


@main.route('/testimonial/<int:testimonial_id>/toggle_visibility')
@login_required
@admin_required
def toggle_testimonial_visibility(testimonial_id):
    testimonial = db.session.query(
        Testimonial).filter_by(id=testimonial_id).first()
    testimonial.visibility = not testimonial.visibility
    db.session.commit()
    return redirect(url_for('main.testimonials'))
