from nuts_and_bolts.cart.forms import CartForm
from flask import Blueprint, render_template, session, url_for, flash, redirect
from nuts_and_bolts import db
from nuts_and_bolts.models import Product, Customer, Receipt, ReceiptProducts
from datetime import datetime
from decimal import Decimal

cart = Blueprint('cart', __name__)


@cart.route('/cart', methods=['GET', 'POST'])
def show_cart():
    form = CartForm()
    if form.validate_on_submit():
        if form.clear_cart.data:
            session['cart'] = {}
            flash('Your cart has been cleared.', 'success')
        if form.checkout.data:
            products = db.session.query(Product).filter(
                Product.id.in_(session['cart'])).all()
            understocked_products = []
            for product in products:
                if session['cart'][str(product.id)] > product.quantity:
                    session['cart'][str(product.id)] = product.quantity
                    understocked_products.append(product.name)
            if understocked_products:
                flash('The following products are in limited supply: ' + ', '.join(understocked_products) + '. The quantities in your cart have been adjusted.', 'danger')
                return redirect(url_for('cart.show_cart'))
            if form.email.data:
                customer = Customer.query.filter_by(email=form.email.data).first()
                if not customer:
                    new_customer = Customer(
                        email=form.email.data
                    )
                    customer = new_customer
                session['email'] = customer.email
                total_cost = 0
                for product in products:
                    total_cost += Decimal(product.price)
                new_receipt = Receipt(
                    customer=customer,
                    total_cost=str(total_cost),
                    datetime=datetime.utcnow()
                )
                for product in products:
                    product.quantity -= session['cart'][str(product.id)]
                    new_receipt_product = ReceiptProducts(
                        product=product,
                        price=product.price,
                        quantity=session['cart'][str(product.id)],
                        receipt=new_receipt
                    )
                    db.session.add(new_receipt_product)
                    db.session.commit()
                    session['cart'].pop(str(product.id))
                db.session.add(new_receipt)
                db.session.commit()
                flash('Thank you for shopping with Nuts & Bolts!', 'success')
                return redirect(url_for('main.product_list'))
            else:
                flash('Please enter an email address to checkout.', 'warning')
                return redirect(url_for('cart.show_cart'))
    cart = {}
    if session['cart']:
        products = db.session.query(Product).filter(
            Product.id.in_(session['cart']))
        for product in products:
            cart[str(product.id)] = {
                "name": product.name,
                "price": product.price,
                "sku": product.sku,
                "quantity": session['cart'][str(product.id)]
            }
    return render_template('show_cart.html', cart=cart, form=form)
