from datetime import datetime
from flask import render_template, Blueprint
from flask.globals import request
from nuts_and_bolts.models import db, Button

main = Blueprint('main', __name__)


@main.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'GET':
        last_button_press = db.session.query(Button).first()
        return render_template('home.html', last_button_press = last_button_press)
    elif request.method == 'POST':
        button = db.session.query(Button).first()
        button.dateTime = datetime.utcnow()
        db.session.commit()
        last_button_press = db.session.query(Button).first()
        return render_template('home.html', last_button_press = last_button_press)
