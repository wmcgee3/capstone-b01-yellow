from flask import Blueprint, render_template
from nuts_and_bolts import db
from nuts_and_bolts.shared.utils import get_cart, get_nav_links
from nuts_and_bolts.models import Category, Subcategory, Product

products = Blueprint('products', __name__)

@products.route('/<string:cat>')
def category(cat):
    cart = get_cart()
    nav_links = get_nav_links()
    _category = cat.replace('_', ' ')
    product_list = db.session.query(Product).order_by(Product.name).join(Subcategory).join(Category).filter_by(name = _category)
    return render_template('category.html', cart = cart, nav_links = nav_links, category = _category, product_list = product_list)

@products.route('/<string:cat>/<string:subcategory>')
def subcategory(cat, subcategory):
    cart = get_cart()
    nav_links = get_nav_links()
    _category = cat.replace('_', ' ')
    _subcategory = subcategory.replace('_', ' ')
    product_list = db.session.query(Product).order_by(Product.name).join(Subcategory).filter_by(name = _subcategory).join(Category).filter_by(name = _category)
    return render_template('category.html', cart = cart, nav_links = nav_links, subcategory = _subcategory, product_list = product_list)
    