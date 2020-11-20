from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from nuts_and_bolts.management.forms import InventoryForm
from nuts_and_bolts.models import Product
from nuts_and_bolts import db

management = Blueprint('management', __name__)


@management.route('/management/add_to_inventory', methods=['GET', 'POST'])
@login_required
def add_to_inventory():
    form = InventoryForm()
    if form.validate_on_submit():
        new_product = Product(
            name=form.name.data,
            description=form.description.data,
            price=form.price.data,
            sku=int(form.sku.data),
            quantity=int(form.quantity.data)
        )
        db.session.add(new_product)
        db.session.commit()
        flash(f'Entry created for {form.name.data}!', 'success')
        return redirect(url_for('products.product_list'))
    form.submit.label.text = 'Add'
    return render_template('add_to_inventory.html', form=form)


@management.route('/management/update_inventory/<int:product_id>',  methods=['GET', 'POST'])
@login_required
def update_inventory(product_id):
    product = Product.query.get_or_404(product_id)
    form = InventoryForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            product.name = form.name.data
            product.description = form.description.data
            product.price = form.price.data
            product.sku = int(form.sku.data)
            product.quantity = int(form.quantity.data)
            db.session.commit()
            flash(f'Entry updated for ' + form.name.data + '!', 'success')
            return redirect(url_for('products.product_list'))
        else:
            return render_template('update_inventory.html', form=form)
    form.id.data = product.id
    form.name.data = product.name
    form.description.data = product.description
    form.price.data = product.price
    form.sku.data = product.sku
    form.quantity.data = int(product.quantity)
    form.submit.label.text = 'Update'
    return render_template('update_inventory.html', form=form)
