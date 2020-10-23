from flask import Blueprint, render_template, redirect, url_for, flash, request
from nuts_and_bolts.management.forms import InventoryForm
from nuts_and_bolts.models import Products
from nuts_and_bolts import db

management = Blueprint('management', __name__)

#add item to inventory
@management.route('/management/add_to_inventory', methods=['GET', 'POST'])
def add_to_inventory():
    form = InventoryForm()
    if form.validate_on_submit():
        new_product = Products(
            name=form.name.data,
            description=form.description.data,
            price=form.price.data,
            sku=int(form.sku.data),
            quantity=int(form.quantity.data)
        )
        db.session.add(new_product)
        db.session.commit()
        flash(f'Entry created for {form.name.data}!', 'success')
        return redirect(url_for('main.product_list'))
    form.submit.label.text = 'Add'
    return render_template('add_to_inventory.html', form=form)

#update inventory item 
@management.route('/management/update_inventory/<int:product_id>',  methods=['GET', 'POST'] )
def update_inventory(product_id):
    product = Products.query.get_or_404(product_id)
    form = InventoryForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            product.name=form.name.data
            product.description=form.description.data
            product.price=form.price.data
            product.sku=int(form.sku.data)
            product.quantity=int(form.quantity.data)
            db.session.commit()
            flash(f'Entry updated for ' + form.name.data + '!', 'success')
            return redirect(url_for('main.product_list'))
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
