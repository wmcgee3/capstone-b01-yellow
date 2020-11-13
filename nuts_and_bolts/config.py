from flask import url_for
import os


class Config:
    SECRET_KEY = str(os.environ.get('NAB_KEY'))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = str(os.environ.get('NAB_USER'))
    MAIL_PASSWORD = str(os.environ.get('NAB_PASS'))
