from datetime import datetime
from nuts_and_bolts import db


class Button(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    dateTime = db.Column(db.DateTime, nullable = False, default = datetime.utcnow())

    def __repr__(self):
        return self.dateTime.strftime("%b %d %Y at %H:%M:%S UTC")