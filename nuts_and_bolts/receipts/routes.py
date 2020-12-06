from flask import Blueprint, render_template, flash
from flask_login import current_user
from nuts_and_bolts.receipts.forms import FindOrdersForm
from nuts_and_bolts.models import User, Receipt

receipts = Blueprint('receipts', __name__)


@receipts.route('/receipts', methods=['GET', 'POST'])
def all_receipts():
    _receipts = []
    form = FindOrdersForm()
    if current_user.is_authenticated:
        _receipts = sorted(current_user.receipts, key=lambda i: i.datetime, reverse=True)
        if not _receipts:
            flash("You don't have any receipts.", 'danger')
    if form.validate_on_submit():
        customer = User.query.filter_by(email=form.email.data).first()
        if customer:
            _receipts = sorted(customer.receipts, key=lambda i: i.datetime, reverse=True)
        if not _receipts:
            flash('No receipts match that email address.', 'danger')
    return render_template('receipts.html', receipts=_receipts, form=form)


@receipts.route('/receipt/<int:receipt_id>', methods=['GET', 'POST'])
def receipt(receipt_id):
    _receipt = Receipt.query.get_or_404(receipt_id)
    return render_template('receipt.html', receipt=_receipt)
