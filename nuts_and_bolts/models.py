from sqlalchemy.sql.schema import ForeignKey
from nuts_and_bolts import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    receipts = db.relationship('Receipt', back_populates='user')


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.Integer, nullable=False, unique=True)
    name = db.Column(db.String, nullable=False, unique=True)
    price = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    quantity = db.Column(db.Integer, nullable=False, default=0)
    receipt_products = db.relationship(
        'ReceiptProducts', back_populates='product')

    def __repr__(self):
        return self.name.title()


class Receipt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime, nullable=False)
    total_cost = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    user = db.relationship('User', back_populates='receipts')
    receipt_products = db.relationship(
        'ReceiptProducts', back_populates='receipt')


class ReceiptProducts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, ForeignKey('product.id'))
    product = db.relationship('Product', back_populates='receipt_products')
    price = db.Column(db.String, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    receipt_id = db.Column(db.Integer, ForeignKey('receipt.id'))
    receipt = db.relationship('Receipt', back_populates='receipt_products')
