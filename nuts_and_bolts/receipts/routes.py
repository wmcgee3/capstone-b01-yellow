from nuts_and_bolts.receipts.forms import FindOrdersForm
from nuts_and_bolts.models import User, Receipt
from flask import Blueprint, render_template, url_for, redirect, flash, session
from flask_login import current_user

receipts = Blueprint('receipts', __name__)


@receipts.route('/receipts', methods=['GET', 'POST'])
def all_receipts():
    receipts = []
    form = FindOrdersForm()
    if current_user.is_authenticated:
        customer = User.query.filter_by(email=current_user.email).first()
        if customer:
            receipts = sorted(customer.receipts, key=lambda i: i.datetime, reverse=True)
        if not receipts:
            flash('No receipts match that email address.', 'danger')
    if form.validate_on_submit():
        customer = User.query.filter_by(email=form.email.data).first()
        if customer:
            receipts = sorted(customer.receipts, key=lambda i: i.datetime, reverse=True)
        if not receipts:
            flash('No receipts match that email address.', 'danger')
    return render_template('receipts.html', receipts=receipts, form=form)


@receipts.route('/receipt/<int:receipt_id>', methods=['GET', 'POST'])
def receipt(receipt_id):
    receipt = Receipt.query.get_or_404(receipt_id)
    return render_template('receipt.html', receipt=receipt)
