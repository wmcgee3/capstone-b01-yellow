from nuts_and_bolts import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.Integer, nullable=False, unique=True)
    name = db.Column(db.String, nullable=False, unique=True)
    price = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    quantity = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return self.name.title()
