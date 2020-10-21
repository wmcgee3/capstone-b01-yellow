from flask import Blueprint, render_template, redirect, url_for, flash
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
    return render_template('add_to_inventory.html', form=form)

#update inventory item 
'''
@management.route('/management/update_inventory/<int:sku>',  methods=['GET', 'POST'] )
def update_inventory(sku):
    form = InventoryForm()
    if form.validate_on_submit():
        new_product = Products(
            name=form.name.data,
            description=form.description.data,
            price=form.price.data,
            sku=int(form.sku.data),
            quantity=int(form.quantity.data)
        )

        db.session.commit()
        flash(f'Entry update for {form.name.data}!', 'success')
        return redirect(url_for('main.product_list'))
    elif request.method == 'GET':
    form.name.data = product.name,
    form.description.data = product.description,
    form.price.data = product.price,
    form.quantity.data = int(product.quantity),
return render_template('update_inventory.html', form=form)

'''   
