from flask import render_template, Blueprint
from nuts_and_bolts.shared.utils import get_cart, get_nav_links

main = Blueprint('main', __name__)


@main.route("/")
def home():
    cart = get_cart()
    nav_links = get_nav_links()
    return render_template('home.html', cart=cart, nav_links=nav_links)


@main.route('/faq')
def faq():
    cart = get_cart()
    nav_links = get_nav_links()
    return render_template('faq.html', cart=cart, nav_links=nav_links)


@main.route('/contact_us')
def contact_us():
    cart = get_cart()
    nav_links = get_nav_links()
    return render_template('contact_us.html', cart=cart, nav_links=nav_links)
    

@main.route('/cart')
def cart():
    cart = get_cart()
    nav_links = get_nav_links()
    return render_template('cart.html', cart=cart, nav_links=nav_links)
    #datetime.now(timezone.utc)
