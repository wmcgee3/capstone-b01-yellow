from datetime import datetime
from flask import Blueprint, redirect, render_template, request, url_for
from nuts_and_bolts.models import db, Button

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        button = db.session.query(Button).first()
        button.dateTime = datetime.utcnow()
        db.session.commit()
        return redirect(url_for('main.home'))
    else:
        last_button_press = db.session.query(Button).first()
        return render_template('home.html', last_button_press=last_button_press)

@main.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')
