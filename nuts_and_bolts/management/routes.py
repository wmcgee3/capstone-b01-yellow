from flask import Blueprint, render_template, redirect, url_for
from nuts_and_bolts.management.forms import InventoryForm

management = Blueprint('management', __name__)

@management.route('/management/add_to_inventory', methods=['GET', 'POST'])
def add_to_inventory():
    form = InventoryForm()
    if form.validate_on_submit():
        return redirect(url_for('main.home'))
    return render_template('add_to_inventory.html')