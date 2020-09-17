from datetime import datetime
from flask import abort, render_template, redirect, request, Blueprint, jsonify
from flask_login import login_required, current_user
from flask.helpers import make_response, url_for
from sqlalchemy import func, select
from nuts_and_bolts import db
from nuts_and_bolts.main.utils import get_cities, get_sites, get_js_date
from nuts_and_bolts.utils.views import get_nav_links

main = Blueprint('main', __name__)


@main.route("/")
def home():
    nav_links = get_nav_links()
    return render_template('home.html', nav_links=nav_links)


@main.route('/faq')
def faq():
    nav_links = get_nav_links()
    return render_template('faq.html', nav_links=nav_links)


@main.route('/contact_us')
def contact_us():
    nav_links = get_nav_links()
    return render_template('contact_us.html', nav_links=nav_links)