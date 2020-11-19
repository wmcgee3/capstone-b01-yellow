from flask import Blueprint, redirect, url_for, render_template, abort, session, flash
from nuts_and_bolts.models import Product
from nuts_and_bolts.products.forms import ProductForm

products = Blueprint('products', __name__)


@products.route('/product/<product_sku>', methods=['GET', 'POST'])
def product_page(product_sku):
    product = Product.query.filter_by(sku=product_sku).first()
    if product:
        form = ProductForm()
        if form.validate_on_submit():
            if product.id in session['cart']:
                quantity = session['cart'][product.id]
                session['cart'][product.id] = int(quantity) + int(form.quantity.data)
            else:
                session['cart'][product.id] = int(form.quantity.data)
            flash(product.name + ' added to cart!', 'success')
            return redirect(url_for('cart.show_cart'))
        i = 1
        form.quantity.choices = [(i, i) for i in range(product.quantity + 1)]
        return render_template('product.html', product=product, form=form)
    return abort(404)
