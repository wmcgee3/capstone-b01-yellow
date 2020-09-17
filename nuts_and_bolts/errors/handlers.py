from flask import Blueprint, render_template
from nuts_and_bolts.utils.views import get_nav_links

errors = Blueprint("errors", __name__)


@errors.app_errorhandler(404)
def error_404(error):
    links = get_nav_links()
    return render_template("errors/404.html", links=links), 404

@errors.app_errorhandler(403)
def error_403(error):
    links = get_nav_links()
    return render_template("errors/403.html", links=links), 403

@errors.app_errorhandler(500)
def error_500(error):
    links = get_nav_links()
    return render_template("errors/500.html", links=links), 500
