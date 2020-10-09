from nuts_and_bolts import db


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.Integer, nullable=False, unique=True)
    name = db.Column(db.String, nullable=False, unique=True)
    price = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)

    def __repr__(self):
        return self.name.title()
