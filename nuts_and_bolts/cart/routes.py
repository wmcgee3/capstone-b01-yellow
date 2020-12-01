from nuts_and_bolts.cart.forms import CartForm
from flask import Blueprint, render_template, session, url_for, flash, redirect, abort
from nuts_and_bolts import db, mail
from nuts_and_bolts.models import Product, User, Receipt, ReceiptProducts
from datetime import datetime
from decimal import Decimal
from flask_mail import Message
from nuts_and_bolts.config import Config

cart = Blueprint('cart', __name__)


@cart.route('/cart', methods=['GET', 'POST'])
def show_cart():
    form = CartForm()
    if form.validate_on_submit():
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
                customer = User.query.filter_by(email=form.email.data).first()
                if not customer:
                    new_customer = User(
                        email=form.email.data
                    )
                    customer = new_customer
                session['email'] = customer.email
                total_cost = 0
                for product in products:
                    total_cost += (Decimal(product.price) * Decimal(session['cart'][str(product.id)]))
                new_receipt = Receipt(
                    customer=customer,
                    total_cost=str(total_cost),
                    datetime=datetime.utcnow()
                )
                items = ''''''
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
                    items += f'''{new_receipt_product.product.name}
    {new_receipt_product.price} each, Quantity: {new_receipt_product.quantity}
'''
                    session['cart'].pop(str(product.id))
                db.session.add(new_receipt)
                db.session.commit()
                msg = Message('Nuts and Bolts Transaction ID: ' + str(new_receipt.id),
                    sender=Config.MAIL_USERNAME,
                    recipients= [customer.email])
                msg.body = f'''Transaction ID #{str(new_receipt.id)} was successful!

    {items}
The total cost was: ${str(new_receipt.total_cost)}

Thank you for shopping with us!
- Nuts and Bolts Staff
'''
                mail.send(msg)               
                flash('Thank you for shopping with Nuts & Bolts! Your receipt was sent to your Email address', 'success')
                return redirect(url_for('products.product_list'))
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

@cart.route('/cart/clear')
def clear_cart():
    if 'cart' in session:
        session['cart'] = {}
        flash('Your cart has been cleared.', 'success')
    return redirect(url_for('cart.show_cart'))


@cart.route('/cart/remove_item/<id>')
def remove_item(id):
    if id in session['cart']:
        session['cart'].pop(id, None)
        product = db.session.query(Product).filter_by(id=id).first()
        flash(product.name + 'has been removed from cart!', 'success')
        return redirect(url_for('cart.show_cart'))
    else:
        abort(404)
