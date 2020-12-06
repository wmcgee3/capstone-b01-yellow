from flask import Blueprint, render_template, redirect, flash, request, url_for
from flask_login import current_user, login_user, logout_user
from nuts_and_bolts import bcrypt
from nuts_and_bolts.models import User
from nuts_and_bolts.auth.forms import LoginForm

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            flash('You are now logged in.', 'success')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login unsuccessful. Please check your credentials.', 'danger')
    return render_template('login.html', form=form)


@auth.route('/logout')
def logout():
    logout_user()
    flash('You are now logged out.', 'success')
    return redirect(url_for('main.home'))
