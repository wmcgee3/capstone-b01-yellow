from flask import render_template, Blueprint
from nuts_and_bolts.models import db, Button

main = Blueprint('main', __name__)


@main.route('/')
def home():
    last_button_press = db.session.query(Button).first()
    return render_template('home.html', last_button_press = last_button_press)
