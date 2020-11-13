from nuts_and_bolts.orders.forms import FindOrdersForm
from nuts_and_bolts.models import Customer, Receipt
from flask import Blueprint, render_template, url_for, redirect, flash, session

orders = Blueprint('orders', __name__)


@orders.route('/orders', methods=['GET', 'POST'])
def receipts():
    form = FindOrdersForm()
    if form.validate_on_submit():
        customer = Customer.query.filter_by(email=form.email.data).first()
        if customer:
            session['customer_id'] = customer.id
            return redirect(url_for('orders.receipts'))
    if 'customer_id' in session:
        customer = Customer.query.filter_by(id=session['customer_id']).first()
        orders = sorted(customer.receipts, key=lambda i: i.datetime, reverse=True)
        return render_template('receipts.html', orders=orders)
    return render_template('receipts.html', form=form)


@orders.route('/order/<int:receipt_id>', methods=['GET', 'POST'])
def receipt(receipt_id):
    receipt = Receipt.query.get_or_404(receipt_id)
    return render_template('receipt.html', receipt=receipt)
