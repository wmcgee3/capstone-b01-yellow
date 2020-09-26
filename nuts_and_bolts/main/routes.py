from flask import render_template, Blueprint

main = Blueprint('main', __name__)


@main.route('/')
def home():
    return render_template('home.html')


@main.route('/faq')
def faq():
    return render_template('faq.html')


@main.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')
    

@main.route('/products')
def products():
    return render_template('products.html')
