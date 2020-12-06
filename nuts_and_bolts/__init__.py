from flask import Flask, session
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask_seeder import FlaskSeeder
from PIL import Image
from nuts_and_bolts.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'
mail = Mail()
seeder = FlaskSeeder()
try:
    logo = Image.open('static/images/logo.png')
except:
    pass


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    @app.before_request
    def initiate_session():
        if 'cart' not in session:
            session['cart'] = {}
        session.permanent = True

    db.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)
    seeder.init_app(app, db)
    login_manager.init_app(app)

    with app.app_context():
        from nuts_and_bolts.auth.routes import auth
        from nuts_and_bolts.cart.routes import cart
        from nuts_and_bolts.main.routes import main
        from nuts_and_bolts.errors.handlers import errors
        from nuts_and_bolts.management.routes import management
        from nuts_and_bolts.products.routes import products
        from nuts_and_bolts.receipts.routes import receipts

        app.register_blueprint(auth)
        app.register_blueprint(cart)
        app.register_blueprint(main)
        app.register_blueprint(errors)
        app.register_blueprint(management)
        app.register_blueprint(products)
        app.register_blueprint(receipts)

        return app
