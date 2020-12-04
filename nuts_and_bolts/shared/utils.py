from functools import wraps
from flask import abort
from flask_login import current_user


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated and current_user.is_admin:
            return f(*args, **kwargs)
        else:
            abort(403)
    return decorated_function
