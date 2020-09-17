from nuts_and_bolts.models import User, Site
from nuts_and_bolts import db, create_app

app = create_app()
db.create_all(app=create_app())


def populate_user_sites():
    user = db.session.query(User).filter_by(id=1).first()
    site = db.session.query(Site).all()
    for item in site:
        item.users.append(user)
    db.session.commit()


with app.app_context():
    populate_user_sites()
