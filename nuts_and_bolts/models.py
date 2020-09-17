from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from nuts_and_bolts import db, login_manager
from flask_login import UserMixin
from sqlalchemy.sql.schema import ForeignKey


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    carts = db.relationship('Cart', backref='user', lazy=True)

    def __repr__(self):
        return self.email


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    open = db.Column(db.Boolean, nullable=False, default=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class UserCartLink(db.Model):
    cart_id = db.Column(db.Integer, ForeignKey('cart.id'), primary_key=True)
    product_id = db.Column(db.Integer, ForeignKey(
        'product.id'), primary_key=True)
    count = db.Column(db.Integer, nullable=False, default=1)
    cart = db.relationship('Cart', backref='product_link', lazy=True)
    product = db.relationship('Product', backref='cart_link', lazy=True)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.String(50), unique=True, nullable=False)
    price = db.Column(db.Numeric, nullable=False)
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'), nullable=False)
    subcategory_id = db.Column(db.Integer, db.ForeignKey(
        'subcategory.id'), nullable=False)

    def __repr__(self):
        return self.name


class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    products = db.relationship('Product', backref='brand', lazy=True)

    def __repr__(self):
        return self.name


class Subcategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    products = db.relationship('Product', backref='subcategory', lazy=True)
    category_id = db.Column(db.Integer, db.ForeignKey(
        'category.id'), nullable=False)

    def __repr__(self):
        return self.name


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    subcategories = db.relationship(
        'Subcategory', backref='category', lazy=True)

    def __repr__(self):
        return self.name
