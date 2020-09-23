from flask import Blueprint, render_template
from nuts_and_bolts.shared.utils import get_cart, get_nav_links

errors = Blueprint("errors", __name__)


@errors.app_errorhandler(404)
def error_404(error):
    cart = get_cart()
    nav_links = get_nav_links()
    return render_template("errors/404.html", cart=cart, nav_links=nav_links), 404

@errors.app_errorhandler(403)
def error_403(error):
    cart = get_cart()
    nav_links = get_nav_links()
    return render_template("errors/403.html", cart=cart, nav_links=nav_links), 403

@errors.app_errorhandler(500)
def error_500(error):
    cart = get_cart()
    nav_links = get_nav_links()
    return render_template("errors/500.html", cart=cart, nav_links=nav_links), 500
