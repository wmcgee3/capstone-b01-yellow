from flask import Blueprint, redirect, url_for, render_template, abort, session, flash
from nuts_and_bolts.models import Product
from nuts_and_bolts.products.forms import ProductForm
from nuts_and_bolts import db

products = Blueprint('products', __name__)


@products.route('/products/all')
def product_list():
    products = db.session.query(Product).order_by(Product.sku)
    return render_template('product_list.html', products=products)


@products.route('/product/<product_sku>', methods=['GET', 'POST'])
def product_page(product_sku):
    product = Product.query.filter_by(sku=product_sku).first()
    if product:
        form = ProductForm()
        if form.validate_on_submit():
            session['cart'][str(product.id)] = int(form.quantity.data)
            flash(product.name + ' added to cart!', 'success')
            return redirect(url_for('cart.show_cart'))
        form.quantity.choices = [(i, i)
                                 for i in range(product.quantity + 1)][1:]
        if str(product.id) in session['cart']:
            form.quantity.data = str(session['cart'][str(product.id)])
            form.add.label.text = 'Update'
        return render_template('product.html', product=product, form=form)
    return abort(404)
