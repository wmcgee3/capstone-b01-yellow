from flask import url_for
import os


class Config:
    SECRET_KEY = os.environ.get('nab_key')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('nab_user')
    MAIL_PASSWORD = os.environ.get('nab_pass')
