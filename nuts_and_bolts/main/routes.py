from datetime import datetime
from flask import Blueprint, redirect, render_template, request, url_for
from nuts_and_bolts.models import db, Button

main = Blueprint('main', __name__)


@main.route('/')
def home():
    return render_template('home.html')
