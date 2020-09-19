from collections import defaultdict
from flask import session
from flask_login import current_user
from nuts_and_bolts import db
from nuts_and_bolts.models import Category, Subcategory


def get_nav_links():
    subcategories_list = []
    subcategories = db.session.query(Subcategory).join(Category).order_by(Category.name).order_by(
        Subcategory.name)
    for subcategory in subcategories:
        subcategories_list.append((subcategory.category, subcategory))
    category_dict = defaultdict(list)
    for key, value in subcategories_list:
        category_dict[key].append(value)
    return category_dict


def get_cart():
    return session['cart'] if 'cart' in session else {}
