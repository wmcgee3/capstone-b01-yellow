from flask import Blueprint, redirect, url_for, render_template
from nuts_and_bolts.models import Product

products = Blueprint('products', __name__)


@products.route('/product/<product_sku>')
def product_page(product_sku):
    product = Product.query.filter_by(sku=product_sku).first()


    return render_template('product.html', product=product)
