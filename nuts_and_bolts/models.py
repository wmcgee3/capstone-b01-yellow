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

    def __repr__(self):
        return self.email


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


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
    contents = db.Column(db.Unicode, nullable=False)
