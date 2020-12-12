import os
from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import login_required
from nuts_and_bolts.management.forms import InventoryForm
from nuts_and_bolts.models import Product
from nuts_and_bolts import db
from nuts_and_bolts.shared.utils import admin_required
from nuts_and_bolts.management.utils import save_image

management = Blueprint('management', __name__)


@management.route('/management/add_to_inventory', methods=['GET', 'POST'])
@login_required
@admin_required
def add_to_inventory():
    form = InventoryForm()
    form.image_file.label.text = 'Add Product Image'
    if form.validate_on_submit():
        image_filename = None
        if form.image_file.data:
            image_filename = save_image(form.image_file.data)
        new_product = Product(
            name=form.name.data,
            description=form.description.data,
            price=form.price.data,
            sku=int(form.sku.data),
            quantity=int(form.quantity.data),
            image_name=image_filename,
            image_alt_text=form.image_alt_text.data
        )
        db.session.add(new_product)
        db.session.commit()
        flash(f'Entry created for {form.name.data}!', 'success')
        return redirect(url_for('products.product_list'))
    form.submit.label.text = 'Add'
    return render_template('add_to_inventory.html', form=form)


@management.route('/management/update_inventory/<int:product_id>',  methods=['GET', 'POST'])
@login_required
@admin_required
def update_inventory(product_id):
    product = Product.query.get_or_404(product_id)
    form = InventoryForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            if form.image_file.data:
                os.remove(
                    os.path.join(
                        current_app.root_path,
                        'static/images/products',
                        product.image_name
                    )
                )
                product.image_name = save_image(form.image_file.data)
            product.image_alt_text = form.image_alt_text.data
            product.name = form.name.data
            product.description = form.description.data
            product.price = form.price.data
            product.sku = int(form.sku.data)
            product.quantity = int(form.quantity.data)
            db.session.commit()
            flash('Entry updated for ' + form.name.data + '!', 'success')
            return redirect(url_for('products.product_list'))
        else:
            return render_template('update_inventory.html', form=form)
    form.id.data = product.id
    form.image_alt_text.data = product.image_alt_text
    form.name.data = product.name
    form.description.data = product.description
    form.price.data = product.price
    form.sku.data = product.sku
    form.quantity.data = int(product.quantity)
    form.submit.label.text = 'Update'
    return render_template('update_inventory.html', form=form)
