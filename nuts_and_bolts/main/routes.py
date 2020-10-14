from flask import Blueprint, render_template
from nuts_and_bolts import db
from nuts_and_bolts.models import Products
from nuts_and_bolts.inventoryForm import InventoryForm

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

@main.route('/add_to_inventory')
def add_to_inventory(methods=('POST')):
    form = InventoryForm(csrf_enabled=False)
    if form.validate_on_submit():
        return render_template('/')
    return render_template('add_to_inventory.html')
