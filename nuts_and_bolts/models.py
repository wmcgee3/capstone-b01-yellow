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


receipts_products = db.Table(db.Model.metadata,
    db.Column('receipt_id', db.Integer, ForeignKey('receipt.id')),
    db.Column('product_id', db.Integer, ForeignKey('product.id'))
)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.Integer, nullable=False, unique=True)
    name = db.Column(db.String, nullable=False, unique=True)
    price = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    quantity = db.Column(db.Integer, nullable=False, default=0)
    receipts = db.relationship('Receipt', secondary=receipts_products, back_populates='products')

    def __repr__(self):
        return self.name.title()


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    receipts = db.relationship('Receipt', back_populates='customer')


class Receipt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, ForeignKey('customer.id'))
    customer = db.relationship('Customer', back_populates='receipts')
    products = db.relationship('Product', secondary=receipts_products, back_populates='receipts')