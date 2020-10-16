from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask_seeder import FlaskSeeder
from nuts_and_bolts.config import Config
from PIL import Image

db = SQLAlchemy()
bcrypt = Bcrypt()
mail = Mail()
seeder = FlaskSeeder()
try:
    logo = Image.open('static/images/logo.png')
except:
    pass


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)
    seeder.init_app(app, db)

    with app.app_context():
        from nuts_and_bolts.main.routes import main
        from nuts_and_bolts.errors.handlers import errors
        from nuts_and_bolts.management.routes import management

        app.register_blueprint(main)
        app.register_blueprint(errors)
        app.register_blueprint(management)

        return app
