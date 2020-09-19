from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_moment import Moment
from flask_seeder import FlaskSeeder
from nuts_and_bolts import Config
from pil import Image

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()
moment = Moment()
seeder = FlaskSeeder()
try:
    logo = Image.open("static/images/logo.png")
except:
    pass


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    seeder.init_app(app, db)

    with app.app_context():
        from nuts_and_bolts.main.routes import main
        from nuts_and_bolts.products.routes import products
        from nuts_and_bolts.errors.handlers import errors
        app.register_blueprint(main)
        app.register_blueprint(products)
        app.register_blueprint(errors)

        return app
