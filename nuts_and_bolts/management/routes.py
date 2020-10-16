from flask import Blueprint, render_template, redirect, url_for, flash
from nuts_and_bolts.management.forms import InventoryForm, addproduct

management = Blueprint('management', __name__)

@management.route('/management/add_to_inventory', methods=['GET', 'POST'])
def add_to_inventory():
    form = InventoryForm()
    if form.validate_on_submit():
        addproduct(name=form.name.data, desc=form.description.data, price=str(form.price.data), sku=form.sku.data, quantity=form.quantity.data)
        flash(f'Entry created for {form.name.data}!', 'success')
        return redirect(url_for('main.product_list'))
    return render_template('add_to_inventory.html', form=form)